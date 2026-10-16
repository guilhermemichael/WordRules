#!/usr/bin/env python3
"""Deterministic artifact checks only; this does not certify model behavior."""
import json, re
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.0.0"
ERRORS = []

def fail(message):
    ERRORS.append(message)

def read_text(relative):
    path = ROOT / relative
    if not path.is_file():
        fail("Missing required file: " + relative)
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"Invalid UTF-8 {relative}: {exc}")
        return ""

def load_json(relative):
    raw = read_text(relative)
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON {relative}:{exc.lineno}:{exc.colno}: {exc.msg}")
        return None

def validate_schema(schema_relative, data_relative, data):
    schema = load_json(schema_relative)
    if schema is None or data is None:
        return
    try:
        from jsonschema import Draft202012Validator
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(data), key=lambda error: list(map(str, error.absolute_path)))
        for error in errors:
            location = "/" + "/".join(str(item) for item in error.absolute_path) if error.absolute_path else "/"
            fail(f"Schema violation {data_relative} at {location}: {error.message}")
    except ImportError:
        fail("Install dependency with: python -m pip install -r requirements-dev.txt")
    except Exception as exc:
        fail(f"Schema validation error for {data_relative}: {exc}")

def check_local_markdown_links():
    checked = 0
    pattern = re.compile(r"(?<!!)\\[[^\\]]+\\]\\(([^)]+)\\)")
    for markdown in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv", "node_modules"} for part in markdown.parts):
            continue
        content = markdown.read_text(encoding="utf-8")
        for match in pattern.finditer(content):
            target = match.group(1).strip().lstrip("<").rstrip(">").split()[0]
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or target.startswith("//") or not parts.path:
                continue
            raw_path = unquote(parts.path)
            candidate = (ROOT / raw_path.lstrip("/")) if raw_path.startswith("/") else (markdown.parent / raw_path)
            candidate = candidate.resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"Local Markdown link escapes repository: {markdown.relative_to(ROOT)} -> {target}")
                continue
            if not candidate.exists():
                fail(f"Broken local Markdown link: {markdown.relative_to(ROOT)} -> {target}")
            else:
                checked += 1
    return checked

def main():
    required = [
        "README.md", "ULTRA_MASTER_GUIA_DE_REGRAS_PARA_IA.md",
        "CAMADA_OPERACIONAL_COMPACTA.md", "SUITE_DE_AVALIACAO_ULTRA_MASTER.md",
        ".gitignore", "spec/ultra_master.schema.json", "spec/ultra_master_rules.json",
        "spec/decision_protocol.schema.json", "spec/decision_protocol.json",
        "spec/evaluation_cases.schema.json", "tests/fixtures/evaluation_cases.json",
        "scripts/validate_wordrules.py", "requirements-dev.txt",
        ".github/workflows/validate.yml", "docs/ARQUITETURA_DO_PROTOCOLO_3_0.md",
        "docs/REGISTRO_DE_CORRECOES_3_0.md"
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail("Missing required file: " + relative)

    guide = read_text("ULTRA_MASTER_GUIA_DE_REGRAS_PARA_IA.md")
    compact = read_text("CAMADA_OPERACIONAL_COMPACTA.md")
    suite = read_text("SUITE_DE_AVALIACAO_ULTRA_MASTER.md")
    gitignore = read_text(".gitignore")

    guide_ids = re.findall(r"^### ([A-Z]+-\\d{3}) — .+$", guide, re.M)
    if len(guide_ids) != len(set(guide_ids)):
        fail("Duplicate normative IDs in canonical guide.")

    registry = load_json("spec/ultra_master_rules.json")
    protocol = load_json("spec/decision_protocol.json")
    fixture = load_json("tests/fixtures/evaluation_cases.json")
    validate_schema("spec/ultra_master.schema.json", "spec/ultra_master_rules.json", registry)
    validate_schema("spec/decision_protocol.schema.json", "spec/decision_protocol.json", protocol)
    validate_schema("spec/evaluation_cases.schema.json", "tests/fixtures/evaluation_cases.json", fixture)

    if registry is not None:
        registry_ids = [rule.get("id") for rule in registry.get("rules", [])]
        if len(registry_ids) != len(set(registry_ids)):
            fail("Duplicate IDs in machine-readable registry.")
        if set(registry_ids) != set(guide_ids):
            fail("Guide/registry IDs differ.")
        if registry.get("rule_count") != len(registry_ids):
            fail("registry.rule_count does not match its rules array.")
        if registry.get("protocol_version") != VERSION or registry.get("behavioral_validation") != "NOT_TESTED":
            fail("Registry version or behavioral status mismatch.")
    if protocol is not None and protocol.get("protocol_version") != VERSION:
        fail("Decision protocol version mismatch.")

    case_ids = re.findall(r"^### (CASE-\\d{2}) — .+$", suite, re.M)
    if len(case_ids) != 40 or len(case_ids) != len(set(case_ids)):
        fail(f"Expected 40 unique Markdown cases; found {len(case_ids)}.")
    if "NOT_RUN" not in suite or "NOT_VERIFIED" not in suite:
        fail("Suite must preserve NOT_RUN and NOT_VERIFIED states.")
    if fixture is not None:
        fixture_ids = [case.get("id") for case in fixture.get("cases", [])]
        if len(fixture_ids) != 40 or len(fixture_ids) != len(set(fixture_ids)) or set(fixture_ids) != set(case_ids):
            fail("Markdown/JSON case IDs are inconsistent.")
        if fixture.get("suite_version") != VERSION or fixture.get("protocol_version") != VERSION:
            fail("Fixture version mismatch.")
        if fixture.get("suite_status") != "DESIGNED_NOT_EXECUTED" or any(case.get("execution_status") != "NOT_RUN" for case in fixture.get("cases", [])):
            fail("Fixture falsely claims that model evaluation was executed.")

    for name, content in [("guide", guide), ("compact layer", compact)]:
        if VERSION not in content[:500]:
            fail("Version mismatch in " + name)
    for pattern in ("*.zip", "*.crdownload"):
        if pattern not in gitignore:
            fail(".gitignore missing " + pattern)

    links_checked = check_local_markdown_links()
    if ERRORS:
        print("WORDRULES VALIDATION: FAIL")
        for error in ERRORS:
            print("ERROR:", error)
        return 1

    print("WORDRULES VALIDATION: PASS")
    print(f"Normative rule IDs: {len(guide_ids)} unique")
    print(f"Evaluation cases: {len(case_ids)} unique; all NOT_RUN")
    print(f"Existing relative Markdown links: {links_checked}")
    print("Behavioral model evaluation: NOT_RUN (not inferred from structural checks)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

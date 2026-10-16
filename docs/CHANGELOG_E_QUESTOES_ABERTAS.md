# Changelog e questões abertas

## 3.0.1 — 16/10/2026 — correção do validador detectada por CI

- Corrigidas as expressões regulares Python: os escapes duplicados impediam reconhecer IDs normativos, CASE IDs e links Markdown.
- A primeira execução da CI em 3.0.0 falhou nestes controles; a falha foi tratada como defeito real, não ocultada como PASS.
- Metadados da versão foram alinhados para 3.0.1 nos artefatos versionados.
- Testes comportamentais em modelos externos continuam `NOT_RUN`; este patch corrige a detecção estrutural, não comprova obediência do modelo.


## 3.0.0 — 16/10/2026 — contratos estruturados e validação automática

**Base auditada:** `26d7396796ae13dd9332fb0feaf01e1df2f820c6`. O SHA do commit 3.0.0 será fornecido pelo Git, não antecipado artificialmente.

### Adicionado
- Protocolo JSON com hierarquia, estados, roteamento, riscos R0–R4, ferramentas e trilha de evidência.
- Registry de regras derivado dos cabeçalhos e schemas Draft 2020-12.
- Fixture JSON para 40 casos, todos NOT_RUN.
- Validador Python para JSON/schema, IDs, versões, links relativos e artefatos.
- Workflow GitHub Actions para push, pull request e execução manual.
- Documentação de arquitetura e registro de correções.
- Dez casos adicionais sobre schemas, injection, pós-condições, autorização, segredos, atualidade, codificação, fidelidade e evidência.

### Corrigido/esclarecido
- Registro dos dois commits da manutenção 2.0.1.
- Separação entre estado estrutural e comportamento.
- JSON/schema não provam verdade; CI não é benchmark.
- Sequências binárias e tokens invisíveis não conferem autoridade especial.
- O mapa de conflitos registra o papel dos artefatos machine-readable.

### Limites mantidos
- Avaliação comportamental externa: `NOT_RUN`.
- Eficácia geral do guia: `NOT_VERIFIED`.
- Auditoria jurídica integral de terceiros: `NOT_VERIFIED`.
- Links externos não são testados pela CI offline.
- Schemas validam estrutura, não semântica completa.

## 2.0.1 — manutenção editorial
- Corrigida a duplicação no mapa de conflitos.
- Commit estrutural: [4bc871a](https://github.com/guilhermemichael/WordRules/commit/4bc871a149e4a28dd968976b18cded1ce5a6f568).
- Commit de limpeza final: [26d7396](https://github.com/guilhermemichael/WordRules/commit/26d7396796ae13dd9332fb0feaf01e1df2f820c6).

## 2.0.0 — consolidação inicial
- Fusão editorial de A e B, núcleo, módulos, camada compacta, 30 casos, proveniência e mapa de conflitos.
- Discrepância histórica 5.406/5.410 preservada.

## Questões abertas
1. Executar os 40 casos em modelos e versões concretos, com baseline e saídas registradas.
2. Auditar licenças específicas se ativos/trechos de terceiros forem incorporados literalmente.
3. Revalidar referências voláteis de APIs, modelos e segurança.
4. Reproduzir a contagem histórica com pacote e método idênticos se necessário.
5. Definir licença geral para material original somente após decisão explícita do titular.

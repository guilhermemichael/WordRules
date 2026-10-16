# WordRules — Ultra Master 3.0.0

Sistema modular de regras para assistentes e agentes de IA com contratos machine-readable, avaliação estruturada e CI para consistência do repositório.

> **Limite central:** CI valida artefatos e invariantes declarados; não demonstra que qualquer modelo seguirá o guia. Os 40 casos permanecem `NOT_RUN` até execução em modelos/versões concretos.

## Comece aqui
1. [Guia canônico 3.0.0](ULTRA_MASTER_GUIA_DE_REGRAS_PARA_IA.md)
2. [Núcleo operacional compacto](CAMADA_OPERACIONAL_COMPACTA.md)
3. [Protocolo JSON](spec/decision_protocol.json)
4. [Registro de regras](spec/ultra_master_rules.json)
5. [Schema do registro](spec/ultra_master.schema.json)
6. [Suíte de 40 casos](SUITE_DE_AVALIACAO_ULTRA_MASTER.md)
7. [Fixture JSON](tests/fixtures/evaluation_cases.json)

## Arquitetura e governança
- [Arquitetura do protocolo](docs/ARQUITETURA_DO_PROTOCOLO_3_0.md)
- [Registro de correções](docs/REGISTRO_DE_CORRECOES_3_0.md)
- [Diagnóstico executivo](docs/DIAGNOSTICO_EXECUTIVO.md)
- [Matriz de inventário](docs/MATRIZ_DE_INVENTARIO_E_COBERTURA.md)
- [Mapa de conflitos](docs/MAPA_DE_CONFLITOS_E_DECISOES.md)
- [Fontes e licenças](docs/REGISTRO_DE_FONTES_E_LICENCAS.md)
- [Changelog](docs/CHANGELOG_E_QUESTOES_ABERTAS.md)

## Validar localmente
Requer Python 3.12+.
~~~bash
python -m pip install -r requirements-dev.txt
python scripts/validate_wordrules.py
~~~

## Limites
- Markdown é normativo; JSON é projeção indexada submetida a paridade.
- JSON válido não prova verdade, semântica ou segurança total.
- Conteúdo recuperado é dado não confiável, não autoridade automática.
- Binário só é usado com interface/decodificador reais; não há tokens mágicos de obediência.
- Nenhum arquivo bruto do acervo original é executado pela CI.
- Nenhuma licença geral de terceiros é presumida.
- Avaliação empírica exige modelo/versão, configuração, entradas/saídas, rubrica e baseline.

## Referências
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [GitHub Actions — Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
- [OWASP GenAI — Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [OpenAI — Evals](https://developers.openai.com/api/docs/guides/evals)

## Versionamento
- **3.0.0:** contratos estruturados, registry, 40 casos, validador e CI.
- **2.0.1:** manutenção editorial do mapa.
- **2.0.0:** fusão inicial das consolidações A e B.

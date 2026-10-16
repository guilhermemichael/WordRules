# Registro de correções e melhorias — 3.0.1

| ID | Achado | Correção | Verificação esperada | Limite |
|---|---|---|---|---|
| FIX-001 | IDs sem paridade automatizada. | Registry JSON derivado + schema. | IDs Markdown=JSON, únicos. | Não prova eficácia semântica. |
| FIX-002 | Suíte só em Markdown. | 40 casos e fixture JSON/schema. | Paridade de CASE IDs. | Casos NOT_RUN em modelos. |
| FIX-003 | Sem CI estrutural. | Workflow push/PR com validador. | Log de workflow. | Só verifica etapas declaradas. |
| FIX-004 | Camada compacta sem links para contratos. | Gatilhos e links adicionados. | Links e versão alinhados. | Não substitui guia integral. |
| FIX-005 | Estados de evidência confundíveis. | Oito estados explícitos. | Fixture/schema. | Reporte exige honestidade. |
| FIX-006 | Código binário confundível com controle. | Política de codificação real e auditável. | Regra no guia/protocolo. | Não controla modelos automaticamente. |
| FIX-007 | Falta de pós-condições. | Contratos e riscos R0–R4. | Protocolo publicado. | Risco depende do contexto. |
| FIX-008 | Histórico incompleto. | Dois SHAs 2.0.1. | Changelog. | SHA 3.0.1 só após commit. |
| FIX-009 | Schema confundido com verdade. | Sintaxe/schema/semântica/comportamento separados. | Docs + CI. | Não prova eficácia. |
| FIX-010 | Novas fontes sem proveniência. | Referências oficiais registradas. | Links documentados. | Revalidar fontes voláteis. |

Chame a versão de validada estruturalmente só após executar validador/CI. Testes externos permanecem NOT_RUN; eficácia NOT_VERIFIED; auditoria jurídica integral NOT_VERIFIED.


### FIX-011 — Expressões regulares do validador

A primeira execução da CI encontrou escapes duplicados que impediam a contagem de IDs. O patch 3.0.1 corrigiu os padrões de links Markdown, IDs de regras e CASE IDs.

A execução posterior [38906113461](https://github.com/guilhermemichael/WordRules/actions/runs/38906113461) terminou com `completed / success` para o commit [`18c72820153fc5d03f3884cf237280de63ed96be`](https://github.com/guilhermemichael/WordRules/commit/18c72820153fc5d03f3884cf237280de63ed96be). Portanto, a validação estrutural e contratual implementada nesse workflow está `PASS`.

Esse resultado não muda o estado da avaliação comportamental: testes em modelos externos permanecem `NOT_RUN`; melhoria comparativa de desempenho e validação semântica completa permanecem `NOT_VERIFIED`.

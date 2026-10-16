# Arquitetura do protocolo — Ultra Master 3.0.0

## Camadas
1. Referência normativa humana: guia Markdown.
2. Camada operacional compacta: roteamento leve.
3. Registro JSON: índice derivado, sem autoridade normativa independente.
4. Protocolo JSON: classes de tarefa, estados, risco e contratos de ferramenta.
5. Schemas Draft 2020-12.
6. Suíte Markdown e fixture JSON de 40 casos.
7. Validador local e GitHub Actions.

## Fluxo
`INTAKE → CLASSIFIED → INSPECTED → PLANNED → [RESEARCHED, se necessário] → PRODUCED → VALIDATED → DELIVERED`

Bloqueio produz PARTIAL ou BLOCKED com limitações registradas. O fluxo adapta-se à complexidade e não concede permissões por si só.

## Codificação estruturada
JSON/schema/IDs são legíveis, portáveis e verificáveis. Código binário, Base64 ou caracteres invisíveis não conferem autoridade especial. Só usar binário com interface e decodificador reais. JSON válido não prova verdade semântica.

## Evidência
O registro separa status estático e comportamental. Os 40 casos continuam NOT_RUN até execução real. CI valida estrutura, não qualidade comportamental.

## Manutenção
Atualizar guia, registry, schema, fixture, docs e changelog no mesmo changeset. Executar `python scripts/validate_wordrules.py` antes de publicar. Reconciliar se o SHA remoto avançar. Ver [fontes/licenças](REGISTRO_DE_FONTES_E_LICENCAS.md).

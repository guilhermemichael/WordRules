# Diagnóstico executivo — consolidação WordRules

**Data:** 16/10/2026
**Base:** consolidação editorial 2.0.0 das versões A e B. **Evolução 3.0.0:** contratos JSON/schema, validação determinística, fixture de 40 casos e CI; avaliação comportamental continua não executada.
**Estado global:** útil para revisão e uso controlado; não equivale a auditoria exaustiva de todos os arquivos nem a benchmark de modelos.

## Addendum de engenharia — 3.0.0

A versão 3.0.0 adiciona registry de regras JSON, protocolo de roteamento/efeitos, schemas Draft 2020-12, fixture de 40 casos, validador e workflow CI. Esses controles verificam consistência dos arquivos, não comportamento de modelos. Ver [registro de correções 3.0.0](REGISTRO_DE_CORRECOES_3_0.md).

## 1. O que foi encontrado

O ZIP externo contém 13 itens de arquivo: 12 arquivos nomeados `.zip` e um arquivo `Não confirmado 351560.crdownload`. O item `.crdownload` foi reconhecido como ZIP, aberto e aprovado no teste CRC; a estrutura interna aponta para `TheBigPromptLibrary-main`. Isso confirma legibilidade estrutural no pacote recebido, não origem, autoria, integridade semântica ou autenticidade de cada prompt.

A recomputação desta edição encontrou **5.406 entradas internas não vazias** nos 13 contêineres disponíveis (12 ZIP e 1 arquivo `.crdownload`), com diretórios excluídos e cada entrada interna contada uma vez por contêiner. A versão B registrava 5.410; esse valor histórico é preservado como discrepância porque a definição/pacote contado não foi idêntico. O acervo reúne coleções de regras anti-slop, skills de agentes, design/motion, UX/UI, direção de arte, prompts de imagem/vídeo, marketing, software de infraestrutura de APIs e uma biblioteca ampla de custom instructions, prompts de sistema, artigos e jailbreaks.

## 2. Forças principais

- Há conteúdo especializado útil, em vez de apenas instruções genéricas: skills por domínio, exemplos e critérios de avaliação.
- As fontes anti-slop dão destaque à preservação da voz e à detecção de padrões repetitivos sem exigir que toda escrita soe igual.
- As coleções de UX, design e motion permitem converter preferências visuais em critérios observáveis, desde que condicionais.
- As skills de vídeo e imagem enfatizam decomposição de cena, referências e restrições específicas de ferramenta.
- As coleções de skills oferecem bons exemplos de modularidade e carregamento por tarefa.
- O acervo inclui fontes com changelogs, licenças e evals, permitindo uma abordagem mais rastreável que simples colagem.

## 3. Problemas críticos

1. **Mistura de tipos:** código de infraestrutura, exemplos de prompts, skills operacionais e princípios comportamentais não são equivalentes.
2. **Risco de absolutismo estético:** regras fortes de design podem produzir uniformidade se tratadas como leis universais.
3. **Risco de voz achatada:** anti-slop aplicado como lista proibida pode esterilizar humor, emoção e escolhas autorais.
4. **Risco de versionamento:** parâmetros de APIs, modelos, técnicas de difusão e skills podem mudar; arquivos locais são capturas e não necessariamente estado atual.
5. **Risco de proveniência:** biblioteca de prompts inclui material de autenticidade e finalidade heterogêneas; conteúdo chamado “system prompt” não é automaticamente oficial.
6. **Risco de segurança:** jailbreaks e instruções adversariais devem ser estudados como conteúdo não confiável, nunca convertidos em instruções normativas.
7. **Risco de licença:** licença raiz não prova cobertura de todos os recursos, imagens, fontes ou conteúdos de terceiros.
8. **Risco de falsa validação:** testes de um repositório, relatos de autores ou discussões comunitárias não demonstram eficácia universal.
9. **Risco de excesso de contexto:** incorporar milhares de prompts ao núcleo aumentaria redundância e conflito sem garantir melhor comportamento.
10. **Cobertura limitada:** a coleção é grande demais para afirmar leitura semântica integral de todos os arquivos nesta etapa; a cobertura é estrutural ampla e leitura dirigida de fontes centrais.

## 4. Decisões editoriais

- Criar um núcleo normativo único e modular, com IDs canônicos.
- Tratar os materiais anti-slop como heurísticas editoriais com preservação de voz.
- Converter taste/UI/motion em critérios contextuais, não presets obrigatórios.
- Separar imagem e vídeo, com regras próprias para fidelidade, continuidade e dependência de modelo.
- Reduzir os milhares de prompts de marketing a uma taxonomia e princípios duradouros.
- Classificar FreeLLMAPI como infraestrutura de software, não como norma de comportamento.
- Isolar TheBigPromptLibrary como referência histórica/de segurança; não adotar jailbreaks nem supostos prompts internos como autoridade.
- Adotar `PASS`, `FAIL`, `NOT VERIFIED`, `NOT APPLICABLE` e distinguir auditoria estática de teste real.
- Registrar fontes, licenças aparentes, hashes de pacote e limitações sem alegar verificação não realizada.

## 5. Pesquisa externa

Foram abertas fontes oficiais de OpenAI sobre prompt engineering, Anthropic sobre skills, a especificação aberta Agent Skills, documentação Google sobre contexto longo e a edição 2026 do OWASP GenAI LLM Top 10. Também foram abertas referências comunitárias do Reddit sobre avaliação e arquitetura de prompts. O registro detalhado está em `docs/REGISTRO_DE_FONTES_E_LICENCAS.md`.

As discussões comunitárias foram usadas apenas para identificar hipóteses e fricções, não como prova científica. A OWASP é uma referência comunitária estruturada de riscos, não substituto para modelagem de ameaça específica.

## 6. Entregáveis produzidos

- `ULTRA_MASTER_GUIA_DE_REGRAS_PARA_IA.md`: referência canônica integral.
- `docs/MATRIZ_DE_INVENTARIO_E_COBERTURA.md`: inventário, integridade, hashes, classificação, licença aparente e decisões.
- `docs/MAPA_DE_CONFLITOS_E_DECISOES.md`: conflitos e decisões de consolidação.
- `CAMADA_OPERACIONAL_COMPACTA.md`: núcleo de uso rápido.
- `SUITE_DE_AVALIACAO_ULTRA_MASTER.md`: 30 cenários com módulos, esperado, falhas, critérios e gravidade.
- `docs/REGISTRO_DE_FONTES_E_LICENCAS.md`: fontes externas e locais.
- `docs/CHANGELOG_E_QUESTOES_ABERTAS.md`: decisões, questões pendentes e gate final.

## 7. Limitações reais

- Não foi feito clone Git nem verificação de commit remoto para cada ZIP.
- Não foram lidos integralmente todos os milhares de prompts, recursos visuais, exemplos e arquivos de código.
- Nenhum script foi executado e nenhuma skill foi instalada.
- Não houve execução da suíte em modelos externos nem benchmark comparativo; os casos são especificações e auditoria editorial estática.
- Licenças foram identificadas por arquivos presentes e leituras pontuais; não é parecer jurídico.
- A pesquisa externa foi seletiva, embora tenha incluído fontes oficiais, repositórios, documentação e Reddit. URLs canônicas de projetos locais foram obtidas de READMEs quando disponíveis; nem todos os commits/releases foram revalidados individualmente.

## 8. Conclusão

A consolidação transforma o acervo em uma arquitetura de referência coerente e utilizável, sem alegar que todos os itens individuais foram exaustivamente lidos ou testados. O próximo estágio de maior valor é validar os 30 casos em modelos e versões específicos, registrar resultados brutos e revisar regras que falhem repetidamente.

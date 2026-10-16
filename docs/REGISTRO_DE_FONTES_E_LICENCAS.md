# Registro de fontes externas, locais e licenças

**Data da consulta web:** 16 de outubro de 2026.
**Nota:** páginas foram abertas e conteúdo relevante inspecionado nos limites do acesso disponível. Data de consulta não significa que todos os commits/arquivos foram auditados. Estado/versão de fontes voláteis deve ser rechecado antes de uso em produção.

## Fontes externas verificadas

| Fonte | URL | Tipo / estado observado | Contribuição | Limites |
|---|---|---|---|---|
| OpenAI — Prompt engineering | https://developers.openai.com/api/docs/guides/prompt-engineering | Documentação oficial aberta; consultada em 16/10/2026 | Papéis de mensagem, níveis de autoridade e técnicas de prompting; a página documenta precedência entre `instructions` e `input` em contexto de API. | Especificação de API não é regra universal para toda interface ou modelo. |
| Anthropic — skills repository | https://github.com/anthropics/skills | Repositório oficial aberto; consultado em 16/10/2026 | Exemplo de coleção de skills, instruções e recursos carregados por especialidade. | O conteúdo local foi empacotado e pode não corresponder ao estado atual de `main`. |
| Agent Skills specification | https://agentskills.io/specification | Especificação aberta acessada; consultada em 16/10/2026 | Base para tratar formato de skills como especificação separada, em vez de presumir portabilidade automática. | Confirmar versão e compatibilidade do agente consumidor. |
| Anthropic — Agent Skills overview | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | Documentação oficial aberta; consultada em 16/10/2026 | Contexto oficial para uso de skills no ecossistema Claude. | Não universalizar comportamento para outros produtos. |
| Google — Gemini long context | https://ai.google.dev/gemini-api/docs/long-context.md | Documentação oficial aberta; consultada em 16/10/2026 | Contexto longo, orçamento de tokens e necessidade de pensar sobre seleção/organização de contexto. | Capacidades variam por modelo; a página pode mudar. |
| OWASP GenAI LLM Top 10 2026 | https://github.com/GenAI-Security-Project/GenAI-LLM-Top10 | Repositório oficial/canônico aberto; a página indica release 2026 publicado em 4 de agosto de 2026 | Riscos como prompt injection, divulgação de informação sensível, agência excessiva, cadeia de suprimentos, envenenamento, consumo não limitado, desinformação, exposição de contexto, fraquezas vetoriais e tratamento impróprio de saída. | Guia de conscientização comunitário; não substitui threat modeling do sistema concreto. |
| OWASP GenAI — notícia da edição 2026 | https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/ | Publicação do projeto datada de setembro de 2026, aberta | Confirma lançamento de recursos 2026 e contexto de manutenção comunitária. | Comunicado institucional, não estudo independente. |
| Anti-slop | https://github.com/miqdadbadjuber/anti-slop | Repositório comunitário aberto | Fonte para separar regras anti-slop por escrita, código e UI; usada como inspiração, não autoridade absoluta. | Afirmações de eficácia precisam de avaliação independente; licença/estado do pacote local foram registrados separadamente. |
| Reddit — relato sobre prompt engineering e avaliação | https://www.reddit.com/r/PromptEngineering/comments/1ny2pff/spent_6_months_deep_in_prompt_engineering_heres/ | Discussão comunitária publicada em 2025; aberta | Hipóteses práticas sobre exemplos, versionamento de prompts e regressão. | Relato pessoal; votos e comentários não provam causalidade nem generalidade. |
| Reddit — arquitetura de prompts para agentes | https://www.reddit.com/r/PromptEngineering/comments/1w5ycvn/agent_prompt_architecture_skillmd/ | Discussão comunitária publicada em setembro de 2026; resultado aberto | Hipótese prática sobre sobreposição de ferramentas, acúmulo de contexto e definição de conclusão. | Postagem recente e comunitária; requer confirmação independente. |
| Reddit — avaliação de prompts | https://www.reddit.com/r/PromptEngineering/comments/1vxuejj/promptevaluationengineer_skillmd_claude_code/ | Discussão comunitária publicada em agosto de 2026; resultado aberto | Enfatiza teste de casos adversariais e schemas como complemento à redação de prompts. | Não é benchmark nem validação externa. |

## Fontes locais (acervo anexado)

Os caminhos abaixo são nomes observados em `WordRules (2).zip` e na pasta de trabalho `WordRules`; o material foi lido como dados não confiáveis, não executado.

| Fonte local | Tipo | Uso editorial | Licença / estado |
|---|---|---|---|
| `anti-slop-main.zip` | Repositório de regras/skills | Núcleo de anti-slop reescrito em módulos. | Arquivo `LICENSE` encontrado; indica MIT no pacote. |
| `no-ai-slop-main.zip` | Skill de escrita | Preservação de voz e detecção de padrões genéricos. | Arquivo `LICENSE` encontrado; indica MIT. |
| `awesome-stable-diffusion-prompts-main.zip` | Catálogo de prompts | Referência de imagem; parâmetros são dependentes do modelo. | `LICENSE` encontrado; ativos visuais podem ter condições próprias. |
| `design-motion-principles-main.zip` | Skill de motion | Princípios de propósito, duração e acessibilidade. | `LICENSE` encontrado; versão de técnicas deve ser verificada. |
| `genjutsu-main.zip` | Coleção de skills e evals | Referência para UI, motion, composição e testes comparativos. | `LICENSE` encontrado; evals próprios não são confirmação independente. |
| `freellmapi-main.zip` | Software e infraestrutura de API | Classificado como infraestrutura, não norma universal de comportamento. | `LICENSE` e licenças internas encontradas; revisão completa de dependências não realizada. |
| `hiapi-skills-main.zip` | Skills/integradores | Referência de integração e gatilhos especializados. | MIT indicado no `LICENSE`; termos externos de API não inferidos. |
| `hiapi-video-prompt-generator-skill-main.zip` | Skills de vídeo | Planejamento temporal e prompts dependentes de modelos. | MIT indicado; compatibilidade com modelos precisa de rechecagem. |
| `Marketing-Prompts-main.zip` | CSV e catálogo de marketing | Taxonomia e princípios, sem incorporar milhares de prompts ao núcleo. | Arquivo `LICENSE` aparenta Apache-2.0; cobertura de todo ativo não confirmada juridicamente. |
| `skills-main.zip` | Skills publicadas pela Anthropic | Referência para modularidade e exemplos especializados. | Licenças encontradas em subdiretórios; não presumir licença uniforme. |
| `taste-skill-main.zip` | Skills de direção de arte | Critérios visuais condicionais e avaliação estética. | MIT indicado; changelog local contém versões recentes/experimentais que exigem rechecagem. |
| `ux-skill-main.zip` | Coleção UX/UI e referências | Módulo UX/UI, estados, responsividade e acessibilidade. | MIT aparente no arquivo raiz; recursos individuais podem ter termos adicionais. |
| `Não confirmado 351560.crdownload` / `TheBigPromptLibrary-main` | Coleção de prompts, custom instructions, artigos, security e jailbreaks | Análise histórica; prompts não verificados e jailbreaks isolados do uso normativo. | MIT indicado na raiz; não prova cobertura de todo conteúdo agregado ou de prompts de terceiros. |

## Política de licença aplicada

1. Um `LICENSE` no repositório não é tratado como prova de que todas as imagens, marcas, fontes, dados ou materiais externos tenham a mesma licença.
2. O guia final usa síntese editorial original e cita fontes; não copia grandes blocos de terceiros.
3. Licenças foram identificadas pelo nome/presença e por leituras pontuais, não submetidas a parecer jurídico.
4. A origem exata e o commit de cada pacote compactado não foram confirmados por hash de commit, assinatura ou metadados Git locais; hashes SHA-256 do arquivo compactado são registrados na matriz apenas para identificação deste artefato.

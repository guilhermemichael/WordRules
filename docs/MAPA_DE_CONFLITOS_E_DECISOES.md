# Mapa de conflitos e decisões de consolidação

**Versão do mapa:** 3.0.1
**Data da manutenção:** 16 de outubro de 2026
**Escopo:** reconciliação semântica das versões A e B e das fontes que fundamentam o guia canônico.

| Tema / fontes relacionadas | Tensão observada | Decisão canônica | Consequência |
|---|---|---|---|
| `anti-slop` + `no-ai-slop` + `taste-skill` | Anti-padrões textuais e visuais podem virar listas rígidas. | Tratar como detectores de padrões e critérios contextuais, não proibições lexicais ou estéticas universais. | Preservar voz, gênero textual e briefing. |
| `ux-skill` + `genjutsu` + `taste-skill` | Regras prescritivas de UI podem sobrepor-se ao contexto do produto. | Núcleo exige estados, hierarquia, acessibilidade e honestidade; estética fica condicionada ao público e tarefa. | Evitar “um único estilo para tudo”. |
| `design-motion-principles` + skills de motion de `genjutsu` | Animação pode ser polimento ou ruído. | Movimento precisa de propósito, acessibilidade e verificação de repetição/desempenho. | Não exigir animação em toda interface. |
| `awesome-stable-diffusion-prompts` + skills de imagem de outras coleções | Tokens e parâmetros são dependentes do modelo. | Separar composição visual geral de sintaxe específica; verificar documentação do modelo. | Nenhum token é prometido como garantia universal. |
| Skills de vídeo HiAPI + biblioteca de prompts | Prompts podem especificar sequência, mas modelos variam em duração, câmera, áudio e referências. | Módulo de vídeo temporal, com ficha de continuidade e versão de ferramenta. | Evita transportar regras de vídeo para imagem/código. |
| `Marketing-Prompts` em grande escala + núcleo comportamental | Volume de prompts pode inflar o guia e introduzir repetição. | Extrair taxonomia e princípios; exemplos ficam como catálogo de referência. | Núcleo menor e mais sustentável. |
| `freellmapi` + skills de agente | Repositório de software é confundível com guia de comportamento. | Classificar como infraestrutura e consultar apenas para integrações/arquitetura. | Não converter código em norma universal. |
| `skills-main` + `hiapi-skills` + formatos `AGENTS.md`/`SKILL.md` | Formatos e gatilhos não são necessariamente portáveis. | Especificação de skills é módulo técnico e depende do ambiente. | Não presumir que uma skill funcione igual em todos os agentes. |
| `TheBigPromptLibrary` (system prompts/custom instructions) | Material oficial, comunitário, extraído e não verificado aparece junto. | Classificar proveniência; não adotar supostos vazamentos como fonte normativa. | Evita falsa autoridade e cópia indevida. |
| `TheBigPromptLibrary` (jailbreaks/security) | Técnicas adversariais podem ser confundidas com instruções recomendadas. | Isolar como material descritivo de segurança; não operacionalizar evasões. | Mantém foco preventivo. |
| Licenças de raiz e ativos embutidos | Uma licença principal pode não cobrir todos os arquivos. | Registrar licença aparente e ressalva; auditar recursos separadamente quando redistribuir. | Não emitir garantia jurídica. |
| Evals locais e relatos Reddit | Avaliação autorrelatada não é replicação independente. | Usar como hipótese; criar suíte com critérios e registrar execução real separadamente. | Não declarar eficácia sem evidência. |
| Contexto longo e instruções extensas | Guia muito grande pode aumentar redundância e competir por atenção. | Guia integral para consulta + camada operacional compacta + módulos sob demanda. | Profundidade sem carregar tudo em toda tarefa. |
| Regra de segurança e utilidade | Bloqueio total pode impedir ajuda legítima; autonomia excessiva pode causar danos. | Menor privilégio, autorização para ações relevantes e alternativa segura quando possível. | Segurança contextual e útil. |

| Registro machine-readable | JSON e Markdown podem divergir se atualizados separadamente. | Markdown fica normativo; CI compara IDs do guia/registry e da suíte/fixture. | Divergência detectável. |
| Codificação opaca | Strings binárias podem parecer controle sem protocolo que as interprete. | Usar JSON, schemas e IDs; binário só com interface/decodificador reais. | Sem alegação de obediência mágica. |
| Avaliação conceitual | Uma suíte escrita não comprova desempenho de modelo. | Manter resultados comportamentais como NOT_RUN até testes reais. | Sem ganho não medido. |

## Notas de confiança

- **Alta:** integridade estrutural ZIP/CRC; nomes e quantidades de entradas observadas; conteúdo textual explicitamente lido.
- **Média:** classificação temática dos repositórios e síntese editorial de seus READMEs/skills representativos.
- **Baixa ou não verificada:** eficácia geral de técnicas, origem de prompts copiados, licenças de ativos embutidos, atualidade de cada commit e comportamento em modelos externos.

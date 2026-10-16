# Matriz de inventário e proveniência

**Data da inspeção:** 16/10/2026. **Fontes:** `WordRules (2).zip`, pasta `WordRules` disponível e pacote de entrega B. A integridade foi testada por leitura de entradas e fluxo de bytes com `System.IO.Compression.ZipFile`; isso não autentica autoria, atualização, conteúdo semântico ou legitimidade.

## Resumo verificável

- Entradas de arquivo no ZIP externo: 13 (mais o diretório-raiz).
- Entradas internas recomputadas: **5.406 não vazias** (diretórios excluídos; soma das 13 fontes; cada entrada contada por contêiner).
- Valor histórico da versão B: **5.410**, mantido como `DISCREPANCY` porque a definição/pacote contado não foi idêntico.
- ZIP externo: CRC PASS; 13 itens de arquivo listados.
- Arquivos internos compactados: todos os 13 itens foram reconhecidos como ZIP e passaram no teste CRC nesta inspeção.
- O item `Não confirmado 351560.crdownload` foi reconhecido estruturalmente como ZIP, com 2.447 entradas e CRC PASS. A extensão incomum não prova download incompleto nem autenticidade; o conteúdo foi classificado como TheBigPromptLibrary pela estrutura interna.
- O acervo inclui coleções grandes (por exemplo, UX Skill e FreeLLMAPI) com centenas/milhares de arquivos. Esta entrega combina inventário estrutural com inspeção de documentos principais e amostragem orientada por relevância; **não declara leitura integral de cada arquivo de cada repositório**.
- Nenhum script ou código do acervo foi executado.

## Matriz por pacote

| Pacote | Entradas | Integridade ZIP/CRC | Arquivos de licença encontrados | README(s) raiz aproximados | Arquivos de instrução (SKILL/AGENTS etc.) | Domínio / decisão | Contribuição e ressalva |
|---|---:|---|---:|---:|---:|---|---|
| `anti-slop-main.zip` | 59 | PASS | 1 | 1 | 6 | Escrita, UI, código, comportamento de agente; Incorporar com reescrita modular | Redução de padrões genéricos; especialização por domínio. Evitar regras estilísticas absolutas. Licença: MIT indicado no LICENSE; validade de cada asset não auditada individualmente. |
| `awesome-stable-diffusion-prompts-main.zip` | 8 | PASS | 1 | 1 | 0 | Prompts de imagem e exemplos; Manter como referência / módulo de imagem | Exemplos e técnicas de prompting; sintaxe e eficácia dependem do modelo. Licença: LICENSE presente; verificar recursos visuais e licenças de imagens separadamente. |
| `design-motion-principles-main.zip` | 18 | PASS | 1 | 1 | 1 | Motion e interação; Reescrever e incorporar ao módulo | Princípios para propósito, temporalidade e auditoria de animações. Licença: LICENSE presente; conferir detalhes e versões antes de adoção técnica. |
| `freellmapi-main.zip` | 1206 | PASS | 2 | 10 | 0 | Software, APIs e infraestrutura; Referência técnica; não núcleo normativo | Arquitetura de roteamento, SDKs, ferramentas e operação; não confundir código de infraestrutura com regras de comportamento. Licença: LICENSE presente; subcomponentes podem ter licenças próprias. |
| `genjutsu-main.zip` | 245 | PASS | 2 | 2 | 20 | Skills de interface, animação, composição e código visual; Mover para módulos especializados | Skills e avaliações para UI, motion, gráficos e implementação visual. Avaliações próprias não são validação independente. Licença: LICENSE presente; claims de versões requerem nova checagem. |
| `hiapi-skills-main.zip` | 27 | PASS | 1 | 1 | 0 | Skills e integração de ferramentas/modelos; Módulo / referência especializada | Catálogo de skills e handoffs; dependências de fornecedor e APIs. Licença: MIT identificado; conferir termos de serviço e recursos externos. |
| `hiapi-video-prompt-generator-skill-main.zip` | 29 | PASS | 1 | 3 | 3 | Prompt de vídeo; Reescrever no módulo de vídeo | Planejamento temporal, storyboards, referências e restrições de modelo. Licença: MIT indicado; claims específicos de modelo são voláteis. |
| `Marketing-Prompts-main.zip` | 3 | PASS | 1 | 1 | 0 | Catálogo de prompts de marketing; Extrair taxonomia; não importar em massa | Grande catálogo de prompts e CSV. Núcleo deve preservar princípios, não milhares de modelos repetitivos. Licença: Apache-2.0 aparente no LICENSE; assets/dados devem ser conferidos conforme distribuição. |
| `no-ai-slop-main.zip` | 14 | PASS | 1 | 1 | 1 | Escrita e edição anti-slop; Incorporar com reescrita | Detectar padrões genéricos sem apagar voz, cadência e intenção do autor. Licença: MIT indicado. |
| `Não confirmado 351560.crdownload` | 2277 | PASS | 2 | 28 | 25 | Prompts de sistema, custom instructions, segurança, artigos e jailbreaks; Isolar; referência histórica e análise de segurança | Coleção ampla e heterogênea; proveniência de cada prompt variável. Jailbreaks e supostos prompts internos não são fonte normativa. Licença: LICENSE MIT aparente na raiz; não assume cobertura de todos os conteúdos agregados. |
| `skills-main.zip` | 445 | PASS | 18 | 14 | 20 | Skills e exemplos de fluxos especializados; Referência para arquitetura modular; adotar por escopo | Exemplos de skill, descrição de gatilhos e recursos; formato é dependente de ecossistema. Licença: LICENSE por skill presente em vários diretórios; não inferir uma licença global uniforme. |
| `taste-skill-main.zip` | 89 | PASS | 1 | 4 | 14 | Direção de arte, design e avaliação visual; Incorporar como heurísticas condicionais | Critérios para especificidade estética, evitar resultados genéricos e avaliar visual. Licença: MIT aparente; versão/experimentalidade indicada em changelog precisa ser revalidada. |
| `ux-skill-main.zip` | 990 | PASS | 1 | 4 | 1 | UX/UI, design e recursos de referência; Incorporar ao módulo UX com ressalvas | Amplo conjunto de orientação, exemplos e referências; distinguir regras, exemplos, recursos e código. Licença: MIT aparente; diretórios e assets individuais podem exigir auditoria de licença. |

## Cobertura de inspeção e limitações

- **Inspecionado estruturalmente:** nomes de todos os itens do ZIP externo, nomes e quantidades de entradas em cada ZIP, integridade CRC, quantidade aproximada de READMEs, arquivos de licença e arquivos de instrução.
- **Inspecionado por leitura dirigida:** READMEs principais e documentos representativos de anti-slop, skills, vídeo, UX, taste/design, marketing, motion e TheBigPromptLibrary; o guia também incorpora o texto de tarefa fornecido pelo usuário.
- **Não inspecionado integralmente:** cada um dos milhares de prompts individuais, imagens de referência, todos os exemplos, todas as dependências, todo o código de FreeLLMAPI e todos os arquivos auxiliares do acervo.
- **Não verificado:** estado de cada commit no momento do empacotamento, origem exata dos downloads, todas as licenças de terceiros, conteúdo binário não textual e funcionamento real das skills em cada modelo.
- **Cuidado:** o inventário lista contagens derivadas dos ZIPs, mas a classificação de relevância/decisão é uma síntese editorial. Licença aparente no arquivo raiz não equivale a parecer jurídico nem prova cobertura de todos os ativos.

### Anti-slop / regras e skills
- **Arquivo:** `WordRules/anti-slop-main.zip`
- **SHA-256 do arquivo compactado:** `0773c1b4996ddb3b9552cea75828cc0b6594ccf742e31b3aaaf3e5b5e4b9cdf9`
- **Tamanho:** 973,418 bytes; **entradas internas:** 59; **integridade:** PASS.
- **Classificação:** Escrita, UI, código, comportamento de agente.
- **Decisão editorial:** Incorporar com reescrita modular.
- **Contribuição:** Redução de padrões genéricos; especialização por domínio. Evitar regras estilísticas absolutas.
- **Licença / ressalva:** MIT indicado no LICENSE; validade de cada asset não auditada individualmente.

### Awesome Stable Diffusion Prompts
- **Arquivo:** `WordRules/awesome-stable-diffusion-prompts-main.zip`
- **SHA-256 do arquivo compactado:** `4b51a293d62d18887bb8a084b71a6889c876b66123979341bc1e81f170365b85`
- **Tamanho:** 1,766,235 bytes; **entradas internas:** 8; **integridade:** PASS.
- **Classificação:** Prompts de imagem e exemplos.
- **Decisão editorial:** Manter como referência / módulo de imagem.
- **Contribuição:** Exemplos e técnicas de prompting; sintaxe e eficácia dependem do modelo.
- **Licença / ressalva:** LICENSE presente; verificar recursos visuais e licenças de imagens separadamente.

### Design Motion Principles
- **Arquivo:** `WordRules/design-motion-principles-main.zip`
- **SHA-256 do arquivo compactado:** `6015c8f0be1fb3490f92902fe9e2734f03610c51d8236f7015d2a258985a08b5`
- **Tamanho:** 74,961 bytes; **entradas internas:** 18; **integridade:** PASS.
- **Classificação:** Motion e interação.
- **Decisão editorial:** Reescrever e incorporar ao módulo.
- **Contribuição:** Princípios para propósito, temporalidade e auditoria de animações.
- **Licença / ressalva:** LICENSE presente; conferir detalhes e versões antes de adoção técnica.

### FreeLLMAPI
- **Arquivo:** `WordRules/freellmapi-main.zip`
- **SHA-256 do arquivo compactado:** `962b5fc58f1547444c43bcc750db70e17753bc18d91c5fad66db86fabefe1efa`
- **Tamanho:** 8,564,156 bytes; **entradas internas:** 1206; **integridade:** PASS.
- **Classificação:** Software, APIs e infraestrutura.
- **Decisão editorial:** Referência técnica; não núcleo normativo.
- **Contribuição:** Arquitetura de roteamento, SDKs, ferramentas e operação; não confundir código de infraestrutura com regras de comportamento.
- **Licença / ressalva:** LICENSE presente; subcomponentes podem ter licenças próprias.

### Genjutsu
- **Arquivo:** `WordRules/genjutsu-main.zip`
- **SHA-256 do arquivo compactado:** `0624b81bac99722353221a49c8dcae8fc14826af8c2bf5e1b11ff2b1379b4606`
- **Tamanho:** 1,044,333 bytes; **entradas internas:** 245; **integridade:** PASS.
- **Classificação:** Skills de interface, animação, composição e código visual.
- **Decisão editorial:** Mover para módulos especializados.
- **Contribuição:** Skills e avaliações para UI, motion, gráficos e implementação visual. Avaliações próprias não são validação independente.
- **Licença / ressalva:** LICENSE presente; claims de versões requerem nova checagem.

### HiAPI Skills
- **Arquivo:** `WordRules/hiapi-skills-main.zip`
- **SHA-256 do arquivo compactado:** `ceefb2f2920cf0ad444b9b8a856adc95c9766331e11d36bbfa84734fa7950371`
- **Tamanho:** 210,802 bytes; **entradas internas:** 27; **integridade:** PASS.
- **Classificação:** Skills e integração de ferramentas/modelos.
- **Decisão editorial:** Módulo / referência especializada.
- **Contribuição:** Catálogo de skills e handoffs; dependências de fornecedor e APIs.
- **Licença / ressalva:** MIT identificado; conferir termos de serviço e recursos externos.

### HiAPI Video Prompt Generator
- **Arquivo:** `WordRules/hiapi-video-prompt-generator-skill-main.zip`
- **SHA-256 do arquivo compactado:** `f094bce8155467cbeb75c56a4a7cc056241e4138105d654082780926eac24220`
- **Tamanho:** 71,166 bytes; **entradas internas:** 29; **integridade:** PASS.
- **Classificação:** Prompt de vídeo.
- **Decisão editorial:** Reescrever no módulo de vídeo.
- **Contribuição:** Planejamento temporal, storyboards, referências e restrições de modelo.
- **Licença / ressalva:** MIT indicado; claims específicos de modelo são voláteis.

### Marketing Prompts
- **Arquivo:** `WordRules/Marketing-Prompts-main.zip`
- **SHA-256 do arquivo compactado:** `4ad4ff74c8209cce7becf06b8239e7cd76689f843e0f84fa9da503503a29e3f5`
- **Tamanho:** 130,860 bytes; **entradas internas:** 3; **integridade:** PASS.
- **Classificação:** Catálogo de prompts de marketing.
- **Decisão editorial:** Extrair taxonomia; não importar em massa.
- **Contribuição:** Grande catálogo de prompts e CSV. Núcleo deve preservar princípios, não milhares de modelos repetitivos.
- **Licença / ressalva:** Apache-2.0 aparente no LICENSE; assets/dados devem ser conferidos conforme distribuição.

### No AI Slop
- **Arquivo:** `WordRules/no-ai-slop-main.zip`
- **SHA-256 do arquivo compactado:** `59c435f1c92e86f58513ede3e649b20b4b4d1db0b1f0c81592943ae1937aaef6`
- **Tamanho:** 250,741 bytes; **entradas internas:** 14; **integridade:** PASS.
- **Classificação:** Escrita e edição anti-slop.
- **Decisão editorial:** Incorporar com reescrita.
- **Contribuição:** Detectar padrões genéricos sem apagar voz, cadência e intenção do autor.
- **Licença / ressalva:** MIT indicado.

### The Big Prompt Library (ZIP sob extensão .crdownload)
- **Arquivo:** `WordRules/Não confirmado 351560.crdownload`
- **SHA-256 do arquivo compactado:** `bd15ccc25bd43d22380440300e19d6ac48d8b97b4a5309b0c2ed4a0623f54783`
- **Tamanho:** 33,463,612 bytes; **entradas internas:** 2277; **integridade:** PASS.
- **Classificação:** Prompts de sistema, custom instructions, segurança, artigos e jailbreaks.
- **Decisão editorial:** Isolar; referência histórica e análise de segurança.
- **Contribuição:** Coleção ampla e heterogênea; proveniência de cada prompt variável. Jailbreaks e supostos prompts internos não são fonte normativa.
- **Licença / ressalva:** LICENSE MIT aparente na raiz; não assume cobertura de todos os conteúdos agregados.

### Anthropic Skills
- **Arquivo:** `WordRules/skills-main.zip`
- **SHA-256 do arquivo compactado:** `149d804241449c2a382079de32e37032ba6a18eb7621ec20217ce4974e1fbc21`
- **Tamanho:** 4,304,638 bytes; **entradas internas:** 445; **integridade:** PASS.
- **Classificação:** Skills e exemplos de fluxos especializados.
- **Decisão editorial:** Referência para arquitetura modular; adotar por escopo.
- **Contribuição:** Exemplos de skill, descrição de gatilhos e recursos; formato é dependente de ecossistema.
- **Licença / ressalva:** LICENSE por skill presente em vários diretórios; não inferir uma licença global uniforme.

### Taste Skill
- **Arquivo:** `WordRules/taste-skill-main.zip`
- **SHA-256 do arquivo compactado:** `374478f49de6268cc6f70e3e72495cbf7f9006dc71433c555d7d22b5b8d34794`
- **Tamanho:** 1,268,314 bytes; **entradas internas:** 89; **integridade:** PASS.
- **Classificação:** Direção de arte, design e avaliação visual.
- **Decisão editorial:** Incorporar como heurísticas condicionais.
- **Contribuição:** Critérios para especificidade estética, evitar resultados genéricos e avaliar visual.
- **Licença / ressalva:** MIT aparente; versão/experimentalidade indicada em changelog precisa ser revalidada.

### UX Skill
- **Arquivo:** `WordRules/ux-skill-main.zip`
- **SHA-256 do arquivo compactado:** `4c9b504e49aafd1a23a91bb388beab896c5122ba3e65610cb8c3255a3f2fa08d`
- **Tamanho:** 45,778,661 bytes; **entradas internas:** 990; **integridade:** PASS.
- **Classificação:** UX/UI, design e recursos de referência.
- **Decisão editorial:** Incorporar ao módulo UX com ressalvas.
- **Contribuição:** Amplo conjunto de orientação, exemplos e referências; distinguir regras, exemplos, recursos e código.
- **Licença / ressalva:** MIT aparente; diretórios e assets individuais podem exigir auditoria de licença.

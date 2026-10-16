# Changelog e questões em aberto

## 2.0.1 — manutenção editorial

- Removida a reprodução do diagnóstico executivo no início de `docs/MAPA_DE_CONFLITOS_E_DECISOES.md`.
- Mantido o diagnóstico exclusivamente em `docs/DIAGNOSTICO_EXECUTIVO.md`.
- Alinhado o título e o escopo do mapa à sua finalidade específica.
- Commit de manutenção: será registrado após a confirmação do push remoto.

## 2.0.0 — 16/10/2026

Fusão editorial das consolidações A e B. A arquitetura granular da B foi preservada; a concisão, a ressalva de proveniência e a contagem recomputada da A foram incorporadas. O guia, a camada compacta e a suíte foram sincronizados.

### Criado
- Guia canônico em português brasileiro com hierarquia, núcleo universal, método adaptativo e módulos de escrita, código, UX/UI, direção visual, motion, imagem, vídeo, marketing, ferramentas e segurança.
- Taxonomia de IDs e fichas de regra para itens críticos.
- Matriz de inventário estrutural, SHA-256 dos pacotes, teste de CRC e classificação editorial.
- Diagnóstico e mapa de conflitos.
- Camada operacional compacta.
- Suíte de 30 casos conceituais e rubrica de 0 a 4.
- Registro de fontes externas e locais, com limitações de licença/proveniência.
- Gate final com status explícitos.

### Fundido ou reescrito
- Anti-slop textual e visual: convertido em detector contextual, preservando voz e gênero.
- Regras de UI/taste/motion: convertidas em critérios condicionais e verificáveis.
- Imagem e vídeo: separados em módulos, para não universalizar sintaxes de modelos.
- Marketing: taxonomia/princípios em vez de importação massiva de prompts.
- Ferramentas e infraestrutura: separadas das normas comportamentais.
- Segurança e jailbreaks: materiais não verificados isolados como dados de análise, não como instruções operacionais.

### Não executado
- Nenhum script, skill ou pacote foi instalado ou executado.
- Não foi executada a suíte em modelos externos.
- Não houve benchmark de eficácia nem validação de UX com usuários.
- Não houve parecer jurídico de licenças.

## Questões em aberto

| Questão | Por que está aberta | Próxima ação recomendada |
|---|---|---|
| Commit exato de cada repositório | Os ZIPs não foram confirmados por commit/assinatura em Git. | Comparar URLs canônicas e tags/releases atuais com os metadados do pacote. |
| Leitura semântica de todos os arquivos | O total é de milhares de entradas; esta etapa usou inventário amplo e leitura dirigida. | Priorizar arquivos normativos e todos os `SKILL.md` centrais, depois ampliar por módulos. |
| Licença de cada ativo | Licença raiz pode não cobrir imagens, marcas, fontes, prompts ou datasets externos. | Auditar avisos por diretório e ativos que se pretende redistribuir. |
| Eficácia de regras em modelos | Não houve teste externo controlado. | Executar os 30 casos em modelos/versões fixos, com entradas e saídas brutas. |
| Atualidade de sintaxe visual e APIs | As técnicas mudam por modelo e release. | Revalidar a documentação antes de usar parâmetros exatos em produção. |
| Comparabilidade de scores | A rubrica está definida, mas não há resultados empíricos. | Usar avaliadores calibrados, registrar discordâncias e comparar com baseline. |
| URLs canônicas de todos os módulos | Alguns foram extraídos de READMEs; nem todas as fontes foram abertas individualmente. | Confirmar release, licença, maintainer e URL para cada módulo antes de redistribuição. |

## Gate final obrigatório — estado honesto

| # | Controle | Estado | Evidência / ressalva |
|---:|---|---|---|
| 1 | ZIP externo inventariado | PASS | 13 itens de arquivo enumerados; CRC externo PASS. |
| 2 | ZIPs internos abertos ou falha registrada | PASS | Todos os 13 itens foram reconhecidos como ZIP e passaram no teste CRC. |
| 3 | `.crdownload` verificado sem confiar na extensão | PASS | Aberto como ZIP, 2.447 entradas e CRC PASS; origem não autenticada. |
| 4 | Domínios separados | PASS | Matriz classifica escrita, imagem, vídeo, UX, código, marketing, segurança e infraestrutura. |
| 5 | Infraestrutura, prompts, regras e conteúdo adversarial diferenciados | PASS | Mapa de conflitos e guia separam esses grupos. |
| 6 | Materiais grandes com estratégia explícita | PASS | Inventário amplo + leitura dirigida; limitações declaradas. |
| 7 | Fontes externas abertas e verificadas | PASS COM LIMITAÇÃO | Fontes oficiais e Reddit foram abertas; pesquisa é seletiva, não exaustiva. |
| 8 | Datas, versões, licenças e autoria factuais ou marcadas | PASS COM LIMITAÇÃO | Licenças aparentes e limitações registradas; commit/autoria de todos os itens não verificados. |
| 9 | Pesquisa oficial, GitHub, web e Reddit com pesos diferentes | PASS | Registro distingue documentação oficial, repositório e discussão comunitária. |
| 10 | Guia é consolidação, não concatenação | PASS | Arquitetura original e síntese editorial com módulos. |
| 11 | Regras com definição canônica e IDs únicos | PASS | Prefixos e IDs usados; revisão final de IDs ainda recomendada automatizar em futuras edições. |
| 12 | Conflitos e exceções documentados | PASS | Seção 18 e mapa de conflitos. |
| 13 | Núcleo separado de módulos | PASS | Capítulos e checklist compacto. |
| 14 | Regras observáveis/testáveis | PASS COM LIMITAÇÃO | Critérios e 30 casos conceituais; não testados em modelos. |
| 15 | Preferências não viram mandamentos universais | PASS | Direção visual, escrita e motion são condicionais. |
| 16 | Voz e intenção preservadas no módulo de escrita | PASS | Regras explícitas de preservação e exemplos contrastivos. |
| 17 | Imagem, vídeo, marketing, UX, motion e código não se impõem | PASS | Módulos separados e regras de escopo. |
| 18 | Segurança, privacidade, injection, segredos, autonomia e licença tratados | PASS COM LIMITAÇÃO | Cobertura normativa presente; não equivale a auditoria de segurança operacional. |
| 19 | Pelo menos 30 casos | PASS | 30 casos incluídos. |
| 20 | Simulação distinguida de teste real | PASS | Todos os casos marcados como NOT RUN; sem alegação empírica. |
| 21 | Links, IDs e referências cruzadas checados | NOT VERIFIED | Links externos principais foram abertos; validação automatizada de todos os links/IDs não foi concluída. |
| 22 | Limitações de leitura declaradas | PASS | Inventário e diagnóstico registram cobertura e lacunas. |
| 23 | Sem grandes trechos externos não atribuídos | PASS | Redação majoritariamente original e fontes registradas; revisão jurídica completa não realizada. |
| 24 | Manutenção documentada | PASS | Changelog, versão, processo de contribuição e questões abertas. |
| 25 | Escopo correto: guia de regras, não execução de projetos futuros | PASS | Nenhum vídeo, imagem, site, campanha ou código de produto foi criado. |

**Resultado do gate:** nenhuma falha crítica identificada na consolidação editorial entregue. Os itens marcados com limitação ou `NOT VERIFIED` continuam pendentes e não devem ser reinterpretados como PASS absoluto.

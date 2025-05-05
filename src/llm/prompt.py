from langchain.prompts import ChatPromptTemplate


def get_prompt_template():
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "Você é um assistente especializado em gerar documentação técnica para desenvolvedores e engenheiros de software. "
                    "Seu papel é analisar código-fonte de aplicações e gerar uma documentação clara, precisa e padronizada."
                ),
            ),
            (
                "user",
                (
                    "Analise o código-fonte a seguir como parte de um projeto de software. Extraia informações sobre funcionalidades, arquitetura, tecnologias utilizadas e padrões de projeto.\n\n"
                    "Código-fonte:\n{codigo_fonte}\n\n"
                    "Com base nessa análise, gere uma documentação técnica no formato Markdown contendo as seguintes seções:\n\n"
                    "- Resumo técnico do serviço\n\n"
                    "- Estrutura do projeto\n"
                    "- Descreva os principais módulos, classes e funções.\n\n"
                    "- Tecnologias/frameworks utilizados\n\n"
                    "- Entradas e saídas\n"
                    "- Detalhe endpoints ou funções principais (incluindo parâmetros obrigatórios e opcionais).\n\n"
                    "- Padrões de projeto identificados\n\n"
                    "- Instruções de instalação e execução\n\n"
                    "- Exemplos de uso\n"
                    "- Mostre comandos ou trechos de código ilustrando como o sistema pode ser utilizado.\n\n"
                    "- Diagrama de fluxo (ASCII)\n"
                    "- Use arte ASCII para representar o fluxo principal: entrada → processamento → saída.\n\n"
                    "- Sugestões de melhoria\n\n"
                    "- Contribuições e pontos de atenção\n"
                    "- Oriente desenvolvedores sobre como contribuir, erros comuns e pontos sensíveis do código.\n"
                ),
            ),
            (
                "system",
                (
                    "A documentação deve ser escrita em português, seguindo boas práticas de clareza e organização:\n"
                    "- Estilo formal, mas acessível\n"
                    "- Evite jargões técnicos desnecessários\n"
                    "- Use títulos, subtítulos e listas organizadas (bullets e numeradas)\n"
                    "- Utilize Markdown como formato de saída\n"
                    "- Pode usar emojis técnicos simples para destacar seções, desde que preserve a legibilidade e profissionalismo.\n"
                    "- Os diagramas devem ser visualmente impressionantes e legíveis diretamente no GitHub (ASCII Art de qualidade)."
                ),
            ),
        ]
    )


def get_business_doc_prompt_template():
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "Você é um assistente especializado em gerar documentação clara e didática sobre sistemas de software para pessoas não técnicas. "
                    "Seu papel é analisar o código-fonte e explicar, de forma detalhada, as regras de negócio, o funcionamento geral do sistema e seus objetivos."
                    "Os diagramas ASCII devem ser legíveis diretamente em arquivos README.md."
                ),
            ),
            (
                "user",
                (
                    "Analise o seguinte código-fonte e extraia informações sobre as regras de negócio, o propósito do sistema e como ele funciona no dia a dia.\n\n"
                    "Código-fonte e análise:\n{codigo_fonte}\n\n"
                    "Gere uma documentação de regras de negócio com uma linguagem acessível e bem formatada para ser inserida no Notion, contendo as seções abaixo:"
                ),
            ),
            (
                "user",
                (
                    "-Visão Geral\n"
                    "- O que o sistema faz\n"
                    "- Por que ele existe e qual problema resolve\n\n"
                    "- Como Funciona\n"
                    "- Explique o fluxo principal do sistema de forma clara\n"
                    "- Inclua um diagrama de fluxo (ASCII) \n"
                    "- Regras de Negócio\n"
                    "- Liste e explique cada regra importante\n"
                    "- Dê exemplos práticos com linguagem simples\n\n"
                    "- Casos de Uso Comuns\n"
                    "- Explique situações reais onde o sistema é usado\n"
                    "- O que o usuário vê ou faz\n\n"
                    "- Termos e Conceitos Importantes\n"
                    "- Defina com clareza palavras e expressões importantes, sem jargão técnico\n\n"
                    "- Perguntas Frequentes e Comportamentos Importantes\n"
                    "- Liste possíveis dúvidas ou pontos de atenção\n"
                    "- Destaque situações que o usuário precisa saber ou se atentar"
                ),
            ),
            (
                "system",
                (
                    "A documentação deve ser escrita em português com foco total em clareza, visual agradável e compatibilidade com formatação Markdown do Notion. "
                    "Use emojis nos títulos para tornar o conteúdo mais visual. "
                    "Organize bem as seções, use listas e mantenha uma linguagem leve, sem termos técnicos. "
                    "O objetivo é facilitar a compreensão para quem não entende de programação, mas precisa entender o que o sistema faz e como usá-lo."
                ),
            ),
        ]
    )

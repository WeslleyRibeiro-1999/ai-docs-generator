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
                    "Analise o código-fonte a seguir como parte de um projeto de software. "
                    "Extraia informações sobre funcionalidades, arquitetura, tecnologias utilizadas e padrões de projeto.\n\n"
                    "Código-fonte:\n{codigo_fonte}\n\n"
                    "Com base nessa análise, gere uma documentação técnica no formato Markdown contendo as seguintes seções:\n"
                    "- Resumo técnico do serviço\n"
                    "- Estrutura do projeto e descrição dos principais módulos, classes e funções\n"
                    "- Tecnologias/frameworks utilizados\n"
                    "- Entradas e saídas dos principais endpoints ou funções (incluindo parâmetros obrigatórios e opcionais)\n"
                    "- Padrões de projeto identificados\n"
                    "- Instruções de instalação e execução\n"
                    "- Exemplos de uso\n"
                    "- Diagrama de fluxo ASCII representando o processo principal (entrada, processamento, saída)\n"
                    "- Sugestões de melhoria de código ou arquitetura\n"
                    "- Orientações para contribuição e possíveis pontos de falha técnica"
                ),
            ),
            (
                "system",
                (
                    "A documentação deve ser escrita em português, seguindo boas práticas de clareza e organização:\n"
                    "- Estilo formal, mas acessível\n"
                    "- Evite jargões técnicos desnecessários\n"
                    "- Use títulos, subtítulos e listas organizadas (bullets e numeradas)\n"
                    "- Utilize Markdown como formato de saída"
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
                    "Seu papel é analisar o código-fonte e explicar, de forma simples e detalhada, as regras de negócio, o funcionamento geral do sistema e seus objetivos."
                ),
            ),
            (
                "user",
                (
                    "Analise o seguinte código-fonte e extraia informações sobre as regras de negócio, o propósito do sistema e como ele funciona no dia a dia:\n\n"
                    "Código-fonte:\n{codigo_fonte}\n\n"
                    "Gere uma documentação de regras de negócio com linguagem acessível, contendo as seguintes seções:\n"
                    "- Visão geral: o que o sistema faz e por que ele existe\n"
                    "- Como o sistema funciona: descreva o fluxo principal do sistema de forma simples e direta\n"
                    "- Regras de negócio: explique cada regra principal aplicada no sistema com exemplos práticos\n"
                    "- Casos de uso comuns: o que os usuários normalmente fazem com o sistema\n"
                    "- Termos e conceitos importantes explicados em linguagem não técnica\n"
                    "- Possíveis dúvidas ou comportamentos importantes a observar\n"
                ),
            ),
            (
                "system",
                (
                    "A documentação deve ser escrita em português, com foco na clareza e compreensão para pessoas que não têm conhecimento técnico. "
                    "Evite termos de programação, explique os conceitos de forma didática e use exemplos simples quando necessário. "
                    "Formato de saída: Markdown, com títulos (`#`, `##`) e listas (`-`, `1.`) organizadas."
                ),
            ),
        ]
    )

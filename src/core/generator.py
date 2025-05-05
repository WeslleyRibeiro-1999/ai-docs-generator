from llm.client import get_llm
from llm.prompt import get_business_doc_prompt_template, get_prompt_template


def documentation_generator(codigo_fonte: str) -> str:
    dev_prompt = get_prompt_template()
    biz_prompt = get_business_doc_prompt_template()

    llm = get_llm()
    dev_chain = dev_prompt | llm
    biz_chain = biz_prompt | llm

    dev_doc = dev_chain.invoke({"codigo_fonte": codigo_fonte})
    biz_doc = biz_chain.invoke({"codigo_fonte": codigo_fonte})

    return dev_doc.content, biz_doc.content

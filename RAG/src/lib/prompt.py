from langchain_core.prompts import ChatPromptTemplate

PROMPT_TEMPLATE = """
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
"""

def getSystemTemplate():
    return PROMPT_TEMPLATE


def getPrompt () -> ChatPromptTemplate:
    prompt = ChatPromptTemplate.from_messages([
        ("system" , getSystemTemplate()),
        ("human" , "{input}"),
    ])
    return prompt
from os import error
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

PROMPT_TEMPLATE = """
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context and the"
    "question to generate an answer."
    "If no question is provided, ask if you can help the user."
    "please answer concise."
    "The following  is helpful to answer: "
    "\n\n"
    "----------"
    "{context}"
    "----------"
    "If no context is provided try to answer it anyway"
"""
    #"If there is no context or the answer is not given in the context say I dont Know ! "

def getSystemTemplate():
    return PROMPT_TEMPLATE


# def getPrompt () -> ChatPromptTemplate:
#     prompt = ChatPromptTemplate.from_messages([
#         ("system" , getSystemTemplate()),
#         ("human" , "{input}"),
#     ])
#     return prompt


def getPrompt () -> ChatPromptTemplate:
    try:
        prompt = ChatPromptTemplate.from_messages([
        ("system" , getSystemTemplate()),
        MessagesPlaceholder("history"),
        ("human" , "{input}"),
        ])
        return prompt
    except Exception as error:
        pass
        print(error)





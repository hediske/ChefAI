from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts.base import BasePromptTemplate

PROMPT_TEMPLATE = """
      You are a helful chatbot for a company
    Use the following context and question to generate an answer.
    If no question is provided, ask if you can help the user.
    Always answer in French.
    The following context is helpful to answer:
    -----
    {context}
    -----
    If there is no context or the answer is not given in the context
    say "Je suis désolé mais je ne sais pas vous répondre"
    The question is:
    Question: {question}
    Helpful Answer:  

"""

def getTemplate():
    return PROMPT_TEMPLATE


def getPrompt () -> BasePromptTemplate:
    template = BasePromptTemplate(template = getTemplate(), input_variables = ["context", "question"])
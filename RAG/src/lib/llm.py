from langchain_openai import OpenAI



def get_llm(temperature = 0.1 , ):
    llm = OpenAI(temperature=0)
    return llm

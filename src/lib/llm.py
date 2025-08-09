from langchain_ollama import OllamaLLM

def get_llm(  temperature = 0.1 , model = "tinyllama" ) :
    return OllamaLLM(
        model=model,
        temperature=temperature
    )
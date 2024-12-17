from src.lib.history_conversional_chain import getHistoryConversionalChain

all_chain = getHistoryConversionalChain()


def evoke_and_save(session_id:str , question :str):
    result = all_chain.invoke({"input": question},{'configurable': {'session_id': session_id,}})["answer"]
    return result
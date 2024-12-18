from lib.history_conversional_chain import getHistoryConversionalChain

all_chain = getHistoryConversionalChain()


async def evoke_and_save(session_id:str , question :str):
    print("Question :",question)
    result = await all_chain.ainvoke({"input": question},{'configurable': {'session_id': session_id,}})
    answer = result.get("answer")
    return answer
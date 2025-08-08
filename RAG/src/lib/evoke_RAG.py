from lib.history_conversional_chain import getHistoryConversionalChain

all_chain = getHistoryConversionalChain()


async def evoke_and_save(session_id:str , question :str):
    print("Question :",question)

    try:
        # Invoke the chain with the provided question and session_id
        result = await all_chain.ainvoke({"input": question}, {'configurable': {'session_id': session_id}})
    except Exception as e:
        print("Error invoking chain:", e)
        return "Internal Error , Please try again later."
    answer = result.get("answer")
    return answer
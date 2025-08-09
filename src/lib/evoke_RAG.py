from lib.history_conversional_chain import getHistoryConversionalChain

all_chain = getHistoryConversionalChain()


# In evoke_RAG.py
def evoke_and_save(session_id: str, question: str):
    try:
        result = all_chain.invoke(
            {"input": question},
            config={"configurable": {"session_id": session_id}}
        )
        print(result)
        return result["answer"]
    except Exception as e:
        print(f"Error in chain invocation: {e}")
        return "Sorry, I encountered an error processing your request"
import asyncio
from uuid import uuid4
from lib.evoke_RAG import evoke_and_save
import streamlit as st

def init_history():
    if "history" not in st.session_state or st.session_state.history is None:
        st.session_state["history"] = []

def create_session():
    if "session_id" not in st.session_state or st.session_state.session_id is None:
        st.session_state.session_id = str(uuid4())

async def send_message(prompt : str):
    print ("sending message")
    if st.session_state.session_id is not None:
        user_msg = prompt
        session_id = st.session_state.session_id
        st.session_state["send_disabled"] = True

        st.chat_message("user").markdown(user_msg)

        try:
            with st.spinner("Waiting for the model to respond ..."):
                response = evoke_and_save(session_id, user_msg)
            with st.chat_message("assistant"):
                st.markdown(response)
                st.session_state["history"].append(("user", user_msg))
                st.session_state["history"].append(("assistant", response))
                st.session_state["send_disabled"] = False
        except Exception as error:
            st.error("Internal Error !")


def show_messages():
    for user, message in st.session_state["history"]:
        with st.chat_message(user):
            st.markdown(message)


def init_sent():
    st.session_state["send_disabled"] = False


# Main Content

st.title("KitchenAI")
st.write("Think culinary! Our AI Assistant is here to help you with recipes and cooking tips. Whether you're looking for a specific dish or need general advice, just ask!")
init_history()
init_sent()
create_session()
show_messages()
if prompt := st.chat_input(placeholder="Enter your message:", key="user_input",disabled=st.session_state["send_disabled"]):
    asyncio.run(send_message(prompt))


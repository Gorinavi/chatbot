import streamlit as st
from backend import result


st.set_page_config(
   page_title="Chatbot",
   page_icon="💬",
   layout="wide",
)

st.markdown(
   """
   <style>
   .block-container {
       max-width: 900px;
       padding-top: 2rem;
       padding-bottom: 2rem;
   }

   [data-testid="stSidebar"] .block-container {
       padding-top: 2rem;
   }

   [data-testid="stChatMessage"] {
       margin-bottom: 0.5rem;
   }

   footer {visibility: hidden;}
   </style>
   """,
   unsafe_allow_html=True,
)


def ensure_api_key() -> str:
   if "api_key" not in st.session_state:
       st.session_state.api_key = ""

   return st.session_state.api_key


def init_chat_state() -> None:
   if "messages" not in st.session_state:
       st.session_state.messages = [
           {
               "role": "assistant",
               "content": "안녕하세요 👋  어떤 걸 도와드릴까요?",
           }
       ]


def render_sidebar():
   with st.sidebar:
       st.markdown("## ⚙️ Settings")
       if "api_key" not in st.session_state:
           st.session_state.api_key = ""

       st.markdown("### 🔐 API Key")
       st.info(
           "이 키는 세션에만 저장되고 새로고침 시 초기화됩니다.",
       )
       with st.form("api-key-form", clear_on_submit=False):
           api_key = st.text_input(
               "API Key 입력",
               type="password",
               placeholder="sk-...",
               value=st.session_state.api_key,
           )
           submitted = st.form_submit_button("저장")
           if submitted:
               st.session_state.api_key = api_key.strip()
               if not st.session_state.api_key:
                   st.error("유효한 API 키를 입력해 주세요.")


def render_chat_messages():
   for msg in st.session_state.messages:
       if msg["role"] == "user":
           with st.chat_message("user"):
               st.markdown(msg["content"])
       else:
           with st.chat_message("assistant"):
               st.markdown(msg["content"])


def handle_user_input():
   user_input = st.chat_input("메시지를 입력하고 Enter를 눌러보세요.")
   if not user_input:
       render_chat_messages()
       return

   if not ensure_api_key():
       st.warning("먼저 API 키를 입력해 주세요.")
       render_chat_messages()
       return

   st.session_state.messages.append({"role": "user", "content": user_input})

   render_chat_messages()

   with st.chat_message("assistant"):
       placeholder = st.empty()
       with st.spinner("답변을 생성하는 중입니다..."):
           response_text = result(user_input)
       placeholder.markdown(response_text)

   st.session_state.messages.append({"role": "assistant", "content": response_text})


def main():
   init_chat_state()

   render_sidebar()

   st.markdown("## 💬 Chatbot")
   st.caption("chatbot")

   handle_user_input()


if __name__ == "__main__":
   main()

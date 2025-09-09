# pages/1_🤖_Gerador_de_Emails.py
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gerador de E-mails", layout="centered")

# Verifica se o usuário está logado
if not st.session_state.get("logged_in", False):
    st.error("🔒 Por favor, faça o login para acessar esta página.")
    st.stop()

st.title("🤖 Gerador de E-mails com IA")

try:
    gemini_api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
except:
    st.error("Chave da API Gemini não configurada nos segredos do Streamlit.")
    st.stop()

with st.form("email_form"):
    destinatario = st.text_input("Para quem é o e-mail?", "cliente, fornecedor...")
    tom = st.selectbox("Tom de voz:", ["Profissional", "Amigável", "Formal"])
    objetivo = st.text_input("Qual o principal objetivo?", "Marcar uma reunião...")
    contexto = st.text_area("Contexto e informações chave:", height=150)
    submitted = st.form_submit_button("Gerar E-mail ✨")

if submitted and contexto:
    with st.spinner("A IA está escrevendo seu e-mail..."):
        prompt = f"Escreva um e-mail com tom {tom} para um {destinatario}. O objetivo é {objetivo}. Use o seguinte contexto: {contexto}. Crie um assunto e o corpo do e-mail."
        response = model.generate_content(prompt)
        st.subheader("E-mail Sugerido:")
        st.info(response.text)
      

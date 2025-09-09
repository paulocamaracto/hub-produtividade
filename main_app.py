# main_app.py
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Hub de Produtividade", layout="wide")

# Simplificamos a autenticação para a versão mobile, sem banco de dados
def check_password():
    """Retorna True se o usuário estiver logado."""
    if st.session_state.get("logged_in", False):
        return True

    # Mostra o formulário de login
    st.title("Hub de Produtividade da Startup 🚀")
    st.write("Por favor, faça o login para acessar as ferramentas.")

    username = st.text_input("Usuário", key="user")
    password = st.text_input("Senha", type="password", key="pass")

    if st.button("Entrar"):
        # SENHA FIXA: Altere aqui se desejar, mas lembre-se que fica visível no código.
        if username == "xgreen" and password == "xgreen":
            st.session_state["logged_in"] = True
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos.")
    return False

if check_password():
    st.sidebar.title(f"Bem-vindo(a), xgreen!")
    st.sidebar.write("Navegue pelos apps abaixo.")

    if st.sidebar.button("Sair"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()

    st.title("Bem-vindo ao Hub de Produtividade! 👋")
    st.markdown("---")
    st.header("Selecione um app na barra lateral à esquerda para começar.")
    st.info("Este é o seu centro de comando para ferramentas de IA que aceleram o trabalho da nossa equipe.")
  

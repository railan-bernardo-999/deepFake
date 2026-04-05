import streamlit as st
import time

# Configuração da página (Tema Dark por padrão)
st.set_page_config(page_title="Terminal de Acesso", page_icon="💻")

# Estilo Hacker (Fundo preto e texto verde neon)
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    /* Força todas as fontes para verde e monoespaçadas */
    p, h1, h2, h3, .stMarkdown {
        color: #00FF00 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    /* Estiliza o bloco de código para parecer um terminal antigo */
    code {
        color: #00FF00 !important;
        background-color: #0a0a0a !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Captura o nome da URL (ex: ?nome=Thiago)
nome_amigo = st.query_params.get("nome", "Antônio Alves")

# --- INÍCIO DA INTERFACE ---

st.title("💾 SYSTEM_ROOT: ACCESS_CORE")
st.write(f"Conexão estabelecida com terminal remoto...")
st.write("---")

# 1. Loading de Suspense inicial
with st.spinner('Criptografando túnel SSH...'):
    time.sleep(3)

# 2. O Terminal (Linhas aparecendo uma a uma)
log_placeholder = st.empty() 
log_conteudo = f"Iniciando varredura em: {nome_amigo}\n"

comandos = [
    "> Localizando endereço IP...",
    "> Bypassando Firewall nível 4...",
    "> Injetando exploit via Buffer Overflow...",
    "> Acessando pacotes de dados privados...",
    "> Descriptografando arquivos confidenciais...",
    "> Analisando histórico de geolocalização...",
    "> [AVISO] Tentativa de rastreio detectada...",
    "> Camuflando endereço MAC... Sucesso!",
    "> Extraindo logs..."
]

# Executa o terminal linha por linha
for cmd in comandos:
    log_conteudo += cmd + "\n"
    log_placeholder.code(log_conteudo) 
    time.sleep(1.2) # Velocidade da "digitação" do hacker

# 3. MENSAGEM FINAL (Só aparece após o loop acima terminar)
st.write("---")
st.balloons() # Efeito de balões para dar um susto de leve
st.success(f"🔓 CONCLUÍDO: {nome_amigo}, eu sei o que você comeu o viado e não pagou, kkkkkkk!")
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGI5MmJid2Z6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/HwNnWtrE1p29M07tXC/giphy.gif")
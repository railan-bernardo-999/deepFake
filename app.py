import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Terminal de Acesso", page_icon="💻")

# Estilo Hacker (Fundo preto e texto verde)
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    .css-10trblm, .stText, p, h1, h2, h3 {
        color: #00FF00 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Captura o nome da URL
nome_amigo = st.query_params.get("nome", "Antônio Alves")

# 1. Título Inicial
st.title("💾 SYSTEM_ROOT: ACCESS_CORE")
st.write("---")

# 2. O "Loading" inicial (Suspense)
with st.spinner('Estabelecendo conexão segura...'):
    time.sleep(3) # Espera 3 segundos fingindo que está conectando

# 3. Simulação do Terminal executando comandos
st.write(f"Iniciando varredura em: {nome_amigo}...")

log_placeholder = st.empty() # Espaço que vamos atualizar com as linhas de código
log_conteudo = ""

comandos = [
    "> Localizando endereço IP...",
    "> Bypassando Firewall nível 4...",
    "> Acessando pacotes de dados privados...",
    "> Descriptografando arquivos confidenciais...",
    "> Analisando histórico de geolocalização...",
    "> [ERRO] Tentativa de bloqueio detectada...",
    "> Ignorando bloqueio... Sucesso!",
    "> Extraindo segredos..."
]

for cmd in comandos:
    log_conteudo += cmd + "\n"
    log_placeholder.code(log_conteudo) # Exibe como bloco de código (estilo terminal)
    time.sleep(1.5) # Pausa entre cada comando para dar realismo

# 4. Finalização de Impacto
st.write("---")
time.sleep(1)
st.success(f"🔓 CONCLUÍDO: {nome_amigo}, eu sei o que você comeu o viado e não pagou kkkkkkkk!")
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGI5MmJid2Z6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/HwNnWtrE1p29M07tXC/giphy.gif")
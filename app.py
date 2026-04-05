import streamlit as st
import time

# Configuração da página para parecer um terminal
st.set_page_config(page_title="System Breach Detected", page_icon="⚠️")

# CSS para deixar a página com cara de hacker (fundo preto e letras verdes)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #00ff00;
        font-family: 'Courier New', Courier, monospace;
    }
    stAlert {
        background-color: #1e1e1e;
    }
    </style>
    """, unsafe_allow_html=True)

# Pega o nome do amigo pela URL (ex: ?nome=Thiago)
query_params = st.query_params
nome_amigo = query_params.get("nome", "Atônio Alves")

st.title("🚨 ACESSO NÃO AUTORIZADO")
st.write(f"Conectando ao terminal de: **{nome_amigo}**...")

# Simulador de progresso
if st.button("INICIAR DECODIFICAÇÃO"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    steps = [
        "Bypassing firewall...",
        "Acessando metadados do WhatsApp...",
        "Localizando coordenadas GPS...",
        "Extraindo histórico de pesquisas vergonhosas...",
        "ACESSO CONCEDIDO!"
    ]
    
    for i, step in enumerate(steps):
        status_text.text(f"Status: {step}")
        progress_bar.progress((i + 1) * 20)
        time.sleep(1.2) # Pausa dramática
    
    st.balloons()
    st.success(f"🔓 CONCLUÍDO: {nome_amigo}, eu sei o que você comeu o viado e não pagou kkkkkkkkkkkk!")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGI5MmJid2Z6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/HwNnWtrE1p29M07tXC/giphy.gif")
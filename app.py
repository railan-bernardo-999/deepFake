import streamlit as st
import time

# Configuração da página para parecer séria
st.set_page_config(page_title="G1 - O Portal de Notícias da Globo", page_icon="https://s2.glbimg.com/uG_v9U8V6Z-XvXvXvXvXvXvXvXv=/i.glbimg.com/og/ig/infoglobo1/f/original/2020/04/23/g1.png")

# --- ESTILO G1 ---
st.markdown("""
    <style>
    .g1-header { color: #c4170c; font-weight: bold; font-size: 30px; font-family: Arial; }
    .g1-titulo { font-size: 42px; font-weight: bold; line-height: 1.1; font-family: 'Open Sans', sans-serif; }
    .g1-subtitulo { font-size: 20px; color: #555; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGAÇÃO ---
# Se houver dados na URL, mostra a notícia. Se não, mostra o formulário de criação.
query_params = st.query_params

if "titulo" in query_params:
    # --- MODO NOTÍCIA (O que o amigo vê) ---
    st.markdown('<p class="g1-header">G1</p>', unsafe_allow_html=True)
    st.write("---")
    
    titulo = query_params.get("titulo")
    subtitulo = query_params.get("desc", "")
    nome = query_params.get("nome", "Indivíduo")
    
    st.markdown(f'<p class="g1-titulo">{titulo}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="g1-subtitulo">{subtitulo}</p>', unsafe_allow_html=True)
    
    st.write(f"**Por G1 — Rio de Janeiro**")
    st.write("05/04/2026 12h30  Atualizado há 5 minutos")
    st.write("---")
    
    # Exibe uma imagem padrão de "procurado" ou "polícia" já que não salvamos a foto enviada em banco de dados real
    st.image("https://p2.trrsf.com/image/fget/cf/1200/675/middle/images.terra.com/2023/03/24/762518607-viatura-policia-civil.jpg")
    
    st.write(f"Segundo informações exclusivas obtidas pelo nosso portal, **{nome}** foi visto(a) em situação suspeita nesta manhã. Testemunhas afirmam que a situação é irreversível e o caso já ganhou repercussão nacional.")
    
    if st.button("ASSISTIR VÍDEO DO FLAGRANTE"):
        st.error("ERRO: O servidor de vídeo está sobrecarregado devido ao alto número de acessos!")
        st.balloons()
        st.info("Pegadinha! Você foi trollado pelo Gerador de Fake News do Python. 😂")

else:
    # --- MODO CRIADOR (O que VOCÊ usa) ---
    st.title("🛠️ Gerador de Trollagem G1")
    st.write("Preencha os dados abaixo para gerar o link da pegadinha.")
    
    with st.form("gerador"):
        nome_alvo = st.text_input("Nome do amigo:")
        manchete = st.text_input("Título da Notícia (Ex: Fulano é preso por...)")
        descricao = st.text_area("Descrição rápida (Subtítulo):")
        foto = st.file_uploader("Enviar foto do amigo (Opcional - veja nota abaixo)", type=["jpg", "png"])
        
        btn_gerar = st.form_submit_button("GERAR LINK DA TROLLAGEM")
        
        if btn_gerar:
            # Criamos o link com os dados encriptados na URL
            base_url = "https://seu-app.streamlit.app/" # Mude para o seu link real depois do deploy
            link_final = f"{base_url}?nome={nome_alvo.replace(' ', '+')}&titulo={manchete.replace(' ', '+')}&desc={descricao.replace(' ', '+')}"
            
            st.success("Link gerado com sucesso!")
            st.code(link_final)
            st.warning("Nota: Por ser uma versão gratuita, a foto enviada não fica salva. O link mostrará uma imagem padrão de polícia/notícia.")
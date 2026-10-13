import streamlit as st
import pandas as pd

# CONFIG AURORA TECHNOLOGY
st.set_page_config(page_title="TESS AI - AURORA TECHNOLOGY", page_icon="💜", layout="wide")

# CSS IGUAL SUA FOTO - TEMA AURORA ESCURO
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f0a1a 0%, #1a0f2e 50%, #0a1628 100%); }
    .sidebar { background: rgba(20, 10, 40, 0.8) !important; }
    .stTextInput > div > div { background: #2a1f3d !important; border: 1px solid #7c3aed !important; }
</style>
""", unsafe_allow_html=True)

# SIDEBAR - IGUAL SUA FOTO
with st.sidebar:
    st.markdown("## 🅣 TESS AI")
    st.caption("AURORA TECHNOLOGY")
    st.divider()
    st.markdown("**Chat IA**")
    st.markdown("Conversas\n\nExplorar\n\nAprender\n\nCriar\n\nRelatórios")
    st.divider()
    st.markdown("**FUNCIONALIDADES**\n\n⚡ Automação\n\n🔗 Integrações\n\nAPI\n\n⚙️ Configurações\n\nPlano\n\nSuporte\n\nSair")
    st.success("Plano Pro • Ativo\nv2.4.1 • Aurora")

# HEADER
st.title("✨ TESS AI - Assistente Inteligente Online")
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("🟢 **Online** | Modelo: Aurora-3.5")
with col2:
    st.markdown("🔍 Buscar prompts, conversas, relatórios...")

# ÁREA DE CHAT
st.divider()

# INPUT
msg = st.text_input("💬 Digite sua mensagem:", placeholder="Ex: Pode gerar o relatório de vendas de setembro?")

if msg:
    # Mensagem do usuário
    st.markdown(f"""
    <div style="background:#6366f1; padding:15px; border-radius:20px; margin:10px 0; text-align:right; color:white;">
        <b>Você:</b> {msg} <br><small>14:32</small>
    </div>
    """, unsafe_allow_html=True)

    # PALAVRAS QUE ATIVAM RELATÓRIO - SÓ MOSTRA SE PEDIR
    ativa_relatorio = any(p in msg.lower() for p in ["relatorio", "relatório", "vendas", "grafico", "gráfico", "setembro", "tabela"])

    if ativa_relatorio:
        st.markdown(f"""
        <div style="background:#4c1d95; padding:15px; border-radius:20px; margin:10px 0; color:white;">
            <b>🅣 TESS:</b> Claro! Aqui está o relatório de vendas de setembro. As vendas totais foram R$ 128.450, um crescimento de +12% em relação a agosto.<br>
            • Destaque: Região Sudeste liderando com 42% do total<br>
            • Produto mais vendido: Stellar Plus (51.150)<br>
            <small>14:32 • Gerado em instantes</small>
        </div>
        """, unsafe_allow_html=True)

        # TABELA - QUADRADO IGUAL SUA FOTO
        st.subheader("📊 Tabela de Vendas por Produto")
        df_produto = pd.DataFrame({
            "Produto": ["Stellar Plus", "Aurora Pro", "Nimbus Lite"],
            "Vendas": ["R$ 51.150", "R$ 42.300", "R$ 35.100"],
            "Variação": ["+14% ↑", "+15% ↑", "+8% ↑"],
            "Ticket Médio": ["R$ 450", "R$ 320", "R$ 210"]
        })
        st.dataframe(df_produto, use_container_width=True, hide_index=True)

        # GRÁFICO - IGUAL SUA FOTO
        st.subheader("📈 Vendas por Região - Setembro 2024")
        df_regiao = pd.DataFrame({
            "Região": ["Sudeste", "Nordeste", "Sul", "Norte", "Centro-Oeste"],
            "Porcentagem": [42, 22, 18, 10, 8]
        })
        st.bar_chart(df_regiao, x="Região", y="Porcentagem")

        # LATERAL DIREITA - VOZ INTERATIVA IGUAL SUA FOTO
        with st.expander("🎙️ Voz Interativa - Em tempo real", expanded=True):
            st.markdown("**Status: Escutando...**")
            st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav")
            st.markdown("""
            **Configurações de Voz**\n
            Voz: Aurora Feminina • Profissional\n
            Velocidade: 1.0x\n
            ✅ Síntese neural ativada • Latência <200ms
            """)
            col_a, col_b, col_c = st.columns(3)
            col_a.button("⏸️ Pausar")
            col_b.button("⏹️ Parar")
            col_c.button("⬇️ Baixar Áudio")

    else:
        # SÓ CONVERSA - NÃO MOSTRA NADA
        st.markdown(f"""
        <div style="background:#312e81; padding:15px; border-radius:20px; margin:10px 0; color:white;">
            <b>🅣 TESS:</b> Entendi! Você disse '{msg}'. Como posso te ajudar? Se quiser ver relatórios, é só pedir 'gera relatório de vendas'.
        </div>
        """, unsafe_allow_html=True)

else:
    # TELA INICIAL SEM RELATÓRIO
    st.info("💜 Olá! Eu sou a TESS AI. Digite algo acima. O relatório só aparece SE você pedir, igual você pediu!")
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800", caption="AURORA TECHNOLOGY - Plataforma AI")

st.divider()
st.caption("TESS AI • Versão Mais Recente • Aurora-3.5 • Operacional 🟢")

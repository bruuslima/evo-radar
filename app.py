import streamlit as st
import socket

# Configuração da Página e Identidade da Empresa
st.set_page_config(
    page_title="EVO Radar Concorrente - Vivo Empresas",
    page_icon="🎯",
    layout="centered"
)

# Estilização básica EVO
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #4B0082; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size: 16px; color: #555555; text-align: center; margin-bottom: 30px; }
    .stButton>button { background-color: #660099; color: white; width: 100%; border-radius: 8px; font-weight: bold; }
    .stButton>button:hover { background-color: #4B0082; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>EVO PARCEIRO VIVO EMPRESAS</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>📡 Inteligência de Mercado: Descubra o Link Dedicado do Cliente</div>", unsafe_allow_html=True)

st.subheader("🔎 Investigação Silenciosa")
dominio_input = st.text_input("Digite o site/domínio do cliente (ex: empresa.com.br):", placeholder="empresa.com.br")

if st.button("Mapear Concorrente 🎯"):
    if dominio_input:
        dominio_limpo = dominio_input.replace("https://", "").replace("http://", "").replace("www.", "").strip("/")
        
        with st.spinner("Rastreando infraestrutura de rede..."):
            try:
                # 1. Descobre o IP principal do site
                ip_alvo = socket.gethostbyname(dominio_limpo)
                
                # 2. Tenta descobrir o nome reverso do IP (Muitas vezes revela a operadora dona do bloco!)
                try:
                    nome_reverso, _, _ = socket.gethostbyaddr(ip_alvo)
                except:
                    nome_reverso = "Não disponível publicamente"
                
                st.success("✅ Varredura Concluída com Sucesso!")
                
                # Exibição dos dados na tela
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="Endereço de IP do Servidor", value=ip_alvo)
                with col2:
                    st.metric(label="Identificação de Rota (Host)", value="Ver abaixo")
                
                st.info(f"🌐 **Nome do Host/Rota Detectada:** {nome_reverso}")
                
                st.markdown("---")
                st.subheader("🎯 Estratégia de Abordagem EVO:")
                
                # Análise lógica simples baseada nos nomes de servidores comuns
                host_lower = nome_reverso.lower()
                
                if "claro" in host_lower or "embratel" in host_lower:
                    st.error("🔥 Concorrente Detectado: Estrutura vinculada ao grupo CLARO / EMBRATEL.")
                    st.write("👉 *Abordagem:* Ataque a instabilidade em dias de chuva e negocie oferecendo a Fibra Óptica Dedicada com rotas exclusivas da Vivo.")
                elif "telemar" in host_lower or "oi." in host_lower:
                    st.error("🔥 Concorrente Detectado: Estrutura vinculada à OI.")
                    st.write("👉 *Abordagem:* Foque na segurança jurídica e na saúde financeira da Vivo como parceira estável para os próximos anos da empresa.")
                elif "hosting" in host_lower or "locaweb" in host_lower or "hostgator" in host_lower or "secureserver" in host_lower:
                    st.warning("⚠️ Estrutura Web em Data Center Comercial (Nuvem).")
                    st.write("👉 *Abordagem:* 'Identificamos que seus sistemas rodam em servidores web profissionais. Para garantir que sua equipe interna acesse essas ferramentas sem lentidão ou quedas, a Vivo oferece soluções de IP Fixo e Link Dedicado simétrico...'")
                else:
                    st.success("🎯 Alvo Comercial Mapeado:")
                    st.write("👉 *Abordagem:* Use o script de sondagem inteligente: *'Estamos mapeando a infraestrutura digital do seu bairro e identificamos que sua empresa possui servidores ativos na rede. Como está o suporte e a garantia de banda contratada do seu provedor de internet atual?'*")
                
            except socket.gaierror:
                st.error("❌ Domínio Inválido ou Inexistente. Verifique se digitou o site corretamente.")
            except Exception as e:
                st.error(f"❌ Ocorreu um erro no processamento: {e}")
    else:
        st.warning("Por favor, digite um domínio antes de buscar.")

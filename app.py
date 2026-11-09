import streamlit as st
import socket
import requests

# 1. Configuração da Página e Identidade da Empresa
st.set_page_config(
    page_title="EVO Radar Concorrente - Vivo Empresas",
    page_icon="🎯",
    layout="centered"
)

# Estilização básica para dar um visual profissional
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #4B0082; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size: 16px; color: #555555; text-align: center; margin-bottom: 30px; }
    .stButton>button { background-color: #660099; color: white; width: 100%; border-radius: 8px; font-weight: bold; }
    .stButton>button:hover { background-color: #4B0082; color: white; }
    </style>
""", unsafe_allow_html=True)

# Topo da página
st.markdown("<div class='main-title'>EVO PARCEIRO VIVO EMPRESAS</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>📡 Inteligência de Mercado: Descubra o Link Dedicado do Cliente</div>", unsafe_allow_html=True)

# 2. Entrada de Dados do Vendedor
st.subheader("🔎 Investigação Silenciosa")
dominio_input = st.text_input("Digite o site/domínio do cliente (ex: empresa.com.br):", placeholder="empresa.com.br")

# 3. Processamento ao Clicar no Botão
if st.button("Mapear Concorrente 🎯"):
    if dominio_input:
        dominio_limpo = dominio_input.replace("https://", "").replace("http://", "").replace("www.", "").strip("/")
        
        with st.spinner("Rastreando infraestrutura na rede..."):
            try:
                # Resolução de DNS
                ip_alvo = socket.gethostbyname(dominio_limpo)
                
                # Consulta de ASN e Provedor
                url_api = f"http://ip-api.com{ip_alvo}?fields=status,message,isp,org,as,hosting"
                resposta = requests.get(url_api).json()
                
                if resposta.get("status") == "success":
                    operadora = resposta.get("isp")
                    organizacao = resposta.get("org")
                    bloco_asn = resposta.get("as")
                    eh_hosting = resposta.get("hosting")
                    
                    st.success("✅ Varredura Concluída com Sucesso!")
                    
                    # Exibição dos Dados em Cards Visuais
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric(label="Provedor Atual (ISP)", value=operadora)
                        st.caption(f"Bloco de Rede: {bloco_asn}")
                    with col2:
                        st.metric(label="Endereço de IP Encontrado", value=ip_alvo)
                        st.caption(f"Registrado para: {organizacao}")
                    
                    # 4. Direcionamento Comercial (Inteligência EVO)
                    st.markdown("---")
                    st.subheader("🎯 Estratégia de Abordagem para o Vendedor:")
                    
                    if eh_hosting:
                        st.warning("⚠️ **Alerta de Nuvem (Hosting):** O site deles roda em servidores compartilhados ou Data Center (ex: AWS, Hostgator).")
                        st.write("👉 *Como abordar:* O link físico da empresa pode ser diferente. Use a abordagem para descobrir: *'Identificamos que a estrutura web de vocês já está modernizada em nuvem, mas como está o link dedicado local que garante o acesso estável a essa nuvem sem quedas?'*")
                    else:
                        st.info(f"🔥 **Concorrente Direto Exposto:** O cliente aponta o tráfego diretamente para a rede da **{operadora}**.")
                        st.write(f"👉 *Como abordar:* Use o argumento de ganho de estabilidade na Fibra Dedicada Vivo contra a rota atual deles. Foque em **SLA de 99,5%**, **Garantia de Banda** e suporte corporativo exclusivo.")
                        
                        # Script rápido de Gancho
                        st.code(
                            f"Script Sugerido:\n"
                            f"\"Olá! Sou da EVO, parceiro estratégico Vivo Empresas. Estamos implementando um anel de fibra de ultra velocidade na sua região para empresas que precisam substituir conexões instáveis de operadoras como a {operadora} por um circuito 100% simétrico e dedicado...\"", 
                            language="text"
                        )
                else:
                    st.error("Não foi possível extrair os dados de provedor para este domínio.")
                    
            except socket.gaierror:
                st.error("❌ Domínio Inválido ou Inexistente. Verifique se digitou o site corretamente.")
            except Exception as e:
                st.error(f"❌ Ocorreu um erro na requisição: {e}")
    else:
        st.warning("Por favor, digite um domínio antes de buscar.")

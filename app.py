import streamlit as st
import socket
import whois

# Configuração da Página e Identidade da Empresa
st.set_page_config(
    page_title="EVO Radar Concorrente - Vivo Empresas",
    page_icon="🎯",
    layout="centered"
)

# Estilização básica
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
        
        with st.spinner("Rastreando servidores e operadoras..."):
            try:
                # 1. Descobre o IP real do servidor do cliente
                ip_alvo = socket.gethostbyname(dominio_limpo)
                
                # 2. Descobre quem é o dono do domínio e os servidores de DNS (onde o link responde)
                info_dominio = whois.whois(dominio_limpo)
                servidores_dns = info_dominio.name_servers
                
                # Transforma a lista de DNS em texto simples para exibição
                dns_texto = ", ".join(servidores_dns) if isinstance(servidores_dns, list) else str(servidores_dns)
                
                st.success("✅ Varredura Concluída com Sucesso!")
                
                # Exibição dos dados na tela
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="Servidores de DNS do Cliente", value="Ver Detalhes Abaixo")
                    st.write(f"🌐 **DNS:** {dns_texto}")
                with col2:
                    st.metric(label="IP do Servidor Web", value=ip_alvo)
                
                st.markdown("---")
                st.subheader("🎯 Estratégia de Abordagem EVO:")
                
                # Lógica comercial baseada no DNS detectado
                dns_lower = dns_texto.lower()
                
                if "locaweb" in dns_lower or "hostgator" in dns_lower or "uolhost" in dns_lower:
                    st.warning("⚠️ **Alerta de Hospedagem Comercial:** O site roda em um provedor de hospedagem em nuvem.")
                    st.write("👉 *Como o vendedor aborda:* 'Notamos que sua estrutura de site/e-mail roda em nuvem de alta performance. Para garantir que seus funcionários não percam o acesso a essas ferramentas por quedas na internet local, a Vivo tem um plano de link dedicado com contingência automática...'")
                elif "cloudflare" in dns_lower:
                    st.info("🛡️ **Proteção Cloudflare Detectada:** A empresa possui uma estrutura profissional de segurança web.")
                    st.write("👉 *Como o vendedor aborda:* 'Empresas que investem em segurança digital como vocês precisam de estabilidade máxima na ponta. Nosso link dedicado entrega simetria total de download e upload...'")
                else:
                    st.success("🔥 **Alvo com Estrutura Própria Local Provável:**")
                    st.write("👉 *Como o vendedor aborda:* Faça as perguntas de qualificação para pescar o concorrente: *'Identificamos que sua empresa possui servidores ativos de rede. Como está o SLA de entrega e o suporte da sua operadora atual de link dedicado hoje?'*")
                
            except socket.gaierror:
                st.error("❌ Domínio Inválido ou Inexistente. Verifique se digitou o site corretamente.")
            except Exception as e:
                st.error(f"❌ Ocorreu um erro no processamento: {e}")
    else:
        st.warning("Por favor, digite um domínio antes de buscar.")

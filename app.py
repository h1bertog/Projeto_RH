import streamlit as st
import urllib.parse

# Configuração da Página
st.set_page_config(page_title="Calculadora de Risco de Retenção", page_icon="⚠️")

st.title("⚠️ Calculadora de Risco de Talento")
st.write("""
Esta ferramenta utiliza heurísticas de RH para estimar a probabilidade de um colaborador chave pedir demissão nos próximos 6 meses.
**Responda pensando num colaborador específico.**
""")

st.markdown("---")

# --- INPUTS (AS PERGUNTAS) ---

# 1. Tempo sem aumento
tempo_aumento = st.selectbox(
    "Há quanto tempo este colaborador não recebe um aumento real ou promoção?",
    ("Menos de 1 ano", "Entre 1 e 2 anos", "Mais de 2 anos")
)

# 2. Salário vs Mercado
mercado = st.selectbox(
    "Como avalia a remuneração dele face ao mercado?",
    ("Acima da média", "Na média", "Abaixo da média")
)

# 3. Relação com Gestão
gestao = st.selectbox(
    "Como é a relação entre o colaborador e a gestão direta?",
    ("Próxima e com feedback frequente", "Estritamente profissional/Neutra", "Distante ou com atritos")
)

# 4. Perfil do Profissional
perfil = st.selectbox(
    "Como classifica o perfil e performance do colaborador?",
    ("Performance Média/Baixa", "Bom executor (Estável)", "High Performer / Alto Potencial")
)

# 5. Flexibilidade
flexibilidade = st.selectbox(
    "O colaborador está satisfeito com o modelo de trabalho (Híbrido/Presencial/Remoto)?",
    ("Sim, trabalha no modelo que prefere", "Não, reclama da falta de flexibilidade")
)

# --- CÁLCULO DO SCORE (O BACKEND) ---
score = 0

# Lógica Pergunta 1
if tempo_aumento == "Entre 1 e 2 anos": score += 15
elif tempo_aumento == "Mais de 2 anos": score += 30

# Lógica Pergunta 2
if mercado == "Na média": score += 10
elif mercado == "Abaixo da média": score += 25

# Lógica Pergunta 3
if gestao == "Estritamente profissional/Neutra": score += 10
elif gestao == "Distante ou com atritos": score += 20

# Lógica Pergunta 4
if perfil == "Bom executor (Estável)": score += 5
elif perfil == "High Performer / Alto Potencial": score += 15

# Lógica Pergunta 5
if flexibilidade == "Não, reclama da falta de flexibilidade": score += 10

# --- RESULTADO FINAL ---

if st.button("Calcular Risco de Saída"):
    st.markdown("---")
    
    # Definição da Cor e Mensagem
    if score < 40:
        cor = "green"
        nivel = "BAIXO"
        mensagem = "Este colaborador parece estável, mas mantenha o acompanhamento."
    elif score < 75:
        cor = "orange"
        nivel = "MÉDIO"
        mensagem = "Atenção! Existem fatores de risco que precisam de ser tratados a curto prazo."
    else:
        cor = "red"
        nivel = "CRÍTICO"
        mensagem = "Ação Imediata Necessária! A probabilidade de saída nos próximos 3-6 meses é muito alta."

    # Exibição
    st.markdown(f"## Risco Identificado: :{cor}[{nivel}]")
    st.progress(score)
    st.metric(label="Pontuação de Risco (0-100)", value=f"{score}/100")
    st.info(mensagem)
    
    # O GANCHO DE VENDA (Call to Action)
    st.markdown("### Quer analisar toda a sua equipe?")
    st.write("Esta análise foi feita para apenas uma pessoa. Imagine ter este dado cruzado com a sua folha de pagamentos para prever o risco de turnover de toda a empresa.")
    # Criando a mensagem automática
    texto = "Oi! Acabei de usar a Calculadora de Risco de Talento e gostaria de mais informações."
    texto_codificado = urllib.parse.quote(texto)
    link_whatsapp = f"https://wa.me/5512991281387?text={texto_codificado}"

    st.link_button("Falar com o Especialista", link_whatsapp)
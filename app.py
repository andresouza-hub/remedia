import streamlit as st
from load_data import load_data
from analyzer import descriptive_stats

st.set_page_config(page_title="RemedIA – Análise Ambiental", layout="wide")
st.title("🧪 RemedIA – Inteligência Artificial para Áreas Contaminadas")

uploaded_file = st.file_uploader("📁 Envie sua planilha (.xlsx ou .csv)", type=["xlsx", "csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.success("Arquivo carregado com sucesso.")
    st.dataframe(df.head())

    if st.button("Calcular Estatísticas"):
        desc_stats = descriptive_stats(df)
        st.write(desc_stats)

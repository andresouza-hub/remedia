import streamlit as st
from load_data import load_data
from analyzer import descriptive_stats
from visualizer import plot_boxplot, plot_series, plot_correlacao
from reporter import generate_report
import tempfile
import os

st.set_page_config(page_title="RemedIA – Análise Ambiental", layout="wide")
st.title("🧪 RemedIA – Inteligência Artificial para Áreas Contaminadas")

# Variáveis globais protegidas por session_state
if "desc_df" not in st.session_state:
    st.session_state["desc_df"] = None

uploaded_file = st.file_uploader("📁 Envie sua planilha (.xlsx ou .csv)", type=["xlsx", "csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.success("Arquivo carregado com sucesso.")
    st.dataframe(df.head())

    if st.button("Calcular Estatísticas Descritivas"):
        st.session_state["desc_df"] = descriptive_stats(df)
        st.write(st.session_state["desc_df"])

    st.header("📉 Gráficos")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Gerar Boxplot"):
            fig_box = plot_boxplot(df)
            st.pyplot(fig_box)

    with col2:
        if st.button("Gerar Série Temporal"):
            fig_serie = plot_series(df)
            st.pyplot(fig_serie)

    if st.button("Gerar Gráfico de Correlação"):
        fig_corr = plot_correlacao(df)
        st.pyplot(fig_corr)

    st.header("📄 Relatório Técnico")

    if st.session_state["desc_df"] is not None:
        if st.button("Gerar Relatório Word"):
            imagens = []

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as f1:
                plot_boxplot(df).savefig(f1.name)
                imagens.append(f1.name)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as f2:
                plot_series(df).savefig(f2.name)
                imagens.append(f2.name)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as f3:
                plot_correlacao(df).savefig(f3.name)
                imagens.append(f3.name)

            doc_path = generate_report(st.session_state["desc_df"], imagens)

            with open(doc_path, "rb") as f:
                st.download_button("📥 Baixar Relatório Word", f, file_name="Relatorio_RemedIA.docx")

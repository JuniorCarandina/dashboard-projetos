
# Dashboard Web para Monitoramento de Projetos
# Utiliza Streamlit para exibir tarefas em andamento de forma interativa

import streamlit as st
import pandas as pd
import plotly.express as px

# Carrega os dados (substituir pelo caminho do seu CSV atualizado)
df = pd.read_csv("tasks_2025-07-17_14_28_56.csv")

# Limpeza e renomeação
colunas = df.columns.tolist()
colunas[:3] = ["Tarefa", "Andamento", "Responsavel"]
df.columns = colunas

# Conversão para numérico
try:
    df["Andamento"] = pd.to_numeric(df["Andamento"], errors="coerce")
except:
    pass

st.set_page_config(layout="wide")
st.title("Dashboard de Andamento de Projetos")

# Filtros
responsaveis = df["Responsavel"].dropna().unique().tolist()
responsavel_sel = st.sidebar.multiselect("Filtrar por responsável:", responsaveis, default=responsaveis)
df_filtrado = df[df["Responsavel"].isin(responsavel_sel)]

# KPIs
col1, col2 = st.columns(2)
media_geral = df_filtrado["Andamento"].mean()
total_tarefas = df_filtrado.shape[0]
col1.metric("Andamento Médio", f"{media_geral:.1f}%")
col2.metric("Total de Tarefas", f"{total_tarefas}")

# Gráfico de Barras por Responsável
df_resp = df_filtrado.groupby("Responsavel")["Andamento"].mean().reset_index()
fig_resp = px.bar(df_resp, x="Responsavel", y="Andamento", title="Média de Andamento por Responsável", color="Responsavel", text_auto=True)
st.plotly_chart(fig_resp, use_container_width=True)

# Gráfico de Pizza por Faixa de Andamento
faixas = pd.cut(
    df_filtrado["Andamento"],
    bins=[-1, 0, 50, 80, 100],
    labels=["0%", "1-50%", "51-80%", "81-100%"]
)

contagem_faixas = faixas.value_counts().reset_index()
contagem_faixas.columns = ["Faixa", "Total"]

# Só plota se houver dados
if not contagem_faixas.empty:
    fig_pizza = px.pie(
        contagem_faixas,
        names="Faixa",
        values="Total",
        title="Distribuição por Faixa de Andamento"
    )
    st.plotly_chart(fig_pizza, use_container_width=True)
else:
    st.warning("Nenhum dado para exibir na pizza de andamento.")


# Tabela detalhada
st.subheader("Tarefas em Andamento")
st.dataframe(df_filtrado.sort_values("Andamento", ascending=False), use_container_width=True)

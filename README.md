
# Dashboard de Andamento de Projetos

Este dashboard interativo foi desenvolvido em **Streamlit** para exibir o andamento das tarefas de projetos da empresa.

## Funcionalidades

- Gráfico de barras com andamento por responsável
- Gráfico de pizza com distribuição por faixa de progresso
- Indicadores gerais de desempenho
- Tabela com todas as tarefas e filtros dinâmicos

## Como executar

1. Instale o Streamlit:
```bash
pip install streamlit plotly pandas
```

2. Rode o aplicativo com:
```bash
streamlit run app.py
```

3. O dashboard abrirá no navegador (geralmente em `http://localhost:8501`)

## Atualização de dados

Basta substituir o arquivo `tasks_2025-07-17_14_28_56.csv` para atualizar as informações no painel.

## Hospedagem

Você pode usar o [Streamlit Cloud](https://streamlit.io/cloud) e apontar este repositório para deixar o painel online.

---
Desenvolvido com ❤ para uso na Sala de Projetos.

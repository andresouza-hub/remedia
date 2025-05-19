import pandas as pd

def load_data(uploaded_file):
    """
    Função para carregar os dados do Excel ou CSV.
    Parâmetros:
    - uploaded_file: Arquivo enviado pelo usuário.

    Retorna:
    - DataFrame com os dados carregados.
    """
    try:
        # Identificar o tipo de arquivo
        if uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            return None

        # Padronizar os nomes das colunas
        df.columns = df.columns.str.strip().str.lower()
        df.rename(columns={
            'data': 'Data',
            'frequencia': 'Frequência',
            'vácuo': 'Vácuo',
            'vazão': 'Vazão'
        }, inplace=True)

        return df

    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None

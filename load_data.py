import pandas as pd

def load_data(uploaded_file):
    try:
        if uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            return None

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

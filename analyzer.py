import pandas as pd

def descriptive_stats(df):
    try:
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        stats = numeric_df.describe().transpose()
        stats['median'] = numeric_df.median()
        stats['variance'] = numeric_df.var()
        stats['std_dev'] = numeric_df.std()
        return stats
    except Exception as e:
        print(f"Erro ao calcular estatísticas: {e}")
        return None

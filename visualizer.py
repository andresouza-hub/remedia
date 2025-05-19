import matplotlib.pyplot as plt

def plot_boxplot(df):
    fig, ax = plt.subplots()
    df.boxplot(column='Vazão', ax=ax)
    ax.set_title("Boxplot de Vazão")
    return fig

def plot_series(df):
    fig, ax = plt.subplots()
    df.plot(x='Data', y='Vazão', ax=ax, marker='o')
    ax.set_title("Série Temporal de Vazão")
    return fig

def plot_correlacao(df):
    fig, ax = plt.subplots()
    ax.scatter(df['Vazão'], df['Frequência'])
    ax.set_xlabel("Vazão")
    ax.set_ylabel("Frequência")
    ax.set_title("Correlação Vazão vs Frequência")
    return fig

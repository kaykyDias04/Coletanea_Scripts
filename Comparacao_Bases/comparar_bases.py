import pandas as pd
import tkinter as tk
from tkinter import filedialog

def sanity_check(df_novo, df_antigo, limiar=0.10):
    stats_novo = {
        "contagem": len(df_novo),
        "faturamento": df_novo["Salario"].sum() if "Salario" in df_novo.columns else 0,
        "nulos": df_novo.isnull().sum().sum()
    }
    
    stats_antigo = {
        "contagem": len(df_antigo),
        "faturamento": df_antigo["Salario"].sum() if "Salario" in df_antigo.columns else 0,
        "nulos": df_antigo.isnull().sum().sum()
    }
    
    alertas = []
    
    if stats_antigo["contagem"] > 0:
        var_contagem = abs(stats_novo["contagem"] - stats_antigo["contagem"]) / stats_antigo["contagem"]
        if var_contagem > limiar:
            alertas.append(f"Variação crítica no volume de dados: {var_contagem:.2%}")
        
    if stats_antigo["faturamento"] > 0:
        var_fat = abs(stats_novo["faturamento"] - stats_antigo["faturamento"]) / stats_antigo["faturamento"]
        if var_fat > limiar:
            alertas.append(f"Variação crítica no faturamento/folha: {var_fat:.2%}")
            
    if stats_novo["nulos"] > stats_antigo["nulos"] * (1 + limiar):
        alertas.append(f"Aumento anormal de campos nulos: {stats_novo['nulos']} encontrados")

    return alertas

def selecionar_arquivo(titulo):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    caminho = filedialog.askopenfilename(title=titulo, filetypes=[("Arquivos Excel", "*.xlsx *.xls")])
    root.destroy()
    return caminho

try:
    print("Selecione a base ATUAL...")
    caminho_atual = selecionar_arquivo("Selecione a Base ATUAL")
    
    print("Selecione a base ANTERIOR...")
    caminho_anterior = selecionar_arquivo("Selecione a Base ANTERIOR")

    if caminho_atual and caminho_anterior:
        base_atual = pd.read_excel(caminho_atual)
        base_anterior = pd.read_excel(caminho_anterior)
        
        resultados = sanity_check(base_atual, base_anterior)
        
        if resultados:
            print("\nALERTA DE INTEGRIDADE:")
            for a in resultados:
                print(f"- {a}")
        else:
            print("\nSanity check aprovado. Dados consistentes com o histórico.")
    else:
        print("\nSeleção de arquivos cancelada.")

except Exception as e:
    print(f"\nErro na execução: {e}")
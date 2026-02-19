import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

def organizar_por_criacao(diretorio_origem):
    meses_pt = {
        1: "Janeiro", 2: "Fevereiro", 3: "Marco",
        4: "Abril", 5: "Maio", 6: "Junho",
        7: "Julho", 8: "Agosto", 9: "Setembro",
        10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    if not diretorio_origem:
        return

    for raiz, diretorios, arquivos in os.walk(diretorio_origem):
        if any(mes in raiz for mes in meses_pt.values()):
            continue

        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            
            timestamp_criacao = os.path.getctime(caminho_completo)
            data = datetime.fromtimestamp(timestamp_criacao)
            
            ano = str(data.year)
            mes_nome = meses_pt[data.month]
            
            destino_pasta = os.path.join(raiz, ano, mes_nome)
            
            if not os.path.exists(destino_pasta):
                os.makedirs(destino_pasta)
            
            try:
                shutil.move(caminho_completo, os.path.join(destino_pasta, arquivo))
                print(f"Criado em {data.strftime('%d/%m/%Y')} -> Movido para {ano}/{mes_nome}")
            except Exception as e:
                print(f"Erro ao mover {arquivo}: {e}")

def selecionar_pasta():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    caminho = filedialog.askdirectory(title="Selecionar Pasta (Organizar por Criação)")
    root.destroy()
    return caminho

if __name__ == "__main__":
    pasta = selecionar_pasta()
    organizar_por_criacao(pasta)
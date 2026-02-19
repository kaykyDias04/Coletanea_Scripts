import os
import time
from datetime import datetime, timedelta

def criar_cenario_complexo():
    pasta_raiz = "Projetos_Engenharia_Complexo"
    
    # Criando estrutura de pastas dentro de pastas
    subpastas = [
        os.path.join(pasta_raiz, "Documentos_Antigos", "RH"),
        os.path.join(pasta_raiz, "Obras_2024", "Plantas", "PDFs"),
        os.path.join(pasta_raiz, "Backup_Temporario", "Fotos_Terreno"),
        os.path.join(pasta_raiz, "Secretaria_X")
    ]
    
    for pasta in subpastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
    
    extensoes = ['.pdf', '.dwg', '.xlsx']
    print(f"Criando ambiente complexo em: {os.path.abspath(pasta_raiz)}")

    # Gerando 20 arquivos espalhados pelas subpastas
    for i in range(20):
        # Seleciona uma subpasta aleatória (circular)
        pasta_alvo = subpastas[i % len(subpastas)]
        
        # Simula datas de até 3 anos atrás
        dias_atras = i * 60 
        data_simulada = datetime.now() - timedelta(days=dias_atras)
        
        nome_arquivo = f"Documento_Teste_{i+1}{extensoes[i % len(extensoes)]}"
        caminho_arquivo = os.path.join(pasta_alvo, nome_arquivo)
        
        with open(caminho_arquivo, 'w') as f:
            f.write("Conteudo de teste para auditoria.")

        # Altera a data no sistema de arquivos
        timestamp = time.mktime(data_simulada.timetuple())
        os.utime(caminho_arquivo, (timestamp, timestamp))
        
        print(f"Criado: .../{os.path.relpath(caminho_arquivo, pasta_raiz)} | Data: {data_simulada.strftime('%m/%Y')}")

    print("\nCenário complexo pronto!")

if __name__ == "__main__":
    criar_cenario_complexo()
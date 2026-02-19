import pandas as pd
import re
from datetime import datetime
from pathlib import Path

# --- VALIDAÇÕES ---

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', str(cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = (soma * 10 % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True

def validar_data(data):
    try:
        return pd.to_datetime(data) <= datetime.now()
    except:
        return False

def validar_uf(uf):
    ufs = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
           'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    return str(uf).upper() in ufs

# --- TRATAMENTO ---

def tratar_dados_excel(df):
    df = df.drop_duplicates()
    colunas_texto = df.select_dtypes(include=['object', 'string']).columns
    for col in colunas_texto:
        df[col] = df[col].apply(lambda x: str(x).strip() if pd.notna(x) else x)

    if 'Nome' in df.columns:
        df['Nome'] = df['Nome'].apply(lambda x: str(x).title() if pd.notna(x) and str(x).lower() != 'nan' else x)
    if 'UF' in df.columns:
        df['UF'] = df['UF'].apply(lambda x: str(x).upper() if pd.notna(x) else x)
    if 'CPF' in df.columns:
        df['CPF'] = df['CPF'].apply(lambda x: str(re.sub(r'\D', '', str(x))).zfill(11) if pd.notna(x) and str(x) != '' else x)
    if 'CEP' in df.columns:
        df['CEP'] = df['CEP'].apply(lambda x: str(re.sub(r'\D', '', str(x))).zfill(8) if pd.notna(x) and str(x) != '' else x)
    if 'Telefone' in df.columns:
        df['Telefone'] = df['Telefone'].apply(lambda x: re.sub(r'\D', '', str(x)) if pd.notna(x) else x)
    return df

# --- EXECUÇÃO ---

def executar_processamento():
    pasta_atual = Path.cwd()
    pasta_destino = pasta_atual / "planilhas formatadas"
    pasta_destino.mkdir(exist_ok=True)
    
    arquivos = [arq for arq in pasta_atual.glob("*.xlsx") if not arq.name.startswith("~") and "_formatado" not in arq.name]

    for arq in arquivos:
        try:
            df = pd.read_excel(arq)
            df = tratar_dados_excel(df)
            
            status_list = []
            detalhes_list = []

            for _, row in df.iterrows():
                erros = []
                
                if not validar_cpf(row.get('CPF')): erros.append("CPF")
                if pd.isna(row.get('Nome')) or str(row.get('Nome')).lower() == 'nan': erros.append("Nome")
                if not re.match(r"[^@]+@[^@]+\.[^@]+", str(row.get('Email'))): erros.append("E-mail")
                if not (10 <= len(str(row.get('Telefone'))) <= 11): erros.append("Telefone")
                if not validar_data(row.get('Data_Admissao')): erros.append("Data")
                
                try:
                    sal = float(str(row.get('Salario')).replace('R$', '').replace('.', '').replace(',', '.'))
                    if sal <= 0: erros.append("Salario<=0")
                except:
                    erros.append("Salario_Inv")

                if not validar_uf(row.get('UF')): erros.append("UF")
                if len(str(row.get('CEP'))) != 8: erros.append("CEP")

                if erros:
                    status_list.append("NOT_OK")
                    detalhes_list.append("Erro em: " + " | ".join(erros))
                else:
                    status_list.append("OK")
                    detalhes_list.append("")

            df['Status'] = status_list
            df['Inconsistencias'] = detalhes_list
            
            # Divisão em dois DataFrames
            df_ok = df[df['Status'] == 'OK'].drop(columns=['Status', 'Inconsistencias'])
            df_not_ok = df[df['Status'] == 'NOT_OK']

            # Salvamento em abas diferentes
            caminho_final = pasta_destino / f"{arq.stem}_formatado.xlsx"
            with pd.ExcelWriter(caminho_final) as writer:
                df_ok.to_excel(writer, sheet_name='Base_Limpa', index=False)
                df_not_ok.to_excel(writer, sheet_name='Revisar_Erros', index=False)
            
            print(f"Sucesso: {arq.name} ({len(df_ok)} OK, {len(df_not_ok)} NOT_OK)")

        except Exception as e:
            print(f"Erro ao processar {arq.name}: {e}")

if __name__ == "__main__":
    executar_processamento()
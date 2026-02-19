# Validador de Planilhas Excel

Este script em Python foi desenvolvido para automatizar o processo de higienização e auditoria de bases de dados em Excel. Ele não apenas limpa os dados, mas também valida regras de negócio críticas, separando o que está pronto para uso do que precisa de correção.

## Funcionalidades

### 1. Tratamento Automático (Auto-Cleaning)
O script corrige falhas comuns de digitação e formatação antes mesmo de validar:
* **Trim Automático**: Remove espaços invisíveis no início e fim de todos os textos.
* **Padronização de Nomes**: Aplica *Title Case* (ex: "JOÃO DA SILVA" -> "João Da Silva").
* **Normalização de UF**: Converte siglas de estados para maiúsculas.
* **Recuperação de Zeros**: Restaura zeros à esquerda em CPFs e CEPs que o Excel costuma remover.
* **Limpeza de Símbolos**: Remove parênteses e traços de campos numéricos (Telefone, CPF, CEP).

### 2. Auditoria de Regras de Negócio
Verifica a integridade de cada linha com base em critérios rigorosos:
* **CPF**: Validação matemática por dígitos verificadores.
* **E-mail**: Verificação de formato padrão (user@dominio.com).
* **Datas**: Bloqueio de datas futuras ou formatos inválidos.
* **Financeiro**: Identificação de salários negativos ou valores não numéricos.
* **Geográfico**: Validação de siglas de UF brasileiras e extensão de CEP.

## Estrutura de Saída

O script lê todos os arquivos `.xlsx` da pasta atual e gera uma pasta chamada `/planilhas formatadas/`. Cada arquivo gerado contém duas abas:

1.  **`Base_Limpa`**: Apenas as linhas que passaram em **todas** as validações.
2.  **`Revisar_Erros`**: Linhas com problemas, acompanhadas das colunas `Status` (NOT_OK) e `Inconsistencias` (detalhando o que deve ser corrigido).

## Pré-requisitos

Python + bibliotecas necessárias:

```bash
pip install pandas openpyxl
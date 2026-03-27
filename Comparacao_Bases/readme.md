## README - Script de Sanity Check
// Este documento descreve o funcionamento e a utilização do script de validação de integridade de dados.

## Objetivo
// Validar a integridade de dados comparando uma base atual com uma base anterior.
// O script identifica desvios superiores a 10% nos seguintes critérios:
* Volume total de registros.
* Soma total de valores (coluna Salário).
* Quantidade de campos nulos.

## Requisitos
// Dependências necessárias para a execução do script:
* Python 3.x
* Bibliotecas: `pandas`, `openpyxl`, `tkinter`

## Estrutura do Código
// Descrição das principais funções e lógica do sistema:

* **sanity_check**: Executa a lógica de comparação entre DataFrames (Contagem, Soma de Salário e Nulos).
* **selecionar_arquivo**: Abre a interface gráfica (Tkinter) para busca de arquivos localmente.
* **Fluxo Principal**: Coordena a leitura dos arquivos Excel e a exibição de alertas de inconsistência no console.

## Como Utilizar
// Passo a passo para operação:

1. **Executar o script**: Inicie o arquivo .py no seu ambiente Python.
2. **Selecionar Arquivos**: O sistema abrirá uma janela para selecionar a "Base Atual" e, em seguida, a "Base Anterior".
3. **Verificar o Console**: 
   * Se houver variações críticas (> 10%), os alertas serão listados detalhadamente.
   * Caso os dados estejam dentro da margem, uma mensagem de aprovação será exibida.

## Tratamento de Erros
// Regras de interrupção e segurança do processo:

* O script interrompe a execução caso a coluna **Salario** não seja encontrada.
* Emite alertas caso os arquivos estejam corrompidos ou ilegíveis.
* Informa erro caso o processo de seleção de arquivos seja cancelado pelo usuário.

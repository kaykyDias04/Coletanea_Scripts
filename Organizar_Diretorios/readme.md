# Organizador de Arquivos por Data (Python)

Este script automatiza a organização de arquivos movendo-os para pastas estruturadas por **Ano** e **Mês**, baseando-se na data de criação de cada arquivo. É ideal para organizar backups de fotos, documentos ou downloads acumulados.

---

## Funcionalidades

* **Seleção Visual:** Abre uma janela do sistema para selecionar a pasta (sem necessidade de digitar caminhos).
* **Nomenclatura em PT-BR:** Cria pastas com nomes dos meses em português (ex: "Janeiro", "Fevereiro").
* **Recursividade Segura:** O script percorre subpastas, mas ignora as pastas que ele mesmo criou para evitar loops.
* **Tratamento de Erros:** Se um arquivo estiver aberto ou bloqueado, o script pula para o próximo e gera um aviso no log.

## Pré-requisitos

O script utiliza apenas bibliotecas padrão do Python:

* **Python 3.14**
* **Tkinter**

## Como Usar

1. Baixe a pasta Organizar_Diretórios
2. Execute o arquivo organizar_diretorios.exe na pasta dist
4. Uma janela aparecerá: selecione a pasta desejada e clique em "Selecionar pasta"

## Estrutura de Saída

Após a execução, seus arquivos serão organizados assim:

```text
Caminho/Da/Sua/Pasta/
├── 2023/
│   ├── Janeiro/
│   │   └── foto_ferias.jpg
│   └── Dezembro/
│       └── nota_fiscal.pdf
└── 2024/
    └── Março/
        └── projeto_final.docx
```

---

## Observações Importantes

> [!CAUTION]
> O script utiliza `shutil.move`, o que significa que os arquivos são **deslocados** da pasta original. Recomenda-se fazer um backup ou testar em uma pasta menor antes de processar grandes volumes de dados críticos.

---

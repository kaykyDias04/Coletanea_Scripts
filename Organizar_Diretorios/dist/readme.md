# Organizador de Google Drive por Data (Google Apps Script)

Este script automatiza a organização de arquivos dentro do seu Google Drive, movendo-os para pastas estruturadas por **Ano** e **Mês** (Ex: `2024 > 03 - Março`). 

Diferente de scripts comuns, este foi projetado para lidar com grandes volumes de dados, utilizando um sistema de **gatilhos automáticos** para não travar devido aos limites de tempo do Google.

---

## Diferenciais desta Versão

* **Execução em Nuvem:** Não precisa baixar nada ou manter o PC ligado. roda diretamente nos servidores do Google.
* **Sistema de Retomada (Checkpoint):** O Google limita scripts a 6 minutos de execução. Este script monitora o tempo e, se estiver perto do limite, cria um agendamento para continuar de onde parou após 1 minuto.
* **Organização Padronizada:** Cria pastas numeradas (ex: `01 - Janeiro`) para garantir que os meses fiquem em ordem alfabética correta no Drive.
* **Recursividade:** Organiza arquivos na raiz e entra em todas as subpastas automaticamente.

## Como Instalar e Usar

1.  Acesse o [Google Apps Script](https://script.google.com/).
2.  Clique em **"Novo Projeto"**.
3.  Apague o código padrão e cole o conteúdo do seu arquivo `.gs`.
4.  Clique no ícone de **Disquete (Salvar)** e dê um nome ao projeto (ex: "Organizador de Drive").
5.  No menu superior, selecione a função `executarOrganizadorComPausa` e clique em **Executar**.
6.  **Autorização:** O Google pedirá permissão para acessar seu Drive. Conceda as permissões (é possível que apareça um aviso de "App não verificado", clique em *Avançado* > *Acessar [Nome do Projeto]*).

## Como funciona a Lógica de Pausa

* O script verifica o tempo de execução a cada pasta.
* Se ultrapassar **5 minutos (300.000ms)**, ele salva o ID da pasta atual no `PropertiesService`.
* Ele cria um **Gatilho (Trigger)** para rodar o script novamente em 1 minuto.
* Ao terminar todo o processo, ele limpa os gatilhos e as propriedades automaticamente.

## Estrutura de Saída

```text
Meu Drive/
├── 2023/
│   ├── 01 - Janeiro/
│   │   └── backup_celular.jpg
│   └── 12 - Dezembro/
│       └── recibo.pdf
└── 2024/
    └── 03 - Março/
        └── planilha_gastos.gsheet
```
<img width="1635" height="256" alt="image" src="https://github.com/user-attachments/assets/5698c9a4-66cc-48c2-9810-20869db58ff8" />

---

## Avisos Importantes

> [!IMPORTANT]
> O script ignora pastas que já tenham o nome de um ano (4 dígitos) ou o nome de um mês da lista, evitando que ele tente organizar o que já está organizado.

> [!CAUTION]
> A função `arquivo.moveTo(destino)` move o arquivo original. Certifique-se de que deseja reorganizar sua estrutura antes de iniciar o processo em pastas compartilhadas.

---

# Instalação  
  
## Requerimentos  

    Para poder rodar o projeto, é necessário ter as seguintes dependências instaladas:  
        - sqlite3  
        - flask  
        - flask_httpauth  
        - json  
        - hashlib  
        - datetime  

## Inicialização

    Depois de instalar os requerimentos, é necessário inicializar o banco de dados e rodar o script de configuração, que popula o banco com a estrutura necessária para seu funcionamento.  
    Para isso, abra um terminal e rode o commando a seguir:  

    ```sh
    $ sqlite3
    ```

    Isso abrirá o shell do sqlite3, com ele aberto podemos criar a base de dados quiz.db com o seguinte commando:

    ```sh
    .open quiz.db
    ```

    E em seguida rodar o script sql com o commando:

    ```sh
    .read quiz.sql
    ```

    Agora o banco de dados está configurado e pronto para uso. Para sair do shell do sqlite3 basta escrever:

    ```sh
    .quit
    ```

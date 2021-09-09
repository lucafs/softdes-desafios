# Instalação  
  
## Requerimentos  

   Para poder rodar o projeto, é necessário ter as seguintes dependências instaladas:  
       - sqlite3  
       - flask  
       - flask_httpauth  
       - json  
       - hashlib  
       - datetime  

## Inicialização do Banco de Dados

   Depois de instalar os requerimentos, é necessário inicializar o banco de dados  
   e rodar o script de configuração, que popula o banco com a estrutura necessária  
   para seu funcionamento.  
   Para isso, abra um terminal e rode o commando a seguir:  
    
    $ sqlite3
    
   Isso abrirá o shell do sqlite3, com ele aberto podemos criar a base de dados quiz.db com o seguinte commando:

    sqlite> .open quiz.db

   E em seguida rodar o script sql com o commando:

    sqlite> .read quiz.sql

   Agora o banco de dados está configurado e pronto para uso. Para sair do shell do sqlite3 basta escrever:
    
    sqlite> .quit

## Inicialização do servidor
    
   Para poder acessar a aplicação é preciso inicar o servidor local antes. Você pode  
   fazer isso rodando o arquivo python softdes.py em seu terminal. É necessário dar  
   permissão de super user para que ele possa rodar sem erros.
    
    $ sudo python softdes.py
    
   Depois de iniciado o servidor estará disponível em http://localhost:80/

## Adicionando o primeiro usuário

   Inicialmente o servidor não terá usuários registrados, portanto é preciso adicionar  
   um usuário para poder se conectar a aplicação. Crie um arquivo chamado users.csv no  
   diretório src do projeto. Este arquivo deverá conter para cada linha o nome do usuário  
   e seu cargo de aluno ou professor (conforme a imagem abaixo). Se for desejado um usuário administrador   
   (no caso de um usuário para professor), de o nome do usuário de admin ou fabioja.
    
![users.csv iamge](https://imgur.com/m1huFhZ.png)

   Com o csv pronto, rode o arquivo python adduser.py com permissão de super user:
    
    $ sudo python adduser.py
    
   Agora você tem um usuário pronto para ser utilizado na aplicação. Para adicionar mais  
   usuários, delete todas as entradas no .csv e escreva novos usuários, caso contrário o  
   programa tentará adicionar um usuário já existente e irá dar erro.
    

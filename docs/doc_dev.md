# [Guia para instalação do ambiente](https://lucafs.github.io/softdes-desafios/Setup)

## Explicação código

## Funções

**addUser(user, password, type):**  
&nbsp;&nbsp;&nbsp; Abre uma conexão com o banco de dados quiz.db e adiciona  
um usuário do tipo **type** com nome **user** e senha **password**.  

&nbsp;&nbsp;&nbsp; A função executa o seguinte query em SQL:

    'Insert into USER(user,pass,type) values("{0}","{1}","{2}");'.format(user, pwd, type)

&nbsp;&nbsp;&nbsp; E depois da um COMMIT e fecha a conexão com o banco de dados.

&nbsp;&nbsp;&nbsp; Pode-se observar o uso da função no arquivo [addUser.py](https://github.com/lucafs/softdes-desafios/blob/main/src/adduser.py).

**OBS:** No arquivo addUser do projeto, a senha é um guardada no banco de dados como um hash do nome do usuário por motivos de segurança.

**converte_Data(orig):**  
&nbsp;&nbsp;&nbsp; Converte a data do campo expire de um Quiz da tabela QUIZ para ser exibida no html de desafios.
Datas na tabela quiz são inseridas no formato **ANO-MES-DIA HORA:MIN:SEG** e são convertidas pela função para o formato **DIA/MES/ANO HORA:MIN:SEG**.

### Getters e setters  

    Neste projeto temos os seguintes getters e setters         
        - get_quizes
            Pega quizes do banco de dados checando se o user que está fazendo a requisição é um admin. Caso não for um admin apenas pega os quizes que foram "released".
        - get_quiz  
            Igual ao get_quizes mas apenas pega um certo quiz.
        - get_user_quiz  
            Pega a resposta de um usuário para dado quiz.
        - set_user_quiz
            Da um resultado para a entrega do usuário.
        - set_info
            Coloca uma senha e um nome para o usuário.
        - get_info  
            Pega a senha e o tipo de certo usuário.
        - get_password + hash_pw
            Get_password usa o get_info para pegar a senha e o hash_pw hasheia a senha usando md5.
            
            

## Rotas

    Neste projeto temos as seguintes funções de rotas.
        - main
            Essa função é onde o grosso do aplicação reside. Nela são feitas a maioria das requests e usado os getters e setters. Além disso, tem a renderização dos templates principais.
        - change
            Uma função dedicada a troca de senhas, onde checagens básicas são feitas, como se a senha antiga confere e se a escrita da nova senha está igual às duas vezes.
        - logout  
            Função para ser feito o logout do usuário, no entanto por enquanto ela não faz nada.


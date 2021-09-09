# Guia para professores

### Setup
  Para adicionar usuários e desafios, antes o professor precisa realizar os passos "**Requerimentos**", "**Inicialização do Banco de Dados**" e "**Inicialização do servidor**" na **[Documentação de Intalação](https://lucafs.github.io/softdes-desafios/Setup)**
  
### Adicionar usuário
  Para adicionar um usuário, o professor deve seguir o passo "**Adicionando o primeiro usuário**" na **[Documentação de Intalação](https://lucafs.github.io/softdes-desafios/Setup)**
  
### Adicionar novo desafio
  Para adiocionar novos desafios o professor deve seguir os seguintes passos:
  
  Abrir um terminal e executar o seguinte comando:
  
    $ sqlite3
    
  Em seguida se conectar ao banco, executando o seguinte comando:
    
    sqlite> .open quiz.db
    
  Para adicionar um desafio, basta executar o seguinte comando, substituindo as chaves pelos valores desejados:
  
    sqlite> Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values ({0}, {1},{2},{3},{4},{5},{6});
    
  As chaves significam o seguinte:
  - {0}: Número do desafio
  - {1}: Data de criação do desafio
  - {2}: Data de expiração do desafio
  - {3}: Descrição do problema
  - {4}: Valores que serão utilizados no momento do teste
  - {5}: Respostas esperadas a partir dos valores em {4}
  - {6}: Feedback para cada teste que falhar

  Abaixo é possível ver um exemplo de inserção de desafio:
  
    sqlite> Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values (1, '2018-08-01','2021-12-31 23:59:59','Exemplo de problema','[[1],[2],[3]]','[0, 0, 0]','["a","b","c"]');
    
  Por último, basta executar o seguinte comando:
  
    sqlite> .quit
  

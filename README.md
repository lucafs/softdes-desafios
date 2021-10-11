# Desafios Soft Des

Este projeto se resume em uma ferramenta para facilitar entregas de desafios da matéria **Design de Software**. Nele o professor pode adicionar desafios e os alunos podem subir soluções para os respectivos desafios.


-----------------

## Visual da plataforma

<div align="center">
  <img src="https://i.imgur.com/D4JPBuY.png"><br>
</div>

-----------------

## Documentações
[**Guia de Instalação**](https://lucafs.github.io/softdes-desafios/Setup)

[**Documentação de Usuário**](https://lucafs.github.io/softdes-desafios/doc_user)

[**Documentação de Desenvolvedor**](https://lucafs.github.io/softdes-desafios/doc_dev)

## Inialização com Docker
Para criar o ambiente com docker, basta entrar no diretório do projeto e rodar o seguinte comando:
```
$ docker compose up
```


## Testes
Para rodar os testes, primeiro é necessarrio instalar o `pytest`, o `selenium` e ter o [driver](https://github.com/mozilla/geckodriver/releases) do firefox instalado.
Em seguida, é necessário criar o ambiente a partir do Docker
Por útlimo, entre na pasta `test` do repositório e rode os seguintes comandos:
```
$ pytest test_unitario.py
```
```
$ pytest test_usuario.py
```

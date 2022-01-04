# Criando um Producer e Consumer utilizando RabbitMQ e Python

## :orange_book: <b>Desafio da aplicação</b>

O desafio é criar um servidor(Broker) com o rabbitMQ e criar uma aplicação para ser o Producer e outra para ser o Consumer, utilizando a linguagem Python, onde o Producer enviará e o Consumer irá receber dados.

## <b>:dart: Objetivo da Aplicação </b>

Realizar testes da funcionalidade do RabbitMQ, com cunho didático. Analisar fluxo de dados, métricas, filas com o RabbitMQ Management.


## <b>⚙️ Tecnologias Adotadas na Solução:</b>

* Python 3.8.10
* RabbitMQ 3.9.11
* Erlang/OTP 24.2
* Ubuntu 20.04.3 LTS


## :books: Bibliotecas Utilizadas

* pika


## :hammer: Construindo o Projeto

### Instalando o Erlang/OTP

O RabbitMQ foi desenvolvido com a linguagem ERLANG e, por isso, deverá ser instalado no servidor onde o Rabbit estará instalado.

#### Instale os pacotes abaixo:

```linux
sudo apt-get install -y erlang-base \
                        erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets \
                        erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key \
                        erlang-runtime-tools erlang-snmp erlang-ssl \
                        erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl
```

### Instalando o RabbitMQ:

```linux
sudo apt-get install rabbitmq-server -y --fix-missing
```

#### Execute o serviço do RabbitMQ:

```linux
systemctl start rabbitmq-server
```


#### Habilitar o RabbitMQ Management

```linux
rabbitmq-plugins enable
```


## Conclusão:

Agora é possível executar os scripts de producer.py e consumer.py. Não se esqueça de criar um ambiente virtual e instalar a biblioteca pika ;)



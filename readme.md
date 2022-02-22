# Instant Messenger 

## Execução do projeto

É necessário possuir instalado alguma versão do python 3 no sistema.
**O servidor deve ser executado antes do cliente.**

- No diretório src/ abra um terminal e execute o script server.py

```
$ python server.py
```

- No mesmo diretório src/ abrir outro terminal e executar o script client.py
```
$ python client.py
```
- Digite o endereço do servidor no prompt de cliente. O endereço do servidor está sendo exibido no prompt do servidor na forma:

```
 [LISTENING] Endereço do servidor: XXX.X.X.X
```
   

- Digite o nome do cliente
- Para enviar uma mensagem o cliente deve digitar somente ao lado das setas:
```
>>
```
- Caso as setas não estejam presentes no prompt, tecle enter.
- Outros clientes podem ser conectados ao servidor pelo mesmo procedimento, devendo apenas ser conectado por outros terminais.
- Outros dispositivos podem ser conectados ao servidor, desde que estejam na mesma rede local.
- Para sair da conversa, o cliente deve escrever o comando:
```
>>!SAIR
```
- O servidor pode ser encerrado pelo comando `Ctrl + c` ou terminando o processo do terminal executando-o.

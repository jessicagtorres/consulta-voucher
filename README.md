# consulta-voucher

**Visão Geral**

Este programa permite aos usuários consultarem os vales presentes e seus status (se foi utilizado ou não) consultando um banco de dados ODBC.

**Instalação e Configuração**

Baixe o código-fonte do programa.
Instale as dependências necessárias listadas no arquivo requirements.txt.
Execute o programa a partir da linha de comando utilizando o seguinte comando:  
```python consulta-voucher.py```

**Guia do Usuário**

Abra o programa "Consulta de Vale Presente".  
Informe o código do vale presente.  
Clique no botão "Consultar".  
O programa consultará o banco de dados ODBC para validar o vale presente e exibirá o resultado com os seguintes dados:   
Código do vale presente;  
Loja utilizada;  
Data de utilização;  
PDV;  
Valor do Vale Presente;  
Data de vencimento;  
Loja autorizada;  
CPF vinculado.

*Obs.: Os campos "Loja utilizada, data de utilização e PDV" somente constarão informações caso o  voucher tenha sido utilizado em algum momento sem cancelamento da venda.*

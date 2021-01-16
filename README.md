## How It Works

* **projeto**
* **python**
* **selenium**
* **chromedriver**


## Projeto de automação e2e utilizando selenium

Principal objetivo desse projeto é compartilhar conhecimentos e através de uma estrutura simplificada.

-e2e

--page_factory

--page_objective 

--test

--utils


#####Primeiro passo para realizar um bom teste é planejar o teste.
**Definição das pré-confições com o setUp**

-Tudo aquilo que será executado para cada teste case executado antes dos steps do test case

**Exemplo:** Acessar a pagina principal da aplicação pois todas as vezes que o teste for executado ele deverá acessar a pagina inicia.


**Definição dos steps de teste**

-Execução dos steps, simulando o comprtamento do usuario

**Exemplo:** 

* Realizar login

   Acessar pagina inicial
   
   Preencher campo nome 
   
   Preencher campo senha
   
   Clicar no botão submmit
   
**Definição das validações em cada test case dependendo do contexto**

**Exemplo:** Após acessar a tela inicial encontrar um item unico que possa ser utilizado como resultado esperado ou esse elemento seja um requisito do sistema que deverá aparecer apos sua execução.


Pode ser validado o resultado após realizar login validando para qual pagina o usuário foi direcionado


**Definição de TearDown**

Tudo aquilo que a aplicação deve executar ao final de cada teste case

**Exemplo** Fechar a janela, limpar o banco de dados e etc.


#Page objects

Tem como objetivo criar um conjunto de funções de teste para reaproveitamento de teste
e centralizar informações e melhorar a leitura dos testes

**Exemplo** Funcionalidade realiza login e criado a estrutura de dados para a função que realiza login.

Quando mais desacoplado for seu page object mais facilidade terá em reaproveitar código.

A funcionalidade pode ser dividia em apenas um comando de input de nome.


#Page Factory

Facilita o mapeamento de todos os elementos de cada tela do sistema 

Pode ser definido com nomenclatura simples e defacil lembrança

Uma vez os elementos mapeados podem ser facilmente chamedos atraves do intelicense da IDE proporcionando mais agilidade para os testes

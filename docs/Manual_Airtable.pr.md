



# Airtable
  
Módulo para interagir com Airtable, consultar tabelas e baixar registros  

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Login
  
Salva uma sessão e lista os bancos de dados disponíveis.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Token de acesso pessoal|Token criado na seção create/tokens do Airtable|patSE7khj3MXjcByw.2a92ada817d7e3d9e9bbe|
|Session|ID da sessão (Opcional)|session|
|Variável|Variável onde o resultado será salvo|res|

### Listar tabelas
  
Obtém uma lista com o nome e id das tabelas que estão no banco de dados escolhido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do banco de dados|ID do banco de dados obtido do comando de login|app6OeOEMw1btcZ9s|
|Session|ID da sessão (Opcional)|session|
|Variável|Variável onde o resultado será salvo|res|

### Obtener Registros
  
Obtenha registros de uma tabela
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do banco de dados|ID do banco de dados obtido do comando de login|app6OeOEMw1btcZ9s|
|ID do Tabela|ID da tabela obtido a partir do comando listar tabelas|tbl9ULBsFxuSU8aLF|
|Filtro|Fórmula de filtragem para obter os registros. Os campos estão entre colchetes. Para mais informações consulte a documentação https//support.airtable.com/docs/formula-field-reference|{Estado}='Todo'|
|Vista|Visualização ocupada conforme escrito no aplicativo, os registros serão obtidos nessa ordem|Grid|
|Session|ID da sessão (Opcional)|session|
|Variável|Variável onde o resultado será salvo|res|

### Baixar CSV
  
Exporte os registros obtidos como csv
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Registro|Dicionário com os registros obtidos com o comando 'Listar Registros'|{registros}|
|Caminho da descarga|URL onde o arquivo csv será baixado, incluindo nome e extensão do arquivo|C:\users\usuario\Downloads\registro.csv|
|Session|ID da sessão (Opcional)|session|
|Variável|Variável onde o resultado será salvo|res|

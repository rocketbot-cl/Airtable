



# Airtable
  
Module to interact with Airtable, consult tables and download records  

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Login
  
Saves a session and lists available databases.
|Parameters|Description|example|
| --- | --- | --- |
|Personal access token|Token created in the create/tokens section of Airtable|patSE7khj3MXjcByw.2a92ada817d7e3d9e9bbe|
|Session|Session ID (Optional)|session|
|Variable|Variable where the result will be saved|res|

### List Tables
  
Obtains a list with the name and id of the tables that are in the chosen database
|Parameters|Description|example|
| --- | --- | --- |
|Data Base ID|Database ID obtained from the login command|app6OeOEMw1btcZ9s|
|Session|Session ID (Optional)|session|
|Variable|Variable where the result will be saved|res|

### Get Records
  
Get records from a table
|Parameters|Description|example|
| --- | --- | --- |
|Data Base ID|Database ID obtained from the login command|app6OeOEMw1btcZ9s|
|Table ID|Table ID obtained from the list tables command|tbl9ULBsFxuSU8aLF|
|Filter|Filtering formula to get the records. The fields are enclosed in braces. For more information check the documentation https//support.airtable.com/docs/formula-field-reference|{Status}='Todo'|
|View|View that is used as it is written in the app, the records will be obtained in that order|Grid|
|Session|Session ID (Optional)|session|
|Variable|Variable where the result will be saved|res|

### Download CSV
  
Export the obtained records as csv
|Parameters|Description|example|
| --- | --- | --- |
|Record|RDictionary with the records obtained with the 'List Records' command|{records}|
|Path to download|URL where the csv file will be downloaded, include file name and extension|C:\users\usuario\Downloads\register.csv|
|Session|Session ID (Optional)|session|
|Variable|Variable where the result will be saved|res|

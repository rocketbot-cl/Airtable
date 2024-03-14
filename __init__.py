# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os.path
import sys

base_path = tmp_global_obj["basepath"] #type: ignore
cur_path = os.path.join(base_path, 'modules', 'Airtable', 'libs')
if cur_path not in sys.path:
        sys.path.append(cur_path)

# from Airtable.libs.airtable_ import Airtable_
import requests
global csv
import csv


class Airtable_:
    def __init__(self, token):
        try:
            self.session = requests.Session()
            self.session.headers = ({'Authorization': f'Bearer {token}'})
            
        except requests.exceptions.RequestException as e:
            print(f"Error de autenticación: {e}")
        
    def listar_bases(self):
        res = []
        url = 'https://api.airtable.com/v0/meta/bases'
        response = self.session.get(url)
        if response.status_code == 200:
            bases = response.json().get('bases', [])
            for base in bases:
                res.append(base.get('name'))
                res.append(base.get('id'))
            return res
        else:
            print('Error al obtener los datos:', response.status_code)
    
    def listar_tablas(self, id):
        res = []
        url = f'https://api.airtable.com/v0/meta/bases/{id}/tables'
        response = self.session.get(url)

        if response.status_code == 200:
            base = response.json()
            tablas = base.get('tables', [])
            for tabla in tablas:
                res.append(tabla['name'])
                res.append(tabla['id'])
            return res
        else:
            print('Error al obtener tablas:', response.status_code)

    def listar_registros(self, base, table, vista, filtro=None, limit=100, offset=None):

        params = {}
        if limit:
            params['pageSize'] = limit
        if filtro:
            params['filterByFormula'] = filtro
        if offset:
            params['offset'] = offset


        url = f'https://api.airtable.com/v0/{base}/{table}?view={vista}'

        records = []
        
        while True:
            response = self.session.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                # for record in data.get('records', []):
                #     records.append(record.get('fields', {}))
                records += [record.get('fields', {}) for record in data.get('records', [])]
                next_offset = data.get('offset')
                print(next_offset)
                if next_offset:
                    params['offset'] = next_offset
                    # records += self.listar_registros(base, table, vista, filtro, limit, next_offset)
                else:
                    break
            else:
                error_message = data.get('error', {}).get('message')
                print('Error al obtener registros:', response.status_code, error_message)
                break
        return records
    
"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module") #type: ignore

global mod_air_session
global column_names

try:
    if not mod_air_session : #type:ignore
        mod_air_session = {}
except NameError:
    mod_air_session = {}

session = GetParams("session") #type: ignore
if not session:
    session = ''

try:
    if module == "login":
        token = GetParams("token")
        session = GetParams("session")
        result = GetParams("result")

        try:
            mod_air_session = Airtable_(token)
            bases = mod_air_session.listar_bases()
            
            SetVar(result, bases)

        except Exception as e:
            import traceback
            traceback.print_exc()
            SetVar(result, False)
            PrintException()
            raise e

    if module == "listar_tablas":
        
        id = GetParams("id")
        session = GetParams("session")
        resultado = GetParams("resultado")

        try:
            tablas = mod_air_session.listar_tablas(id)
            
            SetVar(resultado, tablas)

        except Exception as e:
            SetVar(resultado, False)
            import traceback
            traceback.print_exc()
            PrintException()
            raise e

    if module == "listar_registros":
        base = GetParams("base")
        tabla = GetParams("tabla")
        session = GetParams("session")
        result = GetParams("result")
        filter = GetParams("filter")
        vista = GetParams("vista")
        limit = GetParams("limit")

        try:
            if not filter:
                filter = None
            registros = mod_air_session.listar_registros(base, tabla, vista, filter, limit)
            
            SetVar(result, registros)

        except Exception as e:
            SetVar(result, False)
            import traceback
            traceback.print_exc()
            PrintException()
            raise e
        
    if module == "descargar_csv":
        registros = GetParams("registros")
        session = GetParams("session")
        result = GetParams("result")
        path = GetParams("path")

        try:
            registros = eval(registros)
            if not registros or not isinstance(registros[0], dict):
                raise ValueError("Los datos proporcionados no son una lista de diccionarios.")

            column_names = list(registros[0].keys())
            rows = [[row[column] for column in column_names] for row in registros]
            
            with open(path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(column_names)
                for row in rows:
                    writer.writerow(row)

            SetVar(result, True)

        except Exception as e:
            SetVar(result, False)
            import traceback
            traceback.print_exc()
            PrintException()
            raise e
        
except Exception as e:
    import traceback
    traceback.print_exc()
    PrintException()
    raise e
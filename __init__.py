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
import requests

base_path = tmp_global_obj["basepath"] #type: ignore
cur_path = base_path + 'modules' + os.sep + 'Airtable' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
    sys.path.append(cur_path_x64)
elif sys.maxsize <= 2**32 and cur_path_x86 not in sys.path:
    sys.path.append(cur_path_x86)

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module") #type: ignore


global mod_air_session

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

        
except Exception as e:
    import traceback
    traceback.print_exc()
    PrintException()
    raise e
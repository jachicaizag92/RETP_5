from datetime import datetime as dt
import re

def validar_documento(documento:str):
    """Esta función tiene como objetivo el validar el tipo de documento CC, TI, PA

    Args:
        documento (str): tipo de documento ingresado a la función

    Returns:
        _type_: bool
    """
    
    if documento == 'CC' and documento == 'TI' and documento == 'PA':
        return True
    else:
        return False


def validar_longitud_caracteres(documento:str, longitud:int):
    """Función que tiene como objetivo el validar los caracteres en la totalidad de su longitud
        de acuerdo al numero de caracteres valido ingresado para la funcion.

    Args:
        documento (str): numero de documento
        longitud (int): tamaño de caracteres permitidos a validar

    Returns:
        _type_: bool
    """
    if documento.__len__() == longitud:
        return True
    else:
        return False


def validar_tipo_texto(texto:any, tipo:type):
    """ Funcion que nos permite validar el typo de texto ingresado y validarlo
        con el tipo de texto ingresado a la función.

    Args:
        texto (any): texto a validar 
        tipo (type): tipo de datos solicitado a validar

    Returns:
        _type_: bool
    """
    if type(texto) == tipo:
        return True
    else:
        return False

def buscar_simbolo(texto, simbolo):
    if re.search(rf'(.)\{simbolo}', texto):
        return True
    else:
        return False




def validar_fecha(fecha:str):
    """Funcion que nos permite validar la fecha de acuerdo a un formato preestablecido 

    Args:
        fecha (str): _description_

    Returns:
        _type_: bool
    """
    try:
        fecha_nacimiento = dt.strptime(fecha, "%Y-%m-%d")
        return True
    except:
        return False


def validar_rh(rh:str):
    """Funcion que permite valiadar las primres posiciones del RH y grupo sanguineo


    Args:
        rh (str): rh y grupo sanguineo (O+)

    Returns:
        _type_: _description_
    """

    if validar_longitud_caracteres(rh, 2) and rh[0] == 'O' or rh[0] == 'A' or rh[0]=='B' and re.search(r'\+', rh):
        return True
    else:
        return False







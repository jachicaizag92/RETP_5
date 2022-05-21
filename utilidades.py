from datetime import datetime as dt
import re

def validar_documento(documento:str):
    """Esta función tiene como objetivo el validar el tipo de documento CC, TI, PA

    Args:
        documento (str): tipo de documento ingresado a la función

    Returns:
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    
    if documento == 'CC' or documento == 'TI' or documento == 'PA':
        return True
    else:
        return False

def validar_numero_doc(documento:str):
    if bool(re.search(r'\D', documento)) == False:
        return True
    else:
        return False


def validar_longitud_caracteres(documento:str, longitud_max:int, longitud_min:int = 1):
    """Función que tiene como objetivo el validar los caracteres en la totalidad de su longitud
        de acuerdo al numero de caracteres valido ingresado para la funcion.

    Args:
        documento (str): numero de documento
        longitud (int): tamaño de caracteres permitidos a validar

    Returns:
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    if documento.__len__() <= longitud_max and documento.__len__() >= longitud_min:
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
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    if type(texto) == tipo:
        return True
    else:
        return False

def buscar_simbolo(texto:str, simbolo:str):
    """funcion encargada de buscar un simbolo y compararlo con el texto

    Args:
        texto (str): _description_
        simbolo (str): _description_

    Returns:
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    if re.search(rf'(.)\{simbolo}', texto):
        return True
    else:
        return False




def validar_fecha(fecha:str):
    """Funcion que nos permite validar la fecha de acuerdo a un formato preestablecido 

    Args:
        fecha (str): _description_

    Returns:
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    try:
        fecha_nacimiento = dt.strptime(fecha, "%Y-%m-%d")
        return True
    except:
        return False

def calc_edad(fecha:str):
    """Funcion que permite calcular la edad al obtener una fecha de nacimiento

    Args:
        fecha (str): fecha de nacimiento en el formato(AAAA-MM-DD)

    Returns:
        int: retorna la edad calculada
    """
    fecha_nacimiento = dt.strptime(fecha, "%Y-%m-%d")
    fecha_actual = dt.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    return edad


def validar_rh(rh:str):
    """Funcion que permite valiadar las primres posiciones del RH y grupo sanguineo


    Args:
        rh (str): rh y grupo sanguineo (O+)

    Returns:
        _type_: _description_
    """

    if validar_longitud_caracteres(rh, 2):
        if rh[0] == 'O' or rh[0] == 'A' or rh[0]=='B' :
            if buscar_simbolo(rh, '+') or buscar_simbolo(rh, '-'):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def validar_correo(correo:str):
    """Funcion que nos permite validar el correo analizando analizando correo electronico
        dominio.

    Args:
        correo (string): _description_

    Returns:
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    expresion = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if validar_longitud_caracteres(correo,30,6) and re.search(expresion,correo):
        return True
    else:
        return False

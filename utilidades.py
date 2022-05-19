from datetime import datetime as dt

def validar_documento(documento:str):
    
    if documento == 'CC' and documento == 'TI' and documento == 'PA':
        return True
    else:
        return False


def validar_longitud_caracteres(documento:str, longitud:int):
    if documento.__str__() == longitud:
        return True
    else:
        return False
    
   
def validar_tipo_texto(texto:any, tipo:type):
    if type(texto) == tipo:
        return True
    else:
        return False
    

def validar_fecha(fecha):
    fecha_nacimiento = dt.strptime(fecha, "%Y-%m-%d")
    
    print(fecha_nacimiento)

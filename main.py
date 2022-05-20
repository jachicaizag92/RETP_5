import utilidades as util
import re



print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _    _ _ _ _ _ _ _ _ _ _ _ _')
print('/ \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ /  \     / \ / \ / \ / \ / \ / \ ')
print('(W )( o )( r )( l )( d )( C )( r )( a )( f )( t )   (A )( S )( C )( I )( I )')
print('\ / \ / \ / \  / \  / \ / \ / \ /  \ / \  / \  /    \  / \  / \  / \  / \  /')  
print('- - - - - - - - - - - - - - - - - - - - - - - - -    - - - - - - - - - - - - \n')


# tipo_documento = 'CC'
numero_documento = '1144160583s'
# nombre = 'John Alexander'
# apellido = 'Chicaiza Gavilanes'
# fecha_nacimiento = '24/08/1992'
# rh = 'O+'
# correo_electronico = 'jachicaiz2@aoutlook.co'
# numero_telefonico = 3217505762

print(util.validar_numero_doc(numero_documento))
# print(bool(re.search(r'\D', numero_documento)))

# opcion = int(input('ingresa tu opción: '))
opcion = 0



while opcion != 4:
    print('- - - - - - - - - - - - - - - - - - - - - - - - -    - - - - - - - - - - - - \n')
    print('Bienvenido que deseas hacer\n')
    print('1. Registrarse en el sistema')
    print('2. Visualizar el listado de personas registradas')
    print('3. Asignar cita\n')
    
    opcion = 1
    datos= []
    if opcion == 1:
        tipo_documento = input('Por favor ingresa tu tipo de documento(CC,TI,PA): ').upper()
        # tipo_documento = 'CC'
        if util.validar_documento(tipo_documento):
            numero_documento = input('Ingresa tu número de documento: ')
            if util.validar_longitud_caracteres(numero_documento, 12) and util.validar_numero_doc(numero_documento):
                nombre = input('Ingresa tu nombre: ')
                apellido = input('Ingresa tu apellido: ')
                if util.validar_longitud_caracteres(nombre,30) and util.validar_longitud_caracteres(apellido,30):
                    fecha= input('Ingresa tu fecha de nacimiento (AAAA-MM-DD): ')
                    if util.validar_fecha(fecha):
                        correo = input('Ingresa tu correo electronico: ')
                        if util.validar_correo(correo):
                            numero_tel= input('Ingresa tu número telefonico: ')
                            if util.validar_longitud_caracteres(numero_tel,10) and util.validar_numero_doc(numero_tel):
                                print("numero telefonico ok")
                                opcion = 2
                            else:
                                print("número no valido")
                        else: 
                            print('correo no valido')
                    else:
                        print("formato de fecha no valido")
                else:
                    print('excede la longitud de caracteres')
            else:
                print('no cumple o el tamaño o contiene letras el numero de documento')    
        else:
            print('\nEl tipo de documento no es valido')
    elif opcion == 2:
        print('listado')


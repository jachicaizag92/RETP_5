import utilidades as util
import re



print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _    _ _ _ _ _ _ _ _ _ _ _ _')
print('/ \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ /  \     / \ / \ / \ / \ / \ / \ ')
print('(W )( o )( r )( l )( d )( C )( r )( a )( f )( t )   (A )( S )( C )( I )( I )')
print('\ / \ / \ / \  / \  / \ / \ / \ /  \ / \  / \  /    \  / \  / \  / \  / \  /')  
print('- - - - - - - - - - - - - - - - - - - - - - - - -    - - - - - - - - - - - - \n')


tipo_documento = 'TI'
numero_documento = '1144160583'
nombre = 'John Alexander'
apellido = 'Chicaiza Gavilanes'
fecha = '1992-08-24'
rh = 'O+'
correo = 'jachicaiz2@aoutlook.co'
numero_tel = '3217505762'





print('- - - - - - - - - - - - - - - - - - - - - - - - -    - - - - - - - - - - - - \n')
print('Bienvenido que deseas hacer\n')
print('1. Registrarse en el sistema')
print('2. Visualizar el listado de personas registradas')
print('3. Asignar cita\n')
opcion = int(input("Por Favor ingrese la opcion:"))


registrados = [{'Tipo de documento: ': 'CC', 'Número de documento: ': '1544789653', 'Nombres:': 'Alejandro', 'Apellidos:': 'Chicaiza Muñoz', 'fecha de nacimiento: ': '2020-02-24', 'Edad: ': '12', 'Correo electronico: ': 'alejo@gmail.com', 'Numero Telefonico: ': '3155521552'}]


while opcion != 4:
    
    datos= {}
    
    if opcion == 1:
        print('\n\n*************************************************************************')
        print('*************************************************************************')
        print('                      FORMULARIO DE REGISTRO                              ')
        print('- - - - - - - - - - - - - - - - - - - - - - - - -    - - - - - - - - - - - - \n')

        # tipo_documento = input('Por favor ingresa tu tipo de documento(CC,TI,PA): ').upper()
        datos['Tipo de documento: ']= tipo_documento
        if util.validar_documento(tipo_documento):
            # numero_documento = input('Ingresa tu número de documento: ')
            datos['Número de documento: ']= numero_documento
            if util.validar_longitud_caracteres(numero_documento, 12) and util.validar_numero_doc(numero_documento):
                # nombre = input('Ingresa tu nombre: ')
                # apellido = input('Ingresa tu apellido: ')
                datos['Nombres:'] = nombre
                datos['Apellidos:']= apellido
                if util.validar_longitud_caracteres(nombre,30) and util.validar_longitud_caracteres(apellido,30):
                    # fecha= input('Ingresa tu fecha de nacimiento (AAAA-MM-DD): ')
                    edad= str(util.calc_edad(fecha))
                    datos['fecha de nacimiento: ']= fecha
                    datos['Edad: ']= edad
                    if util.validar_fecha(fecha):
                        # correo = input('Ingresa tu correo electronico: ')
                        datos['Correo electronico: ']= correo
                        if util.validar_correo(correo):
                            # numero_tel= input('Ingresa tu número telefonico: ')
                            datos['Numero Telefonico: ']= numero_tel
                            if util.validar_longitud_caracteres(numero_tel,10) and util.validar_numero_doc(numero_tel):
                                registrados.append(datos)
                                print("TU REGISTRO FUE EXITOSO:")
                                
                                print('- - - - - - - - - - - - - - - - - - - - - - - - -    - - - - - - - - - - - - \n')
                                print('1. Registrarse en el sistema')
                                print('2. Visualizar el listado de personas registradas')
                                print('3. Asignar cita\n')
                            
                                opcion = int(input("Por Favor ingrese la opcion:"))
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
        print('\n\n*************************************************************************')
        print('*************************************************************************')
        print('                      LISTADO DE PERSONAS REGISTRADAS                              ')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n')
        for idx, registrado in enumerate(registrados):
            print(f" {idx+1}. - {registrado['Tipo de documento: ']} - {registrado['Número de documento: ']} - {registrado['Nombres:']} - {registrado['Apellidos:']} - {registrado['Edad: ']}")
        opcion = int(input("Por Favor ingrese la opcion:"))
    elif opcion == 3:
        print("y ahora")
        
    

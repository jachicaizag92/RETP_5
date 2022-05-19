import utilidades as util

print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _    _ _ _ _ _ _ _ _ _ _ _ _')
print('/ \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ /  \     / \ / \ / \ / \ / \ / \ ')
print('(W )( o )( r )( l )( d )( C )( r )( a )( f )( t )   (A )( S )( C )( I )( I )')
print('\ / \ / \ / \  / \  / \ / \ / \ /  \ / \  / \  /    \  / \  / \  / \  / \  /')  
print('- - - - - - - - - - - - - - - - - - - - - - - - -    - - - - - - - - - - - - \n')


tipo_documento = 'CC'
numero_documento = '1144160583'
nombre = 'John Alexander'
apellido = 'Chicaiza Gavilanes'
fecha_nacimiento = '24/08/1992'
rh = 'O*'
correo_electronico = 'jachicaiza@outlook.com'
numero_telefonico = 3217505762


# print(util.validar_tipo_texto(numero_documento, str))
# print(util.validar_tipo_texto(numero_telefonico, int))
# print(type(numero_documento))
# print(type(numero_telefonico))

# print(util.validar_fecha(fecha_nacimiento))
print(util.validar_rh(rh))
# print(util.validar_longitud_caracteres(rh, 2))
# print(rh[1].count('+'))

# if rh[1].count('+') == 1 or rh[1].count('-') == 1:
    # print("hola")
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
fecha_nacimiento = '1992-08-24'
rh = 'O+'
correo_electronico = 'jachicaiza@outlook.com'
numero_telefonico = 3217505762


# print(util.validar_tipo_texto(numero_documento, str))
# print(util.validar_tipo_texto(numero_telefonico, int))
# print(type(numero_documento))
# print(type(numero_telefonico))

util.validar_fecha(fecha_nacimiento)
# import utilidades as util

registrados = {'Tipo de documento: ': 'CC', 'Número_de_documento': '1544789653', 'Nombres:': 'Alejandro', 'Apellidos:': 'Chicaiza Muñoz', 'fecha de nacimiento: ': '2020-02-24', 'Edad: ': '12', 'Correo electronico: ': 'alejo@gmail.com', 'Numero Telefonico: ': '3155521552','cita: ':'2022-05-25', 'hora_cita: ':'4:00'}
# tupla = tuple(registrados)

# print(tupla)

print("hola"+registrados['Número_de_documento']+" "+registrados['Apellidos:'])



# numero_doc ='32'
# print(len(registrados))
# # print(registrados['1544789653'])
# # print(util.comparar_documento(registrados,numero_doc))
# # print(next(x for x in registrados if registrados[0].get('Número de documento: '): print('true')))
# # print(registrados[0].get('Número de documento: '))

# # for x in registrados:
# #     doc = str(registrados[0].get('Número de documento: '))
# #     if doc == numero_doc:
# #         print('True')
# #     else:
# #         print('False')

# lstdict = [
#         { "name": "Klaus", "age": "312" },
#         { "name": "Elijah", "age": "33" },
#         { "name": "Kol", "age": 28 },
#         { "name": "Stefan", "age": "32" }
#     ]
# # print(bool(next(x for x in registrados if x['Número_de_documento'] == numero_doc)))
# # print(next(x for x in lstdict if x["name"] == "Klaus"))

# def c(reg,numero_doc):
#     try:
#         next(x for x in reg if x['age'] == numero_doc)
#         return True
#     except :
#         return False
    
# print(c(lstdict,numero_doc))


# productos = [
#     {
#         'nombre': 'manzana',
#         'cantidad': 10,
#         'fecha_de_modificacion': '2023-05-01'
#     },
#     {
#         'nombre': 'banana',
#         'cantidad': 5,
#         'fecha_de_modificacion': '2023-12-01'
#     }
# ]


# def cantidad_de_datos_invalida(coleccion_de_datos, cantidad_de_valores_validos):
#   if len(coleccion_de_datos) != cantidad_de_valores_validos:
#     print('No estas ingresando los datos requeridos para esta operacion')
#     return True
#   return False


# def agregar_producto(lista_de_productos, datos_de_entrada):
#   nombre_de_producto, cantidad, fecha = datos_de_entrada[1], int(datos_de_entrada[2]), datos_de_entrada[3]
#   for producto in lista_de_productos:
#     if producto['nombre'] == nombre_de_producto:
#         producto['cantidad'] += cantidad
#         producto['fecha_de_modificacion'] = fecha


# def remover_producto(lista_de_productos, datos_de_entrada):
#   nombre_de_producto, cantidad, fecha = datos_de_entrada[1], int(datos_de_entrada[2]), datos_de_entrada[3]
#   for producto in lista_de_productos:
#     if producto['nombre'] == nombre_de_producto:
#         producto['cantidad'] -= cantidad
#         producto['fecha_de_modificacion'] = fecha


# def consultar_producto(lista_de_productos, datos_de_entrada):
#   nombre_de_producto = datos_de_entrada[1]
#   for producto in lista_de_productos:
#     if producto['nombre'] == nombre_de_producto:
#         print(f'La cantidad de {nombre_de_producto} en stock es {producto['cantidad']}')



# bandera = True
# while bandera:
#     valor_de_input = input('Ingresa la operacion a ejecutar sumada de los valores necesarios:')
#     lista_de_entrada = valor_de_input.split()

#     if lista_de_entrada[0] == 'ADD':
#         if cantidad_de_datos_invalida(lista_de_entrada, 4): continue
#         agregar_producto(productos, lista_de_entrada)

#     elif lista_de_entrada[0] == 'REMOVE':
#         if cantidad_de_datos_invalida(lista_de_entrada, 4): continue
#         remover_producto(productos, lista_de_entrada)

#     elif lista_de_entrada[0] == 'QUERY':
#         if cantidad_de_datos_invalida(lista_de_entrada, 2): continue
#         consultar_producto(productos, lista_de_entrada) 

#     else:
#         print('El usuario ingreso lo que le pinto.')

#     if input('Quiere dejar de ingresar comandos? (Si para salir)').lower() == 'si':
#         bandera = False
        

# # ADD manzana 20 2026-02-18
# # REMOVE manzana 5 2026-02-25
# # QUERY banana
# # QUERY manzana
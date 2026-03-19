# class Auto:
#     ...


# auto1 = Auto()
# auto2 = Auto()
# auto3 = Auto()

# print(auto1)
# print(auto2)
# print(auto3)


######################################################################
######################################################################

# class Auto:
    
#     def avanzar(self, metros):
#         return f'El auto {self} avanzo {metros} metros'

#     @staticmethod
#     def tocar_bocina():
#         print('PIIIIIIIIIIIII PIIIIIIII')

# auto1 = Auto()
# auto2 = Auto()
# auto3 = Auto()

# print(auto1)
# print(auto2)
# print(auto3)
# auto1.tocar_bocina() # tocar_bocina(auto1)
# print(auto2.avanzar(15)) # avanzar(auto1, 15)
# auto3.tocar_bocina()

# Auto.tocar_bocina()

######################################################################
######################################################################


# class Auto:
    
#     def avanzar(self, metros):
#         return f'El auto {self} avanzo {metros} metros'

#     @staticmethod
#     def tocar_bocina():
#         print('PIIIIIIIIIIIII PIIIIIIII')

#     @classmethod
#     def identificar_clase(cls):
#         print(f'Soy un {cls}')


# auto1 = Auto()

# auto1.identificar_clase()

######################################################################
######################################################################


# class Auto:
    
#     cant_ruedas = 4
    
#     def __init__(self, marca, modelo, color):
#         self.modelo = modelo
#         self.color = color
#         self.marca = marca
    
#     def __str__(self):
#         return f"Soy un auto {self.marca} {self.modelo}"
    
#     def avanzar(self, metros):
#         # self.color = 'rojo'
#         return f'El auto {self} avanzo {metros} metros'

#     @staticmethod
#     def tocar_bocina():
#         print('PIIIIIIIIIIIII PIIIIIIII')

#     @classmethod
#     def identificar_clase(cls):
#         print(f'Soy un {cls}')


# auto1 = Auto('Ford', 'K', 'rojo')
# auto2 = Auto('Fiat', 'Uno', 'blanco')
# auto3 = Auto('Fiat', 'Siena', 'negro')

# print(auto1, auto1.color, auto1.marca, auto1.modelo, auto1.cant_ruedas)
# print(auto2, auto2.color, auto2.marca, auto2.modelo, auto2.cant_ruedas)
# print(auto3, auto3.color, auto3.marca, auto3.modelo, auto3.cant_ruedas)

######################################################################
######################################################################



# class Auto:
    
#     cant_ruedas = 4
#     cant_de_autos_creados = 0
    
#     def __init__(self, marca, modelo, color):
#         self.modelo = modelo
#         self.color = color
#         self.marca = marca
#         Auto.cant_de_autos_creados += 1
#         self.numero_de_chasis = Auto.cant_de_autos_creados
    
#     def __str__(self):
#         return f"Soy un auto {self.marca} {self.modelo}"
    
#     def avanzar(self, metros):
#         # self.color = 'rojo'
#         return f'El auto {self} avanzo {metros} metros'

#     @staticmethod
#     def tocar_bocina():
#         print('PIIIIIIIIIIIII PIIIIIIII')

#     @classmethod
#     def identificar_clase(cls):
#         print(f'Soy un {cls}')


# auto1 = Auto('Ford', 'K', 'rojo')
# auto2 = Auto('Fiat', 'Uno', 'blanco')
# auto3 = Auto('Fiat', 'Siena', 'negro')

# print(auto1, auto1.color, auto1.marca, auto1.modelo, auto1.cant_ruedas, auto1.cant_de_autos_creados, auto1.numero_de_chasis)
# print(auto2, auto2.color, auto2.marca, auto2.modelo, auto2.cant_ruedas, auto2.cant_de_autos_creados, auto2.numero_de_chasis)
# print(auto3, auto3.color, auto3.marca, auto3.modelo, auto3.cant_ruedas, auto3.cant_de_autos_creados, auto3.numero_de_chasis)


######################################################################
######################################################################

# class Vehiculo:
    
#     tipo = 'vehiculo'
#     prefijo = 'el'
    
#     def avanzar(self, metros):
#         print(f'{self.prefijo.capitalize()} {self.tipo} avanzo {metros} metros!')

# class Auto(Vehiculo):
#     tipo = 'auto'

# class Camion(Vehiculo):
#     tipo = 'camion'
    
#     def saludo(self):
#         print("CUUUUUUUEEE")

# class Monopatin(Vehiculo):
#     tipo = 'monopatin'

# class Lancha(Vehiculo):
#     tipo = 'lancha'
#     prefijo = 'la'

# auto = Auto()
# auto.avanzar(15)

# camion = Camion()
# camion.avanzar(25)

# monopatin = Monopatin()
# monopatin.avanzar(5)

# lancha = Lancha()
# lancha.avanzar(5)

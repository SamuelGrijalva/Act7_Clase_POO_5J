print("Programacion POO")
#definicion de clases
class Perro:
    #funciones dentro de la clase
    def morder(self):
        print("El perro me mordio")
    def Datos_Perro(self,nombre,edad):
        print(f"Nombre: {nombre} edad: {edad}")


#Zona de creacion de objeto
pitbull=Perro()

#Zona de usa de objecto

pitbull.Datos_Perro("boby",4)
pitbull.morder()
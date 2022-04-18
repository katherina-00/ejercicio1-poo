import csv

class email:
    id_cuenta = ""
    dominio = ""
    tipo_de_dominio = ""
    contrasena = ""

    def __init__(self):
        pass

    def getDominio(self):
        return print("."+self.tipo_de_dominio)

    def crearCuenta(self):
        nuevo = input("ingrese nuevo correo \n")
        nuevo = nuevo.split('@')
        self.id_cuenta = nuevo[0]
        nuevo = nuevo[1].split('.')
        self.dominio = nuevo[0]
        self.tipo_de_dominio = nuevo[1]
        self.contrasena = input("ingrese contrasena nuevo \n")

    def retornaEmail(self):
        mail = self.id_cuenta+'@'+self.dominio+'.'+self.tipo_de_dominio
        return (mail)

    def cambiaContr(self):
        contAux = input("Ingrese contraseña actual:")
        while self.contrasena != contAux:
            contAux = input("Esta contraseña no coincide con su contraseña anterior, por favor intente de nuevo:")
        self.contrasena = input("Ingrese su nueva contraseña:")

if __name__ == "__main__":
    print('----------- MENU')
    nuevo = email()
    op= int(input('Ingrese la opcion:\n1- Ingresar nombre y dirección de e-mail\n2- Cambiar contrasena\n3- Leer un archivo\n4- Salir\n'))
    while op != 4:

            if op==1:
                        nombre=input("Ingrese nombre:")
                        nuevo.crearCuenta()
                        print(f"Estimado {nombre} te enviaremos tus mensajes a la direccion {nuevo.retornaEmail()}")
            elif op==2:
                print("--------Cambiar contraseña--------\n")
                nuevo.cambiaContr()

            elif op==3:
                cont=0
                fichero = open('correos.csv','r')
                reader = csv.reader(fichero, delimiter=',')
                identificador=input('Ingrese identificador a buscar: ')
                for fila in reader:
                    if fila[0] == identificador:
                        cont += 1
                if cont > 1:
                    print("La cantidad de personas con el identificador '{}' es: {}".format(identificador, cont))
                    print("El identificador se repite")
                else:
                    print("El identificador no se repite")
                fichero.close()
            op= int(input('Ingrese la opcion:\n1- Ingresar nombre y dirección de e-mail\n2- Cambiar contrasena\n3- Leer un archivo\n4- Salir\n'))

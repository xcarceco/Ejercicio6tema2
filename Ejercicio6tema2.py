# En este segundo ejercicio, tendréis que crear un programa que tenga
# una clase llama Alumno que tenga como atributos su nombre y su nota.
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos
# y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    nombredelalumno = ""
    notadelalumno = 0

    def inicializar(self, alumno, nota):
        self.nombredelalumno = alumno
        self.notadelalumno = nota

    def nombre(self):
       print(self.nombredelalumno)

    def nota(self):
        print(self.notadelalumno)

    def imprimirNota(self):
        if self.notadelalumno >= 5:
            print("Aprobado")
        else:
            print("Suspendido")

aJose = Alumno()
aJose.inicializar("Jose", 9) # a partir de 9 es Sobresaliente
aJose.nombre()
aJose.imprimirNota()

aJorge = Alumno()
aJorge.inicializar("Jorge", 4)
aJorge.nombre()
aJorge.imprimirNota()

aXavi = Alumno()
aXavi.inicializar("Xavi", 9)
aXavi.nombre()
aXavi.imprimirNota()

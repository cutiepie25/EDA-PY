import random
class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Método para insertar un valor en la lista
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Método para imprimir la lista
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def dividir_lista(self, cabeza):
        # Método de dos punteros (rápido y lento) para dividir la lista en dos mitades
        if not cabeza or not cabeza.siguiente:
            return cabeza, None
        
        lento = cabeza
        rapido = cabeza.siguiente
        
        while rapido and rapido.siguiente:
            lento = lento.siguiente
            rapido = rapido.siguiente.siguiente
        
        mitad = lento.siguiente
        lento.siguiente = None
        
        return cabeza, mitad
    
    def fusionar_listas(self, l1, l2):
        # Fusión de las dos listas alternando nodos de manera aleatoria
        cabeza_fusionada = Nodo()
        actual = cabeza_fusionada
        
        while l1 and l2:
            if random.choice([True, False]):
                actual.siguiente = l1
                l1 = l1.siguiente
            else:
                actual.siguiente = l2
                l2 = l2.siguiente
            actual = actual.siguiente
        
        actual.siguiente = l1 if l1 else l2
        return cabeza_fusionada.siguiente
    
    def shuffle(self, cabeza):
        # Caso base: lista vacía o con un solo nodo
        if not cabeza or not cabeza.siguiente:
            return cabeza
        
        # Dividir la lista en dos mitades
        mitad_izquierda, mitad_derecha = self.dividir_lista(cabeza)
        
        # Aleatorizar cada mitad recursivamente
        mitad_izquierda = self.shuffle(mitad_izquierda)
        mitad_derecha = self.shuffle(mitad_derecha)
        
        # Fusionar las mitades aleatoriamente
        return self.fusionar_listas(mitad_izquierda, mitad_derecha)
    
    # Método para iniciar el proceso de shuffle
    def barajar(self):
        self.cabeza = self.shuffle(self.cabeza)

# Crear lista enlazada y añadir elementos
lista = ListaEnlazada()
elementos = [1, 2, 3, 4, 5, 6, 7, 8]
for elem in elementos:
    lista.insertar(elem)

print("Lista original:")
lista.imprimir()

# Barajar la lista
lista.barajar()

print("\nLista barajada:")
lista.imprimir()

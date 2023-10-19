from Nodo import Nodos
from Senal import Senal

class ListaSimple():
    def __init__(self):
        self.head = None
        
    def append(self, tiempo, amplitud, dato):
        nueva_senal = Senal(tiempo, amplitud, dato)
        if not self.head:
            self.head = Nodos(nueva_senal)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Nodos(nueva_senal)
        
    def get_promedio(self, tiempo, amplitud):
        current = self.head
        suma = 0
        while current:
            suma += int(current.senal.dato)
            current = current.next
        return suma / (tiempo * amplitud)
    
    def get_str(self):
        current = self.head
        while current:
            print(current.senal.tiempo, current.senal.amplitud, current.senal.dato, current.senal.nombre)
            current = current.next

from ListaSimple import ListaSimple
from xml.etree import ElementTree as ET

lista = ListaSimple()

class Main():
    def __init__(self) :
        self.lista = ListaSimple()
        
    def leer_xml(self):
        root = ET.parse('src\\senal 1.xml').getroot()
        for senal in root.findall('senal'):
            nombre = senal.get('nombre')
            t_cabecera = int(senal.get('t'))
            A_cabecera = int(senal.get('A'))
            for dato in senal.findall('dato'):
                t = dato.get('t')
                A = dato.get('A')
                dato_ = dato.text
                self.lista.append(t, A, dato_)
            promedio = self.lista.get_promedio(t_cabecera, A_cabecera)
            print(f'Promedio de {nombre} es de {promedio}')        
    
if __name__ == '__main__':
    Main().leer_xml()
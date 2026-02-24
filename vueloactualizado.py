import xml.etree.ElementTree as ET
import os

class Vuelo:
    def __init__(self, codigo, origen, destino, duracion, aerolinea):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.duracion = int(duracion)
        self.aerolinea = aerolinea

    def __str__(self):
        return f"[{self.codigo}] | {self.aerolinea} | {self.origen} -> {self.destino} ({self.duracion}h)"

class GestorVuelos:
    def __init__(self):
        self.vuelos = {}

    def cargar_archivo(self, ruta):
        if not os.path.exists(ruta):
            print("Error: El archivo no existe.")
            return
        try:
            tree = ET.parse(ruta)
            root = tree.getroot()
            count = 0
            for v in root.findall('vuelo'):
                cod = v.find('codigo').text.strip()
                if cod not in self.vuelos:
                    nuevo = Vuelo(cod, v.find('origen').text.strip(), v.find('destino').text.strip(),
                                  v.find('duracion').text.strip(), v.find('aerolinea').text.strip())
                    self.vuelos[cod] = nuevo
                    count += 1
            
            print(f"Se cargaron {count} vuelos.")
            # AQUÍ ES DONDE SE ACTUALIZA EL BLOC DE NOTAS AUTOMÁTICAMENTE
            self.actualizar_bloc_de_notas()
            
        except Exception as e:
            print(f"Error: {e}")

    def actualizar_bloc_de_notas(self):
        """Escribe todos los vuelos actuales en un archivo .txt"""
        try:
            with open("vuelos_reporte.txt", "w", encoding="utf-8") as f:
                f.write("--- REPORTE ACTUALIZADO DE VUELOS ---\n")
                for v in self.vuelos.values():
                    f.write(str(v) + "\n")
            print("¡Archivo 'vuelos_reporte.txt' actualizado!")
        except Exception as e:
            print(f"No se pudo escribir el bloc de notas: {e}")

    def mostrar_todo(self):
        if not self.vuelos:
            print("\nNo hay vuelos cargados.")
            return
        for v in self.vuelos.values():
            print(v)

    def detalle_vuelo(self, codigo):
        if codigo in self.vuelos:
            print(f"\nDETALLE:\n{self.vuelos[codigo]}")
        else:
            print("\nVuelo no encontrado.")

def main():
    gestor = GestorVuelos()
    while True:
        print("\n--- MENÚ AEROLÍNEA ---")
        print("1. Cargar Archivo XML (y actualizar Bloc de Notas)")
        print("2. Detalle de vuelo específico")
        print("3. Mostrar todos en consola")
        print("4. Salir")
        
        op = input("Seleccione: ")
        if op == '1':
            gestor.cargar_archivo(input("Nombre del archivo: "))
        elif op == '2':
            gestor.detalle_vuelo(input("Código del vuelo: "))
        elif op == '3':
            gestor.mostrar_todo()
        elif op == '4':
            break

if __name__ == "__main__":
    main()
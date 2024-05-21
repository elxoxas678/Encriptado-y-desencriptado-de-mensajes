import os
import random
import string

# Función para obtener la ruta de la carpeta de descargas
def obtener_ruta_descargas():
    if os.name == 'nt':  # Para Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:  # Para Unix (Linux, macOS, etc.)
        return os.path.join(os.environ['HOME'], 'Downloads')

# Función para generar una clave de cifrado
def generar_clave():
    letras = list(string.ascii_uppercase)
    random.shuffle(letras)
    return ''.join(letras)

# Función para cifrar el mensaje
def cifrar_mensaje(mensaje, clave):
    mensaje_cifrado = []
    for c in mensaje:
        if c.isalpha():
            offset = 'A' if c.isupper() else 'a'
            idx = ord(c.upper()) - ord('A')
            mensaje_cifrado.append(clave[idx])
        else:
            mensaje_cifrado.append(c)
    return ''.join(mensaje_cifrado)

# Función para descifrar el mensaje
def descifrar_mensaje(mensaje_cifrado, clave):
    mensaje_descifrado = []
    for c in mensaje_cifrado:
        if c.isalpha():
            offset = 'A' if c.isupper() else 'a'
            idx = clave.index(c.upper())
            mensaje_descifrado.append(chr(idx + ord('A')))
        else:
            mensaje_descifrado.append(c)
    return ''.join(mensaje_descifrado)

# Función para guardar el mensaje cifrado en un archivo
def guardar_en_archivo(nombre_archivo, mensaje, clave):
    ruta_completa = os.path.join(obtener_ruta_descargas(), nombre_archivo)
    with open(ruta_completa, 'w') as archivo:
        archivo.write(f"Clave: {clave}\n")
        archivo.write(f"Mensaje: {mensaje}\n")
    print(f"Mensaje cifrado guardado en {ruta_completa}")

# Función para leer el mensaje cifrado y la clave desde un archivo
def leer_desde_archivo(nombre_archivo):
    ruta_completa = os.path.join(obtener_ruta_descargas(), nombre_archivo)
    try:
        with open(ruta_completa, 'r') as archivo:
            clave = archivo.readline().strip().split(": ")[1]
            mensaje = archivo.readline().strip().split(": ")[1]
        return clave, mensaje
    except FileNotFoundError:
        print("No se pudo abrir el archivo para leer.")
        return None, None

def main():
    print("1. Cifrar mensaje\n2. Descifrar mensaje")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mensaje = input("Introduce el mensaje a cifrar: ")
        clave = generar_clave()
        mensaje_cifrado = cifrar_mensaje(mensaje, clave)
        nombre_archivo = input("Introduce el nombre del archivo para guardar el mensaje cifrado (sin ruta): ")
        guardar_en_archivo(nombre_archivo, mensaje_cifrado, clave)
    elif opcion == 2:
        nombre_archivo = input("Introduce el nombre del archivo que contiene el mensaje cifrado (sin ruta): ")
        clave, mensaje_cifrado = leer_desde_archivo(nombre_archivo)
        if clave and mensaje_cifrado:
            mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave)
            print(f"Mensaje descifrado: {mensaje_descifrado}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()

import random
mensaje = "Hola, mundo!"
clave = [random.choice([0,1]) for _ in mensaje]
def XOR(mensaje, clave):
    encriptado = ""
    for i in range(len(mensaje)):
        encriptado += chr(ord(mensaje[i]) ^int(clave[i]))
    return encriptado

x = XOR(mensaje, clave)
y = XOR(x, clave)

print("Mensaje original:", mensaje)
print("Clave generada:  ", clave)
print("Texto encriptado:", x)
print("Texto desencriptado:", y)

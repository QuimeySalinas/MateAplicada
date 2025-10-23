#Ejercicio 7
#XOR es un operador bit a bit que devuelve 0 si los bits son 
#iguales y 1 en caso contrario. En los libros de texto, el operador 
#XOR se denota con ⊕, pero en la mayoría de los desafíos y 
#lenguajes de programación se ^usa el símbolo de intercalación.
#llave = crypto{aloha}

from pwn import *

string = "label"
entero = 13

xor_ints=[]

for char in string:
    xor_valor = ord(char) ^ entero
    xor_ints.append(xor_valor)

nuevos_char=[]

for int in xor_ints:
    nuevo_char = chr(int)
    nuevos_char.append(nuevo_char)

respuesta = ''.join(nuevos_char)
#Que cosa fea dios
print(f"crypto{{{respuesta}}}") 


#Ejercicio 8
KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY12 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY23 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
KEY123 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

def xorBytes(bytes1: bytes, bytes2: bytes) -> bytes:
    bytesxor = bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))
    return bytesxor
KEY2 = xorBytes(KEY1,KEY12)
KEY3 = xorBytes(KEY23,KEY2)
FLAG = xorBytes(KEY1,xorBytes(KEY2,xorBytes(KEY3,KEY123)))

print(FLAG.decode())


#Ejercicio 9
KEY = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
respuesta: bytes
for i in range(256):
    respuesta = bytes(b1 ^ i for b1 in KEY)
    if "crypto" in respuesta.decode():
        break
print(respuesta.decode())

#Ejercicio 10
from pwn import xor
KEY = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

#Seguro empieza con esto, entonces codifico y hago xor
cosas_conocidas = "crypto{".encode()
llave_corta = xor(KEY,cosas_conocidas)


#Como en anteriores pruebas vi que era myXORke, le sume una y
llave_posta = llave_corta[0:7].decode() +'y'

#Hago xor con la llave para conseguir respuesta
respuesta = xor(KEY,llave_posta)

print(respuesta.decode())

# crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}

#Ejercicio 11
from PIL import Image
from pwn import xor

try:
    # Carga la primera imagen
    img1 = Image.open("flag.png").convert("RGB")
    # Carga la segunda imagen
    img2 = Image.open("lemur.png").convert("RGB")


    ancho, alto = img1.size

    img_respuesta = Image.new(img1.mode, (ancho,alto))

    pixeles1 = img1.load()
    pixeles2 = img2.load()
    pixeles_respuesta = img_respuesta.load()

    for i in range(ancho):
        for j in range(alto):
            r1, g1, b1 = pixeles1[i, j]
            r2, g2, b2 = pixeles2[i, j]

            # Aplicar la operación XOR (^) a cada canal de color
            r_xor = r1 ^ r2
            g_xor = g1 ^ g2
            b_xor = b1 ^ b2

            # Asignar el nuevo píxel calculado a la imagen resultado
            pixeles_respuesta[i, j] = (r_xor, g_xor, b_xor)
     
    print("OK")
    img_respuesta.show()
except FileNotFoundError:
    print("Error: Asegúrate de que los archivos 'imagen1.jpg' y 'imagen2.jpg' estén en la misma carpeta.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
# Ejercicio 2

for i in [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]:
    print(chr(i),end='')

# Ejercicio 3

# Cuando ciframos algo, el texto cifrado resultante suele tener bytes que no son caracteres ASCII imprimibles. Si queremos compartir nuestros datos cifrados, es común codificarlos en algo más fácil de usar y portátil en diferentes sistemas.
# Hexadecimal se puede utilizar de esta manera para representar cadenas ASCII. Primero, cada letra se convierte en un número ordinal según la tabla ASCII (como en el desafío anterior). Luego, los números decimales se convierten a números de base 16, también conocidos como hexadecimales. Los números se pueden combinar en una larga cadena hexadecimal.
# A continuación se incluye una bandera codificada como una cadena hexadecimal. Decodifique esto nuevamente en bytes para obtener la bandera.

# 63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
# crypto{You_will_be_working_with_hex_strings_a_lot}

#bytes.fromhex()
#.hex()

hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(hex_string).decode())

# Ejercicio 4

# Otro esquema de codificación común es Base64, que nos permite representar datos binarios como una cadena ASCII utilizando un alfabeto de 64 caracteres. Un carácter de una cadena Base64 codifica 6 dígitos binarios (bits), por lo que 4 caracteres de Base64 codifican tres bytes de 8 bits.
# Base64 se utiliza más comúnmente en línea, por lo que los datos binarios, como imágenes, se pueden incluir fácilmente en archivos HTML o CSS.
# Tome la siguiente cadena hexadecimal, decodifíquela en bytes y luego codifíquela en Base64.

# En Python, después de importar el módulo base64 con import base64, puede utilizar la función base64.b64encode(). Recuerde decodificar primero el hexadecimal como indica la descripción del desafío.

# 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf

#import base64

#hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#print(base64.b64encode(bytes.fromhex(hex_string)).decode())

# Ejercicio 5

# Los criptosistemas como RSA funcionan con números, pero los mensajes están formados por caracteres. ¿Cómo debemos convertir nuestros mensajes en números para poder aplicar operaciones matemáticas?
# La forma más común es tomar los bytes ordinales del mensaje, convertirlos en hexadecimales y concatenarlos. Esto puede interpretarse como un número de base 16/hexadecimal y también representarse en base 10/decimal.

'''
message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487
'''

# La biblioteca PyCryptodome de Python implementa esto con los métodos bytes_to_long() y long_to_bytes(). Primero tendrás que instalar PyCryptodome e importarlo desde Crypto.Util.number import *. Para obtener más detalles, consulte las preguntas frecuentes.

# 11515195063862318899931685488813747395775516287289682636499965282714637259206269

#from Crypto.Util.number import *

#number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
#print(long_to_bytes(number).decode())

# Ejercicio 6

# Ahora que ya dominas las distintas codificaciones que encontrarás, veamos cómo automatizarlas.
# ¿Puedes pasar los 100 niveles para obtener la bandera?
# El archivo 13377.py adjunto a continuación es el código fuente de lo que se ejecuta en el servidor. El archivo pwntools_example.py proporciona el inicio de una solución.
# Para obtener más información sobre cómo conectarse a desafíos interactivos, consulte las preguntas frecuentes. ¡No dude en pasar directamente a la criptografía si no está de humor para un desafío de codificación!

# Si desea ejecutar y probar el desafío localmente, consulte las preguntas frecuentes para descargar el módulo utils.listener.

# Conéctese en socket.cryptohack.org 13377
# Archivos de desafío:  
# - 13377.py  
# - pwntools_example.py
'''
from pwn import *
import json
import base64
from Crypto.Util.number import *
import codecs

r = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()
while True:
    
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    enc = ""

    match received["type"]:
        case "base64":
            enc = base64.b64decode(received["encoded"]).decode()
        
        case "hex":
            enc = bytes.fromhex(received["encoded"]).decode()

        case "utf-8" | "ASCII":
            for i in received["encoded"]:
                    enc += chr(i)
            
        case "bytes" | "bigint":
            enc = long_to_bytes(int(received["encoded"],16)).decode()
            
        case "rot13":
            enc = codecs.decode(received["encoded"], 'rot_13')

        case default:
            print("ayuda")
            enc = ""
    to_send = {
        "decoded": enc
    }
    json_send(to_send)
    received = json_recv()
    if "error" in received or "flag" in received:
        break
print(received)

#{'flag': 'crypto{3nc0d3_d3c0d3_3nc0d3}'}

'''
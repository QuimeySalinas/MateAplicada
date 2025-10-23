# Ejercicio 11

# El máximo común divisor (GCD, por sus siglas en inglés), a veces conocido como el máximo común factor, es el número más grande que divide a dos enteros positivos (a, b).
# Para a = 12, b = 8 podemos calcular los divisores de a: {1, 2, 3, 4, 6, 12} y los divisores de b: {1, 2, 4, 8}. Comparando estos dos, vemos que gcd(a, b) = 4.
# Ahora imagina que tomamos a = 11, b = 17. Tanto a como b son números primos. Como un número primo solo tiene a sí mismo y al 1 como divisores, gcd(a, b) = 1.
# Decimos que para cualquier dos enteros a, b, si gcd(a, b) = 1 entonces a y b son enteros coprimos.
# Si a y b son primos, también son coprimos. Si a es primo y b < a entonces a y b son coprimos.
# Piensa en el caso para a primo y b > a, ¿por qué estos no son necesariamente coprimos?
# Hay muchas herramientas para calcular el GCD de dos enteros, pero para esta tarea recomendamos buscar el Algoritmo de Euclides.
# Intenta programarlo; solo son un par de líneas. Usa a = 12, b = 8 para probarlo.
# Ahora calcula gcd(a, b) para a = 66528, b = 52920 e ingrésalo a continuación.

a = 66528
b = 52920
aux = 0

while b != 0:
    aux = b
    b = a % b
    a = aux

print(a)
# RESULTADO 1512


#ejercicio 12

# a y b sean números enteros positivos. 
# El algoritmo euclidiano extendido es una forma eficiente de encontrar números enteros u, v tales que:
# a*u + b*v = gcd(a,b)
# Más adelante, cuando aprendamos a descifrar textos cifrados RSA, necesitaremos este algoritmo para calcular la inversa modular del exponente público.
# Usando los dos primos p=26513, q=32321 encuentra los números enteros u,v tal que
# p*u + q*v = gcd(p,q)
# Ingrese cualquiera de u y v es el número más bajo que la bandera.
# Sabiendo p, q son primos، qué esperarí gcd(p,q)¿será? Para obtener más detalles sobre el algoritmo euclidiano extendido, consulte esta página.

a = 26513
b = 32321
x = 0
y = 1
aux = 0

while b != 0:
    aux = b
    b = a % b
    a = aux
    x =

print(a)
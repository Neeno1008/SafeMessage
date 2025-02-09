
import sympy
import random

def random_prime(start=1000, end=100000):
    primes = list(sympy.primerange(start, end))
    return random.choice(primes)

p = random_prime() #Primzahl
print(p)
print(p)

g = input("Gebe hier deine Basis an mit der die Verschlüsselung arbeitet ihr müsst beide die gleiche haben!: ") #Basis

print(str(g)+ " " + str(p))

a = input("Gebe jetzt eine Zahl an die du mit niemanden Teilst: ") #Geheimnis

A = int(g) ** int(a) % p

print("Sende jetzt deinem Empfänger diesen Schlüssel: " + str(A))

B = input("Gebe jetzt den Schlüssel ein den du von deinem Empfänger bekommen hast: ")

K = int(B) ** int(a) % p

print("Das ist ihr gemeinsamer Schlüssel: " + str(K))
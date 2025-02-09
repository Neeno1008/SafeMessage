
import sympy
import random

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

def random_prime(start=1000000, end=10000000000):
    primes = list(sympy.primerange(start, end))
    return random.choice(primes)

p = random_prime() #Primzahl

g = get_integer_input("Basis: ") #Basis

print(str(g)+ " " + str(p))

a = get_integer_input("Gebe jetzt eine Geheime Zahl an: ") #Geheimnis

A = int(g) ** int(a) % p

print("Sende jetzt deinem Empfänger diesen Schlüssel: " + str(A))

B = get_integer_input("Gebe jetzt den Schlüssel ein den du von deinem Empfänger bekommen hast: ")

K = int(B) ** int(a) % p

print("Das ist ihr gemeinsamer Schlüssel: " + str(K))
#!/usr/bin/env python

def saludo(nombre):
	print("Hola,", nombre, "!")

def bienvenida():
	print("Bienvenido a esta prueba :)")

def cuadrado(n):
	resultado = n*n
	return resultado

def main():
	name = input("Como te llamas?: ")
	saludo(name)
	bienvenida()
	print("Voy a calcular el cuadrado de tu edad.")
	edad = input("Cuantos tienes?: ")
	cua = cuadrado(int(edad))
	print(cua)

main()
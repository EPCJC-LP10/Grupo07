# -*- coding: iso8859-1 -*-

import menu
import selos
import util


# nome dos ficheiros
fxSelos = "fxSelos.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
	selos.selo = util.ler_ficheiro(fxSelos)


def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
	util.escrever_ficheiro(fxSelos, selos.selo)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        selos.gerir()
    elif op == '2':
        pass    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()
# -*- coding: iso8859-1 -*-

import menu
import selos
import util
import correspondentes


# nome dos ficheiros
fxSelos = "fxSelos.dat"
fxCorrespondentes = "fxCorrespondentes.dat"

def ler_ficheiros():
    # adicionar todos ficheiros a ler
    selos.selo = util.ler_ficheiro(fxSelos)
    correspondentes.listacorrespondente = util.ler_ficheiro(fxCorrespondentes)


def escrever_ficheiros():
    # adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxSelos, selos.selo)
    util.escrever_ficheiro(fxCorrespondentes, correspondentes.listacorrespondente)
     



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':     
        selos.gerir()
    elif op == '2':    
        correspondentes.gerir()
    elif op == '0':
        terminar = True


escrever_ficheiros()
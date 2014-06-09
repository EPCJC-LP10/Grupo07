# -*- coding: utf-8 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Alunos"
    print "   2. Registar Presença (não implementado)"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def selos():
    print
    print " *** Menu Alunos **** "
    print
    print '1. inserir novo selo'
    print '2. Listar todos os selos'
    print '3. alterar dados de um selo'
    print '4. eleminar selo'    
    print
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"


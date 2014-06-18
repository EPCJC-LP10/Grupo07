# -*- coding: iso8859-1 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Selos"
    print "   2. Gestão de Correspondentes"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def selos():
    print
    print " *** Menu Selos **** "
    print
    print '1. inserir novo selo'
    print '2. Listar todos os selos'
    print '3. alterar dados de um selo'
    print '4. eleminar selo'    
    print
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op


def correspondentes():
    print
    print " *** Menu Correspondentes **** "
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


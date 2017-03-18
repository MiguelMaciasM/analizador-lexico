import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['MAS', 'MENOS', 'MULC', 'DIV', 'MOD', 'MENOR', 'MENORIGUAL', 'MAYOR', 'MAYORIGUAL', 'IGUALI', 'DIF', 'ASIGN',
          'PARENTIZQ', 'PARENTDER', 'LLAVEIZQ', 'LLAVEDER', 'COMLINEA', 'COMMULIZQ', 'COMMULDER', 'INC', 'DEC', 'COMA', 'PCOMA']
reservadas = {'main' : 'MAIN', 'if' : 'IF', 'else' : 'ELSE', 'end' : 'END', 'do' : 'DO', 'while' : 'WHILE', 'repeat' : 'REPEAT',
              'until' : 'UNTIL', 'cin' : 'CIN', 'cout' : 'COUT', 'real' : 'REAL', 'int' : 'INT', 'boolean' : 'BOOLEAN'}
tokens = tokens +list(reservadas.values())

t_ignore = ' \t'
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'\%'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYOR = r'>'
t_MAYORIGUAL = r'>='
t_IGUALI = r'=='
t_DIF = r'!='
t_ASIGN = r':='
t_PARENTIZQ = r'\('
t_PARENTDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_COMLINEA = r'//'  
t_COMA = r','
t_PCOMA = r';'
#comment_re = re.compile(r'')

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.lower()
        t.type = t.value
    return t

def t_comentL(t): #posible solucion: checar caracter por caracter o categoria simbolos
    r'//.*'
    pass

def t_numeroE(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_numeroR(t):
    r'\d+(\.\d+)?$'
    t.value = t.value
    return t

def t_error(t):
    print("Caracter ilegal '%s'"% t.value[0])
    t.lexer.skip(1)

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1
    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    for file in files:
        print(str(cont)+". "+file)
        cont = cont+1
    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo-1)]:
                respuesta = True
                break 
    print ('Has escogido %s' %files[int(numArchivo)-1])
    return files[int(numArchivo)-1]

directorio = 'C:/Miguel/sexto semestre/compiladores_I/analisis lexico'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp =  codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)
while True:
    tok=analizador.token()
    if not tok:
        break
    print (tok)
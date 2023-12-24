## String data type
first = "Renan"
last = "Guimarães"

print(type(first)) # string
print(isinstance(first,str)) # Compara o tipo da variavel com outro tipo

## Concatenação
fullname = first + ' ' + last
print(fullname) 

## Typecasting
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s." 
print(statement) 

## Multiplas linhas
multiline = '''
Hey, how are you?

I was just checking in.
                                All good?

'''
print(multiline)

## Caracteres especiais
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located'
print(sentence)

## String methods (Funções chamadas para strings)

print(first)
print(first.lower()) # Minusculo
print(first.upper()) # Maiusculo
print(first)         # Não altera a variavel inicial

print(multiline.title())               # Deixa a primeira letra de cada palavra maiuscula 
print(multiline.replace("good", "ok")) # Troca a primeira string pela segunda
print(multiline)                       # Não altera a variavel inicial

print(len(multiline)) # Tamanho da string 
multiline += "                                    "
multiline = "                      " + multiline
print(len(multiline)) # Tamanho da string após adicionar espaço em branco

print('')
print(len(multiline.strip()))  # Retira os espaços em branco antes e depois do texto
print(len(multiline.lstrip())) # Retira os epaços em branco antes do texto
print(len(multiline.rstrip())) # Retura os espaçço em branco depois do texto

print('')

# Build a menu
title = "menu".upper()
print(title.center(20, "=")) # Centraliza a string e coloca x strings ao lado
print("Coffee".ljust(16, '.') + "$1".rjust(4)) # A esquerda para direita coloca . 
                                               # onde não tiver string e da direita 
                                               # para esquerda coloca 4 espaços em branco
print("Muffin".ljust(16, '.') + "$2".rjust(4)) 
print("Cheesecake".ljust(16, '.') + "$4".rjust(4)) 
print(" ")

# Valores do indice de string
print(first[0]) # String são vetores de caracteres
print(first[1])
print(first[2])
print(first[3])
print(first[4])

print(first[-1])   # O indice -1 é o último como uma lista circular
print(first[0:-1]) # Intervalo fechado aberto
print(first[0:])   # Intervalo fechado até o fim 

# Alguns metodos retornam valores booleanos
print(" ")
print(first.startswith("R")) # Verifica se a string começa com a string x 
print(first.endswith("z"))   # Verifica se a string termina com a string x 
print(first.endswith("enan"))
print(first.startswith("Re"))   

# Boolean Data type
print(" ")
myvalue = True
x = "False"
print(type(x))

x = bool(False)
print(type(x))

print(isinstance(myvalue,bool))

## Tipos Númericos

# Inteiros
preco = 100
melhor_preco = int(80)
print(" ")
print(type(preco))
print(type(melhor_preco))

print(" ")

# Float 
gpa = 3.28
y = float(6)
print(" ")
print(type(gpa))
print(type(y))
print(y)

# Valor complexo, onde j é o i da matematica, ou seja um numero imaginario
comp_value = 5 + 3j
print(" ")
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Funções prontas para numeros
print(" ")
print(gpa)
gpa = -1 * gpa
print(gpa)
print(abs(gpa))      # abs significa valor absoluto, ou seja módulo

print(round(gpa))    # Arrendonda para inteiro
print(round(gpa, 1)) # Arrendonda para o valor decimal especificado
print(round(gpa, 2)) # Arrendonda para o valor decimal especificado
 
import math
print(" ")
print("Pi:",math.pi)          
print("Raiz Quadrada:", math.sqrt(25))
print("Valor:", gpa)
print("Valor arredondado para cima:", math.ceil(gpa)) 
print("Valor arredondado para baixo:", math.floor(gpa))  

# Typecasting de uma string para número
zipcode = "10001"
zip_value = int(zipcode)
print("\n", type(zip_value)) 
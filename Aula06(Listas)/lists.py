users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

# A palavra chave "in" é usada de duas formas:
# - Testar se a algo esta em uma sequência
# - Iterar em uma sequência pelo for loop

# Testa se a string "Dave" está na lista
print("Dave" in users) 
print("Dave" in emptylist)

# Iterando sobre as sequências, o nome não importa
for usuario in users:
    print(usuario)
    
for i in data:
    print(i)
    
string = "Renan Bezerra Guimarães"
if "Renan" in string: print("Sim")
else: print("Não")

# Aqui funciona como um iteradador na lista de chars
for caracter in string: print(caracter)
print(string[0])

print(users[0]) # Primeiro elemento da lista
print(users[-1])# Último elemento da lista

# método que retorna o indice de um dado elemento
print(users.index("Sara"))

# subconjunto de 0 até 2, sem incluir o 2
print(users[0:2])
# subconjunto de 0 até o fim
print(users[0:])

# Tamanho da lista em número de elementos
print(len(data))

# método que adiciona um elemento ao fim lista
users.append("Elsa")
print(users)

# Junta as duas listas, colocando a segunda no fim da primeira
users += ["Jason"]
print(users)

# método para adicionar varios elementos a lista
users.extend(["Robert", 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

# Insere um elemento antes do indice indicado
users.insert(0, 'Bob')
print(users)

# Insere varios elementos antes de 2
users[2:2] = ['Eddie', 'Alex']
print(users)

# Substitui elementos
users[1:3] = ['Robert', 'JPJ']
print(users)

# Remove a primeira ocorrência do elemento
users.remove('Bob')
print(users)

# Remove e retorna o elemento no indice x, padrão o último
users.pop()
print(users)
print(users.pop())
print(users)

# A palavra chave del deleta qualquer objeto, ou seja qualquer coisa praticamente
# incluindo um elemento de uma lista
del users[0]
print(users)

# NameError: name 'data' is not defined
#del data
#print(data)

#Limpa uam lista
data.clear() 
print(data)

# ordena a lista por ordem alfabetica, mas funciona com numeros tbm
# Podendo alterar para ordem decrescente com reverse=True
users.sort(reverse=True)
print(users)

users[1:1] = ['dave'] # Minusculo vem depois de todo mundo quando ordena
users.sort()
print(users)

users.sort(key=str.lower) # Inclui o minusculo como prioridade
print(users)

# Método que reverte a lista 
nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

# Sorted retorna uma nova lista
print(sorted(nums, reverse=True))
print(nums)

# Essa forma não funciona pq é como se numscopy apontasse para a mesma lista
numscopy = nums
print(numscopy)
nums.append(90)
print(nums)
print(numscopy)

# Todos estes funcionam
mynums = nums.copy()
mycopy = nums[:]
mynumscopy = list(nums)

print(type(nums))

mylist = list([1,'Neil', True])
print(mylist)

# Tuples
# São como listas, mas os elementos dentro da lista não mudam
# e a ordem dos elementos dentro da lista também não muda

# Criando uma tuple, sem construtor e com
mytuple = ('Dave', 42, True)
anotherTuple = tuple((1,4,12,34))

print(type(mytuple))
print(type(anotherTuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)
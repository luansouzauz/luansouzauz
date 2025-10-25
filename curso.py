# message = 'Hello Word'
# print (message)


 # Vai deixar o ínicio das frases em letra maiuscula
# nome = 'luan lima'
# print (nome.title())


## Vai deixar todas as letras maiusculas 
# name = 'luan lima'
# print (name.upper())

# nametwo = 'luan lima'
# print (nametwo.lower()) 


## Dessa maneira na próxima atualização, não vai manter
# favorite_language = 'python  '
# #favorite_language.rstrip()
# print (favorite_language)



## metodo que vai manter fixo a remoção do lado direito da string

# favorite_language = 'python    t '
# favorite_language = favorite_language.rstrip()
# print (favorite_language)


## Usando o Append ele joga a nova string ou numero que vc quer para o ultimo da lista 
# motorcycles = ['honda', 'yamaha', 'fazer']
# motorcycles.append ('ducati')
# print (motorcycles)



# motorcycles = []
# motorcycles.append ('Ducati')
# motorcycles.append ('Honda')
# print (motorcycles)

## utilizando o metodo pop para remover algum item da lista 

# frutas = ['maça', 'banana', 'pera', 'iogurte']

# ultimo_item = frutas.pop()

# print (f'O item removido: {ultimo_item}')

# print (f'A lista atualizada: {frutas}')



# frutas2 = ['uva', 'pera', 'iogurte desnatado'] 

# primeiro_item = frutas2.pop(0)

# print (f'O primeiro item descartado {primeiro_item}')

# print (f'A list atualizada de frutas {frutas2}')





## Percorrendo listar com um laço ## 


# magicians = ['David', 'Julia', 'Ana']
# for magician in magicians:
#     print ("O nome dos mágicos são: ", magician)



## Exercicio 4.1 ## 

# pizza = ['Marguerita', 'Calabresa', 'Catupiry']
# for pizzas in pizza:
#     print ("Lista contendo as melhores pizzas do cardápio:",pizzas)
# print (" Eu realmente adoro essas pizzas")   



## Exercicio 4.2 ##

# animais = ["Lobo", "Cachorro", "Raposa"]
# for animal in animais:
#     if animal == Lobo:
#         print ("O lobo blala lbla")
#     elif animal == Cachorro:
#         print ("O cachorro anda")
#     elif animal == Raposa: 
#         print ("A raposa anda")


# mensagem = {
#     "Lobo": " O lobo é selvagem e vive em matilhas.",
#     "Cachorro": " O cachorro é dócil e mora em residência",
#     "Raposa": "A reposa é selvagem e mora na mata",
# }

# for animal in mensagem:
#     print (mensagem[animal])


# animais = ['Lobo', 'Cachorro', 'Raposa']

# for animal in animais:
#     if animal == 'Lobo':
#         print ("Lobo")
#     elif animal == 'Cachorro':
#         print ("Cachorro")
#     elif animal == "Raposa":
#         print ("Raposa")
#         break
# ## Se executar ele vai gerar o print abaixo por conta do for que foi executado corretamente 
# else: 
#     print ("Passou todos os animais")

## Outra maneira inteligente de fazer esse laço for 

# animais = ["Raposa", "Lobo", "Cachorro"]

# search_hunt = input("Qual animal tem apelido de Fox? ")

# for animal in animais:
#     print ("Procurando a Raposa")
#     if search_hunt == "Raposa":
#         print ("Achei a Raposa")
#         break
# else: 
#     print ("Não achei a raposa ")

## Outra forma de fazer esse mesmo código ## 

# animais = ["Lobo", "Cachorro", "Raposa"]

# encontrou = False

# for animal in animais:
#     if animal == "Lobo":
#         print ("Lobo")
#         encontrou = True
#     elif animal == "Cachorro":
#         print ("Cachorro")
#         encontrou = True
#     elif animal == "Raposa":
#         print ("Raposa")
#         encontrou = True

# if not encontrou:
#     print ("Não tem nenhum animal acima na lista ")



## Outra forma de fazer com uma entrada solicitando para o usuário digitar qual animal está na lista, like a imagine ## 

# animais = ['Lobo', 'Cachorro', 'Raposa']

# for animal in animais:
#     search_animal = input ("Digite o nome do animal e veja se está na lista : ")

#     if search_animal == 'Lobo':
#         print ("Está na lista! ")
#     elif search_animal == "Cachorro":
#         print ("Está na lista! ")
#     elif search_animal == "Raposa":
#         print ("Está na lista! ")
#     else: 
#         print ("Não está na lista!")


## Range em python ## 


## Vai repetir 5 vezes a string 
## Posso usar multiplicação para fazer quantas vezes for necessário o range a saída seria 15 começando do 1 e terminando no 14 


# for value in range (5*3):
#     print (value)
    

## Criando uma lista com o range 

numeros = list(range(1,6))
print (numeros)

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

lista=[]
listaf=[]
y=0
lista = input("Digite uma palavra pra ser invertida:  ")
for x in range(len(lista)-1,-1,-1):
    listaf.append(lista[x])
    y=y+1

print(listaf)
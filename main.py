

def inversao():
	lista=[]

	listaf=[]

	y=0

	lista = input("Digite uma palavra pra ser invertida:  ")

	for x in range(len(lista)-1,-1,-1):
    
		listaf.append(lista[x])
    
		y=y+1
	return(listaf)

	print(listaf)

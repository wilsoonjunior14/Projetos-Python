import numpy as np
import matplotlib.pyplot as plt

def aptidao(x):
    return x**3

quantidade = 4
bits = 5
selecionar = 4
geracoes = 30
melhores = []

# GERANDO A POPULACAO INICIAL
populacao = np.random.randint(0,(2**bits)-1,quantidade)
for geracao in range(0,geracoes,1):
    print populacao
    print aptidao(populacao)
    print "----"
    cromossomos = np.zeros((quantidade,bits))

    # CODIFICANDO PARA BINARIO OS INDIVIDUOS
    for i in range(0,quantidade):
        binario = bin(populacao[i])[2:]
        tamanho = len(binario)
        indexes = bits - tamanho
        for j in range(0,tamanho):
            cromossomos[i,indexes] = binario[j]
            indexes+=1
    # SELECAO POR TORNEIO
    selecao = np.zeros((quantidade,bits))

    for i in range(0,4):
        index1 = np.random.randint(0,quantidade,1)[0]
        index2 = np.random.randint(0,quantidade,1)[0]
        if(aptidao(populacao[index1])>=aptidao(populacao[index2])):
            selecao[i,:] = cromossomos[index1,:]
        else:
            selecao[i,:] = cromossomos[index2,:]

    #print selecao
    # CROSSOVER DOS INDIVIDUOS SELECIONADOS
    filhos = selecao
    for i in range(0,4,2):
        crossover = np.random.random()
        if(crossover>=0.6 and crossover<=0.9):
            index1 = np.random.randint(0,quantidade,1)[0]
            index2 = np.random.randint(0,quantidade,1)[0]
            while(index2 == index1):
                index2 = np.random.randint(0, quantidade, 1)[0]
            ponto1 = np.random.randint(0,bits-3,1)[0]
            ponto2 = np.random.randint(3,bits,1)[0]
            pai = selecao[index1,:]
            mae = selecao[index2,:]
            filhos[i,0:ponto1] = pai[0:ponto1]
            filhos[i,ponto1:ponto2] = mae[ponto1:ponto2]
            filhos[i,ponto2:] = pai[ponto2:]
            filhos[i+1,0:ponto1] = mae[0:ponto1]
            filhos[i+1,ponto1:ponto2] = pai[ponto1:ponto2]
            filhos[i+1,ponto2:] = mae[ponto2:]
    print filhos
    # MUTACAO DOS FILHOS GERADOS
    for i in range(0,quantidade):
        for j in range(0,bits):
            mutacao = np.random.random()
            if(mutacao<0.1):
                filhos[i,j] = not filhos[i,j]

    print filhos
    # DECODIFICANDO OS FILHOS GERADOS
    nova_populacao = np.random.randint(0,quantidade,quantidade)
    for i in range(0,quantidade):
        count = 0
        for j in range(0,bits):
            count+= filhos[i,j]*(2**((bits-1)-j))
        nova_populacao[i] = count

    # ELITISMO

    # ENCONTRANDO O MAIS APTO DOS FILHOS GERADOS
    aptidao_nova_populacao = aptidao(nova_populacao)
    maximo = aptidao_nova_populacao[0]
    indice_max = 0
    for i in range(1,quantidade,1):
        if(aptidao_nova_populacao[i]>maximo):
            maximo = aptidao_nova_populacao[i]
            indice_max=i
    print nova_populacao
    print maximo,indice_max

    aptidao_populacao = aptidao(populacao)
    minimo = aptidao_populacao[0]
    indice = 0
    for i in range(1,quantidade,1):
        if(aptidao_populacao[i]<minimo):
            minimo = aptidao_populacao[i]
            indice = i

    populacao[indice] = nova_populacao[indice_max]
    melhores.append(nova_populacao[indice_max])
    print "-> next generation"






print melhores

x = range(0,(2**bits),1)
y=[]
for i in x:
    y.append(aptidao(i))

y_melhores = []
for i in melhores:
    y_melhores.append(aptidao(i))

plt.plot(x,y)
plt.plot(melhores,y_melhores,'r^')
plt.grid(True)
plt.show()






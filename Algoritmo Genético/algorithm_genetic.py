import matplotlib.pyplot as plt
import numpy as np


# FUNCAO DE APTIDAO
def aptidao(x):
    return np.sin(np.pi*x)

# CONFIGURACOES INICIAIS
quantidade = 100
bits = 5
geracoes = 100
melhores = []
selecionar = 80

# POPULACAO INICIAL
populacao = np.random.randint(-5,5,quantidade)
print populacao


# GERANDO GRAFICO
# plotando o grafico da funcao
x = range(-(2**(bits-1))+1,(2**(bits-1)),1)
y=[]
for i in x:
    y.append(aptidao(i))

# plotando a populacao inicial
plt.subplot("221")
plt.title("Populacao Inicial")
plt.plot(x,y)
plt.plot(populacao,aptidao(populacao),'r^')
plt.xlabel("Amostras "+str(quantidade)+" / Amostras com valor maximo "+str(sum(populacao==15))+"")


for contagem in range(0,geracoes,1):
    cromossomos = np.zeros((quantidade,bits))

    # CODIFICANDO PARA BINARIO OS INDIVIDUOS
    for i in range(0,quantidade):
        if(populacao[i]>=0):
            binario = bin(populacao[i])[2:]
            tamanho = len(binario)
            indexes = bits - tamanho
            for j in range(0, tamanho):
                cromossomos[i, indexes] = binario[j]
                indexes += 1
        else:
            binario = bin(populacao[i])[3:]
            tamanho = len(binario)
            indexes = bits - tamanho
            cromossomos[i,0] = 1
            for j in range(0, tamanho):
                cromossomos[i, indexes] = binario[j]
                indexes += 1
    #print "codificacao dos cromossomos"
    #print cromossomos

    # SELECAO POR TORNEIO
    selecao = np.zeros((selecionar,bits))

    for i in range(0,selecionar):
        index1 = np.random.randint(0,quantidade,1)[0]
        index2 = np.random.randint(0,quantidade,1)[0]
        if(aptidao(populacao[index1])>=aptidao(populacao[index2])):
            selecao[i,:] = cromossomos[index1,:]
        else:
            selecao[i,:] = cromossomos[index2,:]

    #print "cromossomos selecionados"
    #print selecao

    # CROSSOVER DOS INDIVIDUOS SELECIONADOS
    filhos = selecao
    for i in range(0,selecionar, 2):
        crossover = np.random.random()
        if (crossover >= 0.6 and crossover <= 0.9):
            index1 = np.random.randint(0, selecionar, 1)[0]
            index2 = np.random.randint(0, selecionar, 1)[0]
            while (index2 == index1):
                index2 = np.random.randint(0, selecionar, 1)[0]
            ponto1 = np.random.randint(0, bits - 3, 1)[0]
            ponto2 = np.random.randint(3, bits, 1)[0]
            pai = selecao[index1, :]
            mae = selecao[index2, :]
            filhos[i, 0:ponto1] = pai[0:ponto1]
            filhos[i, ponto1:ponto2] = mae[ponto1:ponto2]
            filhos[i, ponto2:] = pai[ponto2:]
            filhos[i + 1, 0:ponto1] = mae[0:ponto1]
            filhos[i + 1, ponto1:ponto2] = pai[ponto1:ponto2]
            filhos[i + 1, ponto2:] = mae[ponto2:]

    #print "cromossomos dos filhos gerados"
    #print filhos

    # MUTACAO DOS FILHOS GERADOS
    for i in range(0, selecionar):
        for j in range(0, bits):
            mutacao = np.random.random()
            if (mutacao < 0.1):
                filhos[i, j] = not filhos[i, j]

    #print "cromossomos dos filhos modificados geneticamente"
    #print filhos

    # DECODIFICANDO OS FILHOS GERADOS
    nova_populacao = np.random.randint(0,selecionar,selecionar)
    for i in range(0, selecionar):
        count = 0
        for j in range(1, bits):
            count += filhos[i, j] * (2 ** ((bits - 1) - j))
        if(filhos[i,0]==1):
            count = -count
        nova_populacao[i] = count

    #print "filhos gerados"
    #print nova_populacao

    # ENCONTRANDO O MAIS APTO DOS FILHOS GERADOS
    aptidao_nova_populacao = aptidao(nova_populacao)
    maximo = aptidao_nova_populacao[0]
    indice_max = 0
    for i in range(1, selecionar, 1):
        if (aptidao_nova_populacao[i] > maximo):
            maximo = aptidao_nova_populacao[i]
            indice_max = i
    #print nova_populacao
    #print maximo, indice_max

    aptidao_populacao = aptidao(populacao)
    minimo = aptidao_populacao[0]
    indice = 0
    for i in range(1, quantidade, 1):
        if (aptidao_populacao[i] < minimo):
            minimo = aptidao_populacao[i]
            indice = i

    populacao[indice] = nova_populacao[indice_max]
    melhores.append(nova_populacao[indice_max])
    if(contagem==25):
        plt.subplot("222")
        plt.title("25 Geracao")
        plt.plot(x,y)
        plt.plot(populacao,aptidao(populacao),'r^')
        plt.xlabel("Amostras " + str(quantidade) + " / Amostras com valor maximo " + str(sum(populacao == 15)) + "")
        print "ta qui"
    if(contagem==50):
        plt.subplot("223")
        plt.title("50 Geracao")
        plt.plot(x,y)
        plt.plot(populacao,aptidao(populacao),'r^')
        plt.xlabel("Amostras " + str(quantidade) + " / Amostras com valor maximo " + str(sum(populacao == 15)) + "")



print melhores

print "populacao final"
print populacao

#plotando populacao final
plt.subplot("224")
plt.plot(x,y)
plt.plot(populacao,aptidao(populacao),'r^')
plt.title(""+str(geracoes)+" Geracao")
plt.xlabel("Amostras "+str(quantidade)+" / Amostras com valor maximo "+str(sum(populacao==15))+"")
plt.show()

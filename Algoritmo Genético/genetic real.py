import convert
import numpy as np
import matplotlib.pyplot as plt


# FUNCAO OBJETIVO
def aptidao(x):
    return np.sin(x) * x**3


#   CONFIGURACOES INICIAIS
# TAMANHO DA POPULACAO A SER TRABALHADA
quantidade = 100
# QUANTIDADE DE BITS A SER TRABALHADA
bits = 6
# PRECISAO DAS CASAS DECIMAIS
gl = 10
# QUANTIDADE DE GERACOES
geracoes = 100


#   GERANDO A POPULACAO INICIAL
populacao = np.random.randint(-10,10,quantidade)
print populacao

# PLOTANDO A POPULACAO INICIAL
x = np.linspace(-(2**(bits-1)),2**(bits-1),2000)
y = aptidao(x)

plt.subplot("221")
plt.xlabel("Populacao Inicial")
plt.plot(x,y)
plt.plot(populacao,aptidao(populacao),'ro')

# ARMAZENA OS MELHORES INDIVIDUOS DE CADA GERACAO
melhores = []

for contagem in range(0,geracoes,1):
    # SELECAO NATURAL
    # SELECAO PELO METODO DO TORNEIO
    selecao = np.random.random(quantidade)
    for i in range(0,quantidade):
        index1 = np.random.randint(0,quantidade,1)[0]
        index2 = np.random.randint(0, quantidade,1)[0]
        if(aptidao(populacao[index1])>=aptidao(populacao[index2])):
            selecao[i] = populacao[index1]
        else:
            selecao[i] = populacao[index2]

    print selecao
    # CODIFICANDO OS INDIVIDUOS PARA FORMA BINARIA
    filhos = np.random.randint(0,1,(quantidade,bits+gl))
    for i in range(0,quantidade):
        binary = convert.convert(selecao[i]).retorno()
        filhos[i,0] = int(binary[0])
        for j in range(binary.__len__()-gl,binary.__len__()):
            filhos[i,j] = binary[j]

        binary = binary[1:binary.__len__()-gl]
        for k in range(0,binary.__len__()):
            filhos[i,bits-1-k] = binary[binary.__len__()-1-k]


    # REPRODUCAO DOS INDIVIDUOS SELECIONADOS
    for i in range(0,quantidade,2):
        crossover = np.random.random()
        if(crossover>0.6 and crossover<0.9):
            index1 = np.random.randint(0, quantidade, 1)[0]
            index2 = np.random.randint(0, quantidade, 1)[0]
            ponto1 = np.random.randint(1,3,1)[0]
            ponto2 = np.random.randint(3,7,1)[0]
            pai = filhos[index1,:]
            mae = filhos[index2,:]
            # EDITA O FILHO 1
            filhos[i,0:ponto1] = pai[0:ponto1]
            filhos[i,ponto1:ponto2] = mae[ponto1:ponto2]
            filhos[i,ponto2:] = pai[ponto2:]
            # EDITA O FILHO 2
            filhos[i+1, 0:ponto1] = mae[0:ponto1]
            filhos[i+1, ponto1:ponto2] = pai[ponto1:ponto2]
            filhos[i+1, ponto2:] = mae[ponto2:]


    # MUTACAO DOS FILHOS REPRODUZIDOS
    for i in range(0,quantidade):
        for j in range(0,bits+gl):
            mutacao = np.random.random()
            if(mutacao < 0.1):
                filhos[i,j] = not filhos[i,j]

    # DECODIFICANDO OS FILHOS GERADOS
    nova_populacao = np.random.random(quantidade)
    for i in range(0,quantidade):
        count = 0

        # CALCULANDO O VALOR DA PARTE INTEIRA
        for j in range(1,bits):
            count += filhos[i,j] * (2**(bits-1-j))

        # CALCULANDO O VALOR DAS CASAS DECIMAIS
        count2 = 0
        for k in range(bits,bits+gl):
            count2 += filhos[i,k] * (2**(bits-1-k))

        if(filhos[i,0]==1):
            nova_populacao[i] = -float(count+count2)
        else:
            nova_populacao[i] = float(count+count2)

    # ELITISMO
    # PERMITINDO QUE O MELHOR INDIVIDUO GERADO SE INTEGRE A POPULACAO
    maximo = nova_populacao[0]
    indice1 = 0
    minimo = populacao[0]
    indice2 = 0
    for i in range(0,quantidade):
        if(aptidao(nova_populacao[i])>aptidao(maximo)):
            maximo = nova_populacao[i]
            indice1 = i
        if(aptidao(populacao[i])<aptidao(minimo)):
            minimo = populacao[i]
            indice2 = i

    #populacao[indice2] = float(nova_populacao[indice1])
    #print populacao
    #print maximo

    # EDITANDO A NOVA POPULACAO COM O MELHOR INDIVIDUO ENCONTRADO
    pop = np.random.random(quantidade)
    for i in range(0,quantidade):
        if(i == indice2):
            pop[i] = nova_populacao[indice1]
        else:
            pop[i] = populacao[i]

    populacao = pop
    melhores.append(nova_populacao[indice1])

    if(contagem == 25):
        plt.subplot("222")
        plt.xlabel("Apos "+str(contagem)+" geracoes")
        plt.plot(x,y)
        plt.plot(populacao,aptidao(populacao),'ro')
    elif(contagem == 50):
        plt.subplot("223")
        plt.xlabel("Apos " + str(contagem) + " geracoes")
        plt.plot(x, y)
        plt.plot(populacao, aptidao(populacao), 'ro')


# PLOTANDO OS RESULTADOS OBTIDOS
print populacao
plt.subplot("224")
plt.plot(x,y)
plt.plot(populacao,aptidao(populacao),'ro')
plt.xlabel("Apos "+str(geracoes)+" geracoes")
plt.show()

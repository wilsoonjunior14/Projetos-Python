import neurolab as n
import numpy as np
import matplotlib.pyplot as plt

def aptidao(x):
    return x**3

input = np.linspace(0,32,100)
output = aptidao(input)

input = input.reshape(100,1)
input = input/max(input)
output = output.reshape(100,1)
output = output/max(output)

rede = n.net.newff([[0,1]],[10,1])
rede.trainf = n.net.train.train_rprop
erro = rede.train(input,output,epochs=1000,goal=0.001,show=1000)

output_train = rede.sim(input)

input_test = np.linspace(0,32,10)
input_test = input_test.reshape(10,1)
input_test = input_test/max(input_test)

output_test = rede.sim(input_test)
print output_test
plt.plot(input,output,'-',input_test,output_test,'go')
plt.axis([-0.5,1.5,-0.5,1.5])
plt.legend(['amostras de treinamento','amostras de teste'])
plt.show()
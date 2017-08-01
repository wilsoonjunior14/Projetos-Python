import numpy as np


class convert:
    # NUMERO A SER FORMATADO
    number = ""

    # PRECISAO DE CASAS DECIMAIS
    gl = 10

    # PARTE INTEIRA DO NUMERO FORMATADO
    inteira=0

    # PARTE FRACIONADA DO NUMERO FORMATADO
    fracionada=0


    # CONSTRUTOR DA CLASSE
    def __init__(self,number):
        self.number = number

        # SE O NUMERO FOR POSITIVO O PRIMEIRO BIT DO NUMERO FORMATADO E ZERO
        # CASO CONTRARIO O PRIMEIRO BIT DO NUMERO FORMATADO SERA 1
        bit_positivo_negativo = 0
        indice = 2
        if(self.number<0):
            bit_positivo_negativo = 1
            indice = 3

        string = ""+str(self.number)+""
        if (string.find('.')!=-1):

            part_int = string[0:string.find('.')]
            part_frac = "0"+string[string.find('.'):]

            self.inteira = ""+str(bit_positivo_negativo)+""+bin(int(part_int))[indice:]

            condition = part_frac[part_frac.find('.')+1:]
            integer=""
            bits = 0
            while(bits!= self.gl):
                number = float(part_frac)*2
                number = ""+str(number)+""
                integer = ""+str(integer)+""+str(number[0:number.find('.')])+""
                part_frac = "0"+number[number.find('.'):]
                bits = bits + 1
            self.fracionada = integer

        else:

            integer = ""+str(bit_positivo_negativo)+""+str(bin(self.number)[indice:])+""
            self.inteira = integer
            self.fracionada = "00000"




    # FUNCAO QUE RETORNA O NUMERO DECIMAL FRACIONADO EM BINARIO
    def retorno(self):
        return self.inteira+self.fracionada

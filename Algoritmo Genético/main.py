# Wilson Junior
# CREATED BY 28/07/2017 - IBIAPINA - CEARA - BRAZIL
import numpy as np


import numpy as np

class convert:
    number = ""
    binary = ""

    def __init__(self,number):
        self.number = str(np.around(number,2))
        integer = self.number[0:self.number.find('.')]
        decimal = self.number[self.number.find('.'):]

        print bin(int(integer))[2:]
        dec = str("0"+decimal)





convert(100.1231)
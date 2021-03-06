#=============================================================================================================
# Undergraduate Student: Arturo Burgos
# Professor: João Rodrigo Andrade
# Federal University of Uberlândia - UFU, Fluid Mechanics Laboratory - MFLab, Block 5P, Uberlândia, MG, Brazil
#=============================================================================================================

# Fifth exercise: txt File 

# Apparently it is not possible to use JIT at the same time as file function

import numpy  
import time
from numba import jit

x = numpy.arange(1,1000000,1)
X = str(x)
#print(x)

y = numpy.cos(x)

#print(y)



@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def writetxt(a1,a2):

    z = open('/home/arturo/Desktop/GitHub/IC/Comparing-Languages/txt_File/Python+NUMBA/teste-JIT.txt',"w")
    z.write("X")
    z.write('\n')

    for i in range(len(a1)):
    
        z.write(str(a1[i]))
        z.write(' ')

    z.write('\n')
    z.write("Y")
    z.write('\n')

    for i in range(len(a2)):
    
        z.write(str(a2[i]))
        z.write(' ')

    z.close()

t_initial = time.time()  # I set here the initial time.

writetxt(x,y)

print("--- %s seconds with compilation---\n" % (time.time() - t_initial))

# First we compile the code, then now we execute from cache.
print('\n')

t_initial = time.time()  # I set here the initial time.

writetxt(x,y)

print("--- %s seconds after compilation---\n" % (time.time() - t_initial))




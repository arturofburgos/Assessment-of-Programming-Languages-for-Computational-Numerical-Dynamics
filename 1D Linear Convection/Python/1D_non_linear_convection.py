# Undergraduate Student: Arturo Burgos
# Professor: João Rodrigo Andrade
# Federal University of Uberlândia - UFU, Fluid Mechanics Laboratory - MFLab, Block 5P, Uberlândia, MG, Brazil


# Fifth exercise: 1D Linear Convection

import numpy as np
import matplotlib.pyplot as plt


# First define the:

X = 2 # Length of the grid
nx = 41 # Number of nodes
dx = X/(nx-1) # The distance between consecutive nodes

nt = 25 # The number of timesteps I want to calculate
dt = 0.025 # The amount of time each timestep cover

c = 1 # Wavespeed

# Initial velocity condition:
u = np.ones(nx)

u[int(0.5/dx):int(1/dx+1)] = 2

un = np.ones(nx) # Auxiliar array 


fig , ax = plt.subplots(figsize=(15 , 5),ncols=2)

ax[0].set_title('Wave velocity through time passing in a 1-D grid ')
ax[1].set_title('Comparing the wave in the first and the last timestep')

ax[0].set_xlabel('Length of the grid')
ax[1].set_xlabel('Length of the grid')

ax[0].set_ylabel('Velocity u')
ax[1].set_ylabel('Velocity u')

ax[0].plot(np.linspace(0,2,nx),u)
ax[1].plot(np.linspace(0,2,nx),u,label='First timestep')

u_teste = np.zeros((41,41))

for n in range(1,nt):
    un[:] = u[:]
    #un = u.copy()
    for j in range(1,nx ):
        for i in range(1,nx):
            #u[i] = un[i] - c * (dt/dx) * (un[i]-un[i-1]) # Linear 
            u[i] = un[i] - un[i] * (dt/dx) * (un[i]-un[i-1]) # Non-Linear
            u_teste[j,i] = u[i]
        ax[0].plot(np.linspace(0,2,nx),u) # This shows what happens through time -> first plot only
    

ax[1].plot(np.linspace(0,2,nx),u[:],label='Last timestep') 
ax[1].legend()
plt.show()

print('The velocity last timestep velocity values are: ')
print(u)    

print(u_teste[1,:])
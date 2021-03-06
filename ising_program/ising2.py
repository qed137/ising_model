import numpy as np
from numpy import log,exp,tanh
from scipy.ndimage import convolve
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy.fft import fft2,fftshift

from numpy import genfromtxt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

mu=-100
db = 2*genfromtxt('latech.csv', delimiter='\t')-1

# Set up plotter
fig, axs = plt.subplots(3,2)
ims=[]

class Ising():

	def __init__(self,size,beta,mu,steps):
		self.size = size
		self.beta = beta
		self.mu = mu
		self.window = np.array([[0,1,0],\
								[1,0,1],\
								[0,1,0]])
		self.config = 2*np.random.randint(0,2,size=(size,size))-1
		self.m = -steps+100
		self.steps = steps

	def update(self):
		self.mcmove()
		return None

	def mcmove(self):
		self.m = self.m + 1
		m = self.m
		size = self.size
		config = self.config
		altconfig = 2*np.random.randint(0,2,size=(size,size))-1
		therand = np.random.rand(size,size)
		dH = -self.beta*self.config*(
			2*convolve(config,self.window,mode='wrap'))
		config = np.where(log(therand)<dH,altconfig,config)
		self.config = config
		return None

	def evolve(self):
		global ims,axs
		for i in range(self.steps):
			m1 = model.config
			model.update()
			m2 = model.config
			m = m2
			im0 = m
			#im1 = axs[1].imshow(abs(fftshift(fft2(m))))
			ims.append(im0)




# Running Simulation
model = Ising(400,1,0,1000)
model.evolve()
n=[0,200,400,600,800,1000]
for i in range(6):
	ax = plt.subplot(2, 3,i+1)
	ax.imshow(ims[i],interpolation=None,cmap="pink")
	ax.set_title(r"$t=%i$"%n[i])
	ax.set_xticks([])
	ax.set_yticks([])


plt.tight_layout()
plt.savefig('latech.pdf', bbox_inches='tight')
plt.show()






#ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
#                                repeat_delay=1000)

#ani.save('ising.gif', dpi=80, writer='imagemagick')
#plt.show()






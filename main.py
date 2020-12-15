import random
import matplotlib.pyplot as plt

batas = [(-100,100),(-100,100)]
jumlah_partikel = 25
pos_awal = [-80,10] 
pos_lama = [-80,10]
target = [60,-50]
halang = [[(5,30),(25,-75)],
		  [(-75,50),(65,20)],
		  [(-30,-10),(2,-17)],
		  [(35,85),(15,-20)]]

def plot_halang(halang):
	for i in range(len(halang)):
		coord=[[halang[i][0][0],halang[i][1][0]],
			   [halang[i][0][1],halang[i][1][0]],
			   [halang[i][0][1],halang[i][1][1]],
			   [halang[i][0][0],halang[i][1][1]]]
		coord.append(coord[0])
		xs, ys = zip(*coord)
		plt.fill(xs,ys,'k')

def fitness_function(posisi):
	x0,y0 = target 
	x0=float(x0)
	y0=float(y0)
	fit=0
	fit+=(x0-posisi[0])**2 +(y0-posisi[1])**2
	return fit

class partikel:
	def __init__(self,pos_awal):
		self.pos=[]
		self.vel=[]
		self.best_pos=[]
		self.best_error=-1
		self.error=-1
		for i in range(0,dimensi):
			self.vel.append(random.uniform(-1,1))
			self.pos.append(pos_awal[i])

	def update_velocity(self,global_best_position):
		w = 0.47
		c1 = 1
		c2 = 2

		for i in range(0,dimensi):
			r1=random.random()
			r2=random.random()

			cog_vel=c1*r1*(self.best_pos[i]-self.pos[i])
			social_vel=c2*r2*(global_best_position[i]-self.pos[i])
			self.vel[i]=w*self.vel[i]+cog_vel+social_vel

	def update_position(self,batas,halang):
		for i in range(0,dimensi):
			self.pos[i]=self.pos[i]+self.vel[i]

			if self.pos[i]>batas[i][1]: 
				self.pos[i]=batas[i][1] 

			if self.pos[i]<batas[i][0]:
				self.pos[i]=batas[i][0] 

			for k in range(len(halang)):
				if self.pos[0]>(halang[k][0][0]) and self.pos[0]<(halang[k][0][1]) and self.pos[1]<(halang[k][1][0]) and self.pos[1]>(halang[k][1][1]):
					self.pos[0]=pos_lama[0] 
					self.pos[1]=pos_lama[1] 
				
			pos_lama[0]=self.pos[0] 
			pos_lama[1]=self.pos[1] 

	def evaluate_fitness(self,fitness_function): 
		self.error = fitness_function(self.pos)

		if self.error<self.best_error or self.best_error==-1:
			self.best_pos = self.pos 
			self.best_error = self.error

class pso():
	def __init__(self,fitness_function,pos_awal,batas,jumlah_partikel):
		global dimensi

		dimensi = len(pos_awal) 
		global_best_error = -1
		global_best_position = [] 
		self.gamma = 0.0001 
		swarm = []
		for i in range(0,jumlah_partikel):
			swarm.append(partikel(pos_awal))

		i = 0 
		mat_ge = [] 

		while True:
			plot_halang(halang) 

			for j in range(0,jumlah_partikel):
				swarm[j].evaluate_fitness(fitness_function) 

				if swarm[j].error < global_best_error or global_best_error == -1:
					global_best_position = list(swarm[j].pos) 
					global_best_error = float(swarm[j].error) 
					plt.title("Partikel:{}, Error:{}".format(jumlah_partikel,round(global_best_error,1)))
				
				if i%2 == 0:
					global_best_error = -1
					global_best_position = list([swarm[j].pos[0]+self.gamma*(swarm[j].error)*random.random() ,swarm[j].pos[1]+self.gamma*(swarm[j].error)*random.random() ])
			
			if global_best_error != -1:
				mat_ge.append(global_best_error) 
			
			pos_0 = {} 
			pos_1 = {}

			for j in range(0,jumlah_partikel):
				pos_0[j] = []
				pos_1[j] = []

			for j in range(0,jumlah_partikel):
				swarm[j].update_velocity(global_best_position) 
				swarm[j].update_position(batas,halang)
				pos_0[j].append(swarm[j].pos[0])
				pos_1[j].append(swarm[j].pos[1])
				plt.xlim(batas[0])
				plt.ylim(batas[1])

			for j in range(0,jumlah_partikel):
				plt.plot(pos_0[j], pos_1[j], color='r', marker ='.') 

			plt.plot(float(pos_awal[0]), float(pos_awal[1]), 
				color='C0', marker ='*')
			plt.plot(float(target[0]), float(target[1]), color='C2', marker ='X')
			plt.pause(0.1) 
			plt.clf()

			i+=1
	
			if global_best_error<0.1 and global_best_error>-1:
				print('BERES! Error terkecil: ',global_best_error)
				break 

		n_iter = len(mat_ge)
		mat_iter = range(n_iter)
		plt.plot(mat_iter,mat_ge)
		plt.title("Error dari Langkah ke langkah")
		plt.xlabel("Step")
		plt.ylabel("Error")
		plt.show()

pso(fitness_function,pos_awal,batas,jumlah_partikel)
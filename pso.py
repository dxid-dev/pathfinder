import matplotlib.pyplot as plt
import random

def plot_obstacle(obstacle):
	for i in range(len(obstacle)):
		coord=[[obstacle[i][0][0],obstacle[i][1][0]],
			   [obstacle[i][0][1],obstacle[i][1][0]],
			   [obstacle[i][0][1],obstacle[i][1][1]],
			   [obstacle[i][0][0],obstacle[i][1][1]]]
		coord.append(coord[0])
		xs, ys = zip(*coord)
		plt.fill(xs, ys, 'k')

def fitness_function(position):
	x0,y0 = target 
	x0=float(x0)
	y0=float(y0)
	fit=0
	fit+=(x0-position[0])**2 +(y0-position[1])**2
	return fit

class particle:
	def __init__(self,init_pos):
		self.pos=[]
		self.vel=[]
		self.best_pos=[]
		self.best_error=-1
		self.error=-1
		for i in range(0, dimension):
			self.vel.append(random.uniform(-1,1))
			self.pos.append(init_pos[i])

	def update_velocity(self, global_best_position):
		w = 0.60
		c1 = 0.90
		c2 = 1.45

		for i in range(0,dimension):
			r1=random.random()
			r2=random.random()

			cog_vel=c1*r1*(self.best_pos[i]-self.pos[i])
			social_vel=c2*r2*(global_best_position[i]-self.pos[i])
			self.vel[i]=w*self.vel[i]+cog_vel+social_vel

	def update_position(self,border,obstacle):
		for i in range(0,dimension):
			self.pos[i]=self.pos[i]+self.vel[i]

			if self.pos[i]>border[i][1]: 
				self.pos[i]=border[i][1] 

			if self.pos[i]<border[i][0]:
				self.pos[i]=border[i][0] 

			for k in range(len(obstacle)):
				if self.pos[0]>(obstacle[k][0][0]) and self.pos[0]<(obstacle[k][0][1]) and self.pos[1]<(obstacle[k][1][0]) and self.pos[1]>(obstacle[k][1][1]):
					self.pos[0]=old_pos[0] 
					self.pos[1]=old_pos[1] 
				
			old_pos[0]=self.pos[0] 
			old_pos[1]=self.pos[1] 

	def evaluate_fitness(self,fitness_function): 
		self.error = fitness_function(self.pos)

		if self.error<self.best_error or self.best_error==-1:
			self.best_pos = self.pos 
			self.best_error = self.error

class pso():
	def __init__(self, fitness_function, init_pos, border, n_particles):
		global dimension

		dimension = len(init_pos) 
		global_best_error = -1
		global_best_position = [] 
		self.gamma = 0.0001 
		swarm = []
		for i in range(0,n_particles):
			swarm.append(particle(init_pos))

		i = 0 
		mat_ge = [] 

		while True:
			plot_obstacle(obstacle) 

			for j in range(0, n_particles):
				swarm[j].evaluate_fitness(fitness_function) 

				if swarm[j].error < global_best_error or global_best_error == -1:
					global_best_position = list(swarm[j].pos) 
					global_best_error = float(swarm[j].error) 
					plt.title("{} particles".format(n_particles))
				
				if i%2 == 0:
					global_best_error = -1
					global_best_position = list([swarm[j].pos[0]+self.gamma*(swarm[j].error)*random.random(), swarm[j].pos[1]+self.gamma*(swarm[j].error)*random.random()])
			
			if global_best_error != -1:
				mat_ge.append(global_best_error) 
			
			pos_0 = {} 
			pos_1 = {}

			for j in range(0, n_particles):
				pos_0[j] = []
				pos_1[j] = []

			for j in range(0, n_particles):
				swarm[j].update_velocity(global_best_position) 
				swarm[j].update_position(border, obstacle)
				pos_0[j].append(swarm[j].pos[0])
				pos_1[j].append(swarm[j].pos[1])
				plt.xlim(border[0])
				plt.ylim(border[1])

			for j in range(0, n_particles):
				plt.plot(pos_0[j], pos_1[j], color='r', marker ='.') 

			plt.plot(float(init_pos[0]), float(init_pos[1]), 
				color='C0', marker ='*')
			plt.plot(float(target[0]), float(target[1]), color='C2', marker ='X')
			plt.pause(0.1) 
			plt.clf()

			i+=1
	
			if global_best_error < 0.1 and global_best_error>-1:
				print('DONE! Least Error: ', global_best_error)
				break 
		
		plt.clf()
		n_iter = len(mat_ge)
		mat_iter = range(n_iter)
		plt.plot(mat_iter, mat_ge)
		plt.title("Error from step to step")
		plt.xlabel("Step")
		plt.ylabel("Error")
		plt.show()

border = [(-100, 100),(-100, 100)]
n_particles = 25
init_pos = [-80, -10]
old_pos = [-80, -10]
target = [35, -20]
obstacle = [[(0, 30), (25, -75)],
		  [(-75, 50), (65, 10)],
		  [(-30, -10), (2, -17)],
		  [(40, 90), (0, -55)],
		  [(-75, -15), (-50, -75)]]

pso(fitness_function,init_pos,border,n_particles)
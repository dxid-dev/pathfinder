import random

class Particle:
    def __init__(self,init_pos, dimension):
        self.pos=[]
        self.vel=[]
        self.best_pos=[]
        self.best_error=-1
        self.error=-1
        for i in range(0, dimension):
            self.vel.append(random.uniform(-1,1))
            self.pos.append(init_pos[i])

    def update_velocity(self, global_best_position, dimension):
        w = 0.60
        c1 = 0.90
        c2 = 1.45

        for i in range(0,dimension):
            r1=random.random()
            r2=random.random()

            cog_vel=c1*r1*(self.best_pos[i]-self.pos[i])
            social_vel=c2*r2*(global_best_position[i]-self.pos[i])
            self.vel[i]=w*self.vel[i]+cog_vel+social_vel

    def update_position(self, border, obstacle, old_pos, dimension):
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

    def evaluate_fitness(self,fitness_function, target): 
        self.error = fitness_function(self.pos, target)

        if self.error<self.best_error or self.best_error==-1:
            self.best_pos = self.pos 
            self.best_error = self.error

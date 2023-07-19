import matplotlib.pyplot as plt
from utilities import plot_obstacle, fitness_function
from particle import Particle
import random


class PSO():
    def __init__(self, init_pos, border, n_particles, target):
        dimension = len(init_pos)
        global_best_error = -1
        global_best_position = []
        self.gamma = 0.0001
        swarm = []
        for i in range(0, n_particles):
            swarm.append(Particle(init_pos, dimension))

        i = 0
        mat_ge = []

        while True:
            plot_obstacle(obstacle)

            for j in range(0, n_particles):
                swarm[j].evaluate_fitness(fitness_function, target)

                if swarm[j].error < global_best_error or global_best_error == -1:
                    global_best_position = list(swarm[j].pos)
                    global_best_error = float(swarm[j].error)
                    plt.title("{} particles".format(n_particles))

                if i % 2 == 0:
                    global_best_error = -1
                    global_best_position = list([swarm[j].pos[0]+self.gamma*(swarm[j].error)*random.random(
                    ), swarm[j].pos[1]+self.gamma*(swarm[j].error)*random.random()])

            if global_best_error != -1:
                mat_ge.append(global_best_error)

            pos_0 = {}
            pos_1 = {}

            for j in range(0, n_particles):
                pos_0[j] = []
                pos_1[j] = []

            for j in range(0, n_particles):
                swarm[j].update_velocity(global_best_position, dimension)
                swarm[j].update_position(border, obstacle, old_pos, dimension)
                pos_0[j].append(swarm[j].pos[0])
                pos_1[j].append(swarm[j].pos[1])
                plt.xlim(border[0])
                plt.ylim(border[1])

            for j in range(0, n_particles):
                plt.plot(pos_0[j], pos_1[j], color='r', marker='.')

            plt.plot(float(init_pos[0]), float(init_pos[1]),
                     color='C0', marker='*')
            plt.plot(float(target[0]), float(
                target[1]), color='C2', marker='X')
            plt.pause(0.1)
            plt.clf()

            i += 1

            if global_best_error < 0.1 and global_best_error > -1:
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


border = [(-100, 100), (-100, 100)]
n_particles = 25
init_pos = [-80, -10]
old_pos = [-80, -10]
target = [35, -20]
obstacle = [[(0, 30), (25, -75)],
            [(-75, 50), (65, 10)],
            [(-30, -10), (2, -17)],
            [(40, 90), (0, -55)],
            [(-75, -15), (-50, -75)]]

PSO(init_pos, border, n_particles, target)

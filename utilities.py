import matplotlib.pyplot as plt

def plot_obstacle(obstacle):
    for i in range(len(obstacle)):
        coord=[[obstacle[i][0][0],obstacle[i][1][0]],
               [obstacle[i][0][1],obstacle[i][1][0]],
               [obstacle[i][0][1],obstacle[i][1][1]],
               [obstacle[i][0][0],obstacle[i][1][1]]]
        coord.append(coord[0])
        xs, ys = zip(*coord)
        plt.fill(xs, ys, 'k')

def fitness_function(position, target):
    x0,y0 = target 
    x0=float(x0)
    y0=float(y0)
    fit=0
    fit+=(x0-position[0])**2 +(y0-position[1])**2
    return fit

#importing required mathematical functions

import numpy as np # mathematical module
from numpy import sin,cos
from scipy.integrate import odeint
from matplotlib import pyplot as plt





#define equations

def equations(y0, t):  #takes initial state vector and time
    theta, x = y0         #theta and x equals initially equals state vector, state vector as a list
    f = [x, -(g/l)*sin(theta)]  #function
    return f

def plot_results(time, theta1, theta2):
    plt.plot(time, theta1[:,0])   #entire no. of rows and first column , we don't want the velocity included here
    plt.plot(time, theta2)
    ps = ('initial angle : ' + str(initial_angle_degrees) + 'degrees')
    plt.title('Pendulum motion : ' + ps)




    plt.xlabel('time in secs')
    plt.ylabel('angle in radians')
    plt.grid(True)
    plt.legend(['non linear case', 'linear case'], loc = 'lower right')
    plt.show()







#parameters

g = 9.81
l = 1.0

time = np.arange(0, 10.0, 0.025) # 0 to 10 secs with 0.025 step size, small enough to capture non linearity



#initial conditions

initial_angle_degrees = 120
theta0 = np.radians(initial_angle_degrees)   #converting initial angles to radians
x0 = np.radians(0.0)   # theta', change in theta , angular velocity




#find the solution to the non linear pendulum problem, real pendulum motion

theta1 = odeint(equations, [theta0, x0], time)   # non linear result



# solution to the linear pendulum problem, simple harmonic motion

omega = np.sqrt(g/l)
theta2 = [theta0 * cos(omega*t) for t in time]    # linear result


# plotting results

plot_results(time, theta1, theta2)



#interpreting results

#the graph shows that the pendulum oscillation is only mimicing simple harmonic motion when the angle is small
#otherwise the difference between nonlinear and linear pendulum models are significant
#but as the initial angle increases, the difference becomes huge as the assumption that initial angle displacement is independent doesn't hold
#for extra theory and explanation , refer to https://www.acs.psu.edu/drussell/Demos/Pendulum/Pendula.html
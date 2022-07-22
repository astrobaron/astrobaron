import numpy as np
from matplotlib import pyplot as plt
from math import pi
import matplotlib.font_manager as font_manager

u=0.     #x-position of the center
v=0    #y-position of the center
a=np.zeros(5)+1.     #radius on the x-axis
e=np.zeros(5)+[0,0.2,0.4,0.6,0.9]
b=np.sqrt((1-e**2)*a**2)
t = np.linspace(0, 2*pi, 100)
fig = plt.figure(figsize=(10, 10))
plt.plot( u+a[0]*np.cos(t) , v+b[0]*np.sin(t), label="e=0")
plt.plot( u+a[1]*np.cos(t) , v+b[1]*np.sin(t), label="e=0.2")
plt.plot( u+a[2]*np.cos(t) , v+b[2]*np.sin(t), label='e=0.4')
plt.plot( u+a[3]*np.cos(t) , v+b[3]*np.sin(t), label='e=0.6')
plt.plot( u+a[4]*np.cos(t) , v+b[4]*np.sin(t), label='e=0.9')
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=16)
plt.legend(loc="upper left",prop=font)
plt.savefig('/Users/frederiquebaron/OneDrive - Universite de Montreal/siteweb/astrobaron/assets/images/Module3/ellipses.jpg')
plt.close()

foyer=np.sqrt(a**2-b**2)
fig2 = plt.figure(figsize=(10, 6))
plt.plot( u+a[4]*np.cos(t) , v+b[4]*np.sin(t), label='e=0.9')
plt.plot([-foyer[4],foyer[4]],[0,0],'m.', label='Foyer')
plt.xlim(-1.1,1.1)
plt.ylim(-0.75,0.75)
plt.grid(color='grey', linestyle='--', linewidth=0.5,which='major')
plt.savefig('/Users/frederiquebaron/OneDrive - Universite de Montreal/siteweb/astrobaron/assets/images/Module3/1_ellipse.jpg')

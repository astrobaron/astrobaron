import numpy as np
from matplotlib import pyplot as plt


x = np.arange(0, 100, 0.02);

fig = plt.figure(figsize=(100, 10))
plt.plot(x, np.sin(x),linewidth=10)
plt.axis('off'0)
plt.savefig('/Users/frederiquebaron/OneDrive - Universite de Montreal/siteweb/astrobaron/assets/images/Module3/sinus1.jpg')
plt.close()

fig = plt.figure(figsize=(100, 10))
plt.plot(x, np.sin(0.2*x), linewidth=10)
plt.axis('off')
plt.savefig('/Users/frederiquebaron/OneDrive - Universite de Montreal/siteweb/astrobaron/assets/images/Module3/sinus2.jpg')
plt.close()

fig = plt.figure(figsize=(100, 10))
plt.plot(x, np.sin(2*x),linewidth=10)
plt.axis('off')
plt.savefig('/Users/frederiquebaron/OneDrive - Universite de Montreal/siteweb/astrobaron/assets/images/Module3/sinus3.jpg')
plt.close()

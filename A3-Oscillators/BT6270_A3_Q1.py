
import numpy as np
import matplotlib.pyplot as plt
from  scipy.integrate import odeint
t=np.arange(0,20.01,0.01)

def complex_coupled(y,t,phi,w):
    r1,theta1,r2,theta2=y
    r1dot=(1-r1**2)*(r1)+(0.2)*(r2)*(np.cos((theta2)-(theta1)+(phi)))
    theta1dot=w+(0.2)*(r2)*(np.sin((theta2)-(theta1)+(phi)))/r1
    r2dot=(1-r2**2)*(r2)+(0.2)*(r1)*(np.cos((theta2)-(theta1)+(phi)))
    theta2dot=w-(0.2)*(r1)*(np.sin((theta2)-(theta1)+(phi)))/r2
    return [r1dot,theta1dot,r2dot,theta2dot]
y0=[1,(np.pi)/4,1,0]
sol=odeint(complex_coupled,y0,t,args=(98*(np.pi/180),5))
theta1=sol[:,1]
theta2=sol[:,3]
r1=sol[:,0]
r2=sol[:,2]
realz1=[r1[i]*np.cos(theta1[i]) for i in range(len(t))]
imz1=[r1[i]*np.sin(theta1[i]) for i in range(len(t))]
realz2=[r2[i]*np.cos(theta2[i]) for i in range(len(t))]
imz2=[r2[i]*np.sin(theta2[i]) for i in range(len(t))]


phinorm=[(theta1[i]-theta2[i])*(180/np.pi) for i in range(len(t))]

plt.plot(t,phinorm,'r',label='NormalizedPhaseDifference')
plt.xlabel('time')
plt.ylabel('Theta')
plt.legend(loc='best')
plt.show()

plt.plot(t,realz1,'g',label='real(z1)')
plt.plot(t,realz2,'b',label='real(z2)')
plt.xlabel('time')
plt.ylabel('real(Z)')
plt.legend(loc='best')
plt.show()

plt.plot(t,imz1,'g',label='Im(Z1)')
plt.plot(t,imz2,'b',label='Im(Z2)')
plt.xlabel('time')
plt.ylabel('Im(Z)')
plt.legend(loc='best')
plt.show()
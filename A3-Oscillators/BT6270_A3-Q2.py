import numpy as np
import matplotlib.pyplot as plt
from  scipy.integrate import odeint
t=np.arange(0,60.01,0.01)

def power_coupled(y,t,phinorm,w1,w2):
    r1,theta1,r2,theta2=y
    r1dot=(1-r1**2)*(r1)+(0.2)*((r2)**(w1/w2))*(np.cos(w1*((theta2/w2)-(theta1/w1)+(phinorm))))
    theta1dot=w1+(0.2/r1)*((r2)**(w1/w2))*(np.sin(w1*((theta2/w2)-(theta1/w1)+(phinorm))))
    r2dot=(1-r2**2)*(r2)+(0.2)*(r1)**(w2/w1)*(np.cos(w2*((theta2/w2)-(theta1/w1)+(phinorm))))
    theta2dot=w2-(0.2/r1)*((r1)**(w2/w1))*(np.sin(w2*((theta2/w2)-(theta1/w1)+(phinorm))))
    return [r1dot,theta1dot,r2dot,theta2dot]
y0=[1,2*(np.pi),1,0]
sol=odeint(power_coupled,y0,t,args=((-47)*(np.pi/180),5,15))
theta1=sol[:,1]
theta2=sol[:,3]
r1=sol[:,0]
r2=sol[:,2]
realz1=[r1[i]*np.cos(theta1[i]) for i in range(len(t))]
imz1=[r1[i]*np.sin(theta1[i]) for i in range(len(t))]
realz2=[r2[i]*np.cos(theta2[i]) for i in range(len(t))]
imz2=[r2[i]*np.sin(theta2[i]) for i in range(len(t))]


phinorm=[(theta1[i]/5-theta2[i]/15)*(180/np.pi) for i in range(len(t))]
plt.plot(t,phinorm,'r',label='NormalizedPhaseDifference')
#plt.plot(t,y1,'b',label='Theta1')
#plt.plot(t,y2,'g',label='Thet21')


plt.xlabel('time')
plt.ylabel('Theta')
plt.legend(loc='best')
plt.show()

plt.plot(t[:3000],realz1[:3000],'g',label='Real(z1)')
plt.plot(t[:3000],realz2[:3000],'b',label='Real(z2)')
plt.xlabel('time')
plt.ylabel('Real(Z)')
plt.legend(loc='best')
plt.show()

plt.plot(t[:3000],imz1[:3000],'g',label='Imag(z1)')
plt.plot(t[:3000],imz2[:3000],'b',label='Imag(z2)')
plt.xlabel('time')
plt.ylabel('Imag(Z)')
plt.legend(loc='best')
plt.show()

plt.plot(t[-3000:],realz1[-3000:],'g',label='Real(z1)')
plt.plot(t[-3000:],realz2[-3000:],'b',label='Real(z2)')
plt.xlabel('time')
plt.ylabel('Real(Z)')
plt.legend(loc='best')
plt.show()

plt.plot(t[-3000:],imz1[-3000:],'g',label='Imag(z1)')
plt.plot(t[-3000:],imz2[-3000:],'b',label='Imag(z2)')
plt.xlabel('time')
plt.ylabel('Imag(Z)')
plt.legend(loc='best')
plt.show()



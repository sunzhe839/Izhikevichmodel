'''
Created on Jul 8, 2014

This is my method
The diffrerence with professor's model is the order of (V1-V2) or (V2-V1)
In this program, we simulate the chatting behaviour


July 26
Now I add the synaptic delay

Aug 4

Now I add the Spike-timing-dependent plasticity
from the paper Competitive Hebbian learning through spike-timing-dependent synaptic plasticity
By sen song


@author: sun
'''
from IzhikevichClass_r3 import Izhike
import numpy as np
from matplotlib import pyplot as plt

def STDPupdater(preT,postT):
    '''
    preT presnaptic spike time
    postT postsnaptic spike time
    SdeltT  the difference of presnaptic spike time and postT postsnaptic spike time
    '''
    SdeltT=postT-preT
    Aplus=0.005
    Aminus=1.05*Aplus
    tauPlus=0.20
    tauMinus=0.20
    if SdeltT >0:
        deltW=Aplus*np.exp(SdeltT/tauPlus)
    else:
        deltW=(-Aminus)*np.exp((-SdeltT)/tauMinus)
    return deltW


NN=2
TotalTime=1000  # total Time
deltT=0.25 #0.25ms one step
#TotalSteps=np.arange(0,TotalTime+deltT,deltT)
#chattering =Izhike(0.1,0.2,-65,2.0)#simulate a Chattering neurons 

a0=0.02
b0=0.2
c0=-50
d0=2.0
ri=np.random.uniform(0,1)
#ri=0.0
a=a0+0.08*ri
b=b0-0.05*ri
chattering1 =Izhike(a,b,c0,d0)
ri=np.random.uniform(0,1)
#ri=0.1
a=a0+0.08*ri
b=b0-0.05*ri
chattering2 =Izhike(a,b,c0,d0)

#chattering neurons can fire stereotypical bursts of closely space spikes.
#I=5*np.random.randn()
chattering2.I=8
#I=5
#print I
TotalSteps=np.arange(0,TotalTime,deltT)
#print TotalSteps
v0=-65
u0=0.2*v0
w=[0.5,0.5] #w[0] is the weght of A neuron to B, w[1] is the weight of B to A
Vsignal=np.zeros((NN,1))
Usignal=np.zeros((NN,1))
SynapticSpike=np.zeros((NN,0))
#print SynapticSpike
Vsignal[0,0]=v0
Usignal[0,0]=u0
chattering1.v=v0
chattering1.u=u0
chattering2.v=-10
chattering2.u=0.2*(-10)
#SynapticSpike=[]
#SynapticSpike=[]


for ts in TotalSteps[1:]:
    #print ts
    #chattering.v=Vsignal[-1]
    #chattering.u=Usignal[-1]
    #print chattering.v
    if ts>=1 and ts<=100:
    #if ts==1:
        I=5
    else :
        I=(Vsignal[1,-1]-Vsignal[0,-1])*w[1]
        
    chattering1.v,chattering1.u=chattering1.model(deltT,I=8)
    #print chattering1.u
    Vsignal=np.insert(Vsignal,Vsignal.shape[1],chattering1.v,axis=1)
    #insert the v value after the last index of the numpy array
    Usignal=np.insert(Usignal,Usignal.shape[1],chattering1.u,axis=1)
    print w[1]
    I2=-(Vsignal[1,-2]-Vsignal[0,-2])*w[0]  #electrical potential difference 
    #print chattering2.I
    print I2
    chattering2.v,chattering2.u=chattering2.model(deltT,I2)
    Vsignal[1,-1]=chattering2.v
    Usignal[1,-1]=chattering2.u
#print Vsignal.shape,TotalSteps.shape
plt.plot(TotalSteps,Vsignal[0,])
plt.plot(TotalSteps,Vsignal[1,])
plt.show()

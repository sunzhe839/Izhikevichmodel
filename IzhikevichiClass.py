'''
Created on Jul 8, 2014
This a Izhikevh neuron model class
@author: sun
'''
import numpy as np


class Izhike():
    '''
    classdocs
    '''


    def __init__(self, a, b, c, d):
        '''
        Constructor
        '''
        
        #print ri
        #self.a = a+0.08*ri
        #self.b = b-0.05*ri
        self.a = a
        self.b = b
        self.c = c
        self.d = d    
        self.v=0
        self.u=0
        self.I=0
    

    def model(self,dt,I):
        #VSignal=[]#membrane potential of the neuron
        #USignal=[]#membrane recovery variable
        #tmpv=self.v
        #tmpu=self.u
        self.I=I
        self.v+=(dt/2.)*(0.04*(self.v**2) + 5*self.v + 140 - self.u+self.I)
        self.v+=(dt/2.)*(0.04*(self.v**2) + 5*self.v + 140 - self.u+self.I)
        self.u+=dt*(self.a*(self.b*self.v-self.u))
        if self.v>=30:
            self.v=self.c
            self.u=self.u+self.d
        #print self.v
        #VSignal.append(self.v)
        #USignal.append(self.u)
        return self.v,self.u

                
        
            
        
        
        

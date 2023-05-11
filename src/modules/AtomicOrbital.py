# coding: UTF-8
# This is created 2023/05/11 by Y. Shinohara
# This is lastly modified YYYY/MMD/DD by Y. Shinohara
import sys
from modules.constants import *
import numpy as np
import matplotlib.pyplot as plt
class AtomicOrbital:
    """Description for AtomicOrbital class
    Class for defining atomic orbitals
    """
    def __init__(self):
        self.var1 = None #A template for the variable

    @classmethod
    # Get 2pz orbital for spatial cordinate `r`
    def get_2pz(self, r, Rc, Z, epsilon = 1.0e-8):
        """Description for get_2pz function
        r is an array of three-dimensional vector for spatial grid index
        Rc is a three-dimensional vector to specify atomic position in real-space
        Z is effective nuclear charge, non-integral number is allowed
        epsilon is just introduced to avoid zero-division
        """
        rad = np.sqrt((r[:,0] - Rc[0])**2+(r[:,1] - Rc[1])**2+(r[:,2] - Rc[2])**2 + epsilon**2)
        costheta = (r[:,2] - Rc[2])/rad[:]
        phi = Z*rad*costheta*np.exp(-0.5*Z*rad)*np.sqrt(Z**3/2.0**5/pi)
        return phi
    @classmethod
    # Get 1s orbital for spatial cordinate `r`
    def get_1s(self, r, Rc, Z, epsilon = 1.0e-8):
        """Description for get_1s function
        r is an array of three-dimensional vector for spatial grid index
        Rc is a three-dimensional vector to specify atomic position in real-space
        Z is effective nuclear charge, non-integral number is allowed
        epsilon is just introduced to avoid zero-division
        """
        rad = np.sqrt((r[:,0] - Rc[0])**2+(r[:,1] - Rc[1])**2+(r[:,2] - Rc[2])**2 + epsilon**2)
        costheta = (r[:,2] - Rc[2])/rad[:]
        phi = np.exp(-Z*rad)*np.sqrt(Z**3/pi)
        return phi
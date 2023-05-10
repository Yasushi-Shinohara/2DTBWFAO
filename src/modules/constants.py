# coding: UTF-8
import numpy as np
#Mathematicl constants
pi  = np.pi
tpi = 2.0*np.pi
fpi = 4.0*np.pi
zI  = 1.0j
#Physical constants
#https://ja.wikipedia.org/wiki/%E5%8E%9F%E5%AD%90%E5%8D%98%E4%BD%8D%E7%B3%BB
Bohr2nm = 0.0529177210903 #nanometer
Hartree2eV = 27.211386245988 #eV
Atomtime2fs = 0.024188843265857 #fs
Atomfield2Vpnm = Hartree2eV/Bohr2nm #V/nm
Atomvolume2nmcubic = Bohr2nm**3 #nm^3
#https://ja.wikipedia.org/wiki/%E5%BE%AE%E7%B4%B0%E6%A7%8B%E9%80%A0%E5%AE%9A%E6%95%B0
sol = 137.035999084 #speed of light
ch2eVnm = 1241.5 #eV * nm
chbar2eVnm = 197.3 # eV * nm
halfepsc2Wpcm2 = 3.509e16 # W/cm^2 \frac{1}{2}*\epsilon_0 * c
Atomfluence2Jpcm2 = halfepsc2Wpcm2*Atomtime2fs*1.0e-15 # J/cm^2 ,W/cm^2 * fs = femto J/cm^2
#Well-known quantities
##Pauli matrices
#sigmax = np.matrix([[0.0,  1.0] , [1.0 ,  0.0]],dtype='complex128')
#sigmay = np.matrix([[0.0, -1.0j], [1.0j,  0.0]],dtype='complex128')
#sigmaz = np.matrix([[1.0,  0.0] , [0.0 , -1.0]],dtype='complex128')
sigmax = np.array([[0.0,  1.0] , [1.0 ,  0.0]],dtype='complex128')
sigmay = np.array([[0.0, -1.0j], [1.0j,  0.0]],dtype='complex128')
sigmaz = np.array([[1.0,  0.0] , [0.0 , -1.0]],dtype='complex128')
#
aB = Bohr2nm
Hartree = Hartree2eV #fs
Atomtime = Atomtime2fs #fs
Atomfield = Atomfield2Vpnm #V/nm
Atomvolume = Atomvolume2nmcubic
ch = ch2eVnm #eV * nm
chbar = chbar2eVnm # eV * nm
halfepsc = halfepsc2Wpcm2 # W/cm^2 \frac{1}{2}*\epsilon_0 * c
Atomfluence = Atomfluence2Jpcm2 # J/cm^2 ,W/cm^2 * fs = femto J/cm^2

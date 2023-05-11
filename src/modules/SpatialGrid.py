# coding: UTF-8
# This is created 2023/05/11 by Y. Shinohara
# This is lastly modified YYYY/MMD/DD by Y. Shinohara
import sys
from modules.constants import *
import numpy as np
import matplotlib.pyplot as plt
class SpatialGrid:
    """Description for SpatialGrid class
    Class for defining grids for real-space, reciprocal-space grids.
    r-grid: real space grid for general and fine grids in a cell 
    R-grid: real space grid for different cell
    G-grid: reciprocal grid for reciprocal lattices
    k-grid: reciprocal grid for first-Brillouin zone
    """
    def __init__(self):
        self.var1 = None #A template for the variable

    @classmethod
    # Generate 3D spatial cordinate 
    def get_rgrid(self, Nx, Ny, Nz, Lx, Ly, Lz):
        """Description for get_rgrid function
        Lx, Ly, Lz are sizes of spatial box along x,y, and z axes.
        `r` is generated in a box [(-Lx/2, Lx/2), (-Ly/2, Ly/2), (-Lz/2, Lz/2)], namely the center of box is placed in the origin (0,0,0)
        Nx, Ny, Nz are number of spatial uniform grid along x,y, and z zxes
        """
        dx = Lx/Nx #x-grid size
        dy = Ly/Ny #y-grid size
        dz = Lz/Nz #z-grid size
        dV = dx*dy*dz #Volume of the discretized box
        V = Lx*Ly*Lz #Volume
        r = np.zeros([Nx*Ny*Nz,3],dtype = "float64")
        n = 0
        for ix in range(Nx):
            for iy in range(Ny):
                for iz in range(Nz):
                    r[n, 0] = -Lx/2.0 + ix*dx
                    r[n, 1] = -Ly/2.0 + iy*dy
                    r[n, 2] = -Lz/2.0 + iz*dz
                    n += 1
        return r, dV, V

    @classmethod
    # Generate 2D spatial cordinate 
    def get_2Drgrid(self, Nx, Ny, Lx, Ly):
        """Description for get_2Drgrid function
        Lx and Ly are sizes of spatial box along x and y axes.
        `r` is generated in a box [(-Lx/2, Lx/2), (-Ly/2, Ly/2)], namely the center of box is placed in the origin (0,0)
        Nx, Ny are number of spatial uniform grid along x and y zxes
        """
        dx = Lx/Nx #x-grid size
        dy = Ly/Ny #y-grid size
        dS = dx*dy #Surface of the discretized box
        S = Lx*Ly #Volume
        r = np.zeros([Nx*Ny,2],dtype = "float64")
        n = 0
        for ix in range(Nx):
            for iy in range(Ny):
                r[n, 0] = -Lx/2.0 + ix*dx
                r[n, 1] = -Ly/2.0 + iy*dy
                n += 1
        return r, dS, S

    @classmethod
    # Generate 1D spatial cordinate 
    def get_1Drgrid(self, Nx, Lx):
        """Description for get_1Drgrid function
        Lx is sizes of spatial box.
        `r` is generated in a box [(-Lx/2, Lx/2)], namely the center of box is placed in the origin (0,0)
        Nx is number of spatial uniform grid.
        """
        dx = Lx/Nx #x-grid size
        r = np.zeros([Nx,1],dtype = "float64")
        n = 0
        for ix in range(Nx):
            r[n, 0] = -Lx/2.0 + ix*dx
            n += 1
        return r, dx, Lx
#
    @classmethod
    # Generate spatial cordinate in the Honeycomb cell
    def get_rgrid_Honeycomb(self, N1, N2, Nz, Lz, a=4.6485):
        """Description for get_rgrid_Honeycomb function
        Lz is the size of spatial box z axis.
        `r` is generated in the primitive cell
        N1, N2, Nz are number of spatial uniform grid along a1, a2, and z zxes
        """
        a1 = a*np.array([np.sqrt(3.0)/2.0, -1.0/2.0])
        a2 = a*np.array([np.sqrt(3.0)/2.0, +1.0/2.0])
        b1 = (tpi/a)*np.array([1.0/np.sqrt(3.0), -1.0])
        b2 = (tpi/a)*np.array([1.0/np.sqrt(3.0), +1.0])
        dz = Lz/Nz #z-grid size
        S = a1[0]*a2[1] - a1[1]*a2[0]
        V = S*Lz #Volume
        dS = S/(N1*N2) #Surface of the discretized box
        dV = V/(N1*N2*Nz) #Volume of the discretized box
        r = np.zeros([N1*N2*Nz,3],dtype = "float64")
        n = 0
        for i1 in range(N1):
            for i2 in range(N2):
                for iz in range(Nz):
                    r[n, 0] = i1/N1*a1[0] + i2/N2*a2[0]
                    r[n, 1] = i1/N1*a1[1] + i2/N2*a2[1]
                    r[n, 2] = -Lz/2.0 + iz*dz
                    n += 1
        return r, dV, V, a1, a2, b1, b2
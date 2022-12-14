import numpy as np
import numpy.ctypeslib as ctl
import matplotlib.pyplot as plt
import ctypes
import os.path

lib_name = "ciclibfn.so"
libabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + lib_name
fn = ctypes.CDLL(libabspath)

fn.getR.argtypes = [ctypes.c_float]
fn.getR.restype = ctypes.c_float

fn.scale.argtypes = [ctypes.c_float]
fn.scale.restype = ctypes.c_float

def drawCircles(dict):
    prop=dict['data']
    mx = max(prop)
    ar = []
    for i in range(0,len(prop),1):
        ar.append( (prop[i]/mx)*100 )
    theta = np.linspace( 0 , 2 * np.pi , 100 )
    figure, axes = plt.subplots( 1 )
    for i in range(0,len(ar),1):
        radius = fn.getR(ar[i])
        a = (radius * np.cos( theta ) - fn.scale(radius) )
        b = (radius * np.sin( theta ) - fn.scale(radius) )
        try:
            dict['color']
        except KeyError:
            axes.fill( a, b )
        else:
            axes.fill( a, b, dict['color'][i])
    axes.set_aspect( 1 )
    try:
        dict['title']
    except KeyError:
        dict["title"] = "add title"
    plt.title( dict["title"] )
    plt.show()


import numpy as np

//mds = matriz de senos e cossenos

int c = input("cosseno: ")
int s = input("seno: ")
int E = input("E: ")
int A = input("A: ")
int l = input("l: ")

int mds = np.array([[c**2, c*s, -(c**2), -(c*s)],
                    [c*s, s**2, -(c*s), -(s**2)],
                    [-(c**2), -(c*s), c**2, c*s],
                    [-(c*s), -(s**2), c*s, s**2]])



//matriz de rigidez
def mdr(E, A, l, mds):
    int constante = (E*A)/l
    mdr = constante * mds
    return mdr

//matriz de incidencia
def mdi():
    //montar matriz de incidencia dinamicamente

//matriz de rigidez global
def mrg(mdi):

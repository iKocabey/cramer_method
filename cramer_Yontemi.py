#algoritnmanın bulunduğu sayfa : 364
import numpy as np


def detA(a11,a12,a13,a21,a22,a23,a31,a32,a33):
    MA=np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
    print("A matrisi = \n ",MA)
    deta=np.linalg.det(MA)
    
    return deta

def detAi(b11,a12,a13,b21,a22,a23,b31,a32,a33):
    MAi=np.array([[b11,a12,a13],[b21,a22,a23],[b31,a32,a33]])
    print("Ai matrisi = \n",MAi)
    detai=np.linalg.det(MAi)
    return detai

def detAj(a11,b12,a13,a21,b22,a23,a31,b32,a33):
    MAj=np.array([[a11,b12,a13],[a21,b22,a23],[a31,b32,a33]])
    print("Aj matrisi = \n",MAj)
    detaj=np.linalg.det(MAj)
    return detaj

def detAk(a11,a12,b13,a21,a22,b23,a31,a32,b33):
    MAk=np.array([[a11,a12,b13],[a21,a22,b23],[a31,a32,b33]])
    print("Ak matrisi = \n ",MAk)
    detak=np.linalg.det(MAk)
    return detak


a=detA(1,-1,1,1,1,-1,2,-1,-1)
ai=detAi(4,-1,1,-2,1,-1,1,-1,-1)
aj=detAj(1,4,1,1,-2,-1,2,1,-1)
ak=detAk(1,-1,4,1,1,-2,2,-1,1)

print(a)
print(ai)
print(aj)
print(ak)

print("X1 = ",ai/a)
print("X2 = ",aj/a)
print("X3 = ",ak/a)




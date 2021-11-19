import numpy as np
import copy

def ReflexiveAndAntireflexiveRel(r,n):
    c1=[]
    c0=[]
    for i in range(n):
        for j in range(n):
            if i==j:
                if r[i][j]==1:
                    c1.append(True)
                    c0.append(False)
                elif r[i][j]==0:
                    c0.append(True)
                    c1.append(False)
        if all(c1):
            return f'Reflexive relation'
        elif all(c0):
            return f'Antireflexive relation'
        else:
            return f'Neither reflexive nor antireflexive relation'

def SymmetricRel(r,n):
    cSym = []
    for i in range(n):
        for j in range(n):
            if r[i][j]==r[j][i]:
                cSym.append(True)
            else: 
                cSym.append(False)
    if all(cSym):
        return f'Symmetric relation'
    else:
        return f'Not symmetric relation'

def AsymmetricAndAntisymmetricRel(r,n):
    c1=[]
    c2=[]
    for i in range(n):
        for j in range(n):
            if min(r[i][j],r[j][i])==0:
                c1.append(True)
            elif min(r[i][j],r[j][i])!=0:
                c1.append(False)
            elif i!=j:
                if min(r[i][j],r[j][i])==0:
                    c2.append(True)  
                else:
                    c2.append(False)      
    if all(c1):
        return f'Asymmetric relation'
    elif all(c2):
        return f'Antisymmetric relation'
    else:
        return f'Neither asymmetric nor antisymmetric relation'

def maxMinCompositionForR(r):
    z = []
    for i in r:
        for j in r.T:
            z.append(max(np.minimum(i, j)))
    return np.array(z).reshape((r.shape[0], r.shape[1]))

def minMaxCompositionForR(r):
    z = []
    for i in r:
        for j in r.T:
            z.append(min(np.maximum(i, j)))
    return np.array(z).reshape((r.shape[0], r.shape[1]))

def maxMultCompositionForR(r):
    z = []
    for i in r:
        for j in r.T:
            z.append(max(np.multiply(i, j)))
    return np.array(z).reshape((r.shape[0], r.shape[1]))


def TransitiveRel(r,n):
    r_arr = (copy.deepcopy(r)).tolist()
    maxmin = maxMinCompositionForR(r_arr)
    minmax = minMaxCompositionForR(r_arr)
    maxmult = maxMultCompositionForR(r_arr)
    
    for i in range(n):
        for j in range(n):
            if maxmin[i][j]<=r_arr[i][j]:
                return f"Transitive rel (maxmin)"
            elif minmax[i][j]<=r_arr[i][j]:
                return f"Transitive rel (minmax)"
            elif maxmult[i][j]<=r_arr[i][j]:
                return f"Transitive rel (maxmult)"


    

def fuzzyUnion(r1,r2,n):
    z = []
    r1_arr = (copy.deepcopy(r1)).tolist()
    r2_arr = (copy.deepcopy(r2)).tolist()
    for i in range(n):
        for j in range(n):
            z.append(max(r1_arr[i][j], r2_arr[i][j]))

    return np.array(z).reshape(5,5)

def fuzzyIntersec(r1,r2,n):
    z = []
    r1_arr = (copy.deepcopy(r1)).tolist()
    r2_arr = (copy.deepcopy(r2)).tolist()
    for i in range(n):
        for j in range(n):
            z.append(min(r1_arr[i][j], r2_arr[i][j]))

    return np.array(z).reshape(5,5)

def fuzzyDifference(r1,r2,n):
    z = []
    r1_arr = (copy.deepcopy(r1)).tolist()
    r2_arr = (copy.deepcopy(r2)).tolist()
    for i in range(n):
        for j in range(n):
            z.append(max(r1_arr[i][j]- r2_arr[i][j],0))

    return np.array(z).reshape(5,5)

def fuzzyInverse(r1,r2,n):
    r1_arr = (copy.deepcopy(r1)).tolist()
    r2_arr = (copy.deepcopy(r2)).tolist()
    for i in range(n):
        for j in range(n):
            r1_arr[i][j], r1_arr[j][i] = r1_arr[j][i], r1_arr[i][j]
            r2_arr[i][j], r2_arr[j][i] = r2_arr[j][i], r2_arr[i][j]
    return f"Inverse R1: {np.array(r1_arr).reshape(5,5)}\n Inverse R2: {np.array(r2_arr).reshape(5,5)}"

def fuzzyComplement(r1,r2,n):
    z1 = []
    z2 = []
    r1_arr = (copy.deepcopy(r1)).tolist()
    r2_arr = (copy.deepcopy(r2)).tolist()
    for i in range(n):
        for j in range(n):
            z1.append(1 - r1_arr[i][j])
            z2.append(1 - r2_arr[i][j])

    return f"Complement R1: {np.array(z1).reshape(5,5)}\n Complement R2: {np.array(z1).reshape(5,5)}"

def maxMinComposition(r1,r2):
    z = []
    for i in r1:
        for j in r2.T:
            z.append(max(np.minimum(i, j)))
    return np.array(z).reshape((r1.shape[0], r2.shape[1]))

def minMaxComposition(r1,r2):
    z = []
    for i in r1:
        for j in r2.T:
            z.append(min(np.maximum(i, j)))
    return np.array(z).reshape((r1.shape[0], r2.shape[1]))

def maxMultComposition(r1,r2):
    z = []
    for i in r1:
        for j in r2.T:
            z.append(max(np.multiply(i, j)))
    return np.array(z).reshape((r1.shape[0], r2.shape[1]))

def main():
    r1 = np.array([[1,0.3,0.8,0.5,1],[0.6,1,0.7,0.3,0.7],[0.6,0,1,0.9,0.1],[0.3,1,0.6,1,0.4],[0.2,0,0.1,0.1,1]])
    r2 =  np.array([[1,0,1,0,0.6],[1,1,0.9,0.4,1],[0,0.7,1,0,0.7],[0.3,0.3,0,1,0.7],[1,0.9,0.8,0.3,1]])
    n = len(r1)
    print(f"maxmin: {maxMinComposition(r1,r2)}")
    print(f"minmax: {minMaxComposition(r1,r2)}")
    print(f"maxmult: {maxMultComposition(r1,r2)}")
    print(f"fuzzyUnion: {fuzzyUnion(r1,r2,n)}")
    print(f"fuzzyIntersec: {fuzzyIntersec(r1,r2,n)}")



if __name__=='__main__':
    main()

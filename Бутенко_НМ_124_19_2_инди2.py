import numpy as np
import copy

n = int(input("SIZE: "))
r = [[int(input(f"R[{i}][{j}]: ")) for i in range(n)]  for j in range(n)]

def ReflexiveAndAntireflexiveRel(r):
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

def SymmetricRel(r):
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


def AsymmetricAndAntisymmetricRel(r):
    c1=[]
    c2=[]
    for i in range(n):
        for j in range(n):
            if r[i][j]*r[j][i]==0:
                c1.append(True)
            elif r[i][j]*r[j][i]!=0:
                c1.append(False)
            elif i!=j:
                if r[i][j]*r[j][i]==0:
                    c2.append(True)  
                else:
                    c2.append(False)      
    if all(c1):
        return f'Asymmetric relation'
    elif all(c2):
        return f'Antisymmetric relation'
    else:
        return f'Neither asymmetric nor antisymmetric relation'

def TransitiveRel(r):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if not r[i][j]:
                continue
            for k in range(n):
                if k==i or k ==j:
                    continue
                if r[j][k]==0:
                    continue
                if r[i][k]==0:
                    return f'Not transitive relation'
    return f'Transitive relation'    

def strictRel(r):
    rs = np.transpose(copy.deepcopy(r))
    for i in range(n):
        for j in range(n):
            if  i==j:
                rs[i][j]=0
            elif rs[i][j]==rs[j][i]:
                rs[i][j]= rs[j][i] = 0
            elif rs[i][j]==rs[j][i]:
                rs[i][j], rs[j][i] = rs[j][i], rs[i][j]
                           
    return rs

zeroM = [[0 for i in range(n)]  for j in range(n)]
oneM = [[1 for i in range(n)]  for j in range(n)]

def min(r): 
    minX = []
    for i, col in enumerate(zip(*strictRel(r))):
        if len(set(col)) == 1:
            minX.append(f'x{i+1}')
    return f'min: {minX}'

def max(r):
    maxX=[]
    for i in range(n):
        if np.array_equal(strictRel(r)[i],zeroM[i]):
            maxX.append(f'x{i+1}')
    return f'max: {maxX}'

def greatest(r):
    gr = []
    for i in range(n):
        for j in range(n):
            continue
        if np.array_equal(r[i],oneM[j]):
           gr.append(f'x{i+1}')
    return f'The greatest: {gr}'

def least(r):
    lt=[]
    for i, col in enumerate(zip(*r)):
        if len(set(col)) == 1:
            lt.append(f'x{i+1}')
    return f'The least {lt}'

def invertibleMatrix(r):
    ri = copy.deepcopy(r)
    for i in range(n):
        for j in range(n):
            if ri[i][j]==1:
                ri[i][j]=0
            else:
                ri[i][j]=1
    return f'Invertible rel matrix {ri}'
def complementRel(r):
    rc = r
    for i in range(n):
        for j in range(n):
            if i < j:
                    rc[i][j],rc[j][i] = rc[j][i],rc[i][j]
    return f'Complement rel matrix {rc}'            

def main():
    print(ReflexiveAndAntireflexiveRel(r))
    print(SymmetricRel(r))
    print(AsymmetricAndAntisymmetricRel(r))
    print(TransitiveRel(r))
    print(greatest(r))
    print(least(r))
    print(min(r))
    print(max(r))
    print(f"Matrix: {r}")
    print(invertibleMatrix(r))
    print(complementRel(r))
    print(strictRel(r))

if __name__ == '__main__':
        
    main()
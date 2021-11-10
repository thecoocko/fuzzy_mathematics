import numpy as np
import copy as c

n = int(input("SIZE: "))
r_1 = [[float(input(f"R1[{i}][{j}]: ")) for i in range(n)]  for j in range(n)]
r_2 = [[float(input(f"R2[{i}][{j}]: ")) for i in range(n)]  for j in range(n)]

lambda1 = float(input(f"lambda1: "))
lambda2 = float(input(f"lambda2: "))

def intersectionOfInitialRelations(r1,r2):
    r1 = c.deepcopy(r_1)
    r2 = c.deepcopy(r_2)
    intersection = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            r1[i][j] = round(lambda1*r1[i][j],3)
            r2[i][j] = round(lambda2*r2[i][j],3)
    for i in range(n):
        for j in range(n):
            intersection[i][j] = round(float(min(r1[i][j],r2[i][j])),3)
    return intersection           

def additiveConvolutionOfRelations(r1,r2):
    r2 = c.deepcopy(r_2)
    for i in range(n):
        for j in range(n):
            r2[i][j] = round(lambda1*r1[i][j] + lambda2*r2[i][j],3)
    return r2

def strictRelQ1(q1):
    for i in range(n):
        for j in range(n):
            if  i==j:
                q1[i][j]=0
            elif q1[i][j]>q1[j][i]:
                q1[i][j],q1[j][i] = round(q1[i][j],3) - q1[j][i], 0
            elif q1[i][j]<q1[j][i]:
                q1[j][i],q1[i][j] = round(q1[j][i]-q1[i][j],3), 0              
    return q1     

def strictRelQ2(q2):
    for i in range(n):
        for j in range(n):
            if  i==j:
                q2[i][j]=0
            elif q2[i][j]>q2[j][i]:
                q2[i][j],q2[j][i] = round(q2[i][j] - q2[j][i],3), 0
            elif q2[i][j]<q2[j][i]:
                q2[j][i],q2[i][j] = round(q2[j][i]-q2[i][j],3), 0  

    return q2

def nonDomAltQ1(strictQ1):
    return 1 - np.max(strictQ1,axis=0)

def nonDomAltQ2(strictQ2):
    return 1 - np.max(strictQ2,axis=0)

def sourceSet(nonDom1, nonDom2):
    minSet = []
    for i in range(len(nonDom1)):
        if nonDom1[i]>nonDom2[i]:
            minSet.append(round(nonDom2[i],3))
        else:
            minSet.append(round(nonDom1[i],3))
    return minSet


def main():
    print(f"Q1 Strict: {strictRelQ1(intersectionOfInitialRelations(r_1,r_2))}")
    print(f"Q2 Strict: {strictRelQ2(additiveConvolutionOfRelations(r_1,r_2))}")
    print(f"Non dominated alt1: {nonDomAltQ1(strictRelQ1(intersectionOfInitialRelations(r_1,r_2)))}")
    print(f"Non dominated alt2: {nonDomAltQ2(strictRelQ2(additiveConvolutionOfRelations(r_1,r_2)))}")
    print(f"The original set of non-dominant alternatives: {sourceSet(nonDomAltQ1(strictRelQ1(intersectionOfInitialRelations(r_1,r_2))),nonDomAltQ2(strictRelQ2(additiveConvolutionOfRelations(r_1,r_2))))}")
    print(f"Rational choice: {np.max(sourceSet(nonDomAltQ1(strictRelQ1(intersectionOfInitialRelations(r_1,r_2))),nonDomAltQ2(strictRelQ2(additiveConvolutionOfRelations(r_1,r_2)))))}")

if __name__=="__main__":
    main()
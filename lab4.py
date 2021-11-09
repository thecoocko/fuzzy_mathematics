import numpy as np
import copy as c

n = 3#int(input("SIZE: "))
r1 = [[1,0.5,0.3],[0,1,0.8],[1,0.5,1]]#[[1,0.3,0.8,0.5,1],[0.6,1,0.7,0.3,0.7],[0.6,1,0.7,0.3,0.7],[0.6,0,1,0.9,0.1],[0.3,1,0.6,1,0.4],[0.2,0,0.1,0.1,1]]#[[float(input(f"R1[{i}][{j}]: ")) for i in range(n)]  for j in range(n)]
r2 = [[1,0.1,0],[0.3,1,1],[1,0.5,1]]#[[1,0,1,0,0.6],[1,1,0.9,0.4,1],[0,0.7,1,0,0.7],[0.5,0.3,0,1,0.7],[1,0.9,0.8,0.3,1]]#[[float(input(f"R2[{i}][{j}]: ")) for i in range(n)]  for j in range(n)]
r1_1 = c.deepcopy(r1)
r2_1 = c.deepcopy(r2)


lambda1 = 0.33#float(input(f"lambda1: "))
lambda2 = 0.67#float(input(f"lambda2: "))
print(f"r1 {r1}")
print(f"r2 {r2}")
print(f"r1_1 {r1_1}")
print(f"r2_1 {r2_1}")

q1Strict = [[0 for i in range(n)] for j in range(n)]
q2Strict = [[0 for i in range(n)] for j in range(n)]

intersection1 = [[0 for i in range(n)] for j in range(n)]
q2 = [[0 for i in range(n)] for j in range(n)]

nonDomAltQ1 = []
nonDomAltQ2 = []

for i in range(n):
    for j in range(n):
        r1_1[i][j] = round(lambda1*r1_1[i][j],3)
        r2_1[i][j] = round(lambda2*r2_1[i][j],3)
print(f"after lambda r1_1 {r1_1}")
print(f"after lambda r2_1 {r2_1}")
for i in range(n):
    for j in range(n):
        intersection1[i][j] = round(float(min(r1_1[i][j],r2_1[i][j])),3)#norm
        q2[i][j] = round(lambda1*r1[i][j] + lambda2*r2[i][j],3)#norm

print(f"Intersection: {intersection1}")
print(f"Q2: {q2}")

intersection1 = np.transpose(intersection1)
q2 = np.transpose(q2)

# def strictRel(r):
#     rs = np.transpose(copy.deepcopy(r))
#     for i in range(n):
#         for j in range(n):
#             if  i==j:
#                 rs[i][j]=0
#             elif rs[i][j]==rs[j][i]:
#                 rs[i][j]= rs[j][i] = 0
#             elif rs[i][j]==rs[j][i]:
#                 rs[i][j], rs[j][i] = rs[j][i], rs[i][j]
                           
#     return rs

for i in range(n):
    for j in range(n):
        if i==j:
            q2[i][j] = 0
            intersection1 = 0
        else:
            if intersection1[i][j] == intersection1[j][i]:
                intersection1[i][j],intersection1[j][i]=0
            elif q2[i][j] == q2[j][i]:
                q2[i][j],q2[j][i]=0
            intersection1[i][j],intersection1[j][i] = intersection1[j][i], intersection1[i][j]
            q2[i][j],q2[j][i] = q2[j][i], q2[i][j]
            
            

print(f"Q1 Strict: {q1Strict}")
print(f"Q2 Strict: {q2Strict}")

for i in range(n):
    for j in range(n):
        q1Strict[i][j] = (intersection1[i][j] - q1Strict[i][j]) if (intersection1[i][j] - q1Strict[i][j]) < 0 else 0
        q2Strict[i][j] = (q2[i][j]-q2Strict[i][j]) if (q2[i][j]-q2Strict[i][j]) < 0 else 0
    

for i in range(n):
    for j in range(n):
        continue
    nonDomAltQ1.append(1 - np.max(q1Strict[i][j], axis = 0))
    nonDomAltQ2.append(1 - np.max(q2Strict[i][j], axis = 0))

print(f"A subset of non-dominant alternatives Q1: {nonDomAltQ1}")
print(f"A subset of non-dominant alternatives Q2: {nonDomAltQ2}")

nonDomAlt = []
for i in range(n):
    nonDomAlt.append(min(nonDomAltQ1[i],nonDomAltQ2[i]))

print(f"A subset of non-dominant alternatives: {nonDomAlt}")
print(f"Rational choice of alternatives: {np.max(nonDomAlt)}")
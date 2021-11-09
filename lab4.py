import numpy as np
import copy as c

n = int(input("SIZE: "))
r1 = [[float(input(f"R1[{i}][{j}]: ")) for i in range(n)]  for j in range(n)]
r2 = [[float(input(f"R2[{i}][{j}]: ")) for i in range(n)]  for j in range(n)]
r1_1 = c.deepcopy(r1)
r2_1 = c.deepcopy(r2)


lambda1 = float(input(f"lambda1: "))
lambda2 = float(input(f"lambda2: "))

q1Strict = [[0 for i in range(n)] for j in range(n)]
q2Strict = [[0 for i in range(n)] for j in range(n)]

intersection1 = [[0 for i in range(n)] for j in range(n)]
q2 = [[0 for i in range(n)] for j in range(n)]

nonDomAltQ1 = []
nonDomAltQ2 = []

for i in range(n):
    for j in range(n):
        r1_1[i][j] = lambda1*r1_1[i][j]
        r2_1[i][j] = lambda2*r2_1[i][j]

for i in range(n):
    for j in range(n):
        intersection1[i][j] = float(min(r1_1[i][j],r2_1[i][j]))
        q2[i][j] = lambda1*r1[i][j] + lambda2*r2[i][j]

print(f"Intersection: {intersection1}")
print(f"Q2: {q2}")

for i in range(n):
    for j in range(n):
        if i==j:
            q1Strict[i][j] = 0
            q2Strict[i][j] = 0
            
        else:
            q1Strict[i][j], q1Strict[j][i] = intersection1[j][i], intersection1[i][j]
            q2Strict[i][j], q2Strict[j][i] = q2[j][i], q2[i][j]
            

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
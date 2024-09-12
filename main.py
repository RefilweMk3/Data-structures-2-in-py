t1=()
t2=("Hey",[5,10,15],(2,4,6))

print(t2[2])
print(t2[1])
print(t2[2][1])

t3=("R","e","f","i","l","w","e")
for i in t3:
    print(i)

r1={10,15,20,15,10,20,30}
print(r1)

r2={1,2,3,4,5,6,7}
print(r1.intersection(r2))
print("TU",r1.union(r2))
print("Diff",r1.difference(r2))
print("Sym difference",r1.symmetric_difference(r2))
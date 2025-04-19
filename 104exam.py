n=int(input("taper un nombre:"))
max=n
min=n
posmax=1
posmin=1
som=0
i=2
while i<=5:
    n=int(input("taper un nombre:"))
    if n>max:
        max=n
        posmax=i
    elif n<min:
        min=n
        posmin=1
    som +n
    i += 1
print(f"le maximum est:{max} sa position : {posmax}")
print(f"le maximum est:{min} sa position : {posmin}")
Moy=som/5
print(f"la moyenne est: {Moy:.2f}")
T1=float(input("Enter wall temperature T1: "))
T2=float(input("Enter wall temperature T2: "))
L=float(input("Enter thickness of the slab: "))
A=float(input("Enter cross sectional area of the slab: "))
k=float(input("Enter thermal conductivity of the material: "))
f=open("output.txt","w",encoding="utf-8")
f.write("\tx\t\tTemp\n")
x=0
while x<=L:
    T=T1+(T2-T1)*x/L
    text=[str(x),"\t\t",str(T),"\n"]
    f.writelines(text)
    x+=0.2
q=k*A*(T1-T2)/L
z=["Heat transfer rate is \n",str(q)]
f.writelines(z)
f.close()






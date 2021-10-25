import math
z=1
s = open("output2.txt", "w", encoding="utf-8")
while z>0:
    enter=input("do you want to run the program? ")
    if enter=="y":
        obj=int(input("select the shape of the object:(1 for plane wall,2 for hollow cylinder,3 for hollow sphere):\n"))

        if obj==1:
            T1=float(input("Enter wall temperature t1: \n"))
            T2=float(input("Enter wall temperature t2: \n"))
            L=float(input("Enter the thickness of the slab: "))
            A=float(input("Enter the cross sectional area of the slab: \n"))
            k=float(input("Enter the thermal conductivity of the material: \n"))
            s.write("\tx\t\tTemp\n")
            x=0
            while x<=L:
                T=T1+(T2-T1)*x/L
                ar=[str(x),"\t\t",str(T),"\n"]
                s.writelines(ar)
                x+=0.2
        #code for heat transfer rate
            q=k*A*(T1-T2)/L
            arr=["Heat transfer rate is : ",str(q),"\n"]
            s.writelines(arr)
            continue
        elif obj==2:
            T1=float(input("Enter inner wall temperature: "))
            T2=float(input("Enter outer wall temperature: "))
            r1=float(input("Enter inner radius: "))
            r2=float(input("Enter outer radius: "))
            L=float(input("Enter the length of the cylinder: "))
            k=float(input("Enter thermal conductivity of material: "))
            s.write("\tr\t\tTemp\n")
            r=r1
            while r<=r2:
                d=r/r2
                c=r1/r2
                T=T2+((T1-T2)*math.log10(d))/math.log10(c)
                ar=[str(r),"\t\t",str(T),"\n"]
                s.writelines(ar)
                r+=0.5
        #code for heat transfer rate
            e = r2 / r1
            q=2*3.14*L*k*(T1-T2)/math.log10(e)
            arr=["Heat transfer rate is \n",str(q)]
            s.writelines(arr)
            continue
        elif obj==3:
            T1=float(input("Enter inner wall temperature: "))
            T2=float(input("Enter outer wall temperature: "))
            r1=float(input("Enter inner radius of the sphere: "))
            r2=float(input("Enter outer radius of the sphere: "))
            k=float(input("Enter thermal conductivity of the material: "))
            s.write("\n\tr\t\tTemp\n")
            r=r1
            while r<=r2:
                T=T1+((T1-T2)*((1/r1)-(1/r))/((1/r2)-1/r1))
                ar=[str(r),"\t\t",str(T),"\n"]
                s.writelines(ar)
                r+=0.5
        #code for heat transfer rate
            q = 4 * 3.14 * k * (T1 - T2) / ((1 / r1) - (1 / r2))
            arr=["Heat transfer rate is: ",str(q)]
            s.writelines(arr)
            continue
        else:
            print("wrong choice. ")
            continue
    else:
        break
s.close()




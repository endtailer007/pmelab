import math
l=float(input("Enter the length of the connecting rod: "))
r=float(input("Enter the radius of the crank: "))
N=float(input("Enter the speed of the crank in rpm: "))
w=(2*math.pi*N)/60
n=l/r
dis=open("displacement.txt","w")
vel=open("velocity.txt","w")
acc=open("acceleration.txt","w")
ax=open("angulardisp.txt","w")
av=open("angularvel.txt","w")
aa=open("angularacc.txt","w")
aa.write("\nangularacceleration\t\tcrankangle\n")
av.write("\nangularvelocity\t\tcrankangle\n")
ax.write("\nangulardisplacement\t\tcrankangle\n")
acc.write("\nacceleration\t\tcrankangle\n")
vel.write("\nvelocity\t\tcrankangle\n")
dis.write("\ndisplacement\t\tcrankangle\n")
for i in range(0,37):
    ang=i*10
    rad=(ang*math.pi)/180
    root=(pow(n,2)-pow(math.sin(rad),2))
    x=r*(1-math.cos(rad)+n-math.sqrt(root))
    d=[str(x),"\t\t",str(ang),"\n"]
    dis.writelines(d)
    v=r*w*(math.sin(rad)+math.sin(2*rad)/(2*math.sqrt(root)))
    ve=[str(v),"\t\t",str(ang),"\n"]
    vel.writelines(ve)
    a=r*pow(w,2)*(math.cos(rad)+math.cos(2*rad)/(2*math.sqrt(root)))
    ac=[str(a),"\t\t",str(ang),"\n"]
    acc.writelines(ac)
    ax1=math.asin(math.sin(rad)/n)
    axx=[str(ax1),"\t\t",str(ang),"\n"]
    ax.writelines(axx)
    av1=w*math.cos(rad)/math.sqrt(root)
    avv=[str(av1),"\t\t",str(ang),"\n"]
    av.writelines(avv)
    aa1=-w*w*(pow(n,2)-1)*math.sin(rad)/pow(root,1.5)
    aaa=[str(aa1),"\t\t",str(ang),"\n"]
    aa.writelines(aaa)
dis.close()
vel.close()
acc.close()
ax.close()
av.close()
aa.close()




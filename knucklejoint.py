import math
D=float(input("Enter diameter of the rod(in meters): "))
d=float(input("Enter diameter of knuckle pin(in meters): "))
#DESIGN CRITERIA FOR KNUCKLE JOINT
D1=1.1*D#ENLARGED DIAMETER OF EACH ROD
d0=2*d#OUTSIDE DIAMETER OF EYE OR FORK
a=0.75*D#THICKNESS OF EACH EYE OF FORK
b=1.25*D#THICKNESS OF EYE END OF ROD-B
d1=1.5*d#DIAMETER OF PIN
P=float(input("Enter the force : "))
kn=open("knuckle.txt","w")
#fcalculation of tensile failure of rods
tf=P/((math.pi/4)*pow(D,2))
f=["The given rod fails when tensile stress of ",str(tf),"N/m^2 is exerted\n"]
kn.writelines(f)
#fcalculation of shear failure of pin
tow=P/(2*(math.pi/4)*pow(d,2))
to=["The pin fails when shear stress of magnitude",str(tow),"is exerted.\n"]
kn.writelines(to)
#calculation of crushing falilure of pin in eye
cfe=P/(b*d)
cf=["Crushing failure stress of pin in eye is ",str(cfe),"N/m^2\n"]
kn.writelines(cf)
#calculation of crushing failure of pin in fork
cff=P/(2*a*d)
c=["Crushing failure stress of pin in fork is ",str(cff),"N/m^2\n"]
kn.writelines(c)
#calculation of tensile failure of eye
tfe=P/(b*(d0-d))
ef=["Given eye will fail when a tensile stress of ",str(tfe),"N/m^2 is exerted\n"]
kn.writelines(ef)
#calculation of shear failure of eye
sfe=P/(b*(d0-d))
fe=["Given eye will fail when a shear stress of magnitude",str(sfe),"is exerted.\n"]
kn.writelines(fe)
#calculation of tensile failure of fork
tff=P/(2*a*(d0-d))
tfff=["Given fork will fail when a tensile stress of ",str(tff),"N/m^2 is exerted.\n"]
kn.writelines(tfff)
#calculation of shear failure of fork
sff=P/(2*a*(d0-d))
sfff=["Given fork will fail when a shear stress of magnitude",str(sff),"is exerted\n"]
kn.writelines(sfff)
kn.close()




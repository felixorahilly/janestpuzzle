from numpy import random
import math
#this code will not find you the right answer to 10 decimal places without running billions of simulations. it can however, be used to verify an answer is in the right ballpark prior to submission.
i=0
x=[]
def distfinder()-> int: #generates points r and b and returns 1 if there exists an equidistant point on the blue line, 0 otherwise
    r=[] #creating matrices r and b with random numbers to represent co-ordinates of red dot and blue dot
    b=[]
    ran=10000 #range of co-ordinates to sample from. by default set to 10000
    r.append(random.randint(ran))
    r.append(random.randint(ran))
    b.append(random.randint(ran))
    b.append(random.randint(ran))

    z1=ran-b[0]#z1 and z1 are the inverses of blue dots x and y co-ords.
    z2=ran-b[1]
    side=""
    if min(b[0],b[1],z1,z2)==b[0]: #determines the closest side of the square to blue dot
        side="left"
    elif min(b[0],b[1],z1,z2)==b[1]:
        side="bot"
    elif min(b[0],b[1],z1,z2)==z1:
        side="right"
    elif min(b[0],b[1],z1,z2)==z2:
        side="top"
    if side=="left":
        rmindist=r[0] #find minimum distance from r to the blue line
        borth=max(b[1],ran-b[1]) #find the y(orthogonal) component of the max distance from b to the blue line
        bmaxdist=math.sqrt(((b[0]*b[0])+(borth*borth))) #calculate max distance from b to blue line (hypotenuse)
        bmindist=b[0] #find the x component of the max distance from b to the blue line
        rorth=max(r[1],ran-r[1]) #find the y(orthogonal) component of the max distance from r to the blue line
        rmaxdist=math.sqrt(((r[0]*r[0])+(rorth*rorth)))
        if r[0]<b[0] and rmaxdist>bmindist: #here we leverage the fact that a point on the blue line equidistant to r and b can only exist in one of two cases:
            return 1                              #either b is closer to the wall than r and the max distance from b to the wall is greater than the min distance from a to the wall, or vice versa.
        elif b[0]<r[0] and bmaxdist>rmindist:
            return 1
        else:
            return 0

    elif side=="right": #repeat the same method for all sides of the square
        rmindist=ran-r[0]
        g=ran-b[0]
        borth=max(b[1],ran-b[1])
        bmaxdist=math.sqrt(((g*g)+(borth*borth)))
        bmindist=ran-b[0]
        rorth=max(r[1],ran-r[1])
        h=ran-r[0]
        rmaxdist=math.sqrt(((h*h)+(rorth*rorth)))
        if r[0]>b[0] and rmaxdist>bmindist:
            return 1
        elif b[0]>r[0] and bmaxdist>rmindist:
            return 1
        else:
            return 0
    elif side=="bot":
        rmindist=r[1]
        borth=max(b[0],ran-b[0])
        bmaxdist=math.sqrt(((b[1]*b[1])+(borth*borth)))
        bmindist=b[1]
        rorth=max(r[0],ran-r[0])
        rmaxdist=math.sqrt(((r[1]*r[1])+(rorth*rorth)))
        if r[1]<b[1] and rmaxdist>bmindist:
            return 1
        elif b[1]<r[1] and bmaxdist>rmindist:
            return 1
        else:
            return 0
    elif side=="top":
        rmindist=ran-r[1]
        g=ran-b[1]
        borth=max(b[0],ran-b[0])
        bmaxdist=math.sqrt(((g*g)+(borth*borth)))
        bmindist=ran-b[1]
        rorth=max(r[0],ran-r[0])
        h=ran-r[1]
        rmaxdist=math.sqrt(((h*h)+(rorth*rorth)))
        if r[1]>b[1] and rmaxdist>bmindist:
            return 1
        elif b[1]>r[1] and bmaxdist>rmindist:
            return 1
        else:
            return 0
while i<10000: #run the function 10000 times to approximate the probability
    x.append(distfinder())
    i+=1
print(sum(x)/10000)

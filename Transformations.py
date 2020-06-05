# IP HOMEWORK-4
# NAME: Deepi Garg
# ROLL NO.: 2018389
# SECTION: B
# GROUP: 6

import ast
import math
import matplotlib as mplib
import matplotlib.pyplot as plt
plt.ion()


def non_lin_trans(mat,x,y,disc=False):
        """This function defines multiplication for an input matrix and 2 lists of coordinates
        """
        outx = ''
        outy = ''
        xli = []
        yli = []
        for i in range(len(x)):
                xel = round((mat[0][0]*x[i]),4) + round((mat[0][1]*y[i]),4) + (mat[0][2])
                yel = round((mat[1][0]*x[i]),4) + round((mat[1][1]*y[i]),4) + (mat[1][2])
                one = (mat[2][0]*x[i]) + (mat[2][1]*y[i]) + (mat[2][2])
                xli.append(xel)
                yli.append(yel)
                outx = outx + ' ' + str(xel)
                outy = outy + ' ' + str(yel)
        if disc==False:
                print(outx)
                print(outy)
                return xli, yli

        #for a disc, we need to calculate the center and radii
        else:
                cenx = xli[0]
                ceny = yli[0]
		
                radx = ((xli[1]-cenx)**2) + ((yli[1]-ceny)**2)
                rady = ((xli[2]-cenx)**2) + ((yli[2]-ceny)**2)
	
                print(cenx,ceny,(radx**(1/2)),(rady**(1/2)))
                return xli,yli


shape = input()
if shape == 'polygon':
	xl = list(map(float,input().split()))
	yl = list(map(float,input().split()))
        
        #to close the figure, we append the first coordinate in the end
	xlp = xl + [xl[0]]
	ylp = yl + [yl[0]]
	plt.plot(xlp,ylp)
	#plt.show()
        
	com=input()
	while(com != 'quit'):
		comm = com.split()
		if comm[0]=='S':
			xl,yl = non_lin_trans( [[float(comm[1]),0,0],[0,float(comm[2]),0],[0,0,1]], xl, yl )
			xlp = xl + [xl[0]]
			ylp = yl + [yl[0]]
			plt.clf()
			plt.plot(xlp,ylp)
			#plt.show()
        
		elif comm[0]=='R':			
			ang=math.radians(float(comm[1]))
			xl,yl = non_lin_trans( [[math.cos(ang),-(math.sin(ang)),0],[math.sin(ang),math.cos(ang),0],[0,0,1]], xl, yl )
			xlp = xl + [xl[0]]
			ylp = yl + [yl[0]]
			plt.clf()
			plt.plot(xlp,ylp)
			#plt.show()
        
		elif comm[0]=='T':
			xl,yl = non_lin_trans( [ [ 1, 0, float(comm[1]) ] , [ 0, 1, float(comm[2]) ] , [0, 0, 1] ], xl, yl)
			xlp = xl+[xl[0]]
			ylp = yl+[yl[0]]
			plt.clf()
			plt.plot(xlp,ylp)
			#plt.show()
        
		else:
			exit()
		com=input()

	
elif shape == 'disc':
        
	abr = list(map(float,input().split()))
	abr.append(abr[2])

	# in the new lists, 1st coordinate is of the center, 2nd of an end of major axis and 3rd an end of minor axis
	xlp = [abr[0],abr[0]+abr[2],abr[0]]
	ylp = [abr[1],abr[1],abr[1]+abr[3]]

	# getting 360 coordinates of the ellipse using the parametric form for plotting 
	for i in range(360):
		ang = math.radians(i)
		xlp.append( (abr[2]*math.cos(ang))+abr[0] )
		ylp.append( (abr[2]*math.sin(ang))+abr[1] )
		
	xlp1 = xlp[3:]+[xlp[3]]
	ylp1 = ylp[3:]+[ylp[3]]
	
	plt.clf()
	plt.plot(xlp1,ylp1)
	#plt.show()
	
	command = input()
	while(command!='quit'):
		comm = command.split()
		if comm[0]=='S':
			xlp,ylp = non_lin_trans( [[float(comm[1]),0,0],[0,float(comm[2]),0],[0,0,1]], xlp, ylp, True)

			xlp1=xlp[3:]+[xlp[3]]
			ylp1=ylp[3:]+[ylp[3]]
			plt.clf()
			plt.plot(xlp1,ylp1)
			#plt.show()
			
		elif comm[0]=='R':			
			ang=math.radians(float(comm[1]))
			xlp,ylp= non_lin_trans( [[math.cos(ang),-(math.sin(ang)),0],[math.sin(ang),math.cos(ang),0],[0,0,1]], xlp, ylp, True )
			xlp1=xlp[3:]+[xlp[3]]
			ylp1=ylp[3:]+[ylp[3]]
			plt.clf()
			plt.plot(xlp1,ylp1)
			#plt.show()
			
		elif comm[0]=='T':
			xlp,ylp= non_lin_trans( [ [ 1, 0, float(comm[1]) ] , [ 0, 1, float(comm[2]) ] , [0, 0, 1] ], xlp, ylp, True)
			
			xlp1=xlp[3:]+[xlp[3]]
			ylp1=ylp[3:]+[ylp[3]]
			plt.clf()
			plt.plot(xlp1,ylp1)
			#plt.show()

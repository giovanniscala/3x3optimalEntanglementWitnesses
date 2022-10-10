import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

X,Y = np.meshgrid(np.linspace(0,1,401),np.linspace(0,1,401))

def area(a,b,c):
	def inter(d,e):
		f = 3 - a - b - c - d - e
		L1 = a+d < 1;	L2 = a+e < 1;	L3 = a+f < 1
		####################
		C1 = (c+d)*(b+d)-(a+e)**2;	C2 = (c+d)*(b+d)-(a+f)**2
		S1 = (a+e-1)*(a+f-1);
		Z1 = ((b+d)*(c+d))**.5+S1**.5 - 1;	Z1[S1<0]=0;	Z1[Z1<0] = 0; Z1[Z1!=0]=1;
		Z1[L1] = 0; Z1[L2] = 0; Z1[L3] = 0; Z1[f<0] = 0
		####################
		C3 = (c+e)*(b+e)-(a+f)**2;	C4 = (c+e)*(b+e)-(a+d)**2
		S2 = (a+f-1)*(a+d-1);
		Z2 = ((b+e)*(c+e))**.5+S2**.5 - 1;  Z2[S2<0]=0;	Z2[Z2<0] = 0; Z2[Z2!=0]=1;
		Z2[L1] = 0; Z2[L2] = 0; Z2[L3] = 0; Z2[f<0] = 0
		####################
		C5 = (c+f)*(b+f)-(a+d)**2;	C6 = (c+f)*(b+f)-(a+e)**2
		S3 = (a+d-1)*(a+e-1)
		Z3 = ((b+f)*(c+f))**.5+S3**.5 - 1;	Z3[S3<0]=0;	Z3[C5>0]=1; Z3[C6>0]=1;	Z3[Z3<0] = 0; Z3[Z3!=0]=1;
		Z3[L1] = 0; Z3[L2] = 0; Z3[L3] = 0; Z3[f<0] = 0
		####################
		ga = 3 - (a+b+c)
		be = (d-e)**2+(e-f)**2+(f-d)**2
		r = (a-b)*(3*b+ga)+(a-c)*(3*c+ga)
		ka = (a-ga-2*b-2*c)**2+3*(b-c)**2
		H = r + ka - ((r+ka)**2-r**2)**.5 - be; H[H<0]=0; H[H!=0]=1
		return Z1+Z2+Z3+1.5**3*H
	return inter

fig, ax = plt.subplots()
ai = 1; bi = 0; ci = 0
cont = ax.contourf(X,Y, area(ai,bi,ci)(X,Y))
#bord = [ax.contour(i,[0]) for i in borders(ai,bi,ci)(X,Y)]
#ell1 = ax.contour(elli1(ai,bi,ci)(X,Y),[0])
fig.subplots_adjust(left=0.25, bottom=0.3)
ax.set_title(f'a = {ai:.2f}, b = {bi:.2f}',y=1.0, pad=-14)
a_slider = Slider(ax = fig.add_axes([0.25, 0.2, 0.65, 0.03]), label='a', valmin=0, valmax=2, valinit=ai)
b_slider = Slider(ax = fig.add_axes([0.25, 0.15, 0.65, 0.03]), label='b', valmin=0, valmax=2, valinit=bi)
c_slider = Slider(ax = fig.add_axes([0.25, 0.1, 0.65, 0.03]), label='c', valmin=0, valmax=2, valinit=ci)

def update(val):
	global cont
	global bord
	a = a_slider.val
	b = b_slider.val
	c = c_slider.val
	for co in cont.collections:
		co.remove()
	cont = ax.contourf(X,Y, area(a,b,c)(X,Y))
	ax.set_title(f'a = {a_slider.val:.2f}, b = {b_slider.val:.2f}, c = {c_slider.val:.2f}')
	fig.canvas.draw_idle()

a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)
plt.show()


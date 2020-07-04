import cv2
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
# import glob as g 
import os
# import numpy as np 
mk=Tk()
mk.title('Image Editor')
mk.iconbitmap('edi.ico')
c=ImageTk.PhotoImage(Image.open('cam.png').resize((200,200)))


def save():
	global im
	s=filedialog.asksaveasfilename(defaultextension='*.jpg',filetypes=(('Jpeg file','*.jpg'),('Png file','*.png')))
	# print(s)
	if len(s)>5:
		im.save(s)
def gray():
	global i1,lf2,ii,im
	if ii>30:
		im=im.convert(('L'))
		# im=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
		# print(im)
		# gi=im[:,:, ::-1].copy()
	else:
		im=i1.convert(('L'))
		# i1=np.array(i1)
		# print(im)
		# gi=i1[:,:, ::-1].copy()
	# gray=cv2.cvtColor(gi,cv2.COLOR_BGR2GRAY)
	gray=ImageTk.PhotoImage(im)
	lf2.grid_forget()	
	lf2=Label(f2,image=gray)
	lf2.p=gray
	lf2.grid(row=1,column=7,padx=2,pady=2,columnspan=6)
	b=Button(text='Save',command=lambda : save())
	b.grid(row=3,padx=15,pady=15,column=7,columnspan=6)
def canny():
	global i1,lf2,ii,im
	if ii>30:
		im=im.convert(('P'))
	else:
		im=i1.convert(('P'))
	canny=ImageTk.PhotoImage(im)
	lf2.grid_forget()	
	lf2=Label(f2,image=canny)
	lf2.p=canny
	lf2.grid(row=1,column=7,padx=2,pady=2,columnspan=6)
	b=Button(text='Save',command=lambda : save())
	b.grid(row=3,column=7,columnspan=6,padx=15,pady=15)
def rotate(i):
	global i1,f2,lf2,b6,im,ii
	m=i1.copy()
	m1=m.rotate(90+i)
	mm=ImageTk.PhotoImage(m1)
	lf2.grid_forget()	
	lf2=Label(f2,image=mm)
	lf2.p=mm
	lf2.grid(row=1,column=7,padx=2,pady=2,columnspan=6)
	i=i+90
	ii=i
	im=m1
	b6.config(command=lambda : rotate(i))
	b=Button(text='Save',command=lambda : save())
	b.grid(row=3,column=7,columnspan=6,padx=15,pady=15)

def back():
	global l1,f1,i1,ii
	global b1
	global b2
	global index
	ii=0
	i1=Image.open(m1[index-1]).resize((400,400))
	img=ImageTk.PhotoImage(i1)
	# global index
	l1.grid_forget()
	l1=Label(f1,image=img)
	l1.p=img
	l1.grid(row=1,column=0,padx=2,pady=2,columnspan=6)
	index=index-1
	# b1.configure(command=lambda :back())
	b2.config(command=lambda :forward(),state='active')
	# if i==0:
		# b1.config(state='disabled')

	

def forward():
	global b2
	global b1
	global l1,f1,i1,ii
	global index
	ii=0
	i1=Image.open(m1[index+1]).resize((400,400))
	img=ImageTk.PhotoImage(i1)
	# global index
	l1.grid_forget()
	l1=Label(f1,image=img)
	l1.p=img
	l1.grid(row=1,column=0,padx=2,pady=2,columnspan=6)
	index=index+1
	# b2.configure(command=lambda :forward())
	# b1.configure(command=lambda :back())
	# print(index)
	if index>len(m1)-2:
		b2.config(state='disabled')


def open():
	global mv,ii
	mv=filedialog.askdirectory()
	# print(mv)
	ii=0
	if len(mv)>5:
		v=filedialog.askopenfilename(initialdir=mv,title='Select File',filetypes=(('All files','*.*'),('png files','*.png'),('jpeg files','*.jpg')))
	# global b2
		# print(v)
	# global b1
	# global l2
	# global l1
	# w=cv2.imread(m.v)
	# w1=cv2.cvtColor(w,cv2.COLOR_BGR2RGB)
	# w2=Image.fromarray(w1).resize((700,400))

	# b2.configure(command=lambda :forward(1),state='active')
	# b1.configure(command=lambda :back(1),state='active')
	# l1=Label(m,text=v)
	# l1.grid(row=0,columnspan=3,column=0)
		if len(v)>5:
			global b3,b1,b2,b4,b5,b6
			global l,l1,f1,i1,f2,lf2
			global index
			global m1
			m1=[]
			for i,j,k in os.walk(mv):
				for m in k:
					if '.jpg' in m:
						m1.append(i+'/'+m)
					if '.png' in m:
						m1.append(i+'/'+m)
					if '.JPG' in m:
						m1.append(i+'/'+m)
			# m1=g.glob(m.v+'*.jpg')
			# m2=g.glob(m.v+'*.png')
			# m1.extend(m2)
			# print(m1)
			# print(len(m1))
			# print(m.v)
			i=Image.open(v)
			i1=i.resize((400,400))
			# i1=i.convert('RGB')
			index=m1.index(v)
			# print(index)
			# print(type(i))
			# print(i.size)
			# w,h=i.size
			# if w>3500:
			# 	i=i.resize((w//10,h//10))
			# if w<2000 and w>1200:
			# 	i=i.resize((w//4,h//4))
			# print(i.size)
			v1=ImageTk.PhotoImage(i1)
			b3.pack_forget()
			l.pack_forget()
			mk.config(bg='gray')
			f1=Frame(mk,borderwidth=3,width=450,height=450,padx=3,bg='white').grid(row=1,columnspan=6,padx=25,column=0)
			# f3=Frame(mk,borderwidth=5,width=1100,height=50,padx=3,bg='ghostwhite').grid(row=3,columnspan=12,padx=50,pady=3)
			f2=Frame(mk,borderwidth=3,width=450,height=450,padx=3,bg='white').grid(row=1,column=7,columnspan=6,padx=25)
			lf2=Label(f2,text="Output Area",font=('Ariel Bold',30))
			lf2.grid(row=1,column=8,columnspan=4)
			l1=Label(f1,image=v1)
			l1.p=v1
			l1.grid(row=1,column=0,padx=2,pady=2,columnspan=6)
			b=Button(text="New Image",command= lambda : open()).grid(row=0,ipadx=15,columnspan=13,pady=10)
			b5=Button(text='Gray',command=lambda : gray())
			b5.grid(row=3,column=1,ipadx=10,padx=15,pady=15)
			b4=Button(text='Canny',command=lambda : canny()).grid(row=3,column=2,ipadx=10,padx=15,pady=15)
			b6=Button(text="Rotate",command=lambda : rotate(0))
			b6.grid(row=3,column=3,ipadx=10,padx=15,pady=15)
			b1=Button(text="<<",command=lambda : back())
			b1.grid(row=3,column=0,ipadx=15,padx=19,pady=15)
			b2=Button(text=">>",command=lambda :forward())
			b2.grid(row=3,column=4,ipadx=15,padx=19,pady=15)
			
	# l2=Label(m,image=v1)
	# l2.grid(row=1,column=0,columnspan=3)
# b1=Button(m,text='<<',command=lambda : back(),state='disabled')
# b1.grid(row=3,column=0,columnspan=1)
# b=Button(m,text='Exit',command=m.quit).grid(row=3,column=1,columnspan=1)
# b2=Button(m,text='>>',command=lambda : forward(0),state='disabled')
# b2.grid(row=3,column=2,columnspan=1)
mk.geometry('1000x600')

b3=Button(mk,image=c,command=open,relief='flat')
b3.pack(pady=10)
l=Label(mk,text='Open Image',font=('Ariel Bold',30))
l.pack()


mainloop()
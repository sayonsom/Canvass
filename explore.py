from Tkinter import *

canvas_width = 500
canvas_height = 500

yvalues = list()

def paint( event ):
   python_green = "#000"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )
   jj = 500-event.y
   #a,b=getYAxisScales()
   #diff = a-b
   yvalues.append(jj)


def saveLoadProfile():
    print yvalues
    print len(yvalues)




master = Tk()
master.title( "Create a load profile" )

b = Button(master, text="See Load Profile", command=saveLoadProfile)
b.pack(expand=1, fill=X)

maxy = Entry(master)
maxy.pack()

miny = Entry(master)
miny.pack()

def getYAxisScales():
    #print maxy.get()
    #print miny.get()
    try:
        return int(maxy.get()), int(miny.get())
    except:
        return 100,0

b2 = Button(master, text="Set Y Axis Scales", command=getYAxisScales)
b2.pack(expand=1, fill=Y)



w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.create_line(30, 0, 30, canvas_height, fill="#476042")
w.create_line(30, canvas_height-40, canvas_width, canvas_height-40, fill="#476042")
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )

mainloop()

for i in range(len(yvalues)):
    yvalues[i] = 2

print yvalues

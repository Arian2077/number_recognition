from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab
import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import random as rnd

color=0
num1=0
num2=0

class Draw():
    def __init__(self,root):

#Defining title and Size of the Tkinter Window GUI
        self.root =root
        self.root.state("zoomed") #maximize
        self.root.title("Copy Assignment Painter")
#         self.root.geometry("810x530")
        self.root.configure(background="white")
        self.root.resizable(False,False)
#         self.root.resizable(0,0)
 
#variables for pointer and Eraser
        self.pointer="white"
        self.erase="white"

#Widgets for Tkinter Window
# Welcome sign with a simple Label
        label=Label(root, text="Write a number and see the result!", font=('Arial', 50), fg=rnd.choice(["Blue","red","green","purple"]))
        label.place(x=250,y=5)

        
      

# Reset Button to clear the entire screen 
        self.clear_screen= Button(self.root,text="Clear Screen",bd=4,bg='white',command= lambda :[self.background.delete('all'),self.background2.delete('all')] ,width=20,height=2,relief=RIDGE)
        self.clear_screen.place(x=705,y=260)

# Save Button for saving the image in local computer
       
        self.save_btn= Button(self.root,text="PREDICT 1",bd=4,bg='white',command=self.predict,width=20,height=2,relief=RIDGE)
        self.save_btn.place(x=705,y=360)  
       
        
        self.save_btn2= Button(self.root,text="PREDICT 2",bd=4,bg='white',command=self.predict2,width=20,height=2,relief=RIDGE)
        self.save_btn2.place(x=705,y=460)

        
        # Change Brush color -------------------------------------

        self.selecting_color= Button(self.root,text="Change Brush Color",bd=4,bg='white',command=self.select_color,width=20,height=2,relief=RIDGE)
        self.selecting_color.place(x=705,y=160)
    
        # Four main operations -------------------------------------
        
        self.plus_btn= Button(self.root,text="plus",bd=4,bg='white',command=self.plus_btn,width=20,height=2,relief=RIDGE)
        self.plus_btn.place(x=150,y=660)
        
        self.minus_btn= Button(self.root,text="minus",bd=4,bg='white',command=self.minus_btn,width=20,height=2,relief=RIDGE)
        self.minus_btn.place(x=550,y=660)
       
        self.multipl_btn= Button(self.root,text="multplied",bd=4,bg='white',command=self.multipl_btn,width=20,height=2,relief=RIDGE)
        self.multipl_btn.place(x=900,y=660)
       
        self.divid_btn= Button(self.root,text="divided",bd=4,bg='white',command=self.divid_btn,width=20,height=2,relief=RIDGE)
        self.divid_btn.place(x=1240,y=660)
        
        
        # self.selecting_color= Button(self.root,text="Change Color",bd=4,bg='white',command=self.select_color,width=20,height=2,relief=RIDGE)
        self.selecting_color.place(x=705,y=160)
        
        self.selecting_color= Button(self.root,text="Change Color",bd=4,bg='white',command=self.select_color,width=20,height=2,relief=RIDGE)
        # self.selecting_color.place(x=705,y=160)
        
        self.selecting_color= Button(self.root,text="Change Color",bd=4,bg='white',command=self.select_color,width=20,height=2,relief=RIDGE)
        # self.selecting_color.place(x=705,y=160)
        
        
#Defining a background color for the Canvas 
        self.background = Canvas(self.root,bg='black',bd=5,relief=GROOVE,height=470,width=500)
        self.background.place(x=150,y=100)
        
        ##
        
        self.background2 = Canvas(self.root,bg='black',bd=6,relief=GROOVE,height=470,width=500)
        self.background2.place(x=900,y=100)
####

#Bind the background Canvas with mouse click
        self.background.bind("<B1-Motion>",self.paint)
        
        self.background2.bind("<B1-Motion>",self.paint2) 
        
        self.LblP = Label(text="predict 1= ",font=("Arial",25),bg="#66FF00")
        self.LblP.place(x=330,y=600)
       
        self.LblP2 = Label(text="predict 2= ",font=("Arial",25),bg="red")
        self.LblP2.place(x=1080,y=600)
        
        self.LblP3 = Label(text="pluse = ",font=("Arial",25),bg="#66FF00")
        self.LblP3.place(x=150,y=720)
        
        self.LblP4 = Label(text="minus =",font=("Arial",25),bg="#66FF00")
        self.LblP4.place(x=550,y=720)
        
        self.LblP5 = Label(text="divided =",font=("Arial",25),bg="red")
        self.LblP5.place(x=1240,y=720)
        
        self.LblP6 = Label(text="multiplied =",font=("Arial",25),bg="red")
        self.LblP6.place(x=900,y=720)
        
    ################################## training #########################################
        digits=cv2.imread("f:/digits.png",cv2.IMREAD_GRAYSCALE)
        rows=np.vsplit(digits,50)
        cells=[]
        cells2=[]
        for row in rows :
            row_cells=np.hsplit(row,100)
            for cell in row_cells:
                cells.append(cell)
                #all in one column 
                cells2.append(cell.flatten())

        #cells2 is a list and in openCV we need numpy array because it is faster than list
        cells2=np.array(cells2,dtype=np.float32)
        n=np.arange(10)
        targets=np.repeat(n,500)
        
#        self.knn=KNeighborsClassifier(n_neighbors=6,metric='minkowski')
#        self.knn.fit(cells2,targets)
        
        self.knn=cv2.ml.KNearest_create()
        self.knn.train(cells2,cv2.ml.ROW_SAMPLE,targets)
        
        #self.knn2=cv2.ml.KNearest_create()
        #self.knn2.train(cells2,cv2.ml.ROW_SAMPLE,targets)
    #####################################################################################

    def paint(self,event):       
        x1,y1 = (event.x-1), (event.y-1)  
        x2,y2 = (event.x+1), (event.y+1)  

        self.background.create_oval(x1,y1,x2,y2,fill=self.pointer,outline=self.pointer,width=40)
        
    def paint2(self,event):       
        x1,y1 = (event.x-1), (event.y-1)  
        x2,y2 = (event.x+1), (event.y+1)  

        self.background2.create_oval(x1,y1,x2,y2,fill=self.pointer,outline=self.pointer,width=40)

    def select_color(self):
        global color
        lst=["white","#17DEEE","#FFF000","#FF007F","#66FF00"]
        color+=1
        if color >= len(lst):
            color=0
        self.pointer= lst[color]
        self.erase="white"
    def eraser(self):
        pass
    def canvas_color(self):
        pass
    def plus_btn(self):
        global num1,num2
        plus=str(num1+num2)
        self.LblP3.configure(text="plus = "+plus)
        
        
    def minus_btn(self):
        global num1,num2
        plus=str(num1-num2)
        self.LblP4.configure(text="minus = "+plus)
          
        
    def divid_btn(self):
        global num1,num2
        plus=str(num1/num2)
        self.LblP5.configure(text="divided = "+plus)
        
        
    def multipl_btn(self):
        global num1,num2
        plus=str(num1*num2)
        self.LblP6.configure(text="multiplied = "+plus)
          
        
    def predict(self):
        global num1
        ############################## save image ################################
        try:
            # self.background update()
#            file_ss =filedialog.asksaveasfilename(defaultextension='jpg')
            #print(file_ss)
            x=self.root.winfo_rootx() + self.background.winfo_x()
            #print(x, self.background.winfo_x())
            y=self.root.winfo_rooty() + self.background.winfo_y()
            #print(y)

            x1= x + self.background.winfo_width() 
            #print(x1)
            y1= y + self.background.winfo_height()
            #print(y1)
            ImageGrab.grab().crop((x+200, y+200, x1+1000, y1+800)).save("f:/test.png")
            
            
#            messagebox.showinfo('Screenshot Successfully Saved as' + str(file_ss))

        except:
            print("Error in saving the screenshot")
        
        ######################################### predict ##############################
        my_digit=cv2.imread("f:/test.png",cv2.IMREAD_GRAYSCALE)
        my_digit = cv2.resize(my_digit, (20, 20)) 
        ####################
        my_test_flat=[]
        my_test_flat.append(my_digit.flatten())
        my_test_flat=np.array(my_test_flat,dtype=np.float32)
        
        #################
        
        
#        my_predict = self.knn.predict(my_test_flat)
        ret,result,neighbours,dist=self.knn.findNearest(my_test_flat,k=3)
        print(result)
        num1=result
        # print("This is num 1 :",num1)
        self.LblP.configure(text=result)
        #####################
#        cv2.imshow("digits",my_digit)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()
        #####################
        cv2.imshow("rtwo",my_digit)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
    def predict2(self):
        global num2
        try:
            x=self.root.winfo_rootx() + self.background2.winfo_x()
            #print(x, self.background.winfo_x())
            y=self.root.winfo_rooty() + self.background2.winfo_y()
            #print(y)

            x1= x + self.background2.winfo_width() 
            #print(x1)
            y1= y + self.background2.winfo_height()
            #print(y1)
            ImageGrab.grab().crop((x+1600 , y+200, x1+2000, y1+900)).save("f:/test2.png")
        
        except:
            print("Error in saving the screenshot")
            
            
            ######################################### predict ##############################
        my_digit=cv2.imread("f:/test2.png",cv2.IMREAD_GRAYSCALE)
        my_digit = cv2.resize(my_digit, (20, 20)) 
            ####################
        my_test_flat=[]
        my_test_flat.append(my_digit.flatten())
        my_test_flat=np.array(my_test_flat,dtype=np.float32)
            
            #################
            
            
    #        my_predict = self.knn.predict(my_test_flat)
        ret,result,neighbours,dist=self.knn.findNearest(my_test_flat,k=3)
        print(result)
        num2=result
        # print("This is num 2:",len(num2))
        self.LblP2.configure(text=result)
            
        cv2.imshow("rtwo",my_digit)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
###############################################################################################


if __name__ =="__main__":
    root = Tk()
    p= Draw(root)
    root.mainloop()

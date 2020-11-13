# Write your name using graphics.py
# Jeff Milton
# CS1030-5
# 2020-09-09
#Contributors: Jeffrey Milton, Edward Nyamweya, Ryan Mckenna

from graphics import *

def main():
    win = GraphWin("My Name", 900, 500)    
    aRectangle = Rectangle(Point(50,50), Point(200,100))
    aRectangle.setFill("red")
    aRectangle.setOutline("red")
    
    bRectangle = Rectangle(Point(250,50), Point(400,100))
    bRectangle.setFill("red")
    bRectangle.setOutline("red")  
    
    cRectangle = Rectangle(Point(450,50), Point(600,100))
    cRectangle.setFill("red")
    cRectangle.setOutline("red") 
    
    dRectangle = Rectangle(Point(650,50), Point(800,100))
    dRectangle.setFill("red")
    dRectangle.setOutline("red")   
    
    eRectangle = Rectangle(Point(50,250), Point(150,300))
    eRectangle.setFill("red")
    eRectangle.setOutline("red")
    
    fRectangle = Rectangle(Point(250,150), Point(350,200))
    fRectangle.setFill("red")
    fRectangle.setOutline("red")
    
    gRectangle = Rectangle(Point(250,250), Point(400,300))
    gRectangle.setFill("red")
    gRectangle.setOutline("red")    

    hRectangle = Rectangle(Point(450,150), Point(550,200))
    hRectangle.setFill("red")
    hRectangle.setOutline("red")  
    
    iRectangle = Rectangle(Point(650,150), Point(750,200))
    iRectangle.setFill("red")
    iRectangle.setOutline("red") 
    
    jRectangle = Rectangle(Point(100,50), Point(150,300))
    jRectangle.setFill("red")
    jRectangle.setOutline("red")     
    
    kRectangle = Rectangle(Point(250,50), Point(300,300))
    kRectangle.setFill("red")
    kRectangle.setOutline("red")  
    
    lRectangle = Rectangle(Point(450,50), Point(500,300))
    lRectangle.setFill("red")
    lRectangle.setOutline("red") 
    
    mRectangle = Rectangle(Point(650,50), Point(700,300))
    mRectangle.setFill("red")
    mRectangle.setOutline("red")     
    
    nRectangle = Rectangle(Point(50,350), Point(750,400))
    nRectangle.setFill("red")
    nRectangle.setOutline("red")       

    aRectangle.draw(win)
    bRectangle.draw(win)
    cRectangle.draw(win)
    dRectangle.draw(win)
    eRectangle.draw(win)
    fRectangle.draw(win)
    gRectangle.draw(win)
    hRectangle.draw(win)
    iRectangle.draw(win)
    jRectangle.draw(win)
    kRectangle.draw(win)
    lRectangle.draw(win)
    mRectangle.draw(win)
    nRectangle.draw(win)

    
    win.getMouse() # pause for click in window
    win.close()
main()
import tkinter
from graphics import *

class Button:
    """ A button is a labeled rectangle in a window. It is activated or deactivated
    with the activate() and deactivate() methods. The clicked (p) method returns
    true if the button is active and p is inside it. """

def __init__ (self, win, center, width, height, label):
        """creates a rectangualr button, eg:
        qp = Button (myWin, centerPoint, width, height, 'quit')"""
#set attributes here
    
        self.label = Text(label)
        self.label.draw(win)
        width = width/2.0
        height = height/2.0
        center.getX = x
        center.getY = y
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.tmin = y+h, y-h
        p1 = Point(x-w, y-h)
        p2 = Point(x+w, y+h)
        self.square = Square(p1, p2)
        self.square.setFill('blue')
        self.square.draw(win)
        self.deactivate()

def clicked(self, p):
    """returns true if the button active and p is inside"""

#CODE
    return self.active
           

def getLabel(self):
    """returns the label string of the button"""

#CODE
    return self.label.getText()

def activate(self):
    """Sets this button to 'active'"""

#CODE
    self.active = True
    self.label.setFill('green')
    self.square.setWidth(2)

def deactivate (self):
    """Sets this button to 'active'"""
    
    #CODE
    self.active = False
    self.label.setFill('red')
    self.square.setWidth(1)																																																										
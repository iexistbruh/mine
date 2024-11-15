class Rectangle():
    def_init_(self,l,w):
        self.length = 1
        self.width = w
    
    def rectangle_area(self):
        return self.length*self.width
    
newRectangle = Rectangle(12,10)
print("Dimension of Rectangle - Length: %d Width : %d" % (newRectangle.length,newRectangle.width))
print("Area of Rectangle :", newRectangle.rectangle_area())
print("Area of Rectangle :", newRectangle.rectangle_area())
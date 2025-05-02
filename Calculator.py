 
class Calculator:
  x = 5
  def perimeter (self,l,w):
    return 2*(l+w)
  
  def trianglearea (self,base,height):
    result=0.5*height*base;
    return(result)
  
  def calcmultiply(q,r):
     return q*r
  # Multiply numbers
    


  # square
  def square(self,h):
    return h*h
  def fileapp(self,filename ):
    f=open (filename)
    print (f.read())





calc1=Calculator()
print(calc1.trianglearea(4,4))
print(calc1.perimeter(10,21))

calc1.fileapp('results.csv')

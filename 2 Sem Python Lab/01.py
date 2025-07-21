""""01. Write a python program and execute the python file using .pyc file and also 
print the byte code of the python file
"""

def findArea(r):
    PI = 3.142
    return PI * (r*r);
# Driver method
n = int(input("Enter the radius : "))
if __name__=="__main__":
 print("Area is %.6f" % findArea(n))

 # Run the below commands in the terminal
 """
python -m py_compile area_of_circle.py //creates a .pyc file in __pycache__ folder
cd __pycache__
python area_of_circle.cpython-312.pyc //executes the compiled python file
cd ..
"""
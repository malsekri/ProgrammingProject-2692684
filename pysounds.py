import os
from webchecker import *

r1 = ring1()
r2 = ring2()
r3 = ring3()
r4 = ring4()

def pysounds():
    if r1 == True:
        os.system("mpg123 fullpathname")
    elif r2 == True:
        os.system("mpg123 fullpathname")
    elif r3 == True:
        os.system("mpg123 fullpathname")
    elif r4 == True:
        os.system("mpg123 fullpathname")
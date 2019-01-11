import cx_Freeze
from cx_Freeze import *
import os
os.environ['TCL_LIBRARY'] = r'D:\Users\Whirl\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Users\Whirl\AppData\Local\Programs\Python\Python36\tcl\tk8.6'
setup(
    name = "wavepxls",
    version = "1.0",
    author = "spiderBoy",
    options = {'build_exe':{'packages':["pygame"]}},
    executables = [Executable("wavepxls.py")],
)
import os
from subprocess import call,Popen,PIPE

cmd = "pyinstaller --onefile -w  json_schema_generator.py --hidden-import='PIL._tkinter_finder'"
process = Popen(cmd, shell=True)
process.communicate ()

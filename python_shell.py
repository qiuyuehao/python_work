#!/usr/bin/python3.5

#  import commands  commands is in python2.x version removed in pytyhon 3

#  print(os.system("ls"))

#  print(os.popen("ls"))

#  (status, result) = commands.getstatusoutput("ls")

import subprocess
a = subprocess.run("ls -al", shell=True, stdout=subprocess.PIPE)
print(a)
print(type(a))

(return_code, result) = subprocess.getstatusoutput("ls -al")
print(return_code)
print(type(return_code))

#  the output
#  CompletedProcess(args='ls -al', returncode=0, stdout=b'total 24\ndrwxrwxr-x 2 qyh qyh 4096 12\xe6\x9c\x88 19 17:48 .\ndrwxrwxr-x 4 qyh qyh 4096 12\xe6\x9c\x88 18 11:11 ..\n-rwxrwxr-x 1 qyh qyh 1485 12\xe6\x9c\x88 18 17:31 how_to_log.py\n-rwxrwxr-x 1 qyh qyh  418 12\xe6\x9c\x88 19 17:48 python_shell.py\n-rwxrwxr-x 1 qyh qyh  715 12\xe6\x9c\x88 19 10:27 str_to_byte_array.py\n-rwxrwxr-x 1 qyh qyh  143 12\xe6\x9c\x88 18 15:07 type_isinstance.py\n')
#  <class 'subprocess.CompletedProcess'>
#  0
#  <class 'int'>

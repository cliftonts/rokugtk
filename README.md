# rokugtk

Using the ssdp package by dankrause
https://gist.github.com/dankrause/6000248

This fork attempts to modernise rokugtk to work with Python 3.x and GTK 3.x. 

It does not work yet and fails with the following error:

~~~~
$ python rokugtk.py 
Traceback (most recent call last):
  File "/home/user/build/rokugtk/rokugtk.py", line 364, in <module>
    app = Application()
  File "/home/user/build/rokugtk/rokugtk.py", line 47, in __init__
    response = ssdp.discover("roku:ecp")
  File "/home/user/build/rokugtk/ssdp.py", line 46, in discover
    sock.sendto(message.format(*group, st=service, mx=mx), group)
TypeError: a bytes-like object is required, not 'str'
~~~~

Help with this is appreciated!

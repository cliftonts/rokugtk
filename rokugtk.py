#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import modules
import socket
import os
import sys
import requests
import urllib
if sys.version_info >= (3,0):
	import urllib.request
	from gi.repository import Gtk as gtk
else:
	import urllib2
	import pygtk
	pygtk.require('2.0')
	import gtk


#Initialise variables
version = "0.1.0" #Also change in snapcraft.yaml and setup/gui/rokugtk.desktop
ip = ""

def get_resource_path(rel_path):
	"""https://stackoverflow.com/questions/4416336/adding-a-program-icon-in-python-gtk"""
	dir_of_py_file = os.path.dirname(__file__)
	rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
	abs_path_to_resource = os.path.abspath(rel_path_to_resource)
	return abs_path_to_resource

class Application():
	#Initialise window
	def __init__(self):
		self.window = gtk.Window()
		self.window.connect("delete-event", quitting) # no parenthesis; you pass functions to connect
		self.window.set_title("RokuGtk - " + version)
		self.window.set_icon_from_file(get_resource_path("rokugtk.png"))

		self.create_widgets()
		self.connect_signals()

		self.window.show_all()
		find()
		gtk.main()

	def create_widgets(self):
		self.vbox = gtk.VBox(spacing=10)

	        #Add buttons
		#First row
		self.hbox_1 = gtk.HBox(spacing=10)
		self.button_back = gtk.Button("Back")
		self.button_back.set_size_request(1,4)
		self.hbox_1.pack_start(self.button_back, True, True, 0)

		self.button_up = gtk.Button("Up")
		self.button_up.set_size_request(1,4)
		self.hbox_1.pack_start(self.button_up, True, True, 0)

		self.button_home = gtk.Button("Home")
		self.button_home.set_size_request(1,4)
		self.hbox_1.pack_start(self.button_home, True, True, 0)

		#Second row
		self.hbox_2 = gtk.HBox(spacing=10)
		self.button_left = gtk.Button("Left")
		self.button_left.set_size_request(1,4)
		self.hbox_2.pack_start(self.button_left, True, True, 0)

		self.button_select = gtk.Button("Select")
		self.button_select.set_size_request(1,4)
		self.hbox_2.pack_start(self.button_select, True, True, 0)

		self.button_right = gtk.Button("Right")
		self.button_right.set_size_request(1,4)
		self.hbox_2.pack_start(self.button_right, True, True, 0)

		#Third row
		self.hbox_3 = gtk.HBox(spacing=10)
		self.button_reverse = gtk.Button("Reverse")
		self.button_reverse.set_size_request(1,4)
		self.hbox_3.pack_start(self.button_reverse, True, True, 0)

		self.button_down = gtk.Button("Down")
		self.button_down.set_size_request(1,4)
		self.hbox_3.pack_start(self.button_down, True, True, 0)

		self.button_forward = gtk.Button("Forward")
		self.button_forward.set_size_request(1,4)
		self.hbox_3.pack_start(self.button_forward, True, True, 0)

		#Fourth row
		self.hbox_4 = gtk.HBox(spacing=10)
		self.button_play = gtk.Button("Play")
		self.button_play.set_size_request(1,4)
		self.hbox_4.pack_start(self.button_play, True, True, 0)

		self.button_reload = gtk.Button("Reload")
		self.button_reload.set_size_request(1,4)
		self.hbox_4.pack_start(self.button_reload, True, True, 0)

		#Fifth row
		self.hbox_5 = gtk.HBox(spacing=10)
		self.button_info = gtk.Button("Info")
		self.button_info.set_size_request(1,4)
		self.hbox_5.pack_start(self.button_info, True, True, 0)

		self.button_search = gtk.Button("Search")
		self.button_search.set_size_request(1,4)
		self.hbox_5.pack_start(self.button_search, True, True, 0)

		self.vbox.pack_start(self.hbox_1, True, True, 0)
		self.vbox.pack_start(self.hbox_2, True, True, 0)
		self.vbox.pack_start(self.hbox_3, True, True, 0)
		self.vbox.pack_start(self.hbox_4, True, True, 0)
		self.vbox.pack_start(self.hbox_5, True, True, 0)

		self.window.add(self.vbox)
		self.window.set_size_request(400, 400)


	def connect_signals(self):
		self.button_back.connect("clicked", self.callback_back)
		self.button_up.connect("clicked", self.callback_up)
		self.button_home.connect("clicked", self.callback_home)

		self.button_left.connect("clicked", self.callback_left)
		self.button_select.connect("clicked", self.callback_select)
		self.button_right.connect("clicked", self.callback_right)

		self.button_reverse.connect("clicked", self.callback_reverse)
		self.button_down.connect("clicked", self.callback_down)
		self.button_forward.connect("clicked", self.callback_forward)

		self.button_play.connect("clicked", self.callback_play)
		self.button_reload.connect("clicked", self.callback_reload)

		self.button_info.connect("clicked", self.callback_info)


	def callback_back(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Back"
		send(cmd)


	def callback_up(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Up"
		send(cmd)

	def callback_home(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Home"
		send(cmd)

	def callback_left(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Left"
		send(cmd)

	def callback_select(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Select"
		send(cmd)

	def callback_right(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Right"
		send(cmd)

	def callback_reverse(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Rev"
		send(cmd)

	def callback_down(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Down"
		send(cmd)

	def callback_forward(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Fwd"
		send(cmd)

	def callback_play(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Play"
		send(cmd)

	def callback_reload(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/InstantReplay"
		send(cmd)

	def callback_info(self, widget, callback_data=None):
		cmd = "http://" + ip + ":8060/keypress/Info"
		send(cmd)

	def callback_search(self, widget, callback_data=None):
		print ("Search")

def send(url):
	payload = {'': ''}
	try:
		# POST with form-encoded data
		r = requests.post(url, data=payload)

		# Response, status etc
		#r.text
		#r.status_code
	except:
		print ("ROKU NOT FOUND!")


def find():
	global ip

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8",80))
	ip = s.getsockname()[0]
	s.close()
	ipsplit = ip.split(".")

	ip = ""
	for i in range(0, 3):
		ip = ip + ipsplit[i] + "."
	ip = "192.168.1."
	for i in range(1,257):
		try:
			url = 'http://' + ip + str(i) + ':8060'
			print ("Attempting - " + ip + str(i))
			r = urllib2.urlopen(url, timeout=0.1)
			html=r.read()
			if "Roku" in html:
				print ("Roku found!")
				print (ip + str(i))
				ip = ip + str(i)
				break
		except:
			pass
	if ip[-1:] == ".":
		message = gtk.MessageDialog(parent=None, 
                            flags=0, 
                            type=gtk.MESSAGE_WARNING, 
                            buttons=gtk.BUTTONS_OK, 
                            message_format=None)
		message.set_markup("Roku not found!\nPlease try again.")
		message.run()
		quit()

#This routine will allow for any code to run before quitting.
def quitting(tmp, tmp2):
	gtk.main_quit()


if __name__ == "__main__":
    app = Application()

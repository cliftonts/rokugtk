#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import modules
import socket
import os
import sys
import requests
import urllib.request, urllib.parse, urllib.error
import time
import ssdp
import gi
if sys.version_info >= (3,0):
	import urllib.request
	gi.require_version('Gtk', '3.0')
	from gi.repository import Gtk as Gtk
else:
	import urllib.request, urllib.error, urllib.parse
	import pyGtk
	gi.require_version('Gtk', '3.0')
	import Gtk


#Initialise variables
version = "0.4.0" #Also change in snapcraft.yaml and setup/gui/rokuGtk.desktop
ip = ""

def get_resource_path(rel_path):
	"""https://stackoverflow.com/questions/4416336/adding-a-program-icon-in-python-Gtk"""
	dir_of_py_file = os.path.dirname(__file__)
	rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
	abs_path_to_resource = os.path.abspath(rel_path_to_resource)
	return abs_path_to_resource

class Application():
	#Initialise window
	def __init__(self):
		self.window = Gtk.Window()
		self.window.connect("destroy", Gtk.main_quit) # no parenthesis; you pass functions to connect
		self.window.set_title("RokuGtk - " + version)
		self.window.set_icon_from_file(get_resource_path("rokugtk.png"))

		self.create_widgets()
		self.connect_signals()

		self.window.show_all()
		response = ssdp.discover("roku:ecp")
		if len(response) == 0:
		    find()
		else:
		    global ip
		    ip = response[0].location.encode()
		    print(ip)
		Gtk.main()

	def create_widgets(self):
		self.vbox = Gtk.VBox(spacing=10)

	        #Add buttons
		#First row
		self.hbox_1 = Gtk.HBox(spacing=10)
		self.button_back = Gtk.Button.new_with_label("Back")
		self.button_back.set_size_request(1,4)
		self.hbox_1.pack_start(self.button_back, True, True, 0)

		self.button_up = Gtk.Button.new_with_label("Up")
		self.button_up.set_size_request(1,4)
		self.hbox_1.pack_start(self.button_up, True, True, 0)

		self.button_home = Gtk.Button.new_with_label("Home")
		self.button_home.set_size_request(1,4)
		self.hbox_1.pack_start(self.button_home, True, True, 0)

		#Second row
		self.hbox_2 = Gtk.HBox(spacing=10)
		self.button_left = Gtk.Button.new_with_label("Left")
		self.button_left.set_size_request(1,4)
		self.hbox_2.pack_start(self.button_left, True, True, 0)

		self.button_select = Gtk.Button.new_with_label("Select")
		self.button_select.set_size_request(1,4)
		self.hbox_2.pack_start(self.button_select, True, True, 0)

		self.button_right = Gtk.Button.new_with_label("Right")
		self.button_right.set_size_request(1,4)
		self.hbox_2.pack_start(self.button_right, True, True, 0)

		#Third row
		self.hbox_3 = Gtk.HBox(spacing=10)
		self.button_reverse = Gtk.Button.new_with_label("Reverse")
		self.button_reverse.set_size_request(1,4)
		self.hbox_3.pack_start(self.button_reverse, True, True, 0)

		self.button_down = Gtk.Button.new_with_label("Down")
		self.button_down.set_size_request(1,4)
		self.hbox_3.pack_start(self.button_down, True, True, 0)

		self.button_forward = Gtk.Button.new_with_label("Forward")
		self.button_forward.set_size_request(1,4)
		self.hbox_3.pack_start(self.button_forward, True, True, 0)

		#Fourth row
		self.hbox_4 = Gtk.HBox(spacing=10)
		self.button_play = Gtk.Button.new_with_label("Play")
		self.button_play.set_size_request(1,4)
		self.hbox_4.pack_start(self.button_play, True, True, 0)

		self.button_reload = Gtk.Button.new_with_label("Reload")
		self.button_reload.set_size_request(1,4)
		self.hbox_4.pack_start(self.button_reload, True, True, 0)

		#Fifth row
		self.hbox_5 = Gtk.HBox(spacing=10)
		self.button_info = Gtk.Button.new_with_label("Info")
		self.button_info.set_size_request(1,4)
		self.hbox_5.pack_start(self.button_info, True, True, 0)

		self.button_search = Gtk.Button.new_with_label("Search")
		self.button_search.set_size_request(1,4)
		self.hbox_5.pack_start(self.button_search, True, True, 0)

		self.button_about = Gtk.Button.new_with_label("About")
		self.button_about.set_size_request(1,4)
		self.hbox_5.pack_start(self.button_about, True, True, 0)

		self.vbox.pack_start(self.hbox_1, True, True, 0)
		self.vbox.pack_start(self.hbox_2, True, True, 0)
		self.vbox.pack_start(self.hbox_3, True, True, 0)
		self.vbox.pack_start(self.hbox_4, True, True, 0)
		self.vbox.pack_start(self.hbox_5, True, True, 0)

		self.window.add(self.vbox)
		self.window.set_size_request(200, 200)


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
		self.button_search.connect("clicked", self.callback_search)
		self.button_about.connect("clicked", self.callback_about)

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
		search = EntryDialog(parent=None, 
                            flags=0, 
                            type=Gtk.MESSAGE_INFO, 
                            buttons=Gtk.BUTTONS_OK, 
                            message_format=None)
		search.set_markup("Search")
		searchfor = search.run()
		search.destroy()
		if searchfor !="None":
			keyboard(ip, searchfor)

	def callback_about(self, widget, callback_data=None):
		aboutdialog = Gtk.AboutDialog()
		# lists of authors and documenters (will be used later)
		authors = ["Gareth France"]

        	# we fill in the aboutdialog
		aboutdialog.set_program_name("RokuGtk " + version)
		aboutdialog.set_comments("RokuGtk is a remote control application for controlling Roku and Now TV set top boxes.\n\nIf you have found this program to be useful please consider making a small donation towards future development.\nPaypal:- gareth.france@gmail.com\nPPPay.com:- gareth.france@cliftonts.co.uk\n\n A massive thank you to kyrofa, elopio and Mark Shuttleworth for their help in making the snap version possible.")
		aboutdialog.set_authors(authors)
		aboutdialog.set_website("https://github.com/cliftonts/rokuGtk")
		aboutdialog.set_website_label("Report issues on GitHub")

		# we do not want to show the title, which by default would be "About AboutDialog Example"
		# we have to reset the title of the messagedialog window after setting
		# the program name
		aboutdialog.set_title("")

        	# to close the aboutdialog when "close" is clicked we connect the
        	# "response" signal to on_close
		aboutdialog.connect("response", self.on_close)
        	# show the aboutdialog
		aboutdialog.show()

    		# destroy the aboutdialog
	def on_close(self, action, parameter):
		action.destroy()
		

def send(url):
	payload = {'': ''}
	try:
		# POST with form-encoded data
		r = requests.post(url, data=payload)

		# Response, status etc
		#r.text
		#r.status_code
	except:
		message = Gtk.MessageDialog(parent=None, 
                            flags=0, 
                            type=Gtk.MESSAGE_WARNING, 
                            buttons=Gtk.BUTTONS_OK, 
                            message_format=None)
		message.set_markup("Roku not found!\nPlease try again.")
		message.run()
		quit()


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

	for i in range(1,257):
		try:
			url = 'http://' + ip + str(i) + ':8060'
			print(("Attempting - " + ip + str(i)))
			r = urllib.request.urlopen(url, timeout=0.2)
			html=r.read()
			if b"Roku" in html:
				print ("Roku found!")
				print((ip + str(i)))
				ip = ip + str(i)
				break
		except:
			pass
	if ip[-1:] == ".":
		message = Gtk.MessageDialog(parent=None, 
                            # flags=0, 
                            message_type=Gtk.MessageType.ERROR, 
                            buttons=Gtk.ButtonsType.OK, 
                            text="Roku not found!\nPlease try again.")
		message.run()
		quit()

class EntryDialog(Gtk.MessageDialog):
    def __init__(self, *args, **kwargs):
        '''
        Creates a new EntryDialog. Takes all the arguments of the usual
        MessageDialog constructor plus one optional named argument 
        "default_value" to specify the initial contents of the entry.
        '''
        if 'default_value' in kwargs:
            default_value = kwargs['default_value']
            del kwargs['default_value']
        else:
            default_value = ''
        super(EntryDialog, self).__init__(*args, **kwargs)
        entry = Gtk.Entry()        
        entry.set_text(str(default_value))
        entry.connect("activate", 
                      lambda ent, dlg, resp: dlg.response(resp), 
                      self, Gtk.RESPONSE_OK)
        self.vbox.pack_end(entry, True, True, 0)
        self.vbox.show_all()
        self.entry = entry
    def set_value(self, text):
        self.entry.set_text(text)
    def run(self):
        result = super(EntryDialog, self).run()
        if result == Gtk.RESPONSE_OK:
            text = self.entry.get_text()
        else:
            text = None
        return text

def keyboard(ip, keyin):
	#urllib.quote('/test', safe='')

	#networkCall("POST", "http://" + ip + ":8060/keypress/Backspace");
	#if sys.version_info < (3,0):
	for i in keyin:
		if sys.version_info >= (3,0):
			url = "http://" + ip + ":8060/keypress/Lit_" + urllib.parse.quote(i, safe='');
		else:
			url = "http://" + ip + ":8060/keypress/Lit_" + urllib.parse.quote(i, safe='');
		payload = {'': ''}
		try:
			# POST with form-encoded data
			r = requests.post(url, data=payload)
			
			# Response, status etc
			#r.text
			#r.status_code
		except:
			message = Gtk.MessageDialog(parent=None, 
                            flags=0, 
                            message_type=Gtk.MessageType.WARNING, 
                            buttons=Gtk.ButtonsType.OK, 
                            text=None)
			message.set_markup("Roku not found!\nPlease try again.")
			message.run()
			quit()
		time.sleep(0.2)
	#if sys.version_info < (3,0):


#This routine will allow for any code to run before quitting.
def quitting(tmp, tmp2):
	Gtk.main_quit()


if __name__ == "__main__":
    app = Application()

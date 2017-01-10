#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import modules
import pygtk
pygtk.require('2.0')
import gtk

#Initialise variables
version = "0.0.1"

class Application():
	#Initialise window
	def __init__(self):
		self.window = gtk.Window()
		self.window.set_title("RokuGtk - " + version)
 
		self.create_widgets()
		self.connect_signals()

		self.window.show_all()
		gtk.main()
  
	def create_widgets(self):
		self.vbox = gtk.VBox(spacing=10)

	        #Add buttons
		#First row
	        self.hbox_1 = gtk.HBox(spacing=10)
	        self.button_back = gtk.Button("Back")
	        self.button_back.set_size_request(1,4)
	        self.hbox_1.pack_start(self.button_back)

	        self.button_up = gtk.Button("Up")
	        self.button_up.set_size_request(1,4)
	        self.hbox_1.pack_start(self.button_up)
     
	        self.button_home = gtk.Button("Home")
	        self.button_home.set_size_request(1,4)
	        self.hbox_1.pack_start(self.button_home)

		#Second row
		self.hbox_2 = gtk.HBox(spacing=10)
	        self.button_left = gtk.Button("Left")
	        self.button_left.set_size_request(1,4)
	        self.hbox_2.pack_start(self.button_left)

		self.button_select = gtk.Button("Select")
	        self.button_select.set_size_request(1,4)
	        self.hbox_2.pack_start(self.button_select)

		self.button_right = gtk.Button("Right")
	        self.button_right.set_size_request(1,4)
	        self.hbox_2.pack_start(self.button_right)

		#Third row
		self.hbox_3 = gtk.HBox(spacing=10)
	        self.button_reverse = gtk.Button("Reverse")
	        self.button_reverse.set_size_request(1,4)
	        self.hbox_3.pack_start(self.button_reverse)

		self.button_down = gtk.Button("Down")
	        self.button_down.set_size_request(1,4)
	        self.hbox_3.pack_start(self.button_down)

		self.button_forward = gtk.Button("Forward")
	        self.button_forward.set_size_request(1,4)
	        self.hbox_3.pack_start(self.button_forward)

		#Fourth row
		self.hbox_4 = gtk.HBox(spacing=10)
	        self.button_play = gtk.Button("Play")
	        self.button_play.set_size_request(1,4)
	        self.hbox_4.pack_start(self.button_play)

		self.button_reload = gtk.Button("Reload")
	        self.button_reload.set_size_request(1,4)
	        self.hbox_4.pack_start(self.button_reload)

		#Fifth row
		self.hbox_5 = gtk.HBox(spacing=10)
	        self.button_info = gtk.Button("Info")
	        self.button_info.set_size_request(1,4)
	        self.hbox_5.pack_start(self.button_info)

		self.button_search = gtk.Button("Search")
	        self.button_search.set_size_request(1,4)
	        self.hbox_5.pack_start(self.button_search)

 
	        self.vbox.pack_start(self.hbox_1)
		self.vbox.pack_start(self.hbox_2)
		self.vbox.pack_start(self.hbox_3)
		self.vbox.pack_start(self.hbox_4)
		self.vbox.pack_start(self.hbox_5)
	 
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
	        #name = self.entry.get_text()
	        #print name
	        dialog = gtk.FileChooserDialog("Open..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
	        dialog.set_default_response(gtk.RESPONSE_OK)

	        filter = gtk.FileFilter()
	        filter.set_name("All files")
	        filter.add_pattern("*")
	        dialog.add_filter(filter)

	        filter = gtk.FileFilter()
	        filter.set_name("Images")
	        filter.add_mime_type("image/png")
	        filter.add_mime_type("image/jpeg")
	        filter.add_mime_type("image/gif")
	        filter.add_pattern("*.png")
	        filter.add_pattern("*.jpg")
	        filter.add_pattern("*.gif")
	        filter.add_pattern("*.tif")
	        filter.add_pattern("*.xpm")
	        dialog.add_filter(filter)
	        dialog.set_current_folder("~/")
	
	        response = dialog.run()
	        if response == gtk.RESPONSE_OK:
	            global inputfile
	            inputfile = dialog.get_filename()
	            #inputfile = inputfile.replace(" ", "\ ")
	            #print inputfile
	        #elif response == gtk.RESPONSE_CANCEL:
	            #print 'Closed, no files selected'
	        dialog.destroy()
 
 
	def callback_up(self, widget, callback_data=None):
	        #gtk.main_quit()
	        dialog = gtk.FileChooserDialog("Save..",
	                               None,
	                               gtk.FILE_CHOOSER_ACTION_SAVE,
	                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
	                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
	        dialog.set_default_response(gtk.RESPONSE_OK)
	
	        filter = gtk.FileFilter()
	        filter.set_name("All files")
	        filter.add_pattern("*")
	        dialog.add_filter(filter)

	        filter = gtk.FileFilter()
	        filter.set_name("Images")
	        filter.add_mime_type("image/png")
	        filter.add_mime_type("image/jpeg")
	        filter.add_mime_type("image/gif")
	        filter.add_pattern("*.png")
	        filter.add_pattern("*.jpg")
	        filter.add_pattern("*.gif")
	        filter.add_pattern("*.tif")
	        filter.add_pattern("*.xpm")
	        dialog.add_filter(filter)
	        dialog.set_current_folder("~/")
	
	        response = dialog.run()
	        if response == gtk.RESPONSE_OK:
	            global outputfile
	            outputfile = dialog.get_filename()
	            #outputfile = outputfile.replace(" ", "\ ")
	        #elif response == gtk.RESPONSE_CANCEL:
	            #print 'Closed, no files selected'
	        dialog.destroy() 

	def callback_home(self, widget, callback_data=None):
	        global inputfile
	        global outputfile
	        global test
	        if port == "File" and inputfile == "":
	           message = gtk.MessageDialog(type=gtk.MESSAGE_ERROR)
	           message.set_markup("Check input file selection and try again.")
	           message.run()
	        else:
	           if outputfile != "" and port != "" and test != "":
	              testmode = "--t=" + test
	              method = "--m=std"
	              inputfile2 = "--i=" + inputfile
	              inputfile=inputfile2
	              outputfile = "--o=" + outputfile
	              if cts == "True":
	                 method = "--m=cts"
	              if port == "File":                 
	                 cmd = "/opt/cliftontestsuite/cliftontestsuite "+ testmode + " \"" + inputfile + "\" \"" + outputfile + "\"" + " " + method
	              else:
	                 cmd = "gksu /opt/cliftontestsuite/cliftontestsuite "+ testmode + " " + port + " \"" + outputfile + "\" " + method
	              #print cmd
	              #os.system(cmd)
	              call (cmd, shell=True)
	           else:
	              message = gtk.MessageDialog(type=gtk.MESSAGE_ERROR)
	              message.set_markup("Check\nTester Model\nChosen Port\nInput and output file selections\nand try again.")
	              message.run()

	def callback_left(self, widget, callback_data=None):
		print ("Left")

	def callback_select(self, widget, callback_data=None):
		print ("Select")

	def callback_right(self, widget, callback_data=None):
		print ("Right")

	def callback_reverse(self, widget, callback_data=None):
		print ("Reverse")

	def callback_down(self, widget, callback_data=None):
		print ("Down")

	def callback_forward(self, widget, callback_data=None):
		print ("Forward")

	def callback_play(self, widget, callback_data=None):
		print ("Play")

	def callback_reload(self, widget, callback_data=None):
		print ("Reload")

	def callback_info(self, widget, callback_data=None):
		print ("Info")

	def callback_search(self, widget, callback_data=None):
		print ("Search")
        

if __name__ == "__main__":
    app = Application()

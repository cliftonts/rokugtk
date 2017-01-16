
import wx
from wx.lib.wordwrap import wordwrap
import sys
import requests
import urllib
if sys.version_info >= (3,0):
	import urllib.request
	from gi.repository import Gtk as gtk
else:
	import urllib2

#Initialise variables
version = "0.0.1"
ip = "192.168.0"

#----------------------------------------------------------------------

class Keypad(wx.Frame):
    def __init__(self, parent, title):
	find()
	ipsplit = ip.split(".")
	if len(ipsplit) < 4:
		print ("ROKU NOT FOUND!")
		quit()
        #self.log = log
	super(Keypad, self).__init__(parent, title=title, 
            size=(285, 200), style=wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
        #wx.Panel.__init__(self, parent, -1, (350,200))

        back = wx.Button(self, -1, "Back", (10,10))
        self.Bind(wx.EVT_BUTTON, self.OnBack, back)
	up = wx.Button(self, -1, "Up", (100,10))
	self.Bind(wx.EVT_BUTTON, self.OnUp, up)
	home = wx.Button(self, -1, "Home", (190,10))
	self.Bind(wx.EVT_BUTTON, self.OnHome, home)

	
	left = wx.Button(self, -1, "Left", (10,45))
	self.Bind(wx.EVT_BUTTON, self.OnLeft, left)
	select = wx.Button(self, -1, "Select", (100,45))
	self.Bind(wx.EVT_BUTTON, self.OnSelect, select)
	right = wx.Button(self, -1, "Right", (190,45))
	self.Bind(wx.EVT_BUTTON, self.OnRight, right)

	rev = wx.Button(self, -1, "Rev", (10,80))
	self.Bind(wx.EVT_BUTTON, self.OnRev, rev)
	down = wx.Button(self, -1, "Down", (100,80))
	self.Bind(wx.EVT_BUTTON, self.OnDown, down)
	forward = wx.Button(self, -1, "Forward", (190,80))
	self.Bind(wx.EVT_BUTTON, self.OnForward, forward)

	play = wx.Button(self, -1, "Play", (55,115))
	self.Bind(wx.EVT_BUTTON, self.OnPlay, play)
	reload = wx.Button(self, -1, "Reload", (145,115))
	self.Bind(wx.EVT_BUTTON, self.OnReload, reload)

	info = wx.Button(self, -1, "Info", (10,150))
	self.Bind(wx.EVT_BUTTON, self.OnInfo, info)
	search = wx.Button(self, -1, "Search", (100,150))
	self.Bind(wx.EVT_BUTTON, self.OnSearch, search)
	about = wx.Button(self, -1, "About", (190,150))
	self.Bind(wx.EVT_BUTTON, self.OnAbout, about)


	self.Show()










    def OnBack(self, evt):
        cmd = "http://" + ip + ":8060/keypress/Back"
	send(cmd)

    def OnUp(self, evt):
        cmd = "http://" + ip + ":8060/keypress/Up"
	send(cmd)

    def OnHome(self, evt):
        cmd = "http://" + ip + ":8060/keypress/Home"
	send(cmd)

    def OnLeft(self, evt):
	cmd = "http://" + ip + ":8060/keypress/Left"
	send(cmd)

    def OnSelect(self, evt):
	cmd = "http://" + ip + ":8060/keypress/Select"
	send(cmd)

    def OnRight(self, evt):
	cmd = "http://" + ip + ":8060/keypress/Right"
	send(cmd)

    def OnRev(self, evt):
	cmd = "http://" + ip + ":8060/keypress/Rev"
	send(cmd)

    def OnDown(self, evt):
	cmd = "http://" + ip + ":8060/keypress/Down"
	send(cmd)

    def OnForward(self, evt):
	cmd = "http://" + ip + ":8060/keypress/Fwd"
	send(cmd)

    def OnPlay(self, evt):
	cmd = "http://" + ip + ":8060/keypress/Play"
	send(cmd)

    def OnReload(self, evt):
	cmd = "http://" + ip + ":8060/keypress/InstantReplay"
	send(cmd)

    def OnInfo(self, evt):
	cmd = "http://" + ip + ":8060/keypress/Info"
	send(cmd)

    def OnSearch(self, evt):
	print ("Search")
	
    
    def OnAbout(self, evt):
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = "RokuGtk"
        info.Version = version
        info.Copyright = "Released under GPL V3"
        info.Description = wordwrap(
            "RokuGtk is a remote control application for controlling "
            "Roku and Now TV set top boxes."
            
            "\n\nIf you have found this program to be useful please consider"
            "making a small donation towards future development."
            "\nPaypal:- gareth.france@gmail.com"
            "\nPPPay.com:- gareth.france@cliftonts.co.uk"
            "\n\n A massive thank you to kyrofa, elopio and Mark Shuttleworth for their help "
            "in making the snap version possible.",
            350, wx.ClientDC(self))
        info.WebSite = ("www.github.com/cliftonts", "Report bugs on the GitHub page")
        info.Developers = [ "Gareth France" ]

        info.License = wordwrap(licenseText, 500, wx.ClientDC(self))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)

def send(url):
	payload = {'': ''}
	try:
		# POST with form-encoded data
		r = requests.post(url, data=payload)
	
		# Response, status etc
		#r.text
		#r.status_code
	except:
		print (ip)
		print ("ROKU NOT FOUND!")
        

def find():
	global ip
	for i in range(1,256):
		try:
			url = 'http://' + ip + '.' + str(i) + ':8060'
			print ("Attempting - " + ip + "." + str(i))	
			r = urllib2.urlopen(url, timeout=0.2)
			html=r.read()
			if "Roku" in html:
				print ("Roku found!")
				print (ip + "." + str(i))
				ip = ip + "." + str(i)
				break
		except:
			pass
#----------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

#----------------------------------------------------------------------



overview = """<html><body>
<h2><center>wx.AboutBox</center></h2>

This function shows the native standard about dialog containing the
information specified in info. If the current platform has a native
about dialog which is capable of showing all the fields in info, the
native dialog is used, otherwise the function falls back to the
generic wxWidgets version of the dialog.

</body></html>
"""


licenseText = "Please see license file included with the source"


if __name__ == '__main__':
    import sys,os
    app = wx.App()
    Keypad(None, title='Rokuterm')
    app.MainLoop()


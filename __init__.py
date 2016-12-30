import Tkinter as tkint

import namb.gui.util

global vlc
vlc=None

from datetime import datetime

FORMAT="%Y-%m-%dT%H:%M:%S+01:00" #"2016-12-30T16:10:14+01:00"

class Menu(namb.gui.util.List):
    
    def __init__(self, parent):
        namb.gui.util.List.__init__(self, parent)
        for i in plugin.channels:
            i["callback"]=(self.callback, i)
        self.populate(plugin.channels)
        
    def callback(self, item):
        plugin.stop()
        plugin.set_media(item["url"])
        plugin.play()
        
        
        def get_info():
            import urllib2, json
            data=urllib2.urlopen(item["nowurl"]).read()
            jdata=json.loads(data)
            result={}
            result["artist"]=jdata["results"][0]["songfile"]["artist"]
            result["title"]=jdata["results"][0]["songfile"]["title"]
            
            result["start"] = datetime.strptime("startdatetime", FORMAT)
            result["stop"] = datetime.strptime("stopdatetime", FORMAT)
            return result
        
        player.set_tracker(get_info)
        player.play()
        



def init():
    global plugin
    import plugin
    plugin.init()

def display(parent, geom=(1280,720)):

    #global width
    width=parent.winfo_width() if parent.winfo_width() > 1 else geom[0]
    #global height
    height=parent.winfo_height() if parent.winfo_height() > 1 else geom[1]
    
    frame = tkint.Frame(parent, bg="black")
    frame.place(x=0,y=0,relwidth=1,relheight=1)
    
    frame.width=width
    frame.height=height
    frame.frame=frame


    global menu
    menu=Menu(frame)
    
    global player
    player=namb.gui.util.Player(frame)
    
if __name__=="__main__":
    import plugin
    plugin.load_channels()
    
    root=tkint.Tk()
    root.geometry("1280x720+0+0")
    
    display(root)
    
    root.after(5000, menu.callback(plugin.channels[0]))
    
    root.mainloop()
    
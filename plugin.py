

import extensions


def load_vlc():
    global vlc
    vlc = extensions.get_extension('vlc')
    if not vlc:
        raise Exception("VLC extension not loaded.")
    if not vlc.INSTANCE:
        vlc.INSTANCE = vlc.get_default_instance()
    if not vlc.PLAYER:
        vlc.PLAYER = vlc.INSTANCE.media_player_new()

def init():
    load_channels()
    load_vlc()

def load_channels():
    global channels
    channels=[
        {"name":"Radio 1","url":"http://icecast.omroep.nl/radio1-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/1.json"},
        {"name":"Radio 2","url":"http://icecast.omroep.nl/radio2-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/2.json"},
        {"name":"Radio 3","url":"http://icecast.omroep.nl/radio3-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/3.json"},
        {"name":"Radio 4","url":"http://icecast.omroep.nl/radio4-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/4.json"},
        {"name":"Radio 5","url":"http://icecast.omroep.nl/radio5-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/5.json"},
        {"name":"Radio 6","url":"http://icecast.omroep.nl/radio6-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/6.json"},
        {"name":"Radio 7","url":"http://icecast.omroep.nl/radio7-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/7.json"},
        {"name":"Radio 8","url":"http://icecast.omroep.nl/radio8-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/8.json"},
        {"name":"Radio 9","url":"http://icecast.omroep.nl/radio9-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/9.json"},
        {"name":"Radio 10","url":"http://icecast.omroep.nl/radio10-bb-mp3","nowurl":"http://radioplayer.npo.nl/data/radiobox2/nowonair/10.json"}
        ]
    
def set_media(url):
    media=vlc.INSTANCE.media_new(url)
    vlc.PLAYER.set_media(media)

def play():
    vlc.PLAYER.play()
    
def stop():
    vlc.PLAYER.stop()
    
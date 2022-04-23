import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter import colorchooser
import os
import io
import math
from pydub import AudioSegment
import shutil

#init
def init():
    global coefficient
    coefficient=180
    global trianglecheck
    global triangleinvcheck
    trianglecheck=0
    triangleinvcheck=0
    global sinecheck
    global sineinvcheck
    sinecheck=0
    sineinvcheck=0
    global squarecheck
    global squareinvcheck
    squarecheck=0
    squareinvcheck=0
    global pickcheck
    pickcheck=0

    
#create main window
def create_main_window():
    global top
    global root
    img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AYht+mFUVaBO0g4hCwOlkQFXGUKhbBQmkrtOpgcukfNGlIUlwcBdeCgz+LVQcXZ10dXAVB8AfE0clJ0UVK/C4ptIjx4O4e3vvel7vvAKFRYaoZmABUzTJS8ZiYza2K3a8IIIR+WkckZuqJ9GIGnuPrHj6+30V5lnfdnyOk5E0G+ETiOaYbFvEG8cympXPeJw6zkqQQnxOPG3RB4keuyy6/cS46LPDMsJFJzROHicViB8sdzEqGSjxNHFFUjfKFrMsK5y3OaqXGWvfkLwzmtZU012kOI44lJJCECBk1lFGBhSjtGikmUnQe8/APOf4kuWRylcHIsYAqVEiOH/wPfvfWLExNuknBGND1Ytsfo0D3LtCs2/b3sW03TwD/M3Cltf3VBjD7SXq9rUWOgL5t4OK6rcl7wOUOMPikS4bkSH6aQqEAvJ/RN+WAgVugd83tW+scpw9Ahnq1fAMcHAJjRcpe93h3T2ff/q1p9e8HSB5ylkmT+ZUAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfmBA0SCQ4i+81yAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAsxJREFUSMe1Vr1KM1EQPbkKESR3I1hJRESI2uYBJKSysrCwzgPYbRdYdfNjKaRMowa0sElgn8AXMJhC0CJKMEQE0biYhEB2YjFyvzXqavzWU83Ozp0zO7MzdwJEhL/EOIB0Or23t+e7a13XDcMIEFE4HLZtW0rpo3d22Gq1xvlZSvn09BQIBHzxPhgMpqamWBZK65f3IVdipJOZTCabzY5GxjUA0Gq1vE2bzWYkEhFCtNvtYDDobax8jvAFlUoFABG9vLz8/NQIBKVSiYVOp+M/QbPZPDw8ZPnbZP6G4OzsDEAkEgHw/Pz8vwT9fn9nZyeTyShNuVwGYBjGqAQgIimllJJcOD4+5rePj49E1Gg0ACSTyfPzcwAHBwduY8dxTNM0TdOtVD4/IahUKqpTqtUqEVmWBcCyrHq9DiCXy7l9XVxcsPHDw8NHAuHubzba3NwEsLW1BaBWq6n/JxaLTU5OAri7u3Pn4OTkhIXr6+svU8TjSEo5MTEB4OjoiINNpVIqP0TU7XaFEPF4XEV6c3OjZsP+/r5KmqZp71IEgFVSSsMwer1er9eLRqPRaJQDtCyLD8fjcSFEt9vlx3w+D6BYLAIYGxtjD5qmccT/CDRNcxyH3iOVSgGYn58H0Gg0WMkJ5HTf399LKVdWVjqdjmma0oVhgqG/iKFal/PDyOVyAOr1OhFx4OVyeeig4zifFPkjFhYWWFhfX1fKmZkZbmbbtnd3dxcXFxOJhMe4HvcgmJ2dZSEWiynl9PQ099rp6enV1VWxWAyFQt/cyR4j1zRNFTWDC3h7e1soFEKh0Orq6m862QPVahXA0tISgHw+/5XZj2rgcZNcXl4CWFtb8/M+YHAzc6vPzc39CYEQAsDGxsZPF6+REAwGt7e3B4PB8vKyz5f+L0r17tLnaerX4jWcItu21S7m4+r4VmRd1/1dTHnS6br+VoM/Xd9fAVRROIG1BVk9AAAAAElFTkSuQmCC'
    root= tk.Tk()
    top= root
    top.geometry("320x240")
    top.title("Color to Waveform")
    top.resizable(0,0)
    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)

#ColorDisplayFrame
def color_display_frame():
    global ColorDisplayFrame
    ColorDisplayFrame= Frame(top)
    ColorDisplayFrame.place(relx=0.08, rely=0.1, relheight=0.8, relwidth=0.84)
    ColorDisplayFrame.configure(relief='groove')
    ColorDisplayFrame.configure(borderwidth="2")
    ColorDisplayFrame.configure(relief="groove")
    ColorDisplayFrame.bind("<Button-1>",pick_color_frame)

#menu
def create_menu():
    global sub_menu
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left",label="Choose Color", command=pick_color, accelerator="Ctrl+C")
    sub_menu.add_command(compound="left",label="Generate Waveform", command=generate_waveform, accelerator="Ctrl+W")
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp, accelerator="Ctrl+Q")
    top.bind_all("<Control-c>",pick_color_frame)
    top.bind_all("<Control-w>",generate_wave_hotkey)
    top.bind_all("<Control-q>",quit_hotkey)


#generate wave hotkey
def generate_wave_hotkey(event):
    generate_waveform()

#quit hotkey
def quit_hotkey(event):
    QuitApp()

#choose color
def pick_color():
    global color
    global RGBcolor
    color = colorchooser.askcolor(title ="Choose color")
    ColorDisplayFrame.configure(bg=color[1])
    colorconv=color[1]
    if str(colorconv)!=("None"):        
        RGBcolor= hex_to_rgb(colorconv)
    pickcheck=1

def pick_color_frame(event):
    global color
    global RGBcolor
    global pickcheck
    RGBcolor=0
    color = colorchooser.askcolor(title ="Choose color")
    ColorDisplayFrame.configure(bg=color[1])
    colorconv=color[1]
    if str(colorconv)!=("None"):        
        RGBcolor= hex_to_rgb(colorconv)
    pickcheck=1
    
#convert Hex to RGB
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

#waveform functions
def triangle (amp, samples):
    global trianglecheck
    global triangleinvcheck
    for twice in range (0,2):
        for i in range (0,45,1):
            i=128+(i*(amp/45))
            i=round(i)
            bytewrite=i.to_bytes(1,'big')
            trianglewave.write(bytewrite)
        for n in range (45,0,-1):
            n=128+(n*(amp/45))
            n=round(n)
            bytewrite=n.to_bytes(1,'big')
            trianglewave.write(bytewrite)
        for n in range (0,45,1):
            n=128-(n*(amp/45))
            n=round(n)
            bytewrite=n.to_bytes(1,'big')
            trianglewave.write(bytewrite)
        for m in range (0,45,1):
            m=128+(m*(amp/45))-amp
            m=round(m)
            bytewrite=m.to_bytes(1,'big')
            trianglewave.write(bytewrite)
    for i in range (0,90,1):
        i=i*(NegColorValue/90)
        i=i-i*2+128
        i=round(i)
        if i<0:
            i=0
        lasti=i
        bytewrite=i.to_bytes(1,'big')
        trianglewaveinv.write(bytewrite)
    for n in range (0,90,1):
        n=n*(NegColorValue/90)
        n=n+lasti
        n=round(n)
        if n<0:
            n=0
        lastn1=n
        bytewrite=n.to_bytes(1,'big')
        trianglewaveinv.write(bytewrite)
    for n in range (0,90,1):
        n=n*(NegColorValue/90)
        n=n+lastn1
        n=round(n)
        if n<0:
            n=0
        lastn2=n
        bytewrite=n.to_bytes(1,'big')
        trianglewaveinv.write(bytewrite)
    for m in range (0,90,1):
        m=m*(NegColorValue/90)
        m=m-m*2+lastn2
        m=round(m)
        if m<0:
            m=0
        bytewrite=m.to_bytes(1,'big')
        trianglewaveinv.write(bytewrite)
    trianglecheck=1
    if NegColorValue>0:
        triangleinvcheck=1

def square (amp, samples):
    posamp=128+amp
    negamp=128-amp
    global squarecheck
    global squareinvcheck
    for twice in range(0,2):
        for i in range (0,90,1):
            bytewrite=posamp.to_bytes(1,'big')
            squarewave.write(bytewrite)
        for n in range (0,90,1):
            bytewrite=negamp.to_bytes(1,'big')
            squarewave.write(bytewrite)
    posamp=128+(NegColorValue)/(127/amp)
    negamp=128-(NegColorValue)/(127/amp)
    posamp=round(posamp)
    negamp=round(negamp)
    for i in range (0,180,1):
        bytewrite=negamp.to_bytes(1,'big')
        squarewaveinv.write(bytewrite)
    for n in range (0,180,1):
        bytewrite=posamp.to_bytes(1,'big')
        squarewaveinv.write(bytewrite)
    squarecheck=1
    if NegColorValue>0:
        squareinvcheck=1

def sine(amp, samples):
    global sinecheck
    global sineinvcheck
    for twice in range(0,2):
        for angle in range(0,360, 2):
            y = math.sin(math.radians(angle))
            value=int(y*amp)+128
            bytewrite=value.to_bytes(1,'big')
            sinewave.write(bytewrite)
    amp=NegColorValue/(127/amp)
    amp=round(amp)
    for angle in range(360,0, -1):
        y = math.sin(math.radians(angle))
        value=int(y*amp)+128
        bytewrite=value.to_bytes(1,'big')
        sinewaveinv.write(bytewrite)
    sinecheck=1
    if NegColorValue>0:
        sineinvcheck=1

#generate waveform
def generate_waveform():
    if pickcheck==0:
        return 0

    global trianglewave
    global trianglewaveinv
    global squarewave
    global squarewaveinv
    global sinewave
    global sinewaveinv
    global NegColorValue
    if os.path.isfile("triangle.wav")==True:
        os.remove("triangle.wav")
    trianglewave= open ("triangle.wav",'ab')
    if os.path.isfile("triangleinv.wav")==True:
        os.remove("triangleinv.wav")
    trianglewaveinv= open ("triangleinv.wav",'ab')
    if os.path.isfile("square.wav")==True:
        os.remove("square.wav")
    squarewave= open ("square.wav",'ab')
    if os.path.isfile("squareinv.wav")==True:
        os.remove("squareinv.wav")
    squarewaveinv= open ("squareinv.wav",'ab')
    if os.path.isfile("sine.wav")==True:
        os.remove("sine.wav")
    sinewave= open ("sine.wav",'ab')
    if os.path.isfile("sineinv.wav")==True:
        os.remove("sineinv.wav")
    sinewaveinv= open ("sineinv.wav",'ab')
    if os.path.isfile("nullwav.wav")==True:
        os.remove("nullwav.wav")
    nullwav=open("nullwav.wav",'wb')
    headerbytes=b'RIFF\xce\x07\xf1\x0bWAVEfmt \x10\x00\x00\x00\x01\x00\x02\x00\x11+\x00\x00"V\x00\x00\x02\x00\x08\x00data&\x06\xf1\x0b'
    trianglewave.write(headerbytes)
    squarewave.write(headerbytes)
    sinewave.write(headerbytes)
    trianglewaveinv.write(headerbytes)
    squarewaveinv.write(headerbytes)
    sinewaveinv.write(headerbytes)
    nullwav.write(headerbytes)
    for n in range (0,364):
        bytevalue=128
        bytewrite=bytevalue.to_bytes(1,'big')
        nullwav.write(bytewrite)
    red=RGBcolor[0]
    green=RGBcolor[1]
    blue=RGBcolor[2]
    redgreenblue=[red,green,blue]
    maxvalue=max(redgreenblue)
    R=int(127/maxvalue*red)
    G=int(127/maxvalue*green)
    B=int(127/maxvalue*blue)
    NegColorValue=128-int(maxvalue/2)
    NegColorValue=100*NegColorValue/128
    if R!=0:
        triangle(R,coefficient)
    if G!=0:
        square(G,coefficient)
    if B!=0:
        sine(B,coefficient)
    if trianglecheck==0:
        for n in range(0,360):
            bytevalue=128
            bytewrite=bytevalue.to_bytes(1,'big')
            trianglewave.write(bytewrite)
            
    if squarecheck==0:
        for n in range(0,360):
            bytevalue=128
            bytewrite=bytevalue.to_bytes(1,'big')
            squarewave.write(bytewrite)
            
    if sinecheck==0:
        for n in range(0,360):
            bytevalue=128
            bytewrite=bytevalue.to_bytes(1,'big')
            sinewave.write(bytewrite)
            
    if triangleinvcheck==0:
        for n in range(0,360):
            bytevalue=128
            bytewrite=bytevalue.to_bytes(1,'big')
            trianglewaveinv.write(bytewrite)

    if squareinvcheck==0:
        for n in range(0,360):
            bytevalue=128
            bytewrite=bytevalue.to_bytes(1,'big')
            squarewaveinv.write(bytewrite)

    if sineinvcheck==0:
        for n in range(0,360):
            bytevalue=128
            bytewrite=bytevalue.to_bytes(1,'big')
            sinewaveinv.write(bytewrite)
    for n in range (0,4):
        bytevalue=128
        bytewrite=bytevalue.to_bytes(1,'big')
        trianglewave.write(bytewrite)
        squarewave.write(bytewrite)
        sinewave.write(bytewrite)
        trianglewaveinv.write(bytewrite)
        squarewaveinv.write(bytewrite)
        sinewaveinv.write(bytewrite)
        
    trianglewave.close()
    trianglewaveinv.close()
    squarewave.close()
    squarewaveinv.close()
    sinewave.close()
    sinewaveinv.close()
    nullwav.close()
    trianglebytes=[]
    squarebytes=[]
    sinebytes=[]

    trianglewave= open ("triangle.wav",'rb')
    squarewave= open ("square.wav",'rb')
    sinewave= open ("sine.wav",'rb')
    
    trianglesize=os.path.getsize("triangle.wav")
    squaresize=os.path.getsize("square.wav")
    sinesize=os.path.getsize("sine.wav")
    for n in range (45,trianglesize):
        trianglewave.seek(n)
        byteread=trianglewave.read(1)
        byteint=int.from_bytes(byteread,"big")
        trianglebytes.append(byteint)
    maxtrianglebyte=max(trianglebytes)-128
    for n in range (45,squaresize):
        squarewave.seek(n)
        byteread=squarewave.read(1)
        byteint=int.from_bytes(byteread,"big")
        squarebytes.append(byteint)
    maxsquarebyte=max(squarebytes)-128
    for n in range (45,sinesize):
        sinewave.seek(n)
        byteread=sinewave.read(1)
        byteint=int.from_bytes(byteread,"big")
        sinebytes.append(byteint)
    maxsinebyte=max(sinebytes)-128
    maxbytevar=maxtrianglebyte+maxsquarebyte+maxsinebyte
    gain=int(maxbytevar*0.039)-3
    gain=gain-gain*2
    trianglewave.close()
    squarewave.close()
    sinewave.close()
    
    trianglefile = AudioSegment.from_file("triangle.wav")
    squarefile = AudioSegment.from_file("square.wav")
    sinefile = AudioSegment.from_file("sine.wav")
    triangleinvfile = AudioSegment.from_file("triangleinv.wav")
    squareinvfile = AudioSegment.from_file("squareinv.wav")
    sineinvfile = AudioSegment.from_file("sineinv.wav")
    nullwavfile=AudioSegment.from_file("nullwav.wav")
    trianglegain=trianglefile[:2000].overlay(nullwavfile,gain_during_overlay=gain)
    squaregain=squarefile[:2000].overlay(nullwavfile,gain_during_overlay=gain)
    sinegain=sinefile[:2000].overlay(nullwavfile,gain_during_overlay=gain)
    trianglesquare = trianglegain[:2000].overlay(squaregain)
    trianglesquare.export('trianglesquare.wav', format='wav')
    trianglesquarefile=AudioSegment.from_file("trianglesquare.wav")
    trianglesquaresine=sinegain[:2000].overlay(trianglesquarefile)
    trianglesquaresine.export('waveformpos.wav',format='wav')
    triangleinvgain=triangleinvfile[:2000].overlay(nullwavfile,gain_during_overlay=gain)
    squareinvgain=squareinvfile[:2000].overlay(nullwavfile,gain_during_overlay=gain)
    sineinvgain=sineinvfile[:2000].overlay(nullwavfile,gain_during_overlay=gain)
    trianglesquareinv = triangleinvgain[:2000].overlay(squareinvfile)
    trianglesquareinv.export('trianglesquareinv.wav', format='wav')
    trianglesquareinvfile=AudioSegment.from_file("trianglesquareinv.wav")
    trianglesquaresineinv=sineinvgain[:2000].overlay(trianglesquareinvfile)
    trianglesquaresineinv.export('waveforminv.wav',format='wav')
    waveformposvar=open("waveformpos.wav",'rb')
    waveforminvvar=open("waveforminv.wav",'rb')
    maxbyte=[]
    maxbyteinv=[]
    waveformpossize=os.path.getsize("waveformpos.wav")
    for n in range (45,waveformpossize):
        waveformposvar.seek(n)
        byteread=waveformposvar.read(1)
        byteint=int.from_bytes(byteread,"big")
        maxbyte.append(byteint)
    maxbytevarpos=max(maxbyte)-128
    waveforminvsize=os.path.getsize("waveforminv.wav")
    for n in range (45,waveforminvsize):
        waveforminvvar.seek(n)
        byteread=waveforminvvar.read(1)
        byteint=int.from_bytes(byteread,"big")
        maxbyteinv.append(byteint)
    maxbytevarinv=max(maxbyteinv)-128
    maxbytevar=(maxbytevarpos+maxbytevarinv)
    waveformposvar.close()
    waveforminvvar.close()
    gain=int(maxbytevar*0.039)-4
    gain=gain-gain*2
    waveformpos=AudioSegment.from_file("waveformpos.wav")
    waveformposgain=waveformpos[:2000].overlay(nullwavfile,gain_during_overlay=gain)
    waveforminv=AudioSegment.from_file("waveforminv.wav")
    waveforminvgain=waveforminv[:2000].overlay(nullwavfile,gain_during_overlay=gain)
    mixedwaveform=waveformposgain[:2000].overlay(waveforminvgain)
    if os.path.isfile("waveform.wav")==True:
        os.remove("waveform.wav")
    mixedwaveform.export('waveform.wav', format='wav')
    waveform=open("waveform.wav",'rb')
    waveformtrim=open("waveformtrim",'wb')
    for n in range (0,360+44):
        bytewrite=waveform.read(1)
        waveformtrim.write(bytewrite)
    waveformtrim.close()
    waveform.close()
    os.remove("triangle.wav")
    os.remove("square.wav")
    os.remove("sine.wav")
    os.remove("trianglesquare.wav")
    os.remove("nullwav.wav")
    os.remove("sineinv.wav")    
    os.remove("triangleinv.wav")
    os.remove("squareinv.wav")
    os.remove("trianglesquareinv.wav")
    os.remove("waveformpos.wav")
    os.remove("waveforminv.wav")
    os.remove("waveform.wav")
    Save_File()

def Save_File():
    data=[('WAV', '*.wav')]
    wavefile=asksaveasfilename(filetypes= data, defaultextension= data)
    if str(wavefile)!='':
        shutil.copy("waveformtrim",wavefile)
    os.remove("waveformtrim")
    
#quit
def QuitApp():
    top.destroy()

#main
def main():
    init()
    create_main_window()
    color_display_frame()
    create_menu()

main()
root.mainloop()

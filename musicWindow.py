import os
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer

co1 = '#ffffff'
co2 = '#3C1DC6'
co3 = '#333333'
co4 = '#CFC7F8'



window = Tk()
window.title("Music Player")
icon = Image.open("img/icon.png")
ico = ImageTk.PhotoImage(icon)
window.iconphoto(True,ico)
window.geometry('353x255')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

leftFrame = Frame(window, width=150, height=150, bg=co1)
leftFrame.grid(row=0,column=0, padx=1, pady=1)

rightFrame = Frame(window, width=250, height=150, bg=co3)
rightFrame.grid(row=0,column=1, padx=0)

lowerFrame = Frame(window, width=400, height=100, bg=co4)
lowerFrame.grid(row=1,column=0,columnspan=3, padx=0, pady=1)


playingSong = Label(lowerFrame, text="Escolha uma música", font=("ComicSans 14"),width=44, height=1, padx=10,bg=co1, fg=co3, anchor=NW)
playingSong.place(x=0,y=1)


# eventos

songPath = 'musics'
songs = os.listdir(songPath)

def show():
    for i in songs:
        listbox.insert(END,i)


def playMusic():
    playing = listbox.get(ACTIVE)
    playingSong['text'] = playing
    mixer.music.load("musics/" + playing)
    mixer.music.play()

def pauseMusic():
    mixer.music.pause()


def continueMusic():
    mixer.music.unpause()

def stopMusic():
    mixer.music.stop()

def nextMusic():
    running = playingSong['text']
    index = songs.index(running)
    newIndex = index + 1
    if newIndex >= len(songs):
        newIndex = 0


    running = songs[newIndex]
    mixer.music.load("musics/" + running)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    listbox.select_set(newIndex)
    playingSong['text'] = running



def prevMusic():
    running = playingSong['text']
    index = songs.index(running)
    newIndex = index - 1
    if newIndex >= len(songs):
        newIndex = 0
    elif newIndex < 0:
        newIndex = len(songs) - 1
    running = songs[newIndex]
    mixer.music.load("musics/" + running)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    listbox.select_set(newIndex)
    playingSong['text'] = running



listbox = Listbox(rightFrame, selectmode=SINGLE, font=("ComicSans 9 bold"), width=22, bg=co3, fg=co1)
listbox.grid(row=0,column=0)


w = Scrollbar(rightFrame)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command = listbox.yview)

#Icon musica default
songImg = Image.open('img/musical-note.png')
songImg = songImg.resize((110,110))
songImg = ImageTk.PhotoImage(songImg)
appImg = Label(leftFrame, height=130,image=songImg, padx=10,bg=co1)
appImg.place(x=10,y=15)

#Icon de anterior
prevImg = Image.open('img/rewind.png')
prevImg = prevImg.resize((30,30))
prevImg = ImageTk.PhotoImage(prevImg)
prevButton = Button(lowerFrame, width=40, height=40,image=prevImg, padx=10,bg=co1, font=("ComicSans 10"), command=prevMusic)
prevButton.place(x=38,y=35)


#Icon de play
playImg = Image.open('img/play.png')
playImg = playImg.resize((30,30))
playImg = ImageTk.PhotoImage(playImg)
playButton = Button(lowerFrame, width=40, height=40,image=playImg, padx=10,bg=co1, font=("ComicSans 10"), command=playMusic)
playButton.place(x=84,y=35)

#Icon de avançar
fowardImg = Image.open('img/fast foward.png')
fowardImg = fowardImg.resize((30,30))
fowardImg = ImageTk.PhotoImage(fowardImg)
playButton = Button(lowerFrame, width=40, height=40,image=fowardImg, padx=10,bg=co1, font=("ComicSans 10"), command=nextMusic)
playButton.place(x=130,y=35)

#Icon de pausar
pauseImg = Image.open('img/pause-button.png')
pauseImg = pauseImg.resize((30,30))
pauseImg = ImageTk.PhotoImage(pauseImg)
pauseButton = Button(lowerFrame, width=40, height=40,image=pauseImg, padx=10,bg=co1, font=("ComicSans 10"), command=pauseMusic)
pauseButton.place(x=176,y=35)

#Icon de despausar
unpauseImg = Image.open('img/right-arrow.png')
unpauseImg = unpauseImg.resize((30,30))
unpauseImg = ImageTk.PhotoImage(unpauseImg)
unpauseButton = Button(lowerFrame, width=40, height=40,image=unpauseImg, padx=10,bg=co1, font=("ComicSans 10"), command=continueMusic)
unpauseButton.place(x=222,y=35)

#Icon de proxima
stopImg = Image.open('img/stop-button.png')
stopImg = stopImg.resize((30,30))
stopImg = ImageTk.PhotoImage(stopImg)
stopButton = Button(lowerFrame, width=40, height=40,image=stopImg, padx=10,bg=co1, font=("ComicSans 10"), command=stopMusic)
stopButton.place(x=268,y=35)



line = Label(leftFrame, width=200, height=1, padx=10,bg=co3)
line.place(x=0,y=1)

line = Label(leftFrame, width=200, height=1, padx=10,bg=co1)
line.place(x=0,y=3)






show()

mixer.init()
musicState = StringVar()
musicState.set("Escolha uma música")
window.mainloop()

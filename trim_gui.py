from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import subprocess
import ntpath
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Video Trimmer")
root.geometry("600x600")

# start = Entry(root)
# end = Entry(root)
target = Entry(root)

label1 = Label(root, text='Start Time:')
hour = Entry(root)
hour.insert(END, 'Hour')
# hour.bind("<FocusIn>", lambda args: hour.delete('0', 'end'))
label_hour = Label(root, text=':')
minute = Entry(root)
minute.insert(END, 'Minute')
# minute.bind("<FocusIn>", lambda args: minute.delete('0', 'end'))
label_minute = Label(root, text=':')
sec = Entry(root)
sec.insert(END, 'Seconds')
# sec.bind("<FocusIn>", lambda args: sec.delete('0', 'end'))

label2 = Label(root, text='End Time:')
ehour = Entry(root)
ehour.insert(END, 'Hour')
# ehour.bind("<FocusIn>", lambda args: ehour.delete('0', 'end'))
elabel_hour = Label(root, text=':')
eminute = Entry(root)
eminute.insert(END, 'Minute')
# eminute.bind("<FocusIn>", lambda args: eminute.delete('0', 'end'))
elabel_minute = Label(root, text=':')
esec = Entry(root)
esec.insert(END, 'Seconds')
# esec.bind("<FocusIn>", lambda args: esec.delete('0', 'end'))

label3 = Label(root, text='Output file name:')



def openFile():
	global name
	name = filedialog.askopenfilename()
	label4 = Label(root, text='File has been imported successfully!').grid(row=0 , column=0, sticky=W+E)

def trimming():
	global saveName
	
	#convert start time in seconds
	h = hour.get()
	m = minute.get()
	s = sec.get()

	if h == '' or h == 'Hour':
		h = 0.0
	else:
		h = float(h)

	if m == '' or m == 'Minute':
		m = 0.0
	else:
		m = float(m)

	startTime = h * 3600 + float(m) * 60 + float(s)

	# convert end time in seconds
	eh = ehour.get()
	em = eminute.get()
	es = esec.get()

	if eh == '' or eh == 'Hour':
		eh = 0.0
	else:
		eh = float(eh)

	if em == '' or em == 'Minute':
		em = 0.0
	else:
		em = float(em)
	endTime = eh * 3600 + float(em) * 60 + float(es)

	saveName = target.get()
	ffmpeg_extract_subclip(name, startTime, endTime, targetname=str(saveName)+'.'+name[-3:])
	label5 = Label(root, text='File has been trimmed successfully!').grid(row=5 , column=0, sticky=W+E)

def playFile():
	d = os.path.basename(name)
	d = str(d)
	os.chdir(os.path.dirname(name))
	subprocess.run(d, shell = True)	

def play_trim():
	dirr = os.getcwd()
	subprocess.run('cd /d ' + dirr, shell = True)
	subprocess.run(str(saveName)+'.'+name[-3:], shell = True)

def exit_program():
	root.destroy()

#create menu bar
master_menu = Menu(root)
root.config(menu=master_menu)

#create item
file_menu = Menu(master_menu)
master_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=openFile)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

media_menu = Menu(master_menu)
master_menu.add_cascade(label='Media', menu=media_menu)
media_menu.add_command(label='play', command=playFile)
#end of menu

#create buttons
trim = Button(root, padx=53, text = 'Lets trim', command =trimming)
play = Button(root, padx=48, text = 'Lets play it', command =play_trim)

quit_button = Button(root, text='QUIT', command=exit_program)



trim.grid(row=4, column=0, sticky=W)
# start.grid(row=1 , column=1)
# end.grid(row=2 , column=1)

target.grid(row=3 , column=1, sticky=W)

label1.grid(row=1 , column=0, sticky=W)
hour.grid(row=1, column=1, sticky=W)
label_hour.grid(row=1, column=2, sticky=W)
minute.grid(row=1, column=3, sticky=W)
label_minute.grid(row=1, column=4, sticky=W)
sec.grid(row=1, column=5, sticky=W)

label2.grid(row=2 , column=0, sticky=W)
ehour.grid(row=2, column=1, sticky=W)
elabel_hour.grid(row=2, column=2, sticky=W)
eminute.grid(row=2, column=3, sticky=W)
elabel_minute.grid(row=2, column=4, sticky=W)
esec.grid(row=2, column=5, sticky=W)

label3.grid(row=3 , column=0, sticky=W)
play.grid(row=6 , column=0, sticky=W)

quit_button.grid(row=7 , column=0, sticky=W)


root.mainloop()
import os
import sys
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

## Helper ##
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

## Helper ##
def center(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2

    toplevel.geometry("+%d+%d" % (x, y))


def edf_file_deidentify():
    # Load the file
    root.filenames = filedialog.askopenfilenames(initialdir="~/", title="Select EDF file(s)",
                                                 filetypes=(("EDF files", "*.edf"), ("All files", "*.*")))
    # Handle file cancel
    if root.filenames == '':
        root.destroy()
        sys.exit("Closing executable...")

    # Check if user wants to overwrite data
    copy_file = messagebox.askyesnocancel(title="EDF Deidentifier",
                                          message="Would you like to save the a copy of the data?")

    # Exit if cancel
    if copy_file is None:
        root.destroy()
        sys.exit("Closing executable...")

    # Double check!
    if not copy_file:
        result = messagebox.askyesno(title="EDF Deidentifier",
                                     message="Are you sure you want to overwrite all edf files with the " +
                                             "deidentified files?")
        if not result:
            root.destroy()
            sys.exit("Closing executable...")

    if copy_file:
        file_savedir = filedialog.askdirectory()

    # Loop through all file names
    for path in root.filenames:

        # Skip if bad file
        if not (os.path.isfile(path)):
            print("Invalid file: " + path)
            continue

        # Copy file to new name
        if copy_file:
            os.chdir(os.path.split(path)[0])
            path_new = file_savedir + '/' + os.path.basename(path)[0:-4] + '_deidentified.edf'
            shutil.copy(path, path_new)
            path = path_new

        # Open file(s) and deidentify
        f = open(path, "r+", encoding="iso-8859-1")  # 'r' = read
        try:
            f.write('%-8s' % "0")
            f.write('%-80s' % "X X X X")  # Remove patient info
            f.write('%-80s' % "Startdate X X X X")  # Remove recording info
            f.write('01.01.01')  # Set date as 01.01.01
        except UnicodeDecodeError:
            f.close()
            f = open(path, "r+", encoding="iso-8859-2")  # 'r' = read
            try:
                f.write('%-8s' % "0")
                f.write('%-80s' % "X X X X")  # Remove patient info
                f.write('%-80s' % "Startdate X X X X")  # Remove recording info
                f.write('01.01.01')  # Set date as 01.01.01
            except UnicodeDecodeError:
                f.close()
                f = open(path, "r+", encoding="utf-8")  # 'r' = read
                try:
                    f.write('%-8s' % "0")
                    f.write('%-80s' % "X X X X")  # Remove patient info
                    f.write('%-80s' % "Startdate X X X X")  # Remove recording info
                    f.write('01.01.01')  # Set date as 01.01.01
                    f.close()
                finally:
                    print('No valid encoding format found')

    txt = Label(root, text="File(s) Saved")
    txt.place(relx=0.48, rely=0.95, anchor=CENTER)


# Create window
root = Tk()
root.geometry("950x340")
root.title('EDF Deidentifier')
center(root)

# Put image in window
spath = resource_path("Splash.png")
simg = ImageTk.PhotoImage(Image.open(spath))
panel = Label(root, image=simg)
center(root)
panel.pack()

# Put button on window
btn = Button(root, text="Choose File(s)", width=35, height=3, relief=GROOVE, bg='#0064BB',
             fg="white", command=edf_file_deidentify, highlightbackground='#0064BB')
btn.place(relx=0.48, rely=0.8, anchor=CENTER)

root.mainloop()

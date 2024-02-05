from My_Packages import TkinterGui as tkgui
from pathlib import Path
import webbrowser
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def callback(url):
    webbrowser.open_new(r'C:\\Users\\findl\\OneDrive\\Documents\\Github\\OCC-Mock\\build\\gui1.py')

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\findl\OneDriveDesktop\OCC designs\1\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("862x519")
window.configure(bg = "#24A0FA")
tkgui.Canvas()
tkgui.canvas_placed
tkgui.Button()
tkgui.create_text()
tkgui.create_rectangle()


window.resizable(False, False)
window.mainloop()

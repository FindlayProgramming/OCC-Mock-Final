
from pathlib import Path
import webbrowser
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\\Users\\findl\\OneDrive\\Desktop\\OCC designs\\2\\build\\assets\\frame1")

def callback_page(url):
    webbrowser.open_new(r'C:\\Users\\findl\\OneDrive\\Documents\\Github\\OCC-Mock\\build\\gui.py')

def callback_web(url):
    webbrowser.open_new('https://www.metoffice.gov.uk/weather/warnings-and-advice/seasonal-advice/health-wellbeing/stay-well-in-winter/stay-well-in-winter')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#F8F8F6",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: callback_page (r"C:\\Users\\findl\\OneDrive\Documents\\Github\\OCC-Mock\\build\\gui.py"),
    relief="flat"
)
button_1.place(
    x=631.0,
    y=388.0,
    width=180.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: callback_web ('https://www.metoffice.gov.uk/weather/warnings-and-advice/seasonal-advice/health-wellbeing/stay-well-in-winter/stay-well-in-winter'),
    relief="flat"
)
button_2.place(
    x=631.0,
    y=457.0,
    width=180.0,
    height=55.0
)

canvas.create_text(
    107.0,
    5.0,
    anchor="nw",
    text="Weather Dashboard",
    fill="#333333",
    font=("RubikRoman Bold", 32 * -1)
)

canvas.create_text(
    21.0,
    211.0,
    anchor="nw",
    text="19 °C",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    19.0,
    246.0,
    anchor="nw",
    text="Monday:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    478.0,
    5.0,
    anchor="nw",
    text="Week:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    70.0,
    285.0,
    anchor="nw",
    text="Rain: 40%",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_rectangle(
    107.0,
    49.0,
    167.0,
    54.0,
    fill="#24A0FA",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    196.0,
    139.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    39.0,
    299.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    217.0,
    423.0,
    image=image_image_3
)

canvas.create_rectangle(
    477.0,
    44.0,
    559.0,
    190.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    606.0,
    44.0,
    688.0,
    190.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    748.0,
    44.0,
    830.0,
    190.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    489.0,
    52.0,
    anchor="nw",
    text="Mon:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    622.0,
    54.0,
    anchor="nw",
    text="Tue:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    761.0,
    54.0,
    anchor="nw",
    text="Wed:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    517.0,
    131.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    647.0,
    132.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    788.0,
    129.0,
    image=image_image_6
)

canvas.create_rectangle(
    478.0,
    223.0,
    560.0,
    369.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    8.0,
    7.0,
    90.0,
    153.0,
    fill="#E5E5E5",
    outline="")

canvas.create_rectangle(
    607.0,
    223.0,
    689.0,
    369.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    472.0,
    382.0,
    554.0,
    510.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    744.0,
    223.0,
    826.0,
    369.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    489.0,
    232.0,
    anchor="nw",
    text="Thu:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    486.0,
    388.0,
    anchor="nw",
    text="Sun:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    627.0,
    232.0,
    anchor="nw",
    text="Fri:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    762.0,
    232.0,
    anchor="nw",
    text="Sat:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    519.0,
    295.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    647.0,
    306.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    786.0,
    302.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    513.0,
    456.0,
    image=image_image_10
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=17.0,
    y=11.0,
    width=62.0,
    height=57.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=16.0,
    y=85.0,
    width=63.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()

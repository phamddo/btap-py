from tkinter import *

root = Tk()
root.title("Modern Calculator")
root.geometry("360x540")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

just_calculated = False

# Display
entry = Entry(
    root,
    font=("Arial", 28),
    bd=0,
    bg="#2b2b3c",
    fg="white",
    justify="right",
    insertbackground="white"
)
entry.place(x=20, y=30, width=320, height=80)


def click(value):
    global just_calculated

    current = entry.get()

    if just_calculated and str(value).isdigit():
        entry.delete(0, END)
        current = ""
        just_calculated = False

    entry.delete(0, END)
    entry.insert(0, str(current) + str(value))


def clear():
    global just_calculated
    entry.delete(0, END)
    just_calculated = False


def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])


def equal():
    global just_calculated
    try:
        expression = entry.get().replace("×", "*").replace("÷", "/")
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, str(result))
        just_calculated = True
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")
        just_calculated = True


# Button style
btn_font = ("Arial", 18, "bold")
btn_bg = "#3a3a4f"
btn_fg = "white"
op_bg = "#ff9500"


def create_button(text, x, y, w, h, command, bg=btn_bg):
    Button(
        root,
        text=text,
        font=btn_font,
        bg=bg,
        fg=btn_fg,
        bd=0,
        activebackground="#555",
        activeforeground="white",
        command=command,
        relief="flat",
        cursor="hand2"
    ).place(x=x, y=y, width=w, height=h)


buttons = [
    ("C", 20, 140, lambda: clear(), op_bg),
    ("⌫", 105, 140, lambda: backspace(), op_bg),
    ("%", 190, 140, lambda: click("%"), op_bg),
    ("÷", 275, 140, lambda: click("÷"), op_bg),

    ("7", 20, 220, lambda: click("7"), btn_bg),
    ("8", 105, 220, lambda: click("8"), btn_bg),
    ("9", 190, 220, lambda: click("9"), btn_bg),
    ("×", 275, 220, lambda: click("×"), op_bg),

    ("4", 20, 300, lambda: click("4"), btn_bg),
    ("5", 105, 300, lambda: click("5"), btn_bg),
    ("6", 190, 300, lambda: click("6"), btn_bg),
    ("-", 275, 300, lambda: click("-"), op_bg),

    ("1", 20, 380, lambda: click("1"), btn_bg),
    ("2", 105, 380, lambda: click("2"), btn_bg),
    ("3", 190, 380, lambda: click("3"), btn_bg),
    ("+", 275, 380, lambda: click("+"), op_bg),

    ("0", 20, 460, lambda: click("0"), btn_bg),
    (".", 105, 460, lambda: click("."), btn_bg),
    ("=", 190, 460, lambda: equal(), op_bg),
]

for text, x, y, cmd, color in buttons:
    create_button(text, x, y, 70, 60, cmd, color)

root.mainloop()
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text="TIMER  ", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 2 !=0:
        count_down(25 * 60)
        title_label.config(text = "Work", fg = GREEN)
    elif reps % 8 == 0:
        count_down(20 * 60)
        title_label.config(text="Break", fg= RED)
    else:
        count_down(5 * 60)
        title_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"


    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        start_timer(0)
        mark = ""
        for rep in reps(0, math.floor(reps/2)):
            mark += "✓"
        check_marks.config(text = f"{mark}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady = 100, bg = YELLOW)

title_label = Label(text = 'Timer', fg = GREEN, font = (FONT_NAME, 50), bg = YELLOW)
title_label.grid(column= 1, row = 0)


canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112,  image = tomato)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column= 1, row = 1)

start_button = Button(text = "Start", bg = YELLOW, command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", bg = YELLOW, command = reset)
reset_button.grid(column = 2, row = 2)

check_marks = Label(text = "")



window.mainloop()
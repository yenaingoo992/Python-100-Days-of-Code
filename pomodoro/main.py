import tkinter
import math
from tkinter import PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BACKGROUND = "#FBF6E9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
counting = False
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global counting, reps
    window.after_cancel(timer)
    counting = False
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_label, text="00:00")
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps, counting
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if not counting:
        counting = True
        reps += 1
        if reps % 2 == 0:
            if reps % 8 != 0:
                title_label.config(text="Break", fg=PINK)
                count_down(short_break)
            else:
                reps = 1
                title_label.config(text="Break", fg=RED)
                count_down(long_break)
        else:
            title_label.config(text="Work", fg=GREEN)
            count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global counting,reps
    minutes = math.floor(count / 60)
    sec = count % 60
    canvas.itemconfig(timer_label, text=f"{minutes:02d}:{sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        counting = False
        start()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
# window.maxsize(width=400, height=350)
# window.minsize(width=400, height=350)
window.config(padx=100, pady=50, background=BACKGROUND)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=BACKGROUND)
title_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, background=BACKGROUND, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_label = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="start", padx=16, pady=8)
start_button.grid(row=2, column=0)
start_button.config(command=start)

reset_button = Button(text="reset", padx=16, pady=8, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=BACKGROUND)
check_label.grid(row=3, column=1)

window.mainloop()

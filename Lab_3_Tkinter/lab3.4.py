import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Ковалюк Денис 3.4")
root.geometry("600x700")

tk.Label(root, text="Тестування", font=("Arial", 20)).pack(pady=10)

frame_top = tk.Frame(root)
frame_top.pack()

tk.Label(frame_top, text="Введіть прізвище:", font=("Arial", 12)).grid(row=0, column=0)
entry_surname = tk.Entry(frame_top, width=30)
entry_surname.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_top, text="Введіть групу:", font=("Arial", 12)).grid(row=1, column=0)
entry_group = tk.Entry(frame_top, width=30)
entry_group.grid(row=1, column=1, padx=10, pady=5)

warning_label = tk.Label(root, text="", fg="red", font=("Arial", 11))
warning_label.pack()



canvas = tk.Canvas(root, height=450)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")




q1 = tk.IntVar(value=-1)
tk.Label(scrollable_frame, text="1. Яка найпопулярніша мова програмування", font=("Arial", 10)).pack(anchor="w")
tk.Radiobutton(scrollable_frame, text="Python", variable=q1, value=1).pack(anchor="w")
tk.Radiobutton(scrollable_frame, text="JavaScript", variable=q1, value=2).pack(anchor="w")
tk.Radiobutton(scrollable_frame, text="C++", variable=q1, value=3).pack(anchor="w")

tk.Label(scrollable_frame, text="2. Які операційні системи існують", font=("Arial", 10)).pack(anchor="w")
q2_a = tk.BooleanVar()
q2_b = tk.BooleanVar()
q2_c = tk.BooleanVar()
tk.Checkbutton(scrollable_frame, text="Windows", variable=q2_a).pack(anchor="w")
tk.Checkbutton(scrollable_frame, text="Virus", variable=q2_b).pack(anchor="w")
tk.Checkbutton(scrollable_frame, text="MacOS", variable=q2_c).pack(anchor="w")

tk.Label(scrollable_frame, text="3. Яка столиця Франції", font=("Arial", 10)).pack(anchor="w")
tk.Label(scrollable_frame, text="Введіть відповідь:").pack(anchor="w")
q3 = tk.Entry(scrollable_frame, width=30)
q3.pack(anchor="w")

answers = []
for i in range(4, 11):
    var = tk.IntVar(value=-1)
    answers.append(var)
    tk.Label(scrollable_frame, text=f"{i}. Виберіть 1 (правильна — варіант 2)").pack(anchor="w")
    tk.Radiobutton(scrollable_frame, text="варіант 1", variable=var, value=0).pack(anchor="w")
    tk.Radiobutton(scrollable_frame, text="варіант 2", variable=var, value=1).pack(anchor="w")
    tk.Radiobutton(scrollable_frame, text="варіант 3", variable=var, value=2).pack(anchor="w")

root.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))



def submit():
    surname = entry_surname.get().strip()
    group = entry_group.get().strip()
    if surname == "" or group == "":
        warning_label.config(text="⚠ Заповніть прізвище та групу!")
        return
    warning_label.config(text="")
    score = 0
    if q1.get() == 1:
        score += 1
    if q2_a.get() and q2_c.get() and not q2_b.get():
        score += 1
    if q3.get().strip().lower() == "париж":
        score += 1
    for v in answers:
        if v.get() == 1:
            score += 1
    messagebox.showinfo("Результат", f"{surname} ({group}) набрав(ла) {score} балів із 10.")

def clear_all():
    entry_surname.delete(0, tk.END)
    entry_group.delete(0, tk.END)
    q1.set(-1)
    q2_a.set(False)
    q2_b.set(False)
    q2_c.set(False)
    q3.delete(0, tk.END)
    for v in answers:
        v.set(-1)
    warning_label.config(text="")
    canvas.yview_moveto(0)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=15)

btn_submit = tk.Button(frame_buttons, text="Відправити результат", font=("Arial", 12),
                       bg="#4caf50", fg="white", width=20, command=submit)
btn_submit.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(frame_buttons, text="Очистити", font=("Arial", 12),
                      bg="#f44336", fg="white", width=20, command=clear_all)
btn_clear.grid(row=1, column=0, padx=10)

root.mainloop()
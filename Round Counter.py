#!/usr/local/bin/pypy3.10
#!/Users/michael/project/round-countdown/venv/bin/python3

BLACKISH = "#0F0E0E"
REDISH = "#7B0828"
BLUEISH = "#8DAA9D"
PURPLEISH = "#522B47"
WHITEISH = "#FBF5F3"
BUTTON_WIDTH = 20

MAIN_BG = PURPLEISH

import tkinter as tk
import tkmacosx as tkx

LARGE_FONT = ("Verdana", 18)


class RoundCounterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Round Counter")
        self.config(padx=20, pady=20)
        container = tk.Frame(self)
        container.config(width=300, height=400)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPage, AddPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        if cont == AddPage:
            frame.selection.set(10)
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.round = 0
        tk.Button(self, text="Next", width=BUTTON_WIDTH, command=self.do_next).pack()
        self.controller = controller
        self.timers = tk.Frame(self)
        self.timers.pack()

        tk.Label(self.timers, text="Timers").pack()
        tk.Button(self, text="Prev", width=BUTTON_WIDTH, command=self.do_prev).pack()
        tk.Button(self, text="Reset", width=BUTTON_WIDTH, command=self.do_reset).pack()
        tk.Button(
            self,
            text="Add",
            width=BUTTON_WIDTH,
            command=lambda: controller.show_frame(AddPage),
        ).pack()

    def tick_counters(self, tick="add"):
        for w in self.timers.winfo_children():
            if isinstance(w, tk.Frame):
                for b in w.winfo_children():
                    if isinstance(b, tkx.Button):
                        value = int(b["text"])
                        new_value = value - 1
                        if tick != "add":
                            new_value = value + 1
                        if new_value >= 0:
                            b.configure(text=str(new_value))
                        if new_value == 1:
                            b.configure(bg="orange")
                        if new_value == 0:
                            b.configure(bg="red")
                        if new_value > 1:
                            b.configure(bg=WHITEISH)

    def do_next(self):
        self.round += 1
        self.update_label(f"Timers: Round = {self.round}")
        self.tick_counters("add")

    def do_reset(self):
        self.round = 0
        self.update_label("Timers")
        for w in self.timers.winfo_children():
            if isinstance(w, tk.Frame):
                w.pack_forget()

    def do_prev(self):
        if self.round == 0:
            return
        self.round -= 1
        self.update_label(f"Timers: Round = {self.round}")
        self.tick_counters("subtract")

    def update_label(self, value):
        for w in self.timers.winfo_children():
            if isinstance(w, tk.Label):
                w.config(text=value)

    def add_timer(self, value):
        new_timer = tk.Frame(self.timers)
        new_entry = tk.Entry(new_timer, width=int(BUTTON_WIDTH * 0.66))
        new_entry.pack(side="right")
        new_entry.focus()
        tkx.Button(
            new_timer,
            width=45,
            bg=WHITEISH,
            fg="black",
            text=str(value),
            highlightbackground="#82CC6C",
            highlightthickness=0,
            borderwidth=0,
            relief="groove",
            padx=0,
            pady=0,
            command=new_timer.pack_forget,
        ).pack(side="right")

        new_timer.pack()
        self.controller.show_frame(MainPage)


class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add A Timer", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.controller = controller
        self.selection = tk.IntVar()

        tk.Radiobutton(self, text="1 round", value=1, variable=self.selection).pack()
        tk.Radiobutton(self, text="1 min", value=10, variable=self.selection).pack()
        tk.Radiobutton(self, text="5 min", value=50, variable=self.selection).pack()
        tk.Radiobutton(self, text="10 min", value=100, variable=self.selection).pack()

        self.selection.set(10)
        button = tk.Button(
            self,
            text="Add",
            command=lambda: controller.frames[MainPage].add_timer(self.selection.get()),
        )
        # button.focus()
        button.pack()

    def back(self):
        self.controller.show_frame(MainPage)

    def add_timer(self):
        print(self.selection.get())
        self.back()


if __name__ == "__main__":
    app = RoundCounterApp()
    app.mainloop()

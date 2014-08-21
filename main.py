from tkinter import *


def show_result() -> None:
    res = Tk()
    res.title("Result")

    f = Frame(res)
    Label(f, text=f"Your height is {height.get()}cm") \
        .pack(padx=(0, 20))
    f.pack(padx=20, pady=15)

    Button(res, text="OK", command=res.destroy, width=8) \
        .pack(side=RIGHT, padx=(0, 10), pady=(0, 10))

    res.mainloop()


if __name__ == "__main__":
    win = Tk()
    win.title("Height caculator tool")

    f = Frame(win)

    Label(f, text="Input your height") \
        .pack(side=LEFT)

    height = IntVar(win)
    Entry(f, textvariable=height, width=13) \
        .pack(side=LEFT, padx=5)

    Label(f, text="cm") \
        .pack(side=LEFT)

    f.pack(padx=10, pady=10)

    Button(win, text="Yes", command=show_result, width=8) \
        .pack(side=RIGHT, padx=(0, 10), pady=(0, 10))

    win.mainloop()

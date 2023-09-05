from tkinter import *
from Colours import colours
import os

information: dict[str, list] = {}
logs_loaded: int = 0


def load_logs() -> None:
    global logs_loaded
    directory: str = "logs"
    for filename in os.listdir(directory):
        if filename != "log_instructions.txt":
            animal: str = filename.split(".")[0]
            information[animal] = []
            f = open((directory + "/" + filename), "r")
            file_lines = f.readlines()
            last_line = file_lines[-1]
            sighting = last_line.replace(" ", "")
            sighting = sighting.split(":")[1]
            information[animal].append(sighting)

            summary = ""
            for i in range(2, 3):
                summary += file_lines[i]
            information[animal].append(summary)
            f.close()
            logs_loaded += 1


def display_GUI() -> None:
    load_logs()

    # Main Window
    root = Tk()
    root.title("Conservation Tracker")
    root.geometry("600x500+200+200")
    root.configure(bg=colours["dark-grey"])
    root.resizable(width=False, height=False)
    root.rowconfigure(2, weight=1)
    root.columnconfigure(2, weight=1)

    if logs_loaded == 0:
        empty_logs_label = Label(root,
                                 text="No Logs Available",
                                 bg=colours["dark-grey"],
                                 fg=colours["text-background"],
                                 font="Helvetica 30 bold",
                                 )
        empty_logs_label.pack()
    else:
        # Right Column
        default = list(information.keys())[0]
        animal_label = Label(root,
                             text=default + f" - [Sightings: {information[default][0]}]",
                             bg=colours["dark-grey"],
                             fg=colours["text-background"],
                             font="Helvetica 20 bold", anchor=N)
        animal_label.grid(column=1, row=1, sticky=W + E + N + S)

        summary_label = Label(root,
                              text=information[default][1],
                              bg=colours["dark-grey"],
                              fg=colours["text-background"],
                              font="Helvetica 12",
                              wraplength=450, )
        summary_label.grid(column=1, row=2, sticky=W + E + N + S)

        def update_content():
            current_selection = lb.get(lb.curselection())
            sightings = information[current_selection][0]
            summary = information[current_selection][1]
            animal_label.config(text=current_selection + f" - [Sightings: {sightings}]")
            summary_label.config(text=summary)

        # Left Column
        var = StringVar(root, value=[animal for animal in information.keys()])
        lb = Listbox(root,
                     listvariable=var,
                     bd=2,
                     background=colours["text-background"],
                     selectbackground=colours["teal"],
                     selectforeground=colours["text-background"],
                     font="Helvetica 18 bold")
        lb.grid(column=2, row=2, sticky=W + E + N + S)
        lb.selection_set(first=0)

        button = Button(root, text="Confirm",
                        command=lambda: update_content(),
                        )
        button.grid(column=2, row=1, sticky=W + E + N + S)

    root.mainloop()


if __name__ == "__main__":
    display_GUI()

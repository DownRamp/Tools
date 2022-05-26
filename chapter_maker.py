#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
import customtkinter

class Window():
    def __init__(self, main):
        width_val = 200
        self.main = main

        self.win = customtkinter.CTkFrame(master=self.main, corner_radius=15)
        self.win.pack(fill=BOTH, expand =1)
        self.canvas = Canvas(self.win)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scroll = ttk.Scrollbar(self.win, orient=VERTICAL, command = self.canvas.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand = self.scroll.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))
        self.frm = customtkinter.CTkFrame(master=self.canvas, corner_radius=15)
        self.canvas.create_window((0,0), window = self.frm, anchor="nw")
        self.label = customtkinter.CTkLabel(master=self.frm, justify=LEFT, text="Enter chapter information")
        self.label.pack(padx=20, pady=20)
        self.entry_title = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Title")
        self.entry_title.pack(pady=20, padx=20)
        self.entry_des = customtkinter.CTkEntry(master=self.frm,
                                    height = 120,
                                    width=width_val,
                                    placeholder_text="Enter Description")
        self.entry_des.pack(pady=20, padx=20)
        self.entry_why = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Why")
        self.entry_why.pack(pady=20, padx=20)
        self.entry_set = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Setup instructions (seperate with commas)")
        self.entry_set.pack(pady=20, padx=20)
        self.entry_todo = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter To-dos (seperate with commas)")
        self.entry_todo.pack(pady=20, padx=20)
        self.entry_chapter_num = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Chapter number")
        self.entry_chapter_num.pack(pady=20, padx=20)
        self.entry_next = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Next steps (seperate with commas)")
        self.entry_next.pack(pady=20, padx=20)
        self.entry_git = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Github Link")
        self.entry_git.pack(pady=20, padx=20)

        self.button =customtkinter.CTkButton(master=self.frm, text="Submit", command=lambda: self.enter_values(
            self.entry_title.get(), self.entry_des.get(), self.entry_why.get(), self.entry_set.get(), self.entry_todo.get(),
            self.entry_chapter_num.get() ,self.entry_next.get(), self.entry_git.get()
        ))
        self.button.pack(padx=20, pady=20)

    def enter_values(self, title, description, why, setup_instructions, to_do, chapter_num, next_steps, github_links):
        self.chapter = []
        self.chapter.append("# "+title)
        self.chapter.append("\n---\n")
        self.chapter.append("## Description: ")
        self.chapter.append(description)
        self.chapter.append("\n---\n")
        self.chapter.append("## Why: ")
        self.chapter.append(why)
        self.chapter.append("\n---\n")
        self.chapter.append("## Setup Instructions: ")
        self.count = 1
        for item in setup_instructions.split(","):
            value = "{}. {}".format(self.count, item)
            self.chapter.append(value)
            self.count+=1
        self.chapter.append("\n---\n")
        self.chapter.append("## To do: ")
        self.count = 1
        for item in to_do.split(","):
            value = "{}. {}".format(self.count, item)
            self.chapter.append(value)
            self.count+=1
        self.chapter.append("\n---\n")
        self.code_to_text(self.chapter)
        self.chapter.append("[Github link] {}".format(github_links))
        self.chapter.append("## Next Steps: ")
        self.count = 1
        for item in next_steps.split(","):
            value = "{}. {}".format(self.count, item)
            self.chapter.append(value)
            self.count+=1
        self.chapter.append("\n---\n")
        chap_name = "Chapter_{}_{}.md".format(chapter_num.strip(), title.strip())
        with open(chap_name, 'w') as f:
            for item in self.chapter:
                f.write("%s\n" % item)
        self.main.quit()

    def code_to_text(self, chapter):
        code = []
        chapter.append("## Code: ")

        f = open('code.txt', 'r+')

        for line in f.readlines():
            if "import" in line:
                line = ">" + line
            if "#" in line:
                line = line.replace("#", "###")
            chapter.append("{}\n".format(line))
            code.append(line)
        f.close()
        chapter.append("\n---\n")
        chapter.append("## Translation: ")
        for c in code:
            chapter.append("{}\n".format(self.translate(c)))


    def translate(self, line):
        current = ["<=",">=","<","+=","-=",".init()","__init__(self):", ".", "def", "=", "global", 'if __name__ == "__main__":', "Tk()", "import", "(", ")", "!=", "!", "strftime", "*"]

        change_to = ["less then or equal to ","greater then or equal to ","less then ","add to ","subtract from "," initiate ","initiate class ", " ", "Define a function called ", "variable equal to ", "fetch global variable ", "basic call if file initiated ",
        "initiate tkinter ", "Import package called ", ' function call with parameters: "', '"', "not equal ", "not ", "turn time into string ", "* (means grab everything) "]

        for i in range(len(current)):
            line = line.replace(current[i], change_to[i])
        return line

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
    root = customtkinter.CTk()
    root.title("Chapter maker")
    root.geometry("300x800")
    Window(root)
    root.mainloop()

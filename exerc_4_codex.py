from tkinter import *

to_do = []

while True:
    try:
        root = Tk()
        root.geometry("300x300")
        # Title explain the format of the input
        root.title("Add + task or Delete + task")

        def format_str(string):
        # Format string so the words only have letters from the alphabet
            new_str = []
            for j in range(len(string)):
                if string[j].isalpha():
                    new_str.append(string[j])
            string = "".join(new_str)
            return string

        def format_list(list_to_do):
        # Format the output
            to_do = " ".join(list_to_do)
            new_to_do = 'to-do list: ' + to_do + '\n'
            return new_to_do

        def Take_input():
            INPUT = input_text.get(1.0, 2.0).split(" ")

            # To-do list
            task = INPUT[1]
            task = format_str(task)
            action = INPUT[0]
            if action == "add":
                to_do.append(task)
            else:
                to_do.remove(task)
            new_to_do = format_list(to_do)
            print("to-do list: ", new_to_do)

            #inserting the output in the widget
            Output.insert(END, new_to_do)

        # Editing the interface
        img = PhotoImage(file ="lasers-3.png")
        img_label = Label(root, image = img)
        img_label.place(x=0, y=0)

        input_text = Text(root, height = 10,
                        width = 25,
                        bg = "#10b336")
        
        Output = Text(root, height = 5, 
                    width = 25, 
                    bg = "#10b336")
        
        Screen = Button(root, height = 2,
                        width = 20, 
                        bg = '#03a300',
                        text ="Show my to-do list",
                        command = lambda:Take_input())

        lbl.pack()
        input_text.pack()
        Screen.pack()
        Output.pack()

        mainloop()

    except EOFError:
        break

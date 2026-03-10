import tkinter as tk

class MyGUI:
    def __init__(self):
        #create the main window
        self.main_window = tk.Tk()
        #create 2 lables in the main window
        self.label1 = tk.Label(self.main_window, text="Hello, welcome to my GUI!")  
        self.label2 = tk.Label(self.main_window, text="This is how it is done.")


        self.label1.pack(side='top')
        self.label2.pack(side='top')

        self.main_window.title("My first GUI")





        #Enter the tkinter main loop
        tk.mainloop()




#create an intance of the MyGUI class
my_gui = MyGUI(tk.Tk())

    
#02 ví dụ về kilometers đổi qua miles

import tkinter as tk02
class KiloConverterGUI:
    def __init__(self):
        self.main_window = tk02.Tk()

        self.top_frame = tk02.Frame(self.main_window)
        self.bottom_frame = tk02.Frame(self.main_window)

        #create the label and entry widgets for the top frame
        self.pompt_label = tk02.Label(self.top_frame, text="Enter a distance in kilometers:")
        self.kilo_entry = tk02.Entry(self.top_frame, width=10)

        #pack the label and entry widgets
        self.pompt_label.pack(side='left')  
        self.kilo_entry.pack(side='left')

        # create the convert button and result label for the bottom frame
        self.convert_button = tk02.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.quit_button = tk02.Button(self.bottom_frame, text= "Quit", command=self.main.window.destroy)

        #Back the button
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        #Back the frames 
        self.top_button.pack(side='top')
        self.bottom_button.pack(side='top')

        #Enter the main tkinter
        tk02.mainloop()

        def convert(self):
            kilo = float(self.kilo_entry.get())
            miles = kilo * 0.6214
            tk02.messagebox.showinfo('Result", str(kilo) kilometers is equal to str(miles) miles.')

if __name__ == "__main__":
    kilo_conveter = KiloConverterGUI()


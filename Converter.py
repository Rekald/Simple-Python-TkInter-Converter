import tkinter as tk
from tkinter.font import nametofont
from tkinter import ttk
import Cfuncs as CF

class Root_Frame(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0, 0)
        self.title("Simple Unit Converter")
        self.container = ttk.Frame(self)
        self.container.grid(row=0, column=0, padx=5, pady=5, sticky="EW")
        self.label_container = ttk.Frame(self.container)
        self.label_container.grid(row=1, column=1)

    def frame_creation(self, *args, row, column, tocall, labelrow):
        if tocall in tocall_dictionary["Convcall"]:
            new_frame = Conversion_Frame(self.container, *args, tocall)
            new_frame.grid(row=row, column=column, padx=10, pady=10)
            new_label = ttk.Label(self.label_container, textvariable=new_frame.label_memory_slot)
            new_frame.label_memory_slot.set(f"Slot:{labelrow}")
            new_label.grid(column=0, row=labelrow)
            return new_frame

class Conversion_Frame(ttk.Frame):
    def __init__(self, container, combobox_items, tocall):
        super().__init__(container)

        self.input_box_value = tk.StringVar()
        self.input_box_value.trace('w', self.entrylimit)
        self.input_box_value.trace('w', self.autoconvert)
        self.label_value = tk.StringVar()
        self.Upper_combobox_value = tk.StringVar(value=combobox_items[0])
        self.Upper_combobox_value.trace('w', self.autoconvert)
        self.Bottom_Combobox_value = tk.StringVar(value=combobox_items[0])
        self.Bottom_Combobox_value.trace('w', self.autoconvert)
        self.label_memory_slot = tk.StringVar()
        self.tocall = tocall

        upper_combobox = ttk.Combobox(self, textvariable=self.Upper_combobox_value)
        upper_combobox["values"] = combobox_items
        upper_combobox["state"] = "readonly"
        upper_combobox.grid(row=0, column=0, sticky="EW", pady=(0, 2.5))

        bottom_combobox = ttk.Combobox(self, textvariable=self.Bottom_Combobox_value)
        bottom_combobox["values"] = combobox_items
        bottom_combobox["state"] = "readonly"
        bottom_combobox.grid(row=1, column=0, sticky="EW", pady=(2.5, 2.5))

        input_box = ttk.Entry(self, width=10, textvariable=self.input_box_value, font=("Arial", 10))
        input_box.grid(row=0, column=1, padx=3, sticky="EW", pady=(0,2.5))
        input_box.focus()

        bottom_label = ttk.Label(self, textvariable=self.label_value)
        bottom_label.grid(row = 1 , column = 1, sticky = "EW",pady =(2.5, 2.5), padx = (2.5,0))

        conversion_button = ttk.Button(self, text = "Save",command = self.save_function)
        conversion_button.grid(row = 2, column = 0, sticky = "EW", pady = (2.5, 0))

    def converting_caller(self):
        value = ((CF.hub(self.tocall, self.input_box_value.get(),
                                     self.Upper_combobox_value.get(),
                                     self.Bottom_Combobox_value.get())))
        if len(value) > 12:
            self.label_value.set("Out of Scale")
        else:
            self.label_value.set(value)

    def entrylimit(self,*args):
            if len(self.input_box_value.get()) >= 8  : self.input_box_value.set(self.input_box_value.get()[:8])

    def autoconvert(self,*args):
        if len(self.input_box_value.get())!= 0:
            self.converting_caller()
        else:
            self.label_value.set("")
    def save_function(self):
        if len(self.input_box_value.get()) != 0:
            try:
                self.label_memory_slot.set(f"From {float(self.input_box_value.get())} {self.Upper_combobox_value.get()} \n"
                                   f"to {self.Bottom_Combobox_value.get()}: {self.label_value.get()}")
            except:pass
        else:
            pass

conversion_array = [("Kilometers", "Hectometres", "Decameters", "Meters",
                     "Decimeters", "Centimeters", "Millimeters", "Feet", "Inch"),
                     ("Celsius", "Fahrenheit", "Kelvin"), ("Kilograms", "Grams", "Pound", "Ounces")]

tocall_dictionary = {"Convcall": ["Mconv", "Tconv", "Wconv"]}

root = Root_Frame()
style = ttk.Style(root)
style.theme_use("xpnative")
nametofont("TkDefaultFont").configure(size=10)

first_box = root.frame_creation(conversion_array[0], row=0, column=0,
                                tocall=tocall_dictionary["Convcall"][0], labelrow=0)
second_box = root.frame_creation(conversion_array[1], row=0, column=1,
                                 tocall=tocall_dictionary["Convcall"][1], labelrow=1)
third_box = root.frame_creation(conversion_array[2], row=1, column=0,
                                tocall=tocall_dictionary["Convcall"][2], labelrow=2)

root.mainloop()

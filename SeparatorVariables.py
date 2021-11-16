import tkinter as tk
from tkinter import ttk

class SeparatorVariables(ttk.Frame):
    def __init__(self, parent, Psepvar, Tsepvar):
        ttk.Frame.__init__(self, parent)

        # create variables
        self.P_sep_var = Psepvar
        self.T_sep_var = Tsepvar
        self.print_var = tk.DoubleVar()

        # create widgets
        self.setup_widgets()
    

    def setup_widgets(self):
        # create label frame
        self.separator_variables_frame = ttk.LabelFrame(self, text="Separator Variables")
        self.separator_variables_frame.pack(fill='x')

        # create other widgets
        # label
        self.P_sep = ttk.Label(self.separator_variables_frame, text="Separator Pressure")
        self.P_sep.grid(row=0, column=0, padx=10, pady=5, sticky='W')

        self.P_sep_entry = ttk.Entry(self.separator_variables_frame, textvariable=self.P_sep_var)
        self.P_sep_entry.grid(row=0, column=1, padx=10, pady=5)

        self.P_sep_unit = ttk.Label(self.separator_variables_frame, text="psia")
        self.P_sep_unit.grid(row=0, column=2, padx=10, pady=5)

        self.T_sep = ttk.Label(self.separator_variables_frame, text="Separator Temperature")
        self.T_sep.grid(row=1, column=0, padx=10, pady=5, sticky='W')

        self.T_sep_entry = ttk.Entry(self.separator_variables_frame, textvariable=self.T_sep_var)
        self.T_sep_entry.grid(row=1, column=1, padx=10, pady=5)

        self.T_sep_unit = ttk.Label(self.separator_variables_frame, text="°F")
        self.T_sep_unit.grid(row=1, column=2, padx=10, pady=5)

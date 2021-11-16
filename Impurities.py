import tkinter as tk
from tkinter import ttk

class Impurities(ttk.Frame):
	def __init__(self, parent, CO2Var, H2SVar, N2Var):
		ttk.Frame.__init__(self, parent)

		# control variables
		self.CO2_var = CO2Var
		self.H2S_var = H2SVar
		self.N2_var = N2Var

		self.setup_widgets()


	def setup_widgets(self):
		self.Impurities_labelframe = ttk.LabelFrame(self, text="Impurities (mole fraction)")
		self.Impurities_labelframe.pack(fill="x", expand=True)

		# CO2
		self.CO2_label = ttk.Label(self.Impurities_labelframe, text="CO2")
		self.CO2_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

		self.CO2_spinbox = ttk.Spinbox(self.Impurities_labelframe, 
			textvariable = self.CO2_var, 
			from_=0, 
			to=1, 
			increment=0.01)
		self.CO2_spinbox.insert(0, "")
		self.CO2_spinbox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

		# H2S
		self.H2S_label = ttk.Label(self.Impurities_labelframe, text="H2S")
		self.H2S_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

		self.H2S_spinbox = ttk.Spinbox(self.Impurities_labelframe, 
			textvariable = self.H2S_var, 
			from_=0, 
			to=1, 
			increment=0.01)
		self.H2S_spinbox.insert(0, '')
		self.H2S_spinbox.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

		# N2
		self.N2_label = ttk.Label(self.Impurities_labelframe, text="N2")
		self.N2_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

		self.N2_spinbox = ttk.Spinbox(self.Impurities_labelframe, 
			textvariable = self.N2_var, 
			from_=0, 
			to=1, 
			increment=0.01)
		self.N2_spinbox.insert(0, "")
		self.N2_spinbox.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
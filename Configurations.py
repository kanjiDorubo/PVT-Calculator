import tkinter as tk
from tkinter import ttk

class Configurations(ttk.Frame):
	def __init__(self, parent, ConfigCorrVar, BgUnitVar, MiuWVar):
		ttk.Frame.__init__(self, parent)

		# control variables
		self.config_corr_var = ConfigCorrVar
		self.Bg_unit_var = BgUnitVar
		self.Miu_w_var = MiuWVar

		self.config_corr_list = ['Select correlation', 'Vasquez-Beggs']
		self.Bg_unit_list = ['Select unit', 'idk :/']
		self.Miu_w_list = ['Select correlation', 'idk :/']

		self.setup_widgets()

# 
	def setup_widgets(self):
		self.Configurations_labelframe = ttk.LabelFrame(self, text="Configurations")
		self.Configurations_labelframe.pack(fill='x')

		# Config correlations
		def config_corr_select(event):
			self.config_corr_var.set(self.config_corr.get())

		self.config_corr_label = ttk.Label(self.Configurations_labelframe, text="Select correlation")
		self.config_corr_label.grid(row=0, column=0, padx=10, pady=5)

		self.config_corr = ttk.Combobox(self.Configurations_labelframe, 
			state = 'readonly',
			values = self.config_corr_list)
		self.config_corr.current(0)
		self.config_corr.bind('<<ComboboxSelected>>', config_corr_select)
		self.config_corr.grid(row=0, column=1, padx=10, pady=5)

		# Bg unit
		def Bg_unit_select(event):
			self.Bg_unit_var.set(self.Bg_unit.get())

		self.Bg_unit_label = ttk.Label(self.Configurations_labelframe, text="Bg unit")
		self.Bg_unit_label.grid(row=1, column=0, padx=10, pady=5)
		
		self.Bg_unit = ttk.Combobox(self.Configurations_labelframe,
			state = 'readonly',
			values = self.Bg_unit_list)
		self.Bg_unit.current(0)
		self.Bg_unit.bind("<<ComboboxSelected>>", Bg_unit_select)
		self.Bg_unit.grid(row=1, column=1, padx=10, pady=5)

		# Miu W
		def Miu_W_select(event):
			self.Miu_w_var.set(self.Miu_w.get())

		self.Miu_w_label = ttk.Label(self.Configurations_labelframe, text="µw correlation")
		self.Miu_w_label.grid(row=2, column=0, padx=10, pady=5)

		self.Miu_w = ttk.Combobox(self.Configurations_labelframe,
			state = 'readonly',
			values = self.Miu_w_list)
		self.Miu_w.current(0)
		self.Miu_w.bind("<<ComboboxSelected>>", Miu_W_select)
		self.Miu_w.grid(row=2, column=1, padx=10, pady=5)

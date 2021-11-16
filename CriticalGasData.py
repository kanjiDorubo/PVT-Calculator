import tkinter as tk
from tkinter import ttk

class CriticalGasData(ttk.Frame):
	def __init__(self, parent, GasCorrVar, PpcVar, TpcVar, PprVar, TprVar):
		ttk.Frame.__init__(self, parent)

		# control variables
		self.gas_corr_var = GasCorrVar
		self.Ppc_var = PpcVar
		self.Tpc_var = TpcVar
		self.Ppr_var = PprVar
		self.Tpr_var = TprVar

		self.readonly_combo_list = ['Select correlation','Standing', 'Vasquez-Beggs']

		self.setup_widgets()


	def setup_widgets(self):
		self.CriticalGasData_labelframe = ttk.LabelFrame(self, text="Critical Gas Data")
		self.CriticalGasData_labelframe.pack(fill='x')

		def combo_selected(event):
			self.gas_corr_var.set(self.gas_corr_select.get())

		# Select correlation
		self.gas_corr_select_label = ttk.Label(self.CriticalGasData_labelframe, 
			text="Gas Correlation")
		
		self.gas_corr_select_label.grid(row=0, column=0, padx=10, pady=5)

		self.gas_corr_select = ttk.Combobox(self.CriticalGasData_labelframe,
			state='readonly',
			values=self.readonly_combo_list)
		self.gas_corr_select.current(0)
		self.gas_corr_select.bind('<<ComboboxSelected>>', combo_selected)
		self.gas_corr_select.grid(row=0, column=1, padx=10, pady=15)

		# Ppc entry
		self.Ppc_label = ttk.Label(self.CriticalGasData_labelframe, text="Ppc")
		self.Ppc_label.grid(row=1, column=0, padx=10, pady=5)

		self.Ppc = ttk.Entry(self.CriticalGasData_labelframe, 
			textvariable=self.Ppc_var)
		self.Ppc.grid(row=1, column=1, padx=10, pady=5)

		self.Ppc_unit = ttk.Label(self.CriticalGasData_labelframe, text="psia")
		self.Ppc_unit.grid(row=1, column=2, padx=10, pady=5)

		# Tpc entry
		self.Tpc_label = ttk.Label(self.CriticalGasData_labelframe, text="Tpc")
		self.Tpc_label.grid(row=2, column=0, padx=10, pady=5)

		self.Tpc = ttk.Entry(self.CriticalGasData_labelframe, 
			textvariable=self.Tpc_var)
		self.Tpc.grid(row=2, column=1, padx=10, pady=5)

		self.Tpc_unit = ttk.Label(self.CriticalGasData_labelframe, text="°F")
		self.Tpc_unit.grid(row=2, column=2, padx=10, pady=5)

		# Ppr
		self.Ppr_label = ttk.Label(self.CriticalGasData_labelframe, text="Ppr")
		self.Ppr_label.grid(row=3, column=0, padx=10, pady=5)

		self.Ppr = ttk.Entry(self.CriticalGasData_labelframe, 
			textvariable = self.Ppr_var)
		self.Ppr.grid(row=3, column=1, padx=10, pady=5)

		self.Ppr_unit = ttk.Label(self.CriticalGasData_labelframe, text="psia")
		self.Ppr_unit.grid(row=3, column=2, padx=10, pady=5)

		# Tpr
		self.Tpr_label = ttk.Label(self.CriticalGasData_labelframe, text="Tpr")
		self.Tpr_label.grid(row=4, column=0, padx=10, pady=5)

		self.Tpr = ttk.Entry(self.CriticalGasData_labelframe, 
			textvariable = self.Tpr_var)
		self.Tpr.grid(row=4, column=1, padx=10, pady=5)

		self.Tpr_unit = ttk.Label(self.CriticalGasData_labelframe, text="°F")
		self.Tpr_unit.grid(row=4, column=2, padx=10, pady=5)
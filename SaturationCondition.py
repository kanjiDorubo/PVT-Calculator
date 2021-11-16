import tkinter as tk
from tkinter import ttk

class SaturationCondition(ttk.Frame):
	def __init__(self, parent, ConditionVar, TDSVar):
		ttk.Frame.__init__(self, parent)

		# control variables
		self.readonly_combo_list = ['Select condition','Gas Saturated Brine']

		self.condition_var = ConditionVar
		self.tds_var = TDSVar

		self.setup_widgets()


	def setup_widgets(self):
		self.SaturationCondition_labelframe = ttk.LabelFrame(self, text="Saturation Condition")
		self.SaturationCondition_labelframe.pack(fill='x')

		def combo_selected(event):
			self.condition_var.set(self.saturation_condition.get())

		# saturation condition
		self.saturation_condition_label = ttk.Label(self.SaturationCondition_labelframe, text="Select condition")
		self.saturation_condition_label.grid(row=0, column=0, padx=10, pady=5)

		self.saturation_condition = ttk.Combobox(self.SaturationCondition_labelframe,
			state='readonly',
			values=self.readonly_combo_list)
		self.saturation_condition.current(0)
		self.saturation_condition.bind('<<ComboboxSelected>>', combo_selected)
		self.saturation_condition.grid(row=0, column=1, padx=10, pady=5)

		# TDS
		self.tds_label = ttk.Label(self.SaturationCondition_labelframe, text="TDS")
		self.tds_label.grid(row=1, column=0, padx=10, pady=5)

		self.tds = ttk.Entry(self.SaturationCondition_labelframe,
			textvariable = self.tds_var)
		self.tds.grid(row=1, column=1, padx=10, pady=5)

		self.tds_unit = ttk.Label(self.SaturationCondition_labelframe, text="% Weighted")
		self.tds_unit.grid(row=1, column=2, padx=10, pady=5)
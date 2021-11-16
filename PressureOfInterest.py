import tkinter as tk
from tkinter import ttk

class PressureOfInterest(ttk.Frame):
	def __init__(self, parent, Pinterestvar):
		ttk.Frame.__init__(self, parent)

		# control variables
		self.P_interest_var = Pinterestvar

		self.setup_widgets()

	def setup_widgets(self):
		self.PressureOfInterest_labelframe = ttk.LabelFrame(self, text="Pressure of Interest")
		self.PressureOfInterest_labelframe.pack(fill='x')

		self.P_interest_label = ttk.Label(self.PressureOfInterest_labelframe, text = "P")
		self.P_interest_label.grid(row=0, column=0, padx=10, pady=5)

		self.P_interest = ttk.Entry(self.PressureOfInterest_labelframe, textvariable = self.P_interest_var)
		self.P_interest.grid(row=0, column=1, padx=10, pady=5)

		self.P_interest_unit = ttk.Label(self.PressureOfInterest_labelframe, text="psia")
		self.P_interest_unit.grid(row=0, column=2, padx=5, pady=5)
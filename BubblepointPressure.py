import tkinter as tk
from tkinter import ttk

class BubblepointPressure(ttk.Frame):
	def __init__(self, parent, Pbvar):
		ttk.Frame.__init__(self, parent)

		# control variables
		self.Pb_var = Pbvar

		# setup widgets
		self.setup_widgets()

	def setup_widgets(self):
		self.Pb_labelframe = ttk.LabelFrame(self, text="Bubblepoint Pressure")
		self.Pb_labelframe.pack(fill='x')

		self.Pb_label = ttk.Label(self.Pb_labelframe, text="Bubblepoint Pressure (Pb)")
		self.Pb_label.grid(row = 0, column = 0, padx=10, pady=5)
		
		self.Pb = ttk.Entry(self.Pb_labelframe, textvariable = self.Pb_var)
		self.Pb.grid(row = 0, column = 1, padx=10, pady=5)

		self.Pb_unit = ttk.Label(self.Pb_labelframe, text = "psia")
		self.Pb_unit.grid(row = 0, column = 2, padx=10, pady=5)

		

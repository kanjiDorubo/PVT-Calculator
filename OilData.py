import tkinter as tk
from tkinter import ttk


class OilData(ttk.Frame):
	def __init__(self, parent, oilapivar, RsatPbvar):
		ttk.Frame.__init__(self, parent)

		# create variable
		self.oil_api_var = oilapivar
		self.Rs_at_Pb_var = RsatPbvar

		# setup widgets
		self.setup_widgets()

	def setup_widgets(self):
		# Oil data frame
		self.oil_data_labelframe = ttk.LabelFrame(self, text="Oil Data")
		self.oil_data_labelframe.pack(fill='x')

		# oil api
		self.oil_api = ttk.Entry(self.oil_data_labelframe, textvariable = self.oil_api_var)
		self.oil_api.grid(row=0, column=1, padx=10, pady=5)

		self.oil_api_label = ttk.Label(self.oil_data_labelframe, text="Oil API")
		self.oil_api_label.grid(row=0, sticky="W", column=0, padx=10, pady=5)

		self.oil_api_unit_label = ttk.Label(self.oil_data_labelframe, text="°API")
		self.oil_api_unit_label.grid(row=0, sticky="W", column=2, padx=10, pady=5)

		# Rs @ Pb
		self.Rs_at_Pb = ttk.Entry(self.oil_data_labelframe, textvariable = self.Rs_at_Pb_var)
		self.Rs_at_Pb.grid(row=1, column=1, padx=10, pady=5)

		self.Rs_at_Pb_label = ttk.Label(self.oil_data_labelframe, text="Rs @ Pb")
		self.Rs_at_Pb_label.grid(row=1, sticky="W", column=0, padx=10, pady=5)

		self.Rs_at_Pb_unit_label = ttk.Label(self.oil_data_labelframe, text="MSCF/STB")
		self.Rs_at_Pb_unit_label.grid(row=1, sticky="W", column=2, padx=10, pady=5)

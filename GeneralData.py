import tkinter as tk
from tkinter import ttk


class GeneralData(ttk.Frame):
	def __init__(self, parent, Tresvar, Presvar, Pscvar, Gas_gravity_var):
		ttk.Frame.__init__(self, parent)

		# create variable
		self.P_res_var = Presvar
		self.T_res_var = Tresvar
		self.P_sc_var = Pscvar
		self.Gas_gravity_var = Gas_gravity_var

		# setup widgets
		self.setup_widgets()

	def setup_widgets(self):
		 # general data input frame
		self.general_data_frame = ttk.LabelFrame(self, text="General Data")
		self.general_data_frame.pack(fill='x')

		# T reservoir
		self.T_res = ttk.Entry(self.general_data_frame, textvariable = self.T_res_var)
		self.T_res.grid(row=0, column=1,padx=10, pady=5)

		self.T_res_label = ttk.Label(self.general_data_frame, text="Reservoir Temperature")
		self.T_res_label.grid(row=0, sticky="W", column=0, padx=10, pady=5)

		self.T_res_unit_label = ttk.Label(self.general_data_frame, text="°F")
		self.T_res_unit_label.grid(row=0, sticky="W", column=2, padx=10, pady=5)

		# Initial res pressure
		self.P_init = ttk.Entry(self.general_data_frame, textvariable = self.P_res_var)
		self.P_init.grid(row=1, column=1, padx=10, pady=5)

		self.P_init_label = ttk.Label(self.general_data_frame, text="Initial Reservoir Pressure")
		self.P_init_label.grid(row=1, sticky="W", column=0, padx=10, pady=5)

		self.P_init_unit_label = ttk.Label(self.general_data_frame, text="psia")
		self.P_init_unit_label.grid(row=1, sticky="W", column=2, padx=10, pady=5)

		# standard pressure
		self.P_sc = ttk.Entry(self.general_data_frame, textvariable = self.P_sc_var)
		self.P_sc.grid(row=2, column=1, padx=10, pady=5)

		self.P_sc_label = ttk.Label(self.general_data_frame, text="Standard Pressure")
		self.P_sc_label.grid(row=2, sticky="W", column=0, padx=10, pady=5)

		self.P_sc_unit_label = ttk.Label(self.general_data_frame, text="psia")
		self.P_sc_unit_label.grid(row=2, sticky="W", column=2, padx=10, pady=5)

		# gas gravity
		self.Gas_SG = ttk.Entry(self.general_data_frame, textvariable = self.Gas_gravity_var)
		self.Gas_SG.grid(row=3, column=1, padx=10, pady=5)

		self.Gas_SG_label = ttk.Label(self.general_data_frame, text="Gas Gravity (Air = 1.0)")
		self.Gas_SG_label.grid(row=3, sticky="W", column=0, padx=10, pady=5)

		self.Gas_SG_unit_label = ttk.Label(self.general_data_frame, text="")
		self.Gas_SG_unit_label.grid(row=3, sticky="W", column=2, padx=10, pady=5)

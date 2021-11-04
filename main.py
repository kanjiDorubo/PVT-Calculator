import tkinter as tk
from tkinter import ttk
from functions import *

class App(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self)
    
        # create control variables
        self.var_bool = tk.BooleanVar()
        self.var_str = tk.StringVar()
        self.var_int = tk.IntVar()
        self.var_float = tk.DoubleVar()
        
        # create widgets
        self.setup_widgets()


    # create widgets
    def setup_widgets(self):
        # notebook for containing things
        self.notebook = ttk.Notebook(self) #make notebook for input tab and graph tab
        self.notebook.pack(fill="both", expand=True)

        # input tab
        self.input_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.input_tab, text="INPUT")

        # graph tab
        self.graph_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.graph_tab, text="GRAPH")



        # general data input frame
        self.general_data_frame = ttk.LabelFrame(self.input_tab, text="General Data")
        self.general_data_frame.grid(row=0, column=0, columnspan=1)

        # T reservoir
        self.T_res = ttk.Entry(self.general_data_frame)
        self.T_res.grid(row=0, column=1,padx=10, pady=5)

        self.T_res_label = ttk.Label(self.general_data_frame, text="Reservoir Temperature")
        self.T_res_label.grid(row=0, sticky="W", column=0, padx=10, pady=5)

        self.T_res_unit_label = ttk.Label(self.general_data_frame, text="deg F")
        self.T_res_unit_label.grid(row=0, sticky="W", column=2, padx=10, pady=5)

        # Initial res pressure
        self.P_init = ttk.Entry(self.general_data_frame)
        self.P_init.grid(row=1, column=1, padx=10, pady=5)

        self.P_init_label = ttk.Label(self.general_data_frame, text="Initial Reservoir Pressure")
        self.P_init_label.grid(row=1, sticky="W", column=0, padx=10, pady=5)

        self.P_init_unit_label = ttk.Label(self.general_data_frame, text="psia")
        self.P_init_unit_label.grid(row=1, sticky="W", column=2, padx=10, pady=5)

        # standard pressure
        self.P_sc = ttk.Entry(self.general_data_frame)
        self.P_sc.grid(row=2, column=1, padx=10, pady=5)

        self.P_sc_label = ttk.Label(self.general_data_frame, text="Standard Pressure")
        self.P_sc_label.grid(row=2, sticky="W", column=0, padx=10, pady=5)

        self.P_sc_unit_label = ttk.Label(self.general_data_frame, text="psia")
        self.P_sc_unit_label.grid(row=2, sticky="W", column=2, padx=10, pady=5)

        # gas gravity
        self.Gas_SG = ttk.Entry(self.general_data_frame)
        self.Gas_SG.grid(row=3, column=1, padx=10, pady=5)

        self.Gas_SG_label = ttk.Label(self.general_data_frame, text="Gas Gravity (Air = 1.0)")
        self.Gas_SG_label.grid(row=3, sticky="W", column=0, padx=10, pady=5)

        self.Gas_SG_unit_label = ttk.Label(self.general_data_frame, text="")
        self.Gas_SG_unit_label.grid(row=3, sticky="W", column=2, padx=10, pady=5)



        # Oil data frame
        self.oil_data_frame = ttk.LabelFrame(self.input_tab, text="Oil Data")
        self.oil_data_frame.grid(row=1, column=0)

        # oil api
        self.oil_API = ttk.Entry(self.oil_data_frame)
        self.oil_API.grid(row=0, column=1, padx=10, pady=5)

        self.oil_API_label = ttk.Label(self.oil_data_frame, text="Oil API")
        self.oil_API_label.grid(row=0, sticky="W", column=0, padx=10, pady=5)

        self.oil_API_unit_label = ttk.Label(self.oil_data_frame, text="deg API")
        self.oil_API_unit_label.grid(row=0, sticky="W", column=2, padx=10, pady=5)
        
        # Rs @ Pb
        self.Rs_at_Pb = ttk.Entry(self.oil_data_frame)
        self.Rs_at_Pb.grid(row=1, column=1, padx=10, pady=5)

        self.Rs_at_Pb_label = ttk.Label(self.oil_data_frame, text="Rs @ Pb")
        self.Rs_at_Pb_label.grid(row=1, sticky="W", column=0, padx=10, pady=5)

        self.Rs_at_Pb_unit_label = ttk.Label(self.oil_data_frame, text="MSCF/STB")
        self.Rs_at_Pb_unit_label.grid(row=1, sticky="W", column=2, padx=10, pady=5)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("PVT Calculator")
    root.geometry("1200x600")
    root.resizable(False, False)

    # Simply set the theme
    root.tk.call("source", "./Azure-ttk-theme/azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    root.update()
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()

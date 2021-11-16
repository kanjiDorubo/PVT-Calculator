import tkinter as tk
from tkinter import ttk
from helperfunc.Functions import *

from GeneralData import GeneralData
from OilData import OilData
from BubblepointPressure import BubblepointPressure
from SeparatorVariables import SeparatorVariables
from CriticalGasData import CriticalGasData
from SaturationCondition import SaturationCondition
from Impurities import Impurities
from Configurations import Configurations
from PressureOfInterest import PressureOfInterest

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('azure_dark')
        
class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
    
        # create control variables
        self.var_bool = tk.BooleanVar()
        self.var_str = tk.StringVar()
        self.var_int = tk.IntVar()
        self.var_float = tk.DoubleVar()

        # General Data variables
        self.T_res_var = tk.DoubleVar(value = 0)
        self.P_res_var = tk.DoubleVar(value = 0)
        self.P_sc_var = tk.DoubleVar(value=0)
        self.Gas_gravity_var = tk.DoubleVar(value=0)

        # # Oil Data variables
        self.oil_api_var = tk.DoubleVar(value=0)
        self.Rs_at_Pb_var = tk.DoubleVar(value = 0) 

        # Separator variables
        self.P_sep_var = tk.DoubleVar(value=0)
        self.T_sep_var = tk.DoubleVar(value=0)
        
        # Bubblepoint Pressure variable
        self.Pb_var = tk.DoubleVar(value=0)

        # P of interest variable
        self.P_interest_var = tk.DoubleVar(value=0)

        # Critical gas data variables
        self.gas_corr_var = tk.StringVar(value='hello')
        self.Ppc_var = tk.DoubleVar(value=0)
        self.Tpc_var = tk.DoubleVar(value=0)
        self.Ppr_var = tk.DoubleVar(value=0)
        self.Tpr_var = tk.DoubleVar(value=0)

        # saturatioin condition variables
        self.sat_condition_var = tk.StringVar()
        self.tds_var = tk.DoubleVar(value=0)

        # impurities var
        self.CO2_var = tk.DoubleVar()
        self.H2S_var = tk.DoubleVar()
        self.N2_var = tk.DoubleVar()

        # configurations var
        self.config_corr_var = tk.DoubleVar()
        self.Bg_unit_var = tk.DoubleVar()
        self.Miu_w_var = tk.DoubleVar()


        self.CalcVar = tk.DoubleVar(value=0)
        self.CalcLabel = tk.StringVar()
        
        # create widgets
        self.setup_widgets()

    def calc(self):
        def sum(var1, var2):
            return var1+var2

        self.CalcLabel.set('')
        self.CalcVar.set(sum(self.P_sep_var.get(), self.T_sep_var.get()))
        self.CalcLabel.set('Calculations finished!')



    # create widgetsb
    def setup_widgets(self):
        # notebook for containing things
        self.notebook = ttk.Notebook(self) #make notebook for input tab and graph tab
        self.notebook.pack(fill="both", expand=True)

        # input tab
        self.input_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.input_tab, text="INPUT")
        # for i in [0,1,2]:
        #     self.input_tab.columnconfigure(index=i, weight=1)
        
        # self.input_tab.rowconfigure(index=0, weight=1)


        # graph tab
        self.graph_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.graph_tab, text="GRAPH")

        # output tab
        self.output_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.output_tab, text="OUTPUT")

        # another notebook in graph
        self.graph_notebook = ttk.Notebook(self.graph_tab)
        self.graph_notebook.pack(fill="both", expand=True)

        self.Bo_graph = ttk.Frame(self.graph_tab)
        self.graph_notebook.add(self.Bo_graph, text="Bo")

        self.Rs_graph = ttk.Frame(self.graph_tab)
        self.graph_notebook.add(self.Rs_graph, text="Rs")

        self.Bo_label = ttk.Label(self.Bo_graph, textvariable=self.CalcVar).pack()


        # add table on graph
        self.table_contoh_columns = ('#1', '#2')

        self.table_contoh = ttk.Treeview(self.Rs_graph, columns = self.table_contoh_columns, show = 'headings')
    
        self.table_contoh.heading('#1', text='P', anchor='center')
        self.table_contoh.heading('#2', text='Rs', anchor='center')

        self.table_contoh.column('#1', anchor='center')
        self.table_contoh.column('#2', anchor='center')

        self.x = []
        self.y = []
        self.table_contoh_data = []
        for P in range(0, 5000, 500):
            self.table_contoh_data.append((P,testfunc(P)))
            self.x.append(P)
            self.y.append(testfunc(P))

        for data in self.table_contoh_data:
            self.table_contoh.insert('', tk.END, values=data)

        self.table_contoh.grid(row=0, column=0, padx=20, pady=20, sticky='e')

        # buat plot dri data
        fig, ax = plt.subplots(figsize=(6,4), dpi=100)
        # fig = Figure(figsize = (6,4), dpi = 100)
        plot1 = fig.add_subplot(111)
        plot1.plot(self.y, self.x, marker='o')
        plot1.set_xlabel("P (psia)")
        plot1.set_ylabel("Rs (MSCF/STB)")
        plot1.set_title("P - Rs Graph")
        canvas = FigureCanvasTkAgg(fig, self.Rs_graph)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

        # add styling



        



        # make 3 frames to divide the input_tab
        self.input_tab_left = ttk.Frame(self.input_tab)
        self.input_tab_left.grid(row=0, column=0, sticky='nsew')

        self.input_tab_center = ttk.Frame(self.input_tab)
        self.input_tab_center.grid(row=0, column=1, sticky='nsew')

        self.input_tab_right = ttk.Frame(self.input_tab)
        self.input_tab_right.grid(row=0, column=2, sticky='nsew')


        # general data widget
        self.general_data = GeneralData(
            self.input_tab_left,
            Presvar = self.P_res_var,
            Tresvar = self.T_res_var,
            Pscvar = self.P_sc_var,
            Gas_gravity_var = self.Gas_gravity_var
            )
        self.general_data.pack(fill='both', padx=10, pady=10)


        # oil data widget
        self.oil_data = OilData(self.input_tab_left,
            oilapivar = self.oil_api_var,
            RsatPbvar = self.Rs_at_Pb_var
            )
        self.oil_data.pack(fill='both', padx=10, pady=10)

        
        # separator variables widget
        self.separator_variables = SeparatorVariables(self.input_tab_left, self.P_sep_var, self.T_sep_var)
        self.separator_variables.pack(fill='both', padx=10, pady=10)


        # bubblepoint pressure widget
        self.bubblepoint_pressure = BubblepointPressure(self.input_tab_center, Pbvar=self.Pb_var)
        self.bubblepoint_pressure.pack(fill='both', padx=10, pady=10)


        # Saturation Condition widget
        self.saturation_condition = SaturationCondition(self.input_tab_center,
            ConditionVar = self.sat_condition_var, 
            TDSVar = self.tds_var)
        self.saturation_condition.pack(fill='both', padx=10, pady=10)


        # Critical Gas Data widget
        self.critical_gas_data = CriticalGasData(self.input_tab_center,
            GasCorrVar = self.gas_corr_var, 
            PpcVar = self.Ppc_var, 
            TpcVar = self.Tpc_var,
            PprVar = self.Ppr_var,
            TprVar = self.Tpr_var)
        self.critical_gas_data.pack(fill='both', padx=10, pady=10)


         # Pressure of Interest widget
        self.P_interest = PressureOfInterest(self.input_tab_right, Pinterestvar = self.P_interest_var)
        self.P_interest.pack(fill='both', padx=10, pady=10)


        # Impurities widget
        self.impurities = Impurities(self.input_tab_right,
            CO2Var = self.CO2_var, 
            H2SVar = self.H2S_var, 
            N2Var = self.N2_var)
        self.impurities.pack(fill='both', padx=10, pady=10)


        # Configurations widget
        self.configurations = Configurations(self.input_tab_right,
            ConfigCorrVar = self.config_corr_var, 
            BgUnitVar = self.Bg_unit_var, 
            MiuWVar = self.Miu_w_var)
        self.configurations.pack(fill='both', padx=10, pady=10)
       

        # coba2 calculate
        # tambahin berdasar gas corr
        self.calc_button = ttk.Button(self.input_tab_right, text="Calculate", style="Accent.TButton",command=self.calc)
        self.calc_button.pack(fill='both', padx=10, pady=10)

        self.calc_label = ttk.Label(self.input_tab_right, textvariable=self.CalcLabel)
        self.calc_label.pack(fill='both', padx=10, pady=0)

         

        

       



if __name__ == "__main__":
    root = tk.Tk()
    root.title("PVT Calculator")
    root.geometry("1170x530")
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

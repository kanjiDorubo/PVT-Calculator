import tkinter as tk
from tkinter import ttk
from helperfunc.Functions import *
from SeparatorVariables import SeparatorVariables
from GeneralData import GeneralData
from OilData import OilData
from BubblepointPressure import BubblepointPressure

        
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



        self.CalcVar = tk.DoubleVar(value=0)
        self.CalcLabel = tk.StringVar()
        
        # create widgets
        self.setup_widgets()

    def calc(self):
        def sum(var1, var2):
            return var1+var2

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

        # graph tab
        self.graph_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.graph_tab, text="GRAPH")

        # another notebook in graph
        self.graph_notebook = ttk.Notebook(self.graph_tab)
        self.graph_notebook.pack(fill="both", expand=True)

        self.Bo_graph = ttk.Frame(self.graph_tab)
        self.graph_notebook.add(self.Bo_graph, text="Bo")

        self.Rs_graph = ttk.Frame(self.graph_tab)
        self.graph_notebook.add(self.Rs_graph, text="Rs")

        self.Bo_label = ttk.Label(self.Bo_graph, textvariable=self.CalcVar).pack()

        # add table on graph
        self.table_contoh = ttk.Treeview(self.Rs_graph)
        self.table_contoh['columns'] = ('P','Rs')

        self.table_contoh.column("#0", width=0,  stretch='NO')
        self.table_contoh.column('P', anchor='center')
        self.table_contoh.column('Rs', anchor='center')

        self.table_contoh.heading('#0', text='', anchor='center')
        self.table_contoh.heading('P', text='P', anchor='center')
        self.table_contoh.heading('Rs', text='Rs', anchor='center')





        # general data widget
        self.general_data = GeneralData(
            self.input_tab,
            Presvar = self.P_res_var,
            Tresvar = self.T_res_var,
            Pscvar = self.P_sc_var,
            Gas_gravity_var = self.Gas_gravity_var
            )
        self.general_data.grid(row=0, column=0)

        # oil data widget
        self.oil_data = OilData(self.input_tab,
            oilapivar = self.oil_api_var,
            RsatPbvar = self.Rs_at_Pb_var
            )
        self.oil_data.grid(row=1, column=0)

        

        # separator variables widget
        self.separator_variables = SeparatorVariables(self.input_tab, self.P_sep_var, self.T_sep_var)
        self.separator_variables.grid(row=2, column=0)

        self.calc_button = ttk.Button(self.input_tab, text="Calculate", command=self.calc)
        self.calc_button.grid(row=2, column=1, padx=10, pady=5)

        self.calc_label = ttk.Label(self.input_tab, textvariable=self.CalcLabel)
        self.calc_label.grid(row=2, column=2, padx=10, pady=5)

        # bubblepoint pressure widget
        self.bubblepoint_pressure = BubblepointPressure(self.input_tab, Pbvar=self.Pb_var)
        self.bubblepoint_pressure.grid(row=3, column=0)

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

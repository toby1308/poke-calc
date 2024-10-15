import tkinter as tk
from tkinter import ttk
from pok_eq import *


def Find_HP():
    print("button pressed")
    req_stats = [TH_HP_INT.get(),TH_ATK_INT.get(),TH_DEF_INT.get(),TH_SATK_INT.get(),TH_SDEF_INT.get(),TH_SPD_INT.get()]
    type_arr = ["Fighting","Flying","Poision","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark"]
    P1 = [HP1INT.get(),ATK1INT.get(),DEF1INT.get(),SATK1INT.get(),SDEF1INT.get(),SPD1INT.get()]
    P2 = [HP2INT.get(),ATK2INT.get(),DEF2INT.get(),SATK2INT.get(),SDEF2INT.get(),SPD2INT.get()]
    data_set = HP_from_parents(P1,P2,req_stats)
    string = ""
    spacing = "        "
    if SH_string.get() == "Yes":
        shiny_rate = 8192
    else:
        shiny_rate = 1
    shiny_rate = 1
    total = array_total_2d(data_set,0)
    total = 5242880/8
    nature_options = ["ALL","SPECIFIC","GENERAL","NEUTRAL"]
    nature_chossen = Natures_string.get()
    nature_prob = 0
    Everstone = ES_string.get()
    for i in range(len(nature_options)):
        if nature_chossen == nature_options[i]:
            if i == 0:
                nature_prob = 1
            if i == 1:
                nature_prob = 0.04
            if i == 2:
                nature_prob = 0.16
            if i == 3:
                nature_prob = 0.2

    if Everstone == "Yes":
        nature_prob = 0.5 + 0.5*nature_prob
    
    if HP_string.get() == "All":
        for i in range(len(data_set)):
            string = string + type_arr[i] + spacing[len(type_arr[i]):] + ": " + str(data_set[i][0] / total) + ": " + str((data_set[i][1] * nature_prob)/(total * shiny_rate)) + "\n"

    else:
        for i in range(len(data_set)):
            if type_arr[i] == HP_string.get():
                string = string + type_arr[i] + spacing[len(type_arr[i]):] + ": " + str(data_set[i][0] / total) + ": " + str((data_set[i][1] * nature_prob)/(total * shiny_rate)) + "\n"
                string = string + "Average encounter rate: " + str((total * shiny_rate)/(data_set[i][1]*nature_prob))

    OP_Label["text"] = string
        
            
    return 0




window = tk.Tk()
window.title("PBP")
window.geometry("520x460")


title_label = ttk.Label(master = window, text = "Pokemon HP Probability", font = "Calibri 24")
title_label.pack()

Parent_1_frame = ttk.Frame(master = window)
Parent_2_frame = ttk.Frame(master = window)
dropdown_frame = ttk.Frame(master = window)
IV_title_frame = ttk.Frame(master = window)
HPOutput_frame = ttk.Frame(master = window)
Calculat_frame = ttk.Frame(master = window)
Threshold_frame = ttk.Frame(master = window)
Natures_frame = ttk.Frame(master = dropdown_frame)
EV_stone_frame = ttk.Frame(master = dropdown_frame)
Shiny_pk_frame = ttk.Frame(master = dropdown_frame)


P1_frame_label = ttk.Label(master = Parent_1_frame, text = "Father")
P2_frame_label = ttk.Label(master = Parent_2_frame, text = "Mother")
HP_frame_label = ttk.Label(master = HPOutput_frame, text = "Hidden Powers")
NA_frame_label = ttk.Label(master = Natures_frame, text = "Natures & Hidden Power:")
HS_frame_label = ttk.Label(master = Natures_frame, text = "Hidden Power:")
ES_frame_label = ttk.Label(master = EV_stone_frame, text = "Everstone (Emerald Only):")
TH_frame_label = ttk.Label(master = Threshold_frame, text = "IV Min:")
SH_frame_label = ttk.Label(master = Shiny_pk_frame, text = "Shiny:")

HP_label = ttk.Label(master = IV_title_frame, text = "HP: ")
ATK_label = ttk.Label(master = IV_title_frame, text = "ATK: ")
DEF_label = ttk.Label(master = IV_title_frame, text = "DEF: ")
SDEF_label = ttk.Label(master = IV_title_frame, text = "SDEF: ")
SATK_label = ttk.Label(master = IV_title_frame, text = "SATK: ")
SPD_label = ttk.Label(master = IV_title_frame, text = "SPD: ")
IV_label = ttk.Label(master = IV_title_frame, text = "IVs")
OP_Label = ttk.Label(master = HPOutput_frame, text = "")

HP1INT = tk.IntVar()
HP2INT = tk.IntVar()
ATK1INT = tk.IntVar()
ATK2INT = tk.IntVar()
DEF1INT = tk.IntVar()
DEF2INT = tk.IntVar()
SATK1INT = tk.IntVar()
SATK2INT = tk.IntVar()
SDEF1INT = tk.IntVar()
SDEF2INT = tk.IntVar()
SPD1INT = tk.IntVar()
SPD2INT = tk.IntVar()
TH_HP_INT = tk.IntVar()
TH_ATK_INT = tk.IntVar()
TH_DEF_INT = tk.IntVar()
TH_SATK_INT = tk.IntVar()
TH_SDEF_INT = tk.IntVar()
TH_SPD_INT = tk.IntVar()
Natures_string = tk.StringVar()
HP_string = tk.StringVar()
ES_string = tk.StringVar()
SH_string = tk.StringVar()

HP1 = ttk.Entry(master = Parent_1_frame,  textvariable = HP1INT)
HP2 = ttk.Entry(master = Parent_2_frame, textvariable = HP2INT)
ATK1 = ttk.Entry(master = Parent_1_frame, textvariable = ATK1INT)
ATK2 = ttk.Entry(master = Parent_2_frame, textvariable = ATK2INT)
DEF1 = ttk.Entry(master = Parent_1_frame, textvariable = DEF1INT)
DEF2 = ttk.Entry(master = Parent_2_frame, textvariable = DEF2INT)
SATK1 = ttk.Entry(master = Parent_1_frame, textvariable = SATK1INT)
SATK2 = ttk.Entry(master = Parent_2_frame, textvariable = SATK2INT)
SDEF1 = ttk.Entry(master = Parent_1_frame, textvariable = SDEF1INT)
SDEF2 = ttk.Entry(master = Parent_2_frame, textvariable = SDEF2INT)
SPD1 = ttk.Entry(master = Parent_1_frame, textvariable = SPD1INT)
SPD2 = ttk.Entry(master = Parent_2_frame, textvariable = SPD2INT)
TH_HP = ttk.Entry(master = Threshold_frame, textvariable = TH_HP_INT)
TH_ATK = ttk.Entry(master = Threshold_frame, textvariable = TH_ATK_INT)
TH_DEF = ttk.Entry(master = Threshold_frame, textvariable = TH_DEF_INT)
TH_SATK = ttk.Entry(master = Threshold_frame, textvariable = TH_SATK_INT)
TH_SDEF = ttk.Entry(master = Threshold_frame, textvariable = TH_SDEF_INT)
TH_SPD = ttk.Entry(master = Threshold_frame, textvariable = TH_SPD_INT)

Natures = ttk.Combobox(master = Natures_frame, textvariable = Natures_string)
Natures['values'] = ("ALL","SPECIFIC","GENERAL","NEUTRAL")
HP_selection = ttk.Combobox(master = Natures_frame, textvariable = HP_string)
HP_selection['values'] = ["All","Fighting","Flying","Poision","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark"]
ES_selection = ttk.Combobox(master = EV_stone_frame, textvariable = ES_string)
ES_selection['values'] = ["Yes","No"]
SH_selection = ttk.Combobox(master = Shiny_pk_frame, textvariable = SH_string)
SH_selection['values'] = ["Yes","No"]
Calculate = ttk.Button(master = Calculat_frame, text = "Calculate", command = Find_HP)
Calculate.pack()

P1_frame_label.pack(pady = 5)
P2_frame_label.pack(pady = 5)
NA_frame_label.pack(side = "top",padx = 2,pady= 1)
ES_frame_label.pack(side = "top", padx =2)
#HS_frame_label.pack(side = "top",padx = 2,pady =1)
HP_frame_label.pack(side = "top", pady = 3)
IV_label.pack(pady = 2)
HP_label.pack(pady = 2)
ATK_label.pack(pady = 2)
DEF_label.pack(pady = 2)
SATK_label.pack(pady = 2)
SDEF_label.pack(pady = 2)
SPD_label.pack(pady = 2)
OP_Label.pack(side = "right")
SH_frame_label.pack()
TH_frame_label.pack(pady = 5)


input_pady = 1
HP1.pack(pady = input_pady)
HP2.pack(pady = input_pady)
ATK1.pack(pady = input_pady)
ATK2.pack(pady = input_pady)
DEF1.pack(pady = input_pady)
DEF2.pack(pady = input_pady)
SATK1.pack(pady = input_pady)
SATK2.pack(pady = input_pady)
SDEF1.pack(pady = input_pady)
SDEF2.pack(pady = input_pady)
SPD1.pack(pady = input_pady)
SPD2.pack(pady = input_pady)
TH_HP.pack(pady = input_pady)
TH_ATK.pack(pady = input_pady)
TH_DEF.pack(pady = input_pady)
TH_SATK.pack(pady = input_pady)
TH_SDEF.pack(pady = input_pady)
TH_SPD.pack(pady = input_pady)

dropdown_frame.pack(side = "top")
Natures.pack(side = "left", padx = 2)
HP_selection.pack(side = "left", padx =2)
ES_selection.pack(side = "right")
SH_selection.pack()
Calculat_frame.pack(side = "top")
Natures_frame.pack(side = "top", pady = 5)
IV_title_frame.pack(side = "left", padx = 5)
Parent_1_frame.pack(side = "left", padx = 5)
Parent_2_frame.pack(side = "left", padx = 5)
HPOutput_frame.pack(side = "right",padx = 5)
EV_stone_frame.pack(side = "bottom",padx = 5)
#Shiny_pk_frame.pack(side = "right",padx = 5)
Threshold_frame.pack(side = "left")

window.mainloop()


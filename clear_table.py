#!coding:utf-8

import tkinter as tk
from sys import exit
from pandas import read_excel
from tkinter import messagebox
from tkinter.scrolledtext import *


def entervalue():
	global check
	check = tk.messagebox.askyesno(title="FEEDCACK", message="清洗后的数据正确？")
	# if check == 0:
		# exit()
	# else:
		# pass
	

def clean_table(input_file):
	table = read_excel(input_file, index=False, sheet_name="Results")
	table = table.dropna(axis=0, thresh=3)
	table = table.dropna(axis=1, how='any')
	new_table = table.iloc[1:]
	new_table.index = range(len(table)-1)
	new_table.columns = list(table.iloc[0])
	root = tk.Tk(className="CLEAN DATA, CHECK")
	textPad = ScrolledText(root, height=50)
	a = textPad.insert(tk.constants.END, chars = str(new_table))
	textPad.pack()
	
	btn = tk.Button(root, text="反 馈", width=10, command=entervalue)
	btn.pack()
	root.mainloop()

	
if __name__ == "__main__":
	clean_table("origin_data.xls")
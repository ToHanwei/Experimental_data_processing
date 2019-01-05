from tkinter import *
import tkinter.ttk as ttk
from pandas import read_excel
import numpy as np


def clean_table(input_file):
	table = read_excel(input_file, index=False, sheet_name="Results")
	table = table.dropna(axis=0, thresh=3)
	table = table.dropna(axis=1, how='any')
	new_table = table.iloc[1:]
	new_table.index = range(len(table)-1)
	new_table.columns = list(table.iloc[0])
	
	root = Tk()
	tree = ttk.Treeview(root, columns=new_table.columns, show="headings")
	for col in new_table.columns:
		# print(col)
		tree.column(col, width=100, anchor='center')
		# tree.heading(col, text=col)
	# tree.column('col1', width=100, anchor='center')
	# tree.column('col2', width=100, anchor='center')
	# tree.column('col3', width=100, anchor='center')
	# tree.heading('col1', text='col1')
	# tree.heading('col2', text='col2')
	# tree.heading('col3', text='col3')
	#def onDBClick(event):
	#    item = tree.selection()[0]
	#    print("you clicked on ", tree.item(item, "values"))
		 
	# for i in range(10):
		# tree.insert('',i,values=('a'+str(i),'b'+str(i),'c'+str(i)))
	# tree.bind("")#("<Double-1>")#, onDBClick)
	 
	 
	tree.pack()
	root.mainloop()
	
if __name__ == "__main__":
	clean_table("origin_data.xls")
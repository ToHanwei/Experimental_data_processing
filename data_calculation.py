#!coding:utf-8

import tkinter as tk
from sys import exit
from numpy import array
from pandas import DataFrame
from pandas import read_excel
from pandas import ExcelWriter
from tkinter import constants
from tkinter import messagebox
from tkinter.scrolledtext import *
from collections import defaultdict

"""
This script is write for shu.
processing experimental data 
The way of this script in "calculation.jpg" file
"""

__author__ = "Wei"
__tate__ = "20181221"
__mail__ = "hanwei@shanghaitech.edu.cn"
__update__ = ["20190103"]


def data_conduct(data, inter):
	group = set(list(data["Sample Name"]))
	diff_dict = defaultdict(array)
	#group the data
	for key in group:
		target_bool = (data["Target Name"] == inter)
		sample_bool = (data["Sample Name"] == key)
		value_bool = (target_bool & sample_bool)
		value = array(data.loc[sample_bool, "CT"]) - array(data.loc[value_bool, "CT"])
		diff_dict[key] = value
	#calculate the experimental data
	out_dict = defaultdict(array)
	for key in list(group):
		contrast = array(diff_dict["nc"], dtype="float64")
		gene = array(diff_dict[key], dtype="float64")
		out_dict[key] = pow(2, contrast - gene)
	#output the data
	data_out, res, j = [], "", 0
	for key in data["Sample Name"]:
		i = 0
		if key == res: continue
		data_out.extend(list(out_dict[key]))
		res = key
	data_out = DataFrame(array(data_out), columns=["RQ"], index=data.index)
	data = data.join(data_out)
	return(data)
	

def repeat(arry):
	"""get number of repeat,return a list"""
	repeat_list = []
	for repe in arry:
		if repe not in repeat_list:
			repeat_list.append(repe)
	return(repeat_list)


def integrate(target, sample, name, group_num, df):
	index, names = [], []
	res_dict = defaultdict(list)
	for row in sample:
		index.extend([row]*3)
	result = DataFrame(index=index, columns=target)
	for tag in target:
		res = df.loc[df["Target Name"]==tag, "RQ"]
		res_dict[tag] = list(res)
	result = DataFrame(res_dict, index=index)
	for key in index:
		if key == "nc":
			names.append(key.upper())
		elif key == "pc":
			names.append(name)
		else:
			names.append(name+"#"+key)
	result.index = names
	return(result.T)


def clean_table(input_file):
	table = read_excel(input_file, index=False, header=None, sheet_name="Results")
	table = table.dropna(axis=0, thresh=3)
	table = table.dropna(axis=1, how='any')
	new_table = table.iloc[1:]
	new_table.index = range(len(table)-1)
	new_table.columns = list(table.iloc[0])
	new_table.to_excel("CLEAN_CHECK.xlsx", index=False, sheet_name="Results")


def transDf(input_file, outfile, inter, name):
	#determine the file name
	if not outfile.endswith(".xlsx"):
		outfile = outfile.split(".")[0] + ".xlsx"
	data = read_excel(input_file, index=False, sheet_name="Results")
	#get number of target
	target = repeat(data["Target Name"])
	target_num = len(target)
	#get number of sample
	sample = repeat(data["Sample Name"])
	sample_num = len(sample)
	
	#some necessary number
	data_num = len(data)
	group_num = int(data_num/(target_num*sample_num))
	
	#create Panel dataformat
	cols = list(data.columns)+["RQ"]
	out_data = DataFrame(columns=cols, index=data.index, dtype="float64")
	for i in range(group_num):
		trans_df = data.iloc[range(i, data_num, target_num)]
		trans_df = data_conduct(trans_df, inter)
		out_data.loc[trans_df.index] = trans_df
	result = integrate(target, sample, name, group_num, out_data)
	#save data
	writer = ExcelWriter(outfile)
	#result.to_excel()
	out_data.to_excel(writer, index=False, sheet_name="Treated")
	result.to_excel(writer, index=True, sheet_name="Transform")
	writer.close()
	

if __name__ == "__main__":
	#some test file
	inter = "actin"
	name = "Gapdh-siRNA"
	# input_file = "test_data.xls"
	input_file = "origin_data.xls"
	outfile = "test_deal_2.xlsx"
	#call the function
	#data_conduct(input_file, outfile, inter)
	trans = transDf(input_file, outfile, inter, name)
	
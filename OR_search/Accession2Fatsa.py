#! coding: utf-8

import os
import sys
import pickle
import pandas as pd

#Folder that save Blast output file, format 6
#Here, use Acctions only
ResultDir = sys.argv[1]
#Folder name, Save NrDataBase(pickle) dict
DbDir = sys.argv[2]
#A Empty folder, Savesearch sequences
SeqDir = sys.argv[3]

#AccessionSet = set()
#for i in range(1, 139):
#    FileName = ResultDir+"/O5AN1_BlastResE60SecondE60_"+str(i)+".txt"
#    if FileName in [os.path.join(ResultDir, File) for File in os.listdir(ResultDir)]:
#         with open(FileName) as AccessionFile:
#             Accession = [acce.strip() for acce in AccessionFile]
#         AccessionSet = AccessionSet | set(Accession)

with open(ResultDir) as Result:
	AccessionSet = set([line.strip() for line in Result])

SeqList = []
DbDictNames = os.listdir(DbDir)
count = 1
for db in DbDictNames:
	#print(db)
	with open(os.path.join(DbDir, db), 'rb') as DB:
		DbDict = pickle.load(DB)
	for acce in AccessionSet:
		acce = ">"+acce+"\n"
		if acce in DbDict.keys():
			SeqList.append(acce)
			SeqList.append(DbDict[acce])
	outfile= db.split(".")[0] + ".fasta"
	outfile = os.path.join(SeqDir, outfile)
	with open(outfile, 'w') as out:
		out.writelines(SeqList)
		SeqList = []

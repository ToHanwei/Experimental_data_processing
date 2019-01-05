# Experimental_data_processing
Help Shuhua process experimental data
这是给树华写的一个小应用；目的是处理实验数据。\n
原始数据样例是文件test_data_1.xlsx和test_data_2.xlsx.处理流程是对原始数据清洗，生成一个文件CLEAN_CHECK.xlsx\n
用于使用者检查清洗的结果是否正确。如果正确，则可进行下一步计算步骤。查看calulation.jpg可查看详细的计算过程。\n
最主要的脚本是data_gui.py这个脚本用于调用其它脚本并生成一个GUI界面。
使用pyinstaller -i logo.ico -w data_gui.py可在windows系统打包生成一个安装包。其中-i参数用于指定exe文件的图标
-w的使用不会在使用EXE文件是出现“小黑窗”。这样运行结果是产生一个文件夹。如果想产生一个独立的可运行文件的的话需要
使用-F参数。

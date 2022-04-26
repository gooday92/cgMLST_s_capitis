import os

strain_list = []
path_o = r"D:\python\cgMLST_SC\4.core_genes\5. Ridom验证\core_genes_1564"
path_n = r"D:\python\cgMLST_SC\4.core_genes\5. Ridom验证\core_genes_new"
file = open(r"D:\python\cgMLST_SC\4.core_genes\5. Ridom验证\验证2-去除stop_codon\v8 cgMLST结果，删除95%一下\删除的列表")
for strain in file.readlines():
    strain_list.append(strain[0:-1])
file.close()


for file in os.listdir(path_o):
    strain = file.replace(".fa", "")
    if strain not in strain_list:
        file_o = fr"{path_o}\{strain}.fa"
        file_n = fr"{path_n}\{strain}.fa"
        file_1 = open(file_o)
        file_2 = open(file_n,"w")
        for line in file_1.readlines():
            file_2.write(line)
        file_1.close()
        file_2.close()
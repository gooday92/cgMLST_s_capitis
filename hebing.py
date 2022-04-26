from Bio import SeqIO
import os


path_input = r"D:\python\cgMLST_SC\4.core_genes\5. Ridom验证\core_genes_1492"
path_output = r"D:\python\cgMLST_SC\4.core_genes\5. Ridom验证\核心基因分布"
file_name = "core_genes_query.fasta"

records = []
for file in os.listdir(path_input):
    file_fa = os.path.join(path_input,file)
    record = SeqIO.read(file_fa,"fasta")
    records.append(record)
file_output = os.path.join(path_output,file_name)
SeqIO.write(records, file_output, "fasta")
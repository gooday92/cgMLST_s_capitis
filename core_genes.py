import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from pandas.core.frame import DataFrame
import os

# path = r"D:\python\cgMLST_SC\panaroo_jieguo\aligned_gene_sequences"
# gene_list = []
# os.chdir(path)
# for f in os.listdir():
#     gene_list.append(f.split(".")[0])
# df = DataFrame(gene_list)
#
# df.to_excel("core_genes.xlsx")

df = pd.read_csv("core_genes_list.txt")
gene_list = df["gene"].tolist()

print(len(gene_list))

my_record = []
file = open("length_gene.txt", "w")
records = SeqIO.parse("pan_genome_reference.fa","fasta")
for record in records:
    if record.id in gene_list:
        gene_list.remove(record.id)
        gene = SeqRecord(record.seq, record.id,  description="")
        my_record.append(gene)
        l = str(len(record.seq))
        file.write(f"{record.id}   {l}\n")
file.close()
# print(len(my_record))
# print(gene_list)
# SeqIO.write(my_record, "Sc_core_genes.fa", "fasta")



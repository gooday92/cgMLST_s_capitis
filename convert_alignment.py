from Bio import AlignIO

path = r"/data4/CLC_data4/wangzhengan/other/cgMLST_SC/genomes/Nature/1_nature_only/snp/core_gene_alignment.aln.varsites.phy"
path_out = r"/data4/CLC_data4/wangzhengan/other/cgMLST_SC/genomes/Nature/1_nature_only/snp/core_gene_alignment.aln.varsites.fasta"

alignment = AlignIO.read(path,"phylip")

AlignIO.write(alignment,path_out, "fasta")
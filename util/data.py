import scipy as sp


def read_tsv(tsv_file_name):
    return sp.genfromtxt(tsv_file_name, delimiter='\t')

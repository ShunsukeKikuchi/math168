if __name__ == '__main__':
    import warnings
    import scanpy as sc
    import sys
    sys.path.append('/u/home/s/skikuchi/project-xyang123/SCING/src/')
    from scing import buildGRNHelpers as build
    import glob
    import numpy as np
    # filter warnings
    warnings.filterwarnings("ignore")

    out='/u/home/s/skikuchi/project-xyang123/math168/SCING/intermediate_networks/'
    # data loading
    path = '/u/home/s/skikuchi/project-xyang123/math168/SCING/supercells.h5ad'

    i = sys.argv[1]
    # Get the path from the command line arguments
    #path = glob.glob(data_dir + '*.h5ad')[0]
    #else:

    #file = sys.argv[2]
    #path = sys.argv[2]
    #path_li = glob.glob(data_dir + '*.h5ad')
    #if (len(sys.argv)>=3):   
    #print('output_dir: ',out) // for debugging
    adata_merged = sc.read_h5ad(path)
    
    #print(i)
    adata_saved = adata_merged.copy()
    grn = build.grnBuilder(adata=adata_saved, 
                        ngenes=-1, 
                        nneighbors=100,
                        npcs=10,
                        subsample_perc=0.7,
                        prefix= "net" + str(i),
                        outdir= out,
                        ncore=1,
                        mem_per_core=int(4e9),
                        verbose=True)
    grn.subsample_cells()
    grn.filter_genes()
    grn.filter_gene_connectivities()
    grn.build_grn()
    
    df_edges = grn.edges
    df_edges.to_csv(out + 'net.' + str(i) + '.edges.csv.gz', index=False)


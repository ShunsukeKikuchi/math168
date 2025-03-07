import os
os.chdir('/u/home/s/skikuchi/project-xyang123/SCING/tutorials/')
import scanpy as sc
import sys
sys.path.append('/u/home/s/skikuchi/project-xyang123/SCING/src/')
from scing import supercellHelpers as supercells
import sys
# Get the path from the command line arguments
adata = sc.read_h5ad("/u/home/s/skikuchi/project-xyang123/math168/alz.h5ad")

os.makedirs("/u/home/s/skikuchi/project-xyang123/math168/SCING/supercells", exist_ok=True)

adata_merged = supercells.supercell_pipeline(
                                adata,
                                ngenes=2000,###?
                                npcs=20,
                                ncell=500,
                                verbose=True,
                                #profiler_output_file=out+'supercells/{}_{}_profiler.txt'.format(file,cell_type))
)
adata_merged.write(f"/u/home/s/skikuchi/project-xyang123/math168/SCING/supercells.h5ad")

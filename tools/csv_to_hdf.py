import pandas as pd
import sys
import os
import gzip

for file_name in sys.argv[1:]:
    file_name_no_ext = os.path.splitext(file_name)[0] # Get file name without extension
    print("Reading " + file_name)
    df = pd.read_csv(file_name, index_col="cell_specimen_id") # Read in csv file
    print("Saving " + file_name)
    df.to_hdf(file_name_no_ext + '.hdf5', complib="blosc", key=file_name_no_ext) # Output hdf file

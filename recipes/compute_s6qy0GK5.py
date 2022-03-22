# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import os

# Read recipe inputs and get a dataframe
dataset = dataiku.Dataset("data_by_state_filtered_ordered")
df = dataset.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# folder handle
folder_handle = dataiku.Folder("s6qy0GK5")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# location wished in the output folder
path_output_folder="datasets"

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
final_path=os.path.join(path_output_folder,"my_file.csv")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
with folder_handle.get_writer(final_path) as writer:
    writer.write(df.to_csv().encode("utf-8"))
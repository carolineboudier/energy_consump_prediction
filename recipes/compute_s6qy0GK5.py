# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
data_by_state_filtered_ordered = dataiku.Dataset("data_by_state_filtered_ordered")
data_by_state_filtered_ordered_df = data_by_state_filtered_ordered.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
import os
folder_handle = dataiku.Folder("s6qy0GK5")
folder_path = folder_handle.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
path_output_folder="datasets"

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
final_path=os.path.join(folder_path,path_output_folder,"my_file.csv")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
with folder_handle.get_writer(final_path) as writer:
    writer.write(data_by_state_filtered_ordered_df.to_csv().encode("utf-8"))
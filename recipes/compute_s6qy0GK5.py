# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
data_by_state_filtered_ordered = dataiku.Dataset("data_by_state_filtered_ordered")
data_by_state_filtered_ordered_df = data_by_state_filtered_ordered.get_dataframe()




# Write recipe outputs
output_datasets = dataiku.Folder("s6qy0GK5")
output_datasets_info = output_datasets.get_info()

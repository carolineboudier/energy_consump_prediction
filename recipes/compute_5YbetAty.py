# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
full_data_prepared = dataiku.Dataset("full_data_prepared")
full_data_prepared_df = full_data_prepared.get_dataframe()




# Write recipe outputs
custom_graphs = dataiku.Folder("5YbetAty")
custom_graphs_info = custom_graphs.get_info()

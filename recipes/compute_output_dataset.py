# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
html_files = dataiku.Folder("1UUJ7dDF")
html_files_info = html_files.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

output_dataset_df = ... # Compute a Pandas dataframe to write into output_dataset


# Write recipe outputs
output_dataset = dataiku.Dataset("output_dataset")
output_dataset.write_with_schema(output_dataset_df)

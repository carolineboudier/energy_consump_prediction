# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
full_data_prepared = dataiku.Dataset("full_data_prepared")
full_data_prepared_df = full_data_prepared.get_dataframe(infer_with_pandas=False)


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

full_data_with_code_df = full_data_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
full_data_with_code = dataiku.Dataset("full_data_with_code")
full_data_with_code.write_with_schema(full_data_with_code_df)

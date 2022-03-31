# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
full_data_prepared = dataiku.Dataset("full_data_prepared")
full_data_prepared_df = full_data_prepared.get_dataframe(infer_with_pandas=False)
infered_df = full_data_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.


# Write recipe outputs
full_data_with_code = dataiku.Dataset("full_data_with_code")
full_data_with_code.write_with_schema(full_data_with_code_df)

# Write recipe outputs
infered_full_data_with_code = dataiku.Dataset("full_data_infered_pandas")
infered_full_data_with_code.write_with_schema(infered_df)
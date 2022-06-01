# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
full_data_prepared = dataiku.Dataset("full_data_prepared")
full_data_prepared_df = full_data_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

to_del_test_df = full_data_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
to_del_test = dataiku.Dataset("to_del_test")
to_del_test.write_with_schema(to_del_test_df)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

my_dataset = dataiku.Dataset("__FIRST_INPUT__")
dataset_dataframe = my_dataset.get_dataframe()



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

test_df = dataset_dataframe


# Write recipe outputs
test = dataiku.Dataset("test")
test.write_with_schema(test_df)
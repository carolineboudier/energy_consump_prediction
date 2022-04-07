# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import matplotlib.pyplot as plt
import io

# Read recipe inputs
full_data_prepared = dataiku.Dataset("full_data_prepared")
full_data_prepared_df = full_data_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# It is possible to import **custom code** (edited in the Library editor)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from my_package import calc_missing_vals

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# extract train set
train_df=full_data_prepared_df.dropna(subset=['site_eui'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
missing_df=calc_missing_vals(train_df)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from dataiku import insights
my_dpi=96
plt.figure(figsize=(1200/my_dpi, 500/my_dpi), dpi=my_dpi)
missing_df.plot.barh(title='Proportion_of_missing_values')
# save as insights
insights.save_figure('Proportion_of_missing_values')

bs=io.BytesIO()
plt.savefig(bs,format='png')
folder=dataiku.Folder("5YbetAty")
folder.upload_stream("fig_2.png",bs.getvalue())
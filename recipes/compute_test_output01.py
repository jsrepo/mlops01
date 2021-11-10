# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
westnile_joined_by_Trap_prepared = dataiku.Dataset("westnile_joined_by_Trap_prepared")
westnile_joined_by_Trap_prepared_df = westnile_joined_by_Trap_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
test_output01_df = westnile_joined_by_Trap_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
test_output01 = dataiku.Dataset("test_output01")
test_output01.write_with_schema(test_output01_df)
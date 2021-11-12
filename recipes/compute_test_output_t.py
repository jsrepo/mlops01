# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
westnile_joined = dataiku.Dataset("westnile_joined")
westnile_joined_df = westnile_joined.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_output_t_df = westnile_joined_df # For this sample code, simply copy input to output


# Write recipe outputs
test_output_t = dataiku.Dataset("test_output_t")
test_output_t.write_with_schema(test_output_t_df)

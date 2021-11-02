# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
past = dataiku.Dataset("past")
past_df = past.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_01_df = past_df # For this sample code, simply copy input to output


# Write recipe outputs
test_01 = dataiku.Dataset("test_01")
test_01.write_with_schema(test_01_df)

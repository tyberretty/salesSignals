import pymannkendall as mk
import pandas as pd


# Function for ADF to test for unit roots in the timeseries
def nonParamatricTrendtest(pdfInput):

    pdfInput.index = \
        pd.DatetimeIndex(pdfInput.index, freq='W')

    # Apply  Mann-Kendall Test to timeseries
    result = mk.original_test(pdfInput)
    print(result)

    trend = 0

    if result.p <= 0.05:
        trend = 1
    if result.p > 0.05:
        trend = 0

    return trend

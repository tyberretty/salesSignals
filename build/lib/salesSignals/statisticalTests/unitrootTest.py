from statsmodels.tsa.stattools import adfuller
import pandas as pd


# Function for ADF to test for unit roots in the timeseries
def unitrootTest(pdfInput):

    pdfInput.index = \
        pd.DatetimeIndex(pdfInput.index, freq='W')

    # Apply Dickey Fuller to timeseries
    result0 = adfuller(pdfInput)

    unitRoot = 0

    if result0[1] <= 0.05:
        unitRoot = 0
    if result0[1] > 0.05:
        unitRoot = 1

    return unitRoot

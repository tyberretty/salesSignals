import pandas as pd


def extendDataframe(pdfInput, forecastSteps):
    pdfInput.index = pd.DatetimeIndex(pdfInput.index, freq='W')

    idx = pdfInput.index
    extended = idx.union(idx.shift(forecastSteps)[-forecastSteps:])
    pdfForecast = pdfInput.reindex(extended)

    return pdfForecast

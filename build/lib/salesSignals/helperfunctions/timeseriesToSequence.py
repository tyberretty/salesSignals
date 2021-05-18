import pandas as pd


def timeseriesToSequence(data, lag=1):
    pdf = pd.DataFrame(data)
    columns = [pdf.shift(i) for i in range(1, lag + 1)]
    columns.append(pdf)
    pdf = pd.concat(columns, axis=1)
    pdf.fillna(0, inplace=True)
    return pdf

import pmdarima
from salesSignals.helperfunctions.stringToDate import stringToDate


# Function for OCSBTest to test for predictiveModels in the timeseries
def seasonalityTest(pdfInput, varTestFrequency, fieldName, maxLag):

    pdfInput.reset_index(inplace=True)

    if isinstance(pdfInput['date'].values[0], str) is True:
        print('String to date correction needed')
        pdfInput['dateFormatted'] = \
            pdfInput['date'].\
            apply(lambda row: stringToDate(row))

    if isinstance(pdfInput['date'].values[0], str) is False:
        print('String to date correction not needed')
        pdfInput['dateFormatted'] = \
            pdfInput['date']

    pdfInput['Quarter'] = \
        pdfInput['dateFormatted'].dt.quarter

    pdfInput['Year'] = \
        pdfInput['dateFormatted'].dt.strftime('%Y')

    pdfInput['YearQuarter'] = \
        pdfInput['Year'].astype(str) + pdfInput['Quarter'].astype(str)

    pdfInput['YearMonth'] = \
        pdfInput['dateFormatted'].dt.strftime('%Y%m')

    pdfInput['YearWeek'] = \
        pdfInput['dateFormatted'].dt.strftime('%Y%W')

    if varTestFrequency == 52:
        pdfInput = \
            pdfInput.groupby(['YearWeek']).agg({fieldName: ['mean']})

        pdfInput.columns = \
            [''.join(col) for col in pdfInput.columns]

        pdfInput = \
            pdfInput.rename(columns={fieldName+'mean': fieldName})

        pdfInput.reset_index(inplace=True)

        pdfInput = \
            pdfInput.set_index('YearWeek')

    if varTestFrequency == 12:
        print(pdfInput.head(5))
        pdfInput = \
            pdfInput.groupby(['YearMonth']).agg({fieldName: ['mean']})

        pdfInput.columns = \
            [''.join(col) for col in pdfInput.columns]

        pdfInput = \
            pdfInput.rename(columns={fieldName+'mean': fieldName})

        pdfInput.reset_index(inplace=True)

        pdfInput = \
            pdfInput.set_index('YearMonth')

    if varTestFrequency == 4:
        pdfInput = \
            pdfInput.groupby(['YearQuarter']).agg({fieldName: ['mean']})

        pdfInput.columns = [''.join(col) for col in pdfInput.columns]

        pdfInput = \
            pdfInput.rename(columns={fieldName+'mean': fieldName})

        pdfInput.reset_index(inplace=True)

        pdfInput = \
            pdfInput.set_index('YearQuarter')

    # Perform OCSB test
    seasonality = pmdarima.arima.\
        OCSBTest(m=varTestFrequency, lag_method='aic', max_lag=3).\
        estimate_seasonal_differencing_term(pdfInput[[fieldName]])

    return seasonality

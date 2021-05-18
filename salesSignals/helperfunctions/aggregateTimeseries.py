from salesSignals.helperfunctions.stringToDate import stringToDate


def aggregateTimeseries(pdfInput, dateField,
                        dimensionFields, indexField,
                        lstFields, dictTransformation,
                        resampleFrequency=None):

    pdfInput[dateField] = \
        pdfInput[dateField].apply(lambda row: stringToDate(row))

    # Drop duplicates
    pdfOutput = pdfInput[[dateField]+dimensionFields+lstFields].\
        drop_duplicates()

    if resampleFrequency is not None and resampleFrequency != 'Total':
        # Create new date field
        if resampleFrequency == 'Yearly':
            dateFormat = '%Y'

        if resampleFrequency == 'Monthly':
            dateFormat = '%Y%m'

        if resampleFrequency == 'Weekly':
            dateFormat = '%Y%W'

        pdfOutput[dateField] = \
            pdfOutput[dateField].dt.strftime(dateFormat)

    # Reset Index
    pdfOutput.reset_index(inplace=True)

    if resampleFrequency == 'Total':
        # Transform Fields
        pdfOutput = pdfOutput. \
            groupby(dimensionFields). \
            agg(dictTransformation)

        # Concatenate different levels of column names
        pdfOutput.columns = [''.join(col) for col in pdfOutput.columns]
        # pdfOutput.columns = \
        #     pdfOutput.columns.droplevel(0)

        # Reset index
        pdfOutput.reset_index(inplace=True)

        # Set datefield as index
        pdfOutput = pdfOutput.set_index(indexField)

    if resampleFrequency != 'Total':
        # Transform Fields
        pdfOutput = pdfOutput.\
            groupby([dateField]+dimensionFields).\
            agg(dictTransformation)

        # Concatenate different levels of column names
        pdfOutput.columns = [''.join(col) for col in pdfOutput.columns]
        # pdfOutput.columns = \
        #     pdfOutput.columns.droplevel(0)

        # Reset index
        pdfOutput.reset_index(inplace=True)

        # Set datefield as index
        pdfOutput = pdfOutput.set_index(dateField)

    return pdfOutput

import pandas as pd


def aggregateGoogleTrendsData(pdfInput, lstDimensions, lstFields):
    # Aggregate data for normal keyword (using the average search volume).
    pdfAggrLeft = \
        pdfInput.\
        groupby(lstDimensions).\
        agg({str(lstFields[0]): ['mean']})

    pdfAggrLeft.columns = \
        pdfAggrLeft.columns.droplevel(0)

    pdfAggrLeft = \
        pdfAggrLeft.rename(columns={'mean': 'mean' +
                                            str(lstFields[0]).title()})

    pdfAggrLeft.reset_index(inplace=True)

    print(pdfAggrLeft.head(3))

    if len(lstDimensions) > 1:
        # Aggregate data for benchmark keyword
        # (using the average search volume).

        pdfAggrRight = pdfInput.\
                groupby(lstDimensions).\
                agg({str(lstFields[1]): ['mean']})

        pdfAggrRight.columns = \
            pdfAggrRight.columns.droplevel(0)

        pdfAggrRight = \
            pdfAggrRight.rename(columns={'mean': 'mean' +
                                                 str(lstFields[1]).title()})

        pdfAggrRight.reset_index(inplace=True)

    if len(lstDimensions) > 1:
        pdfGoogleTrendsResultsAggregated = \
            pd.merge(pdfAggrLeft, pdfAggrRight, on=lstDimensions, how='outer')

    if len(lstDimensions) == 1:
        pdfGoogleTrendsResultsAggregated = \
            pdfAggrLeft

    return pdfGoogleTrendsResultsAggregated

from salesSignals.googleTrendsData.createDateFilter \
    import createDateFilter
from salesSignals.googleTrendsData.downloadGoogleTrendsData \
    import downloadGoogleTrendsData


def createTestData(varKeyword):
    varFilterDuration = 48
    varDateFilter = createDateFilter(varFilterDuration, '2019-12-31')
    pdfGoogleTrendsData = downloadGoogleTrendsData(varDateFilter,
                                                   lstKeywords=[varKeyword])

    pdfGoogleTrendsData = pdfGoogleTrendsData.sort_index()

    timeseriesTest = pdfGoogleTrendsData[['interest']]

    return timeseriesTest

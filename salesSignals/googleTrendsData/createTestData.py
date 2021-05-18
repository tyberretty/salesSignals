from salesSignals.googleTrendsData.createDateFilter \
    import createDateFilter
from salesSignals.googleTrendsData.downloadGoogleTrendsData \
    import downloadGoogleTrendsData


def createTestData(varKeyword,
                   varEndDateFilter='2019-12-31'):

    varFilterDuration = 48
    varDateFilter = createDateFilter(varFilterDuration,
                                     varEndDateFilter)

    pdfGoogleTrendsData = downloadGoogleTrendsData(varDateFilter,
                                                   lstKeywords=[varKeyword])

    pdfGoogleTrendsData = pdfGoogleTrendsData.sort_index()

    timeseriesTest = pdfGoogleTrendsData[['interest']]

    return timeseriesTest

import pandas as pd
import datetime
from pytrends.request import TrendReq


def downloadGoogleTrendsData(GTdatefilter, lstKeywords=None,
                             longFormat=True, countryCode='NL',
                             language='en-US', searchCategory=71,
                             GTtz=360, GTtimeout=(10, 25),
                             GTretries=2, GTbackoff_factor=0.1):

    # Send error message if the list with keywords is not supplied
    if lstKeywords is None:
        print('Supplied list of keywords is empty.')
        print('Please make sure to supply a list of keywords')

        # Download the search volumes for the supplied keywords
    if lstKeywords is not None:
        print(datetime.datetime.now(),
              ' - Start downloading Google Trends API Output')

        # Configure quasi-API
        pytrends = TrendReq(hl=language, tz=GTtz,
                            timeout=GTtimeout, retries=GTretries,
                            backoff_factor=GTbackoff_factor)

        # Set the right configuration for request query Google trends.
        # Where needed make sure the request is a global one.

        if countryCode != 'WORLD':
            print(lstKeywords, searchCategory, GTdatefilter)

            pytrends.build_payload(kw_list=lstKeywords,
                                   cat=searchCategory,
                                   timeframe=GTdatefilter,
                                   geo=countryCode)

        if countryCode == 'WORLD':
            pytrends.build_payload(kw_list=lstKeywords,
                                   cat=searchCategory,
                                   timeframe=GTdatefilter)

        # Download timeseries
        pdfTempGoogleTrendsResults = None
        pdfTempGoogleTrendsResults = pytrends.interest_over_time()

        print(len(pdfTempGoogleTrendsResults.index))
        print(pdfTempGoogleTrendsResults.head(3))

        if pdfTempGoogleTrendsResults is not None and \
                len(pdfTempGoogleTrendsResults.index) > 0:

            # Reset the index of dataframe
            pdfTempGoogleTrendsResults.reset_index(inplace=True)

            pdfTempGoogleTrendsResults = pdfTempGoogleTrendsResults.\
                reset_index(drop=True)

            # Recast date field into string
            pdfTempGoogleTrendsResults['date'] = \
                pdfTempGoogleTrendsResults['date'].astype(str).str[:10]

            # Reshape the dataframe into long format (if configured).
            if longFormat is True:
                pdfTempGoogleTrendsResultsLong = \
                    pd.melt(pdfTempGoogleTrendsResults,
                            id_vars=['date', 'isPartial'],
                            value_vars=lstKeywords,
                            var_name=None, value_name='value',
                            col_level=None)

                pdfTempGoogleTrendsResultsFinal = \
                    pdfTempGoogleTrendsResultsLong.\
                    rename(columns={'variable': 'keyword',
                                    'value': 'interest'})

            # Keep the dataframe into wide format (if configured).
            if longFormat is False:
                pdfTempGoogleTrendsResultsFinal = \
                    pdfTempGoogleTrendsResults

        # Create the right Index for the dataframe
        pdfTempGoogleTrendsResultsFinal = \
            pdfTempGoogleTrendsResultsFinal.set_index('date')

        print(datetime.datetime.now(), ' - Download finished')

    return pdfTempGoogleTrendsResultsFinal

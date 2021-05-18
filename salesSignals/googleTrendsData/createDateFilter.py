import datetime
from dateutil.relativedelta import relativedelta


def createDateFilter(varFilterDuration,
                     varEndDateFilter=None,
                     varDateFormat='%Y-%m-%d'):

    # Reformat Date
    print('Duration filter Google Trends', varFilterDuration)

    if varEndDateFilter is not None:
        varEndDateFilter = datetime.\
            datetime.\
            strptime(varEndDateFilter, varDateFormat)

        varEndDateFilter = varEndDateFilter.date()

    # If no end date is defined for the filter
    # use today as end date

    if varEndDateFilter is None:
        varEndDateFilter = datetime.date.today()

    print('End Date time filter Google Trends',
          varEndDateFilter)

    print('Duration filter Google Trends',
          varFilterDuration)

    # Deduct Startdate of the date filter
    # from the end date & the defined duration

    varStartDateFilter = \
        varEndDateFilter + \
        relativedelta(months=-varFilterDuration)

    varTimeFilter = \
        str(varStartDateFilter) + ' ' + str(varEndDateFilter)

    print('Time filter for Google Trends: ', varTimeFilter)

    return varTimeFilter

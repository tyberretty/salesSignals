"""
Unit tests for the Statistical Tests
"""


class TestStatisticalTesting:

    def test_unitTestStatisticalTestTrendAcceptTrend(self):
        from salesSignals.googleTrendsData.createTestData \
            import createTestData
        from salesSignals.statisticalTests.nonParamatricTrendtest \
            import nonParamatricTrendtest

        timeseriesTest = createTestData('vegan')

        trend = nonParamatricTrendtest(timeseriesTest)

        assert (1 == trend)

    def test_unitTestStatisticalTestRejectTrend(self):
        from salesSignals.googleTrendsData.createTestData \
            import createTestData
        from salesSignals.statisticalTests.nonParamatricTrendtest \
            import nonParamatricTrendtest

        timeseriesTest = createTestData('asoerges')

        trend = nonParamatricTrendtest(timeseriesTest)

        assert (0 == trend)

    def test_unitTestStatisticalTestAcceptSeasonality(self):
        from salesSignals.googleTrendsData.createTestData \
            import createTestData
        from salesSignals.statisticalTests.seasonalityTest \
            import seasonalityTest

        varTestFrequency = 12
        timeseriesTest = createTestData('asperges')

        seasonality = seasonalityTest(timeseriesTest,
                                      varTestFrequency,
                                      'interest',
                                      3)

        assert (1 == seasonality)

    def test_unitTestStatisticalTestRejectSeasonality(self):
        from salesSignals.googleTrendsData.createTestData \
            import createTestData
        from salesSignals.statisticalTests.seasonalityTest \
            import seasonalityTest

        varTestFrequency = 12
        timeseriesTest = createTestData('cola')

        seasonality = seasonalityTest(timeseriesTest,
                                      varTestFrequency,
                                      'interest',
                                      3)

        assert (0 == seasonality)

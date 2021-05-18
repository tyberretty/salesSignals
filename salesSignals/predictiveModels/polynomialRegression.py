from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np


def polynomialRegression(pdfInput,
                         varFieldName,
                         polyOrder,
                         pdfForecast=None):

    # Create Polynomial Features
    pdfInput['rowNumber'] = np.arange(len(pdfInput))
    XTrain = pdfInput['rowNumber'].values

    poly = PolynomialFeatures(polyOrder)
    XTrainPoly = poly.fit_transform(XTrain.reshape(-1, 1))

    # fitting the polynomial model with timeseries data
    scaler = MinMaxScaler()
    scaler = scaler.fit(pdfInput[varFieldName].values.reshape(-1, 1))
    yTrainScaled = \
        scaler.transform(pdfInput[varFieldName].values.reshape(-1, 1))

    model = LinearRegression()
    model = model.fit(XTrainPoly, yTrainScaled)

    if pdfForecast is not None:
        pdfForecast['rowNumber'] = np.arange(len(pdfForecast))
        XTest = pdfForecast['rowNumber'].values

        poly = PolynomialFeatures(polyOrder)
        XTestPoly = poly.fit_transform(XTest.reshape(-1, 1))

        # trend
        trend = model.predict(XTestPoly)
        pdfForecast['trend'] = scaler.inverse_transform(trend)

    if pdfForecast is None:
        pdfForecast = pdfInput
        trend = model.predict(XTrainPoly)
        pdfForecast['trend'] = scaler.inverse_transform(trend)

    return pdfForecast[['trend']]

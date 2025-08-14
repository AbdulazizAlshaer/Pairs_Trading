import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

def run_cointegration_test(y, x):
    """
    Tests for cointegration between two price series using the Engle-Granger method.

    Parameters:
    y (Series): Dependent variable (e.g., stock A)
    x (Series): Independent variable (e.g., stock B)

    Returns:
    dict: hedge ratio, p-value, and cointegration result
    """
    # Add constant to x for regression
    x = sm.add_constant(x)

    # Run ordinary least squares linear regression: y = βx + c
    model = sm.OLS(y, x).fit()

    # Get β (hedge ratio is the coefficient of x)
    beta = model.params[1]

    # Get residuals from the regression
    residuals = model.resid

    # Apply Augmented Dickey-Fuller test on residuals
    adf_result = adfuller(residuals)
    p_value = adf_result[1]

    # Decide if the pair is cointegrated (p-value < 0.05)
    is_cointegrated = p_value < 0.05

    return {
        "hedge_ratio": beta,
        "p_value": p_value,
        "is_cointegrated": is_cointegrated
    }

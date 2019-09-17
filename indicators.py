
def RSI(candles, length):
    # Get the difference in price from previous step
    delta = candles['close'].diff()
    # Get rid of the first row, which is NaN since it did not have a previous
    # row to calculate the differences
    delta = delta[1:]
    # Make the positive gains (up) and negative gains (down) Series
    up, down = delta.copy(), delta.copy()
    up[up < 0.0] = 0.0
    down[down > 0.0] = 0.0
    # Calculate the EWMA
    roll_up1 = up.ewm(com=(length - 1), min_periods=length).mean()
    roll_down1 = down.abs().ewm(com=(length - 1), min_periods=length).mean()
    # Calculate the RSI based on EWMA
    RS1 = roll_up1 / roll_down1
    RSI1 = 100.0 - (100.0 / (1.0 + RS1))

    return RSI1
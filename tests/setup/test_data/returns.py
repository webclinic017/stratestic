import pandas as pd
import numpy as np
from pandas import Timestamp

cumulative = np.array([1.25, 1.26, 1.27, 1.23, 1.20, 1.22, 1.25, 1.30, 1.29, 1.26])
log_returns = np.array([0.025, 0.016, -0.10, 0.03, 0.07, 0.04, -0.02, -0.05, 0.01, 0.03])

index = pd.DatetimeIndex([
    Timestamp('2023-09-01 20:00:00+0000', tz='UTC'),
    Timestamp('2023-09-01 21:00:00+0000', tz='UTC'),
    Timestamp('2023-09-01 22:00:00+0000', tz='UTC'),
    Timestamp('2023-09-01 23:00:00+0000', tz='UTC'),
    Timestamp('2023-09-02 00:00:00+0000', tz='UTC'),
    Timestamp('2023-09-02 01:00:00+0000', tz='UTC'),
    Timestamp('2023-09-02 02:00:00+0000', tz='UTC'),
    Timestamp('2023-09-02 03:00:00+0000', tz='UTC'),
    Timestamp('2023-09-02 04:00:00+0000', tz='UTC'),
    Timestamp('2023-09-02 05:00:00+0000', tz='UTC'),
], freq='1H')

cum_returns = pd.Series(cumulative, index=index)

returns = pd.Series(log_returns, index=index)

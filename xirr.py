from datetime import date
from pyxirr import xirr
import datetime
import numpy as np
# dates = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]
# amounts = [-1000, 750, 500]


dates = [
    date(2020, 4, 1),
    date(2020, 5, 1),
    date(2020, 6, 1),
    date(2020, 7, 1),
    date(2020, 8, 1),
    date(2020, 9, 1),
    date(2020, 10, 1),
    date(2020, 11, 1),
    date(2020, 11, 23)
]

amounts = [
    -10000,
    -10000,
    -10000,
    -10000,
    -10000,
    -10000,
    -10000,
    -10000,
    97538
]







# dates = [
#     datetime.date(2023, 1, 15),
#     datetime.date(2023, 2, 15),
#     datetime.date(2023, 8, 15),
#     datetime.date(2023, 4, 15),
#     datetime.date(2023, 5, 15),
#     datetime.date(2023, 8, 15),
#     datetime.date(2023, 7, 15),
#     datetime.date(2023, 8, 15),
#     datetime.date(2023, 9, 15),
#     datetime.date(2023, 10, 15),  # Remove duplicate,
#     datetime.date(2023, 10, 15)  # Remove duplicate

# ]

# amounts = [
#     -10000.0,
#     -15000.0,
#     -12000.0,
#     -10000.0,
#     -11000.0,
#     -13000.0,
#     -10000.0,
#     -14000.0,
#     -12000.0,
#     -15000.0,
#     135032
# ]

# Convert dates to strings for pyxirr
# dates_str = [date.strftime("%Y-%m-%d") for date in dates]

# feed columnar data
result = xirr(dates, amounts)
print(result)
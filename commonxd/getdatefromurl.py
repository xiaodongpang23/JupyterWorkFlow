import os
from urllib.request import urlretrieve

import pandas as pd

Data_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'


def get_data_fromurl(filename='Fremont.csv', url=Data_URL,
                     force_download=False):
    """Download and cache the url data
    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data
    Returns
    -------
    data : pandas.DataFrame
        The fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    #data = pd.read_csv(filename, index_col='Date', parse_dates=True)
    data = pd.read_csv(filename, index_col='Date')
    # below is to speed up parse_dates by specifying the format of date in the data file, for more format see "Python strftime reference" online

    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)

    return data


import pandas as pd
from commonxd.getdatefromurl import get_data_fromurl

def test_fremont_data():
    data = get_data_fromurl()
    data.columns = ["West", "East"]
    data['Total'] = data['West'] + data['East']
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)



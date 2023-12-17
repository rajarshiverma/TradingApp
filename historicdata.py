from login import *
from tickData import *
import sys

exchange = "NSE"
tick = "TATACHEM-EQ"
symboltoken = str(findTickToken(exchange,tick))
print(symboltoken)

try:
    historicParam={
    "exchange": exchange,
    "symboltoken": symboltoken ,
    "interval": "FIVE_MINUTE",
    "fromdate": "2023-12-15 09:15", 
    "todate": "2023-12-15 15:30"
    }

    #columns which are present in data
    columns =['TIME','OPEN','HIGH','LOW','CLOSE','VOLUME']
    data = pd.DataFrame(sma.getCandleData(historicParam)['data'],columns = columns)
    # data["TIME"] = pd.to_datetime(data["TIME"], format="%Y-%m-%dT%H:%M:%S")

    # For converting data into json format and adding into json file for better utilisation of data
    json_data = data.to_json(orient = 'records',indent=2)
    with open('output.json', 'w') as json_file:
        json_file.write(json_data)
except Exception as e:
    logger.exception(f"Historic Api failed: {e}")

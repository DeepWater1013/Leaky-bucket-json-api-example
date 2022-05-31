import json
import time
import requests
import hone
import logging
import sys
from pandas import read_csv

logging.basicConfig(filename='Update3DCart.log', filemode='w',
                    format='%(asctime)s : %(message)s', level=logging.DEBUG)

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'SecureURL': 'xxxxx',
    'PrivateKey': 'xxxxx',
    'Token': 'xxxxxx'
}
# filename = sys.argv[1]
filename = 'tempstock.csv'

# Add header in csv file using Pandas module
df = read_csv(filename, header=None)
filename = "header_" + filename
df.to_csv(filename, header=["SKUInfo_catalogid", "SKUInfo_id", "SKUInfo_stock",
          "SKUInfo_price", "SKUInfo_saleprice", "SKUInfo_onsale"], index=False)

# Hone module default usage
# optional_arguments = {
#  "delimiters": [" ", "_", ","]
# }
#Hone = hone.Hone(**optional_arguments)
# schema = Hone.get_schema('path/to/input.csv')  # nested JSON schema for input.csv

Hone = hone.Hone()
_lst = Hone.convert(filename)  # final structure, nested according to schema

n = 50
for i in range(0, len(_lst), n):
    result = _lst[i:i + n]
    print(result)
    reqs = requests.put('https://apirest.3dcart.com/3dCartWebAPI/v2/Products',
                        data=json.dumps(result), headers=headers)
    time.sleep(0.5)
    print(reqs)

import pandas as pd
from dateutil import parser
import logging
import numpy as np


class DataProcessing:
    def __init__(self):
        self.data_record = {"date": [], "type": [], "value": []}
        self.json_data = {}
        self.trend_data_df = pd.DataFrame()
        self.read_data()

    def read_data(self):
        total_data = pd.read_json('https://raw.githubusercontent.com/datameet/covid19/master/data/all_totals.json')
        self.json_data = total_data.to_dict()['rows']

    def process_json_data(self, row):
        dt = (parser.parse(row['key'][0])).date()
        self.data_record['date'].append(dt)
        self.data_record['type'].append(row['key'][1])
        self.data_record['value'].append(row['value'])

    def make_data(self):
        for key, item in self.json_data.items():
            self.process_json_data(item)

    def get_group_by_type_data(self):
        val = np.array(self.trend_data_df['value'].values.tolist())
        return np.reshape(val, (-1,4))


    def start_data_process(self):
        # self.read_data()
        self.make_data()
        if len(self.data_record['date']) > 0:
            self.trend_data_df = pd.DataFrame(self.data_record)
            logging.info("Data parsed")
        else:
            logging.error("No data found")
            raise Exception("No data found")

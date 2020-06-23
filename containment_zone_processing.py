import pandas as pd

class ContainmentZoneProcessing:
    def __init__(self):
        self.data_df = pd.DataFrame()
        self.read_data()

    def read_data(self):
        url = 'https://raw.githubusercontent.com/datameet/covid19/master/data/district-containment-zones-2020-04-30.csv'
        self.data_df = pd.read_csv(url)

    def get_state_list(self):
        return list(self.data_df.State.unique())

    def get_zone_type_list(self):
        return list(self.data_df.Classification.unique())

    def get_state_wise_districts_zone(self, state, zone_type):
        temp_df = self.data_df[(self.data_df['State'] == state) & (self.data_df['Classification'] == zone_type)]
        return temp_df['District Name'].values.tolist()
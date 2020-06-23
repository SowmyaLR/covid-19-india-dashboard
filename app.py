import streamlit as st
import pandas as pd
from data_processing import DataProcessing
from containment_zone_processing import ContainmentZoneProcessing

dp = DataProcessing()
dp.start_data_process()
data_list = dp.get_group_by_type_data()
containment = ContainmentZoneProcessing()
state_list = containment.get_state_list()
zone_list = containment.get_zone_type_list()

st.header("India COVID-19 dashboard")
st.sidebar.header('User Input')


def create_active_cases_chart():
    st.subheader('COVID-19 trend')
    chart_data = pd.DataFrame(data_list, columns=['Active Case', 'Cured', 'Death', 'Total Cases'])
    st.line_chart(chart_data)


def create_sidebar_menu():
    state = st.sidebar.selectbox('Select a State', state_list)
    zone = st.sidebar.selectbox('Select zone type', zone_list)
    df = pd.DataFrame({"state": state, "zone": zone}, index=[0])
    return df


create_active_cases_chart()
temp = create_sidebar_menu()
district_list = containment.get_state_wise_districts_zone((temp.state)[0], (temp.zone)[0])
st.subheader(f"Containment zone regions for {(temp.state)[0]}- {(temp.zone)[0]}")
st.table(pd.DataFrame({"District": district_list}, columns=["District"]))
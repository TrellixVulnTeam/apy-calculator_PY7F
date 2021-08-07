import streamlit as st
import pandas as pd

st.sidebar.header("Configuration")

apr = st.sidebar.number_input("APR%: ")
apr = apr / 100

weekly = 52
daily = 365
hourly = daily * 24
half_hourly = hourly * 2
minutely = hourly * 60

# token_starting_price = st.sidebar.number_input("Token price at start: ", value=1)
# token_ending_price = st.sidebar.number_input("Token price at end: ", value=1)

# token_price_change = (token_ending_price - token_starting_price) / 100

n = float(hourly)

period_dict = {"Monthly" : 12,
               "Weekly": 52,
               "Daily": 365,
               "Hourly": 8760}

_period = st.sidebar.selectbox("Compounding period:", options=["Hourly","Daily","Weekly","Monthly"])
period = period_dict[_period]

initial_capital = st.sidebar.number_input("Initial capital ($): ", value=30000)

compound_cost = st.sidebar.number_input("Cost of compounding: ", value=0.01)

capital_list = []
capital = initial_capital

for _ in range(int(period)):
    _capital = capital * (1 + (apr / period)) - compound_cost
    capital_list.append(round(_capital, 2))
    capital = _capital


df = pd.DataFrame(list(capital_list), index = range(int(period)), columns = ["Cumulative Capital"])

st.subheader("One Year Projection")

apy = int((capital/initial_capital)*100)

st.text("APY: {}%".format(apy))
st.text("Final capital: ${}".format(int(capital)))

st.subheader("1 year projection:")
st.line_chart(df)

# st.text("APY = {}x, {}%".format((int(apy)), int(apy*100)))
# st.text("Total year = {}".format(int(total)))
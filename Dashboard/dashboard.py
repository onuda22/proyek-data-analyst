import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.header('Bike Sharing Dashboard :sparkles:')


day_data = pd.read_csv('daydf.csv')
hour_data = pd.read_csv('hourdf.csv')

day_data['dteday'] = pd.to_datetime(day_data['dteday'])
data_2011 = day_data[day_data["dteday"].dt.year == 2011]
data_2012 = day_data[day_data["dteday"].dt.year == 2012]

rental_month2011 = data_2011.groupby("mnth")['cnt'].sum()
rental_month2012 = data_2012.groupby("mnth")['cnt'].sum()
rental_season = hour_data.groupby('season')['cnt'].sum()

#Grafik Tahun 2011
st.subheader("Rental Bike Performance in 2011")

fig, ax = plt.subplots()
rental_month2011.plot(kind='bar', ax=ax)
ax.set_ylabel('Total Rental')
ax.set_xlabel('Bulan')
ax.set_title('Total Rental per Bulan Tahun 2011')

st.pyplot(fig)

#Grafik Tahun 2012
st.subheader("Rental Bike Performance in 2012")

fig, ax = plt.subplots()
rental_month2012.plot(kind='bar', ax=ax)
ax.set_ylabel('Total Rental')
ax.set_xlabel('Bulan')
ax.set_title('Total Rental per Bulan Tahun 2012')

st.pyplot(fig)

#Grafik Musim
st.subheader("Rental Bike Performance on Season")

fig, ax = plt.subplots()
rental_season.plot(kind='bar', ax=ax)
ax.set_ylabel('Total Rental')
ax.set_xlabel('Musim')
ax.set_title('Total Rental per Musim')

st.pyplot(fig)
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


df = yf.download(tickers='BTC-USD', start = '2017-01-01', end = '2025-12-31', interval= '1d')
df = df.reset_index()
df.columns = [col[0] for col in df.columns]
df['Date'] = pd.to_datetime(df['Date'])
data = df.sort_index(ascending = False).reset_index()
data.drop('index', axis =1 , inplace=True)

bitcoin_sample = data[0:100]
data.set_index('Date', inplace=True)
data['Close_price_pct_change'] = data['Close'].pct_change() * 100


st.set_page_config(page_title= 'Bitcoin Dashboard',
           layout= 'wide' )
st.title('Comprehensive Bitcoin Price Analysis Dashboard')

## 1st plot:

st.subheader('Bitcoin Candlestick Chart (First 100 Days)')

trace = go.Candlestick(x=bitcoin_sample['Date'],
               high=bitcoin_sample['High'],
               open=bitcoin_sample['Open'],
               close=bitcoin_sample['Close'],
               low=bitcoin_sample['Low']

               )

candle_data = [trace]

layout = {
'title' : 'Bitcoin Historical Price',
'xaxis': {'title' : 'Date'}
}

fig_candle = go.Figure(data= candle_data, layout = layout)
fig_candle.update_layout(xaxis_rangeslider_visible = False)

st.plotly_chart(fig_candle, use_container_width=True)


## 2nd plot:
st.subheader('Daily Percentage Change in Closing Price')

fig_pct = go.Figure([
    go.Scatter(x = data.index,
               y = data['Close_price_pct_change'],
               mode = 'lines')
    ])

fig_pct.update_layout(
    xaxis_title = 'Date',
    yaxis_title = '% Change',
    template = 'plotly_white'
)

st.plotly_chart(fig_pct, use_container_width=True)

## 3rd plot:

st.subheader('Bitcoin Price Trends Over Time')
price_type = st.selectbox('Select Price Type:', options = ['Open', 'High', 'Low', 'Close'], index = 3)

fig_trend = go.Figure([
    go.Scatter(x = data.index,
               y = data[price_type],
               mode = 'lines')
    ])

fig_trend.update_layout(
    title = price_type + ' Price Over Time',
    xaxis_title = 'Date',
    yaxis_title = 'Price(USD)',
    template = 'plotly_white'
)

st.plotly_chart(fig_trend, use_container_width=True)

## 4th plot:

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Yearly Average Close Price')
    yearly_average = data['Close'].resample('YE').mean()
    fig_year = px.bar(
        x=yearly_average.index.strftime('%Y'),
        y = yearly_average.values,
        labels = {'x':'Year', 'y':'Average Value'},
        title = 'Yearly Average Trend',
    )

    st.plotly_chart(fig_year, use_container_width=True)

with col2:
    st.subheader('Quarterly Average Close Price')
    quarterly_average = data['Close'].resample('QE').mean()
    fig_quarter = px.bar(
        x=quarterly_average.index.strftime('%Y'),
        y=quarterly_average.values,
        labels={'x': 'Quarter', 'y': 'Average Value'},
        title='Quarterly Average Trend',
    )

    st.plotly_chart(fig_quarter, use_container_width=True)

with col3:
    st.subheader('Monthly Average Close Price')
    monthly_average = data['Close'].resample('ME').mean()
    fig_month = px.line(
        x=monthly_average.index,
        y=monthly_average,
        labels={'x': 'Month', 'y': 'Average Value'},
        title='Monthly Average Trend',
    )

    st.plotly_chart(fig_month, use_container_width=True)

## 5th plot:

col4, col5 = st.columns(2)

with col4:
    st.subheader('Closing Price (Normal Scale)')
    fig_normal = px.line(
        data_frame = data,
        x=data.index,
        y='Close',
        labels={'x': 'Date', 'Close': 'Closing Price'},
        title='Bitcoin Closing Price (Normal Scale)'
    )

    st.plotly_chart(fig_normal, use_container_width=True)

with col5:
    st.subheader('Closing Price (Log Scale)')
    fig_log = px.line(
        data_frame = data,
        x=data.index,
        y= np.log1p(data['Close']),
        labels={'x': 'Date', 'y': 'Log(Closing Price + 1)'},
        title='Bitcoin Closing Price (Log Scale)'
    )

    st.plotly_chart(fig_log, use_container_width=True)

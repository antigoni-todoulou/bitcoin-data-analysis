# bitcoin-data-analysis

Historical Bitcoin market data was obtained using the `yfinance` library.
 
Ticker:
 
```python
BTC-USD
```
 
Data period:
 
```text
2017 – 2025
```
 
## Technologies Used
 
- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- yFinance
- Matplotlib
- Seaborn
 
---
 
## Analysis Performed
 
### 1. OHLC Candlestick Analysis
 
Built interactive candlestick charts using:
 
- Open price
- High price
- Low price
- Close price
 
to visualise Bitcoin price action over time.
 
### 2. Bitcoin Risk & Volatility Analysis
 
Calculated:
 
- Daily returns
- 30-day rolling volatility
- 90-day rolling volatility
 
to evaluate changing risk levels through time.
 
### 3. Investment Growth Simulation
 
Modelled the growth of a €1 investment in Bitcoin using cumulative returns.
 
Key metric:
 
```python
cumulative_return = (1 + daily_return).cumprod()
```
 
### 4. Bitcoin Crash Analysis
 
Identified the largest daily crashes in Bitcoin history.
 
Analyses include:
 
- Worst daily losses
- Crash visualisations
- Historical crash comparison
 
### 5. Volume Confirmation Analysis
 
Investigated whether trading volume confirms price movements.
 
Market states were classified as:
 
- Strong Bullish
- Weak Bullish
- Strong Bearish
- Weak Bearish
 
based on simultaneous changes in price and volume.
 
### 6. Best & Worst Years Analysis
 
Calculated annual compounded returns and identified:
 
- Best performing year
- Worst performing year
 
for Bitcoin investors.
 
---
 
## Interactive Dashboard
 
A Streamlit dashboard was built to provide interactive access to the analysis.
 
Dashboard features include:
 
- Candlestick chart
- Daily percentage change visualisation
- Interactive price selector
- Annual, quarterly and monthly summaries
- Normal vs logarithmic price comparison
 
---
 
 
## How to Run the Dashboard
 
Install dependencies:
 
```bash
pip install -r requirements.txt
```
 
Launch the Streamlit application:
 
```bash
streamlit run dashboard.py
```
 
---
 
## Key Skills Demonstrated
 
- Data Cleaning
- Financial Data Analysis
- Time Series Analysis
- Volatility Modelling
- Investment Performance Analysis
- Exploratory Data Analysis (EDA)
- Plotly Visualisation
- Dashboard Development
- Streamlit
 
---
 
## Author
 
Antigoni Todoulou

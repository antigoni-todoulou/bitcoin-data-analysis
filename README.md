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

## Key Takeaways

### Bitcoin Exhibits High Volatility

Rolling 30-day and 90-day volatility analysis shows that Bitcoin experiences significant fluctuations in risk over time.

Key observation:

- Short-term volatility spikes can exceed longer-term volatility periods.
- Market risk is highly dynamic and changes rapidly during major price events.

### Long-Term Returns Have Been Extraordinary

A simulated €1 investment at the beginning of the dataset grew substantially over time through the power of compounding.

Key observation:

- Despite multiple severe crashes, long-term investors were rewarded by significant cumulative returns.

### Major Single-Day Crashes Are Common

Analysis of the worst performing trading days identified several periods where Bitcoin lost a large percentage of its value within a single day.

Key observation:

- Extreme downside events are a recurring characteristic of Bitcoin markets.

### Trading Volume Only Partially Confirms Price Movements

Price and volume movements were classified into four market states:

- Strong Bullish
- Weak Bullish
- Strong Bearish
- Weak Bearish

Key observation:

- Strong Bullish and Weak Bullish signals occur with almost identical frequency.
- Strong Bearish and Weak Bearish signals are also relatively balanced.
- Volume does not consistently confirm Bitcoin price movements.

This suggests that price increases and declines often occur without corresponding increases in trading activity.

### Market Behaviour Is Not Strongly Dominated by Any Single State

Volume-price classification produced a relatively balanced distribution of market states.

Key observation:

- Bitcoin frequently alternates between bullish and bearish conditions.
- No single market regime overwhelmingly dominates the dataset.

### Bitcoin's Best and Worst Years Differ Dramatically

Annual compounded returns vary significantly across years.

Key observation:

- Bitcoin can deliver exceptional positive performance during favorable periods.
- The asset can also experience substantial annual drawdowns, highlighting its speculative nature.
 
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

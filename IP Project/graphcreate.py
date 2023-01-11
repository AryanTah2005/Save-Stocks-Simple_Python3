from plotly.subplots import make_subplots
import plotly.graph_objects as go
import yfinance as yf
def creategraph(tick,time):
    s2 = yf.Ticker(tick)
    hist=s2.history(period=time)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Candlestick(x=hist.index,open=hist['Open'], high=hist['High'],low=hist['Low'],close=hist['Close']))
    fig.update_layout(title={'text':tick})
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()

    return print('The graph has been launched in your web browser.')
     

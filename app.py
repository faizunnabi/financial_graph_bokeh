import pandas as pd
import pandas_datareader as pdr
from bokeh.plotting import figure,show,output_file
from datetime import datetime

start=datetime(2017,10,26)
end=datetime(2017,11,26)
data=pdr.get_data_yahoo('AAPL',start,end)
data_sorted=data.sort_index(axis=0,ascending=True)
open_list=list(data_sorted['Open'])
close_list=list(data_sorted['Close'])
date_list=list(data_sorted.index)
date_time=[datetime.strptime(str(d),'%Y-%m-%d %H:%M:%S').date() for d in date_list]
p=figure(x_axis_type='datetime',plot_width=800,plot_height=500,title="Financial Analysis of Apple",tools="",
              toolbar_location=None)
p.circle(date_time,open_list,legend="Open Price",size=6,color="green", alpha=0.5)
p.line(date_time,open_list,legend="Open Price",color="green", alpha=0.5)
p.circle(date_time,close_list,legend="Close Price",size=6,color="red", alpha=0.5)
p.line(date_time,close_list,legend="Close Price",color="red", alpha=0.5)
p.legend.location = "bottom_right"
show(p)

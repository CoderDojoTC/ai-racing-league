import plotly.express as px

df = px.data.tips()

fig = px.histogram(df, x="total_bill")

# this will start a web server and open your browser on the page
fig.show()
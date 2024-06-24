import dash
from dash import html
# from dash import dcc
# from dash.dependencies import Output, Input
# import plotly.express as px
# import pandas as pd

app = dash.Dash(__name__)
app.title = "Hello World"

# app root
app.layout = html.P("Hello World! :)")


# Run the app in Debug for development - change to False for production
if __name__ == "__main__":
    app.run_server(debug=True)
    
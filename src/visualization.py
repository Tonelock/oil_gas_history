
from pandas import DataFrame
import plotly.graph_objects as go

def create_time_series(df: DataFrame) -> go.Figure:
    """Creates a simple line plot from given data

    Args:
        df (DataFrame): Raw data

    Returns:
        fig: plotly graphic object
    """
    fig = go.Figure([go.Scatter(x=df["Date"], y =df["Close"], name = "Close")])
    fig.add_trace(go.Scatter(x=df["Date"],y=df["Open"],mode='lines', name = "Open"))

    return fig

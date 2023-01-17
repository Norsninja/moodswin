# Import the necessary packages
import plotly
import plotly.graph_objects as go
from cleaning_and_manipulating_data import clean_data
from flask import jsonify
from pymongo import MongoClient
import json


# Generate the visualization
def generate_visualization(df):
    # Create a figure object
    fig = go.Figure()
    
    # Add the data to the figure
    fig.add_trace(go.Bar(x=df.index, y=df['Mental Confidence'], name='Mental Confidence'))
    fig.add_trace(go.Bar(x=df.index, y=df['Physical Confidence'], name='Physical Confidence'))
    fig.add_trace(go.Bar(x=df.index, y=df['Embarrassment and Shame vs Pride and Self-Love'], name='Embarrassment and Shame vs Pride and Self-Love'))
    fig.add_trace(go.Bar(x=df.index, y=df['Feeling of Extroversion vs Introversion'], name='Feeling of Extroversion vs Introversion'))
    fig.add_trace(go.Bar(x=df.index, y=df['Appetite'], name='Appetite'))
    fig.add_trace(go.Bar(x=df.index, y=df['Intestinal Pain'], name='Intestinal Pain'))
    fig.add_trace(go.Bar(x=df.index, y=df['Did you exercise yesterday (15+ minutes or more)'], name='Did you exercise yesterday (15+ minutes or more)'))
    fig.add_trace(go.Bar(x=df.index, y=df['How did you sleep last night?'], name='How did you sleep last night?'))
    
    # Customize the figure
    fig.update_layout(title='Mood Swinger Survey Results', xaxis_title='Survey Result', yaxis_title='Score')
    
    # Convert the visualization dataframe to a JSON-serializable type 
    fig_json = plotly.io.to_json(fig)

    return fig



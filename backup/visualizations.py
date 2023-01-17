# Import the necessary packages
import plotly
import plotly.express as px
from cleaning_and_manipulating_data import clean_data
from flask import jsonify
from pymongo import MongoClient
import json


# Generate the visualization
def generate_visualization(data):
    df = data
    fig = px.line(
        df, 
        x="date_submitted", 
        y=["Appetite", "Embarrassment and Shame vs Pride and Self-Love", "Feeling of Extroversion vs Introversion", 
           "How did you sleep last night?", "Intestinal Pain", "Mental Confidence", "Physical Confidence"],
        labels={'date_submitted': 'Submitted Date', 
                'Appetite': 'Appetite',
                'Embarrassment and Shame vs Pride and Self-Love': 'Embarrassment and Shame vs Pride and Self-Love',
                'Feeling of Extroversion vs Introversion': 'Feeling of Extroversion vs Introversion',
                'How did you sleep last night?': 'Sleep Quality',
                'Intestinal Pain': 'Intestinal Pain',
                'Mental Confidence': 'Mental Confidence',
                'Physical Confidence': 'Physical Confidence'},
        title="MoodSwinger Survey Results Over Time"
    )
    
    # Convert the visualization dataframe to a JSON-serializable type 
    fig_json = plotly.io.to_json(fig)


    return fig_json



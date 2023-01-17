# Cleaning and manipulating data
import pandas as pd


def clean_data(results):
    # Extract the keys and values from the data
    keys = results[0].keys()
    values = [[result[key] if key in result else None for key in keys] for result in results]

    
    # Create a data frame from the keys and values
    df = pd.DataFrame(values, columns=keys)
    
    # Clean and manipulate the data as needed
    df = df.drop(columns=['_id', 'Pick a Color'])
    df['Appetite'] = df['Appetite'].astype(int)
    df['Did you exercise yesterday (15+ minutes or more)'] = df['Did you exercise yesterday (15+ minutes or more)'].apply(lambda x: 1 if x == 'yes' else 0)
    df['Embarrassment and Shame vs Pride and Self-Love'] = df['Embarrassment and Shame vs Pride and Self-Love'].astype(int)
    df['Feeling of Extroversion vs Introversion'] = df['Feeling of Extroversion vs Introversion'].astype(int)
    df['How did you sleep last night?'] = df['How did you sleep last night?'].astype(int)
    df['Intestinal Pain'] = df['Intestinal Pain'].astype(int)
    df['Mental Confidence'] = df['Mental Confidence'].astype(int)
    df['Physical Confidence'] = df['Physical Confidence'].astype(int)
    
    return df

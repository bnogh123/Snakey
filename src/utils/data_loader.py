"""
Data loading utilities for the Snakey dashboard
"""

import pandas as pd
import os
from config import RAW_DATA_DIR

def load_us_snakes():
    """Load US snake species data"""
    file_path = os.path.join(RAW_DATA_DIR, 'us_snake_species.csv')
    df = pd.read_csv(file_path)
    return df

def load_global_snakes():
    """Load global snake species data"""
    file_path = os.path.join(RAW_DATA_DIR, 'global_snake_species.csv')
    df = pd.read_csv(file_path)
    return df

def load_domesticated_snakes():
    """Load domesticated snake data"""
    file_path = os.path.join(RAW_DATA_DIR, 'domesticated_snakes.csv')
    df = pd.read_csv(file_path)
    return df

def load_media_snakes():
    """Load snakes in media data"""
    file_path = os.path.join(RAW_DATA_DIR, 'snakes_in_media.csv')
    df = pd.read_csv(file_path)
    return df

def load_farming_data():
    """Load snakeskin farming data"""
    file_path = os.path.join(RAW_DATA_DIR, 'snakeskin_farming.csv')
    df = pd.read_csv(file_path)
    return df

def get_us_snake_by_state(state_abbrev):
    """Get all snakes found in a specific US state"""
    df = load_us_snakes()
    # Filter snakes that have the state in their 'states' column
    return df[df['states'].str.contains(state_abbrev, na=False)]

def get_snakes_by_continent(continent):
    """Get all snakes from a specific continent"""
    df = load_global_snakes()
    return df[df['continent'] == continent]

def get_venomous_snakes(df):
    """Filter for venomous snakes only"""
    return df[df['venomous'] == 'Yes']

def get_lethality_stats(df):
    """Calculate lethality statistics"""
    venomous = get_venomous_snakes(df)
    if len(venomous) == 0:
        return {
            'avg_lethality': 0,
            'max_lethality': 0,
            'high_lethality_count': 0
        }

    return {
        'avg_lethality': venomous['lethality_score'].mean(),
        'max_lethality': venomous['lethality_score'].max(),
        'high_lethality_count': len(venomous[venomous['lethality_score'] >= 7])
    }

def get_size_stats(df):
    """Calculate size statistics"""
    return {
        'avg_length': df['avg_length_cm'].mean(),
        'max_length': df['max_length_cm'].max(),
        'largest_species': df.loc[df['max_length_cm'].idxmax(), 'common_name']
    }

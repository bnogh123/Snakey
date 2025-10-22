"""
Configuration settings for the Snakey dashboard
"""

import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directories
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Assets directory
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# Color scheme for visualizations
COLORS = {
    'primary': '#2C3E50',
    'secondary': '#E74C3C',
    'success': '#27AE60',
    'warning': '#F39C12',
    'danger': '#C0392B',
    'info': '#3498DB',
    'background': '#ECF0F1',
    'text': '#2C3E50'
}

# Lethality scale (0-10)
LETHALITY_COLORS = {
    'low': '#27AE60',      # Green (0-3)
    'medium': '#F39C12',   # Orange (4-6)
    'high': '#E74C3C',     # Red (7-8)
    'extreme': '#8B0000'   # Dark Red (9-10)
}

# Map settings
MAP_SETTINGS = {
    'us_center': [39.8283, -98.5795],
    'us_zoom': 4,
    'world_center': [20, 0],
    'world_zoom': 2
}

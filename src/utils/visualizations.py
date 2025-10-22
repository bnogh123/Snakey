"""
Visualization utilities for creating charts and maps
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from config import LETHALITY_COLORS, COLORS

def create_lethality_heatmap(df, title="Snake Lethality Heatmap"):
    """Create a choropleth map showing lethality by region"""
    # For US data, we need to expand the states column
    if 'states' in df.columns:
        # Create a row for each state a snake is found in
        rows = []
        for _, row in df.iterrows():
            if pd.notna(row['states']):
                states = row['states'].split(',')
                for state in states:
                    new_row = row.copy()
                    new_row['state'] = state.strip()
                    rows.append(new_row)

        expanded_df = pd.DataFrame(rows)

        # Calculate average lethality per state
        state_lethality = expanded_df.groupby('state')['lethality_score'].mean().reset_index()
        state_lethality.columns = ['state', 'avg_lethality']

        # Create choropleth map
        fig = go.Figure(data=go.Choropleth(
            locations=state_lethality['state'],
            z=state_lethality['avg_lethality'],
            locationmode='USA-states',
            colorscale='Reds',
            colorbar_title="Lethality Score",
            zmin=0,
            zmax=10
        ))

        fig.update_layout(
            title_text=title,
            geo_scope='usa',
            height=600
        )

        return fig

    return None

def create_size_distribution(df, title="Snake Size Distribution"):
    """Create a histogram of snake sizes"""
    fig = px.histogram(
        df,
        x='avg_length_cm',
        nbins=30,
        title=title,
        labels={'avg_length_cm': 'Average Length (cm)', 'count': 'Number of Species'},
        color_discrete_sequence=[COLORS['primary']]
    )

    fig.update_layout(
        showlegend=False,
        height=400
    )

    return fig

def create_venom_type_pie(df, title="Venom Types"):
    """Create a pie chart showing distribution of venom types"""
    venomous = df[df['venomous'] == 'Yes']
    venom_counts = venomous['venom_type'].value_counts()

    fig = px.pie(
        values=venom_counts.values,
        names=venom_counts.index,
        title=title,
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    fig.update_layout(height=400)

    return fig

def create_conservation_status_bar(df, title="Conservation Status"):
    """Create a bar chart of conservation status"""
    status_counts = df['conservation_status'].value_counts()

    fig = px.bar(
        x=status_counts.index,
        y=status_counts.values,
        title=title,
        labels={'x': 'Conservation Status', 'y': 'Number of Species'},
        color=status_counts.values,
        color_continuous_scale='RdYlGn_r'
    )

    fig.update_layout(
        showlegend=False,
        height=400
    )

    return fig

def create_top_species_bar(df, metric, n=10, title="Top Species"):
    """Create a bar chart of top N species by a given metric"""
    top_species = df.nlargest(n, metric)[['common_name', metric]]

    fig = px.bar(
        top_species,
        x=metric,
        y='common_name',
        orientation='h',
        title=title,
        labels={'common_name': 'Species', metric: metric.replace('_', ' ').title()},
        color=metric,
        color_continuous_scale='Viridis'
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        height=400
    )

    return fig

def create_scatter_size_vs_lethality(df, title="Size vs Lethality"):
    """Create a scatter plot of size vs lethality"""
    venomous = df[df['venomous'] == 'Yes']

    fig = px.scatter(
        venomous,
        x='avg_length_cm',
        y='lethality_score',
        size='max_length_cm',
        color='venom_type',
        hover_data=['common_name'],
        title=title,
        labels={
            'avg_length_cm': 'Average Length (cm)',
            'lethality_score': 'Lethality Score',
            'venom_type': 'Venom Type'
        }
    )

    fig.update_layout(height=500)

    return fig

def create_invasive_species_indicator(df):
    """Create indicator cards for invasive species"""
    invasive = df[df['invasive'] == 'Yes']
    return {
        'count': len(invasive),
        'species_list': invasive['common_name'].tolist()
    }

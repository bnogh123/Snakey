"""
Global Snake View Page
Displays snake species data across different continents
"""

from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from src.utils.data_loader import load_global_snakes, get_snakes_by_continent
from src.utils.visualizations import create_top_species_bar
import pandas as pd

# Load data
df = load_global_snakes()

# Calculate continental statistics
continent_stats = df.groupby('continent').agg({
    'species_name': 'count',
    'lethality_score': 'mean',
    'avg_length_cm': 'mean'
}).reset_index()
continent_stats.columns = ['continent', 'species_count', 'avg_lethality', 'avg_length']

# Create continental comparison bar chart
continent_comparison = px.bar(
    continent_stats,
    x='continent',
    y='species_count',
    title="Snake Species Count by Continent",
    labels={'continent': 'Continent', 'species_count': 'Number of Species'},
    color='avg_lethality',
    color_continuous_scale='Reds',
    hover_data=['avg_lethality', 'avg_length']
)
continent_comparison.update_layout(height=400)

# Create lethality comparison
lethality_comparison = px.bar(
    continent_stats,
    x='continent',
    y='avg_lethality',
    title="Average Lethality Score by Continent",
    labels={'continent': 'Continent', 'avg_lethality': 'Average Lethality Score'},
    color='avg_lethality',
    color_continuous_scale='YlOrRd'
)
lethality_comparison.update_layout(height=400)

# World's most lethal snakes
top_lethal_global = create_top_species_bar(
    df[df['venomous'] == 'Yes'],
    'lethality_score',
    n=15,
    title="World's 15 Most Lethal Snakes"
)

# World's largest snakes
top_largest = create_top_species_bar(
    df,
    'max_length_cm',
    n=10,
    title="World's 10 Largest Snakes"
)

# Conservation concerns by continent
conservation_by_continent = df.groupby(['continent', 'conservation_status']).size().reset_index(name='count')
conservation_fig = px.bar(
    conservation_by_continent,
    x='continent',
    y='count',
    color='conservation_status',
    title="Conservation Status by Continent",
    labels={'continent': 'Continent', 'count': 'Number of Species'},
    barmode='stack'
)
conservation_fig.update_layout(height=400)

# Venom types by continent
venom_by_continent = df[df['venomous'] == 'Yes'].groupby(['continent', 'venom_type']).size().reset_index(name='count')
venom_fig = px.bar(
    venom_by_continent,
    x='continent',
    y='count',
    color='venom_type',
    title="Venom Types by Continent",
    labels={'continent': 'Continent', 'count': 'Number of Species'},
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Set2
)
venom_fig.update_layout(height=400)

# Layout
layout = dbc.Container([
    html.H1("Global Snake Overview", className="mt-4 mb-4 text-center"),

    # Introduction
    dbc.Row([
        dbc.Col([
            dbc.Alert([
                html.H5("Exploring Snakes Around the World", className="alert-heading"),
                html.P(
                    "This page provides insights into snake species across different continents, "
                    "comparing their characteristics, lethality, and conservation status."
                )
            ], color="info")
        ])
    ], className="mb-4"),

    # Continental statistics cards
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{len(df)}", className="card-title text-center"),
                    html.P("Global Species", className="card-text text-center text-muted")
                ])
            ], color="primary", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{len(df[df['venomous'] == 'Yes'])}", className="card-title text-center text-danger"),
                    html.P("Venomous Species", className="card-text text-center text-muted")
                ])
            ], color="danger", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{df['avg_length_cm'].mean():.0f} cm", className="card-title text-center"),
                    html.P("Average Length", className="card-text text-center text-muted")
                ])
            ], color="success", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{len(df['continent'].unique())}", className="card-title text-center"),
                    html.P("Continents Covered", className="card-text text-center text-muted")
                ])
            ], color="info", outline=True)
        ], width=3),
    ], className="mb-4"),

    # Continental comparisons
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=continent_comparison)
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=lethality_comparison)
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    # Most lethal and largest snakes
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=top_lethal_global)
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=top_largest)
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    # Venom types and conservation by continent
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=venom_fig)
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=conservation_fig)
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    # Continental breakdown section
    html.H2("Continental Breakdown", className="mt-5 mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Accordion([
                dbc.AccordionItem([
                    html.P(f"Species count: {len(get_snakes_by_continent('Africa'))}"),
                    html.P(f"Most lethal: {get_snakes_by_continent('Africa').nlargest(1, 'lethality_score')['common_name'].values[0] if len(get_snakes_by_continent('Africa')) > 0 else 'N/A'}"),
                    html.P(f"Largest: {get_snakes_by_continent('Africa').nlargest(1, 'max_length_cm')['common_name'].values[0] if len(get_snakes_by_continent('Africa')) > 0 else 'N/A'}")
                ], title="Africa"),

                dbc.AccordionItem([
                    html.P(f"Species count: {len(get_snakes_by_continent('Asia'))}"),
                    html.P(f"Most lethal: {get_snakes_by_continent('Asia').nlargest(1, 'lethality_score')['common_name'].values[0] if len(get_snakes_by_continent('Asia')) > 0 else 'N/A'}"),
                    html.P(f"Largest: {get_snakes_by_continent('Asia').nlargest(1, 'max_length_cm')['common_name'].values[0] if len(get_snakes_by_continent('Asia')) > 0 else 'N/A'}")
                ], title="Asia"),

                dbc.AccordionItem([
                    html.P(f"Species count: {len(get_snakes_by_continent('Australia'))}"),
                    html.P(f"Most lethal: {get_snakes_by_continent('Australia').nlargest(1, 'lethality_score')['common_name'].values[0] if len(get_snakes_by_continent('Australia')) > 0 else 'N/A'}"),
                    html.P(f"Largest: {get_snakes_by_continent('Australia').nlargest(1, 'max_length_cm')['common_name'].values[0] if len(get_snakes_by_continent('Australia')) > 0 else 'N/A'}")
                ], title="Australia"),

                dbc.AccordionItem([
                    html.P(f"Species count: {len(get_snakes_by_continent('Europe'))}"),
                    html.P(f"Most lethal: {get_snakes_by_continent('Europe').nlargest(1, 'lethality_score')['common_name'].values[0] if len(get_snakes_by_continent('Europe')) > 0 else 'N/A'}"),
                    html.P(f"Largest: {get_snakes_by_continent('Europe').nlargest(1, 'max_length_cm')['common_name'].values[0] if len(get_snakes_by_continent('Europe')) > 0 else 'N/A'}")
                ], title="Europe"),

                dbc.AccordionItem([
                    html.P(f"Species count: {len(get_snakes_by_continent('South America'))}"),
                    html.P(f"Most lethal: {get_snakes_by_continent('South America').nlargest(1, 'lethality_score')['common_name'].values[0] if len(get_snakes_by_continent('South America')) > 0 else 'N/A'}"),
                    html.P(f"Largest: {get_snakes_by_continent('South America').nlargest(1, 'max_length_cm')['common_name'].values[0] if len(get_snakes_by_continent('South America')) > 0 else 'N/A'}")
                ], title="South America"),
            ], start_collapsed=True)
        ])
    ], className="mb-4"),

], fluid=True)

"""
US Snake Overview Page
Displays heatmaps and visualizations for snake species across the United States
"""

from dash import html, dcc
import dash_bootstrap_components as dbc
from src.utils.data_loader import load_us_snakes, get_lethality_stats, get_size_stats
from src.utils.visualizations import (
    create_lethality_heatmap,
    create_size_distribution,
    create_venom_type_pie,
    create_conservation_status_bar,
    create_top_species_bar,
    create_scatter_size_vs_lethality,
    create_invasive_species_indicator
)

# Load data
df = load_us_snakes()
lethality_stats = get_lethality_stats(df)
size_stats = get_size_stats(df)
invasive_info = create_invasive_species_indicator(df)

# Create visualizations
lethality_map = create_lethality_heatmap(df, "Average Snake Lethality by US State")
size_dist = create_size_distribution(df, "Distribution of Snake Sizes in the US")
venom_pie = create_venom_type_pie(df, "Venom Types of US Snakes")
conservation_bar = create_conservation_status_bar(df, "Conservation Status of US Snakes")
top_lethal = create_top_species_bar(
    df[df['venomous'] == 'Yes'],
    'lethality_score',
    n=10,
    title="Top 10 Most Lethal US Snakes"
)
size_vs_lethality = create_scatter_size_vs_lethality(df, "Snake Size vs Lethality in the US")

# Calculate statistics
total_species = len(df)
venomous_count = len(df[df['venomous'] == 'Yes'])
non_venomous_count = total_species - venomous_count

# Layout
layout = dbc.Container([
    html.H1("United States Snake Overview", className="mt-4 mb-4 text-center"),

    # Summary statistics row
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{total_species}", className="card-title text-center"),
                    html.P("Total Species", className="card-text text-center text-muted")
                ])
            ], color="primary", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{venomous_count}", className="card-title text-center text-danger"),
                    html.P("Venomous Species", className="card-text text-center text-muted")
                ])
            ], color="danger", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{invasive_info['count']}", className="card-title text-center text-warning"),
                    html.P("Invasive Species", className="card-text text-center text-muted")
                ])
            ], color="warning", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{size_stats['largest_species']}", className="card-title text-center"),
                    html.P("Largest Species", className="card-text text-center text-muted",
                          style={'fontSize': '0.9rem'})
                ])
            ], color="info", outline=True)
        ], width=3),
    ], className="mb-4"),

    # Lethality heatmap
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Lethality Heatmap", className="card-title"),
                    html.P(
                        "This map shows the average lethality score of venomous snakes by state. "
                        "Darker red indicates higher average lethality.",
                        className="card-text text-muted"
                    ),
                    dcc.Graph(figure=lethality_map) if lethality_map else html.P("Map unavailable")
                ])
            ])
        ])
    ], className="mb-4"),

    # Two column row for venom types and conservation
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=venom_pie)
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=conservation_bar)
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    # Size distribution and top lethal species
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=size_dist)
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=top_lethal)
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    # Size vs Lethality scatter
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Size vs Lethality Analysis", className="card-title"),
                    html.P(
                        "Explore the relationship between snake size and venom lethality. "
                        "Bubble size represents maximum recorded length.",
                        className="card-text text-muted"
                    ),
                    dcc.Graph(figure=size_vs_lethality)
                ])
            ])
        ])
    ], className="mb-4"),

    # Invasive species alert
    dbc.Row([
        dbc.Col([
            dbc.Alert([
                html.H5("Invasive Species Alert", className="alert-heading"),
                html.P(f"There are {invasive_info['count']} invasive snake species in the United States:"),
                html.Ul([html.Li(species) for species in invasive_info['species_list']]),
                html.Hr(),
                html.P(
                    "These species, primarily found in Florida, pose threats to native ecosystems and wildlife.",
                    className="mb-0"
                )
            ], color="warning")
        ])
    ], className="mb-4"),

], fluid=True)

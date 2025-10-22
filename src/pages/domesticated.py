"""
Domesticated Snakes Page
Explores snake species commonly kept as pets and their domestication history
"""

from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from src.utils.data_loader import load_domesticated_snakes
import pandas as pd

# Load data
df = load_domesticated_snakes()

# Create visualizations
popularity_chart = px.bar(
    df.sort_values('popularity_score', ascending=False).head(10),
    x='common_name',
    y='popularity_score',
    title="Top 10 Most Popular Pet Snakes",
    labels={'common_name': 'Species', 'popularity_score': 'Popularity Score'},
    color='popularity_score',
    color_continuous_scale='Viridis'
)
popularity_chart.update_layout(height=400, xaxis_tickangle=-45)

# Cost comparison
cost_comparison = px.scatter(
    df,
    x='avg_cost_usd',
    y='popularity_score',
    size='avg_lifespan_years',
    color='care_difficulty',
    hover_data=['common_name'],
    title="Cost vs Popularity (Size = Lifespan)",
    labels={
        'avg_cost_usd': 'Average Cost (USD)',
        'popularity_score': 'Popularity Score',
        'care_difficulty': 'Care Difficulty'
    },
    color_discrete_map={
        'Beginner': '#27AE60',
        'Intermediate': '#F39C12',
        'Advanced': '#E74C3C'
    }
)
cost_comparison.update_layout(height=500)

# Domestication level pie chart
domestication_pie = px.pie(
    df,
    names='domestication_level',
    title="Domestication Levels",
    color_discrete_sequence=px.colors.qualitative.Set3
)
domestication_pie.update_layout(height=400)

# Care difficulty distribution
care_diff_bar = px.histogram(
    df,
    x='care_difficulty',
    title="Distribution by Care Difficulty",
    labels={'care_difficulty': 'Care Difficulty', 'count': 'Number of Species'},
    color_discrete_sequence=['#3498DB'],
    category_orders={'care_difficulty': ['Beginner', 'Intermediate', 'Advanced']}
)
care_diff_bar.update_layout(height=400)

# Temperament analysis
temperament_data = df['temperament'].value_counts().reset_index()
temperament_data.columns = ['temperament', 'count']
temperament_bar = px.bar(
    temperament_data,
    x='temperament',
    y='count',
    title="Temperament Distribution",
    labels={'temperament': 'Temperament', 'count': 'Number of Species'},
    color='count',
    color_continuous_scale='Blues'
)
temperament_bar.update_layout(height=400, xaxis_tickangle=-45)

# Timeline of domestication
timeline_data = df.groupby('first_domesticated_era').size().reset_index(name='count')
timeline_data = timeline_data.sort_values('first_domesticated_era')
timeline_chart = px.bar(
    timeline_data,
    x='first_domesticated_era',
    y='count',
    title="Snake Domestication Timeline",
    labels={'first_domesticated_era': 'Era', 'count': 'Species Domesticated'},
    color='count',
    color_continuous_scale='Greens'
)
timeline_chart.update_layout(height=400)

# Layout
layout = dbc.Container([
    html.H1("Domesticated Snakes", className="mt-4 mb-4 text-center"),

    # Introduction
    dbc.Row([
        dbc.Col([
            dbc.Alert([
                html.H5("Understanding Pet Snakes", className="alert-heading"),
                html.P(
                    "This page explores snake species commonly kept as pets, their domestication history, "
                    "care requirements, and what makes them suitable companions. Learn about the journey "
                    "from wild species to beloved pets."
                )
            ], color="info")
        ])
    ], className="mb-4"),

    # Summary statistics
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{len(df)}", className="card-title text-center"),
                    html.P("Species Profiled", className="card-text text-center text-muted")
                ])
            ], color="primary", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{len(df[df['care_difficulty'] == 'Beginner'])}", className="card-title text-center text-success"),
                    html.P("Beginner-Friendly", className="card-text text-center text-muted")
                ])
            ], color="success", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"${df['avg_cost_usd'].mean():.0f}", className="card-title text-center"),
                    html.P("Average Cost", className="card-text text-center text-muted")
                ])
            ], color="warning", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{df['avg_lifespan_years'].mean():.0f} yrs", className="card-title text-center"),
                    html.P("Average Lifespan", className="card-text text-center text-muted")
                ])
            ], color="info", outline=True)
        ], width=3),
    ], className="mb-4"),

    # Popularity and cost analysis
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=popularity_chart)
                ])
            ])
        ], width=12),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Cost vs Popularity Analysis", className="card-title"),
                    html.P(
                        "This scatter plot shows the relationship between cost and popularity. "
                        "Bubble size represents lifespan. Colors indicate care difficulty level.",
                        className="card-text text-muted"
                    ),
                    dcc.Graph(figure=cost_comparison)
                ])
            ])
        ], width=12),
    ], className="mb-4"),

    # Domestication and care
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=domestication_pie)
                ])
            ])
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=care_diff_bar)
                ])
            ])
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=temperament_bar)
                ])
            ])
        ], width=4),
    ], className="mb-4"),

    # Domestication timeline
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Domestication Timeline", className="card-title"),
                    html.P(
                        "The reptile pet trade began expanding significantly in the 1970s-1980s as "
                        "captive breeding techniques improved and regulations around wildlife trade evolved.",
                        className="card-text text-muted"
                    ),
                    dcc.Graph(figure=timeline_chart)
                ])
            ])
        ])
    ], className="mb-4"),

    # Detailed species information
    html.H2("Detailed Species Information", className="mt-5 mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dash_table.DataTable(
                        data=df[['common_name', 'origin', 'care_difficulty', 'avg_cost_usd',
                                'avg_lifespan_years', 'temperament', 'domestication_level']].to_dict('records'),
                        columns=[
                            {'name': 'Species', 'id': 'common_name'},
                            {'name': 'Origin', 'id': 'origin'},
                            {'name': 'Care Level', 'id': 'care_difficulty'},
                            {'name': 'Cost (USD)', 'id': 'avg_cost_usd'},
                            {'name': 'Lifespan (years)', 'id': 'avg_lifespan_years'},
                            {'name': 'Temperament', 'id': 'temperament'},
                            {'name': 'Domestication', 'id': 'domestication_level'},
                        ],
                        style_cell={
                            'textAlign': 'left',
                            'padding': '10px',
                            'font-family': 'sans-serif'
                        },
                        style_header={
                            'backgroundColor': '#2C3E50',
                            'color': 'white',
                            'fontWeight': 'bold'
                        },
                        style_data_conditional=[
                            {
                                'if': {'column_id': 'care_difficulty', 'filter_query': '{care_difficulty} = "Beginner"'},
                                'backgroundColor': '#D5F4E6',
                            },
                            {
                                'if': {'column_id': 'care_difficulty', 'filter_query': '{care_difficulty} = "Intermediate"'},
                                'backgroundColor': '#FCF3CF',
                            },
                            {
                                'if': {'column_id': 'care_difficulty', 'filter_query': '{care_difficulty} = "Advanced"'},
                                'backgroundColor': '#FADBD8',
                            },
                        ],
                        page_size=20,
                        sort_action='native',
                        filter_action='native',
                    )
                ])
            ])
        ])
    ], className="mb-4"),

    # Why these snakes were domesticated
    html.H2("Reasons for Domestication", className="mt-5 mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Ball Python", className="card-title"),
                    html.P(df[df['common_name'] == 'Ball Python']['reasons_for_domestication'].values[0])
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Corn Snake", className="card-title"),
                    html.P(df[df['common_name'] == 'Corn Snake']['reasons_for_domestication'].values[0])
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Western Hognose Snake", className="card-title"),
                    html.P(df[df['common_name'] == 'Western Hognose Snake']['reasons_for_domestication'].values[0])
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Boa Constrictor", className="card-title"),
                    html.P(df[df['common_name'] == 'Boa Constrictor']['reasons_for_domestication'].values[0])
                ])
            ])
        ], width=6),
    ], className="mb-4"),

], fluid=True)

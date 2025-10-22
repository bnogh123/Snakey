"""
Snakes in Media Page
Explores the representation of snakes in movies, TV, literature, and culture
"""

from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from src.utils.data_loader import load_media_snakes
import pandas as pd

# Load data
df = load_media_snakes()

# Filter out rows where protagonist_antagonist is N/A for certain analyses
df_roles = df[df['protagonist_antagonist'].notna()]

# Create visualizations
# Protagonist vs Antagonist distribution
role_counts = df_roles['protagonist_antagonist'].value_counts()
role_pie = px.pie(
    values=role_counts.values,
    names=role_counts.index,
    title="Snakes as Protagonists vs Antagonists",
    color_discrete_map={'Antagonist': '#E74C3C', 'Protagonist': '#27AE60', 'Neutral': '#95A5A6'}
)
role_pie.update_layout(height=400)

# Media type distribution
media_type_bar = px.histogram(
    df,
    x='media_type',
    title="Snake Appearances by Media Type",
    labels={'media_type': 'Media Type', 'count': 'Number of Appearances'},
    color_discrete_sequence=['#3498DB']
)
media_type_bar.update_layout(height=400)

# Cultural impact over time
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df_with_year = df[df['year'].notna()].copy()
impact_timeline = px.scatter(
    df_with_year,
    x='year',
    y='cultural_impact',
    size='cultural_impact',
    color='protagonist_antagonist',
    hover_data=['title', 'snake_character'],
    title="Cultural Impact of Snake Characters Over Time",
    labels={
        'year': 'Year',
        'cultural_impact': 'Cultural Impact',
        'protagonist_antagonist': 'Role'
    },
    color_discrete_map={
        'Antagonist': '#E74C3C',
        'Protagonist': '#27AE60',
        'Neutral': '#95A5A6',
        'N/A': '#BDC3C7'
    }
)
impact_timeline.update_layout(height=500)

# Accuracy rating analysis
df_with_accuracy = df[df['accuracy_rating'] != 'N/A'].copy()
df_with_accuracy['accuracy_rating'] = pd.to_numeric(df_with_accuracy['accuracy_rating'])
accuracy_hist = px.histogram(
    df_with_accuracy,
    x='accuracy_rating',
    nbins=10,
    title="Accuracy of Snake Portrayals (0-10 scale)",
    labels={'accuracy_rating': 'Accuracy Rating', 'count': 'Number of Portrayals'},
    color_discrete_sequence=['#9B59B6']
)
accuracy_hist.update_layout(height=400)

# Cultural impact categories
df['impact_category'] = df['cultural_impact'].apply(
    lambda x: 'Very High' if 'Very High' in str(x)
    else 'High' if 'High' in str(x)
    else 'Medium' if 'Medium' in str(x)
    else 'Low'
)
impact_bar = px.histogram(
    df,
    x='impact_category',
    title="Distribution of Cultural Impact",
    labels={'impact_category': 'Impact Level', 'count': 'Number of Appearances'},
    color_discrete_sequence=['#E67E22'],
    category_orders={'impact_category': ['Very High', 'High', 'Medium', 'Low']}
)
impact_bar.update_layout(height=400)

# Top influential snake characters
df_ranked = df_with_year.copy()
df_ranked['impact_score'] = df_ranked['cultural_impact'].apply(
    lambda x: 4 if 'Very High' in str(x)
    else 3 if 'High' in str(x)
    else 2 if 'Medium' in str(x)
    else 1
)
top_influential = df_ranked.nlargest(10, 'impact_score')[['title', 'snake_character', 'year', 'protagonist_antagonist']]

# Layout
layout = dbc.Container([
    html.H1("Snakes in Media and Culture", className="mt-4 mb-4 text-center"),

    # Introduction
    dbc.Row([
        dbc.Col([
            dbc.Alert([
                html.H5("Demystifying Snake Representation", className="alert-heading"),
                html.P(
                    "Snakes have played significant roles in human storytelling throughout history - from ancient "
                    "mythology to modern cinema. This page explores how snakes are portrayed in media, whether as "
                    "villains, heroes, or symbols, and how accurate these portrayals are."
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
                    html.P("Media Appearances", className="card-text text-center text-muted")
                ])
            ], color="primary", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{len(df_roles[df_roles['protagonist_antagonist'] == 'Antagonist'])}", className="card-title text-center text-danger"),
                    html.P("As Antagonists", className="card-text text-center text-muted")
                ])
            ], color="danger", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{len(df_roles[df_roles['protagonist_antagonist'] == 'Protagonist'])}", className="card-title text-center text-success"),
                    html.P("As Protagonists", className="card-text text-center text-muted")
                ])
            ], color="success", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{df_with_accuracy['accuracy_rating'].mean():.1f}/10", className="card-title text-center"),
                    html.P("Avg Accuracy", className="card-text text-center text-muted")
                ])
            ], color="warning", outline=True)
        ], width=3),
    ], className="mb-4"),

    # Role distribution and media types
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=role_pie)
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=media_type_bar)
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    # Cultural impact analysis
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Cultural Impact Timeline", className="card-title"),
                    html.P(
                        "This visualization shows how snake characters have appeared across different eras, "
                        "sized by their cultural impact. Ancient mythology entries show the earliest influence.",
                        className="card-text text-muted"
                    ),
                    dcc.Graph(figure=impact_timeline)
                ])
            ])
        ])
    ], className="mb-4"),

    # Impact and accuracy
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=impact_bar)
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=accuracy_hist)
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    # Analysis insights
    html.H2("Key Insights", className="mt-5 mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("The Villain Stereotype", className="card-title text-danger"),
                    html.P(
                        f"Out of {len(df_roles)} portrayals with defined roles, "
                        f"{len(df_roles[df_roles['protagonist_antagonist'] == 'Antagonist'])} "
                        f"({len(df_roles[df_roles['protagonist_antagonist'] == 'Antagonist'])/len(df_roles)*100:.1f}%) "
                        "cast snakes as antagonists. This reinforces negative stereotypes and contributes to "
                        "ophidiophobia (fear of snakes)."
                    )
                ])
            ], className="mb-3")
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Accuracy Concerns", className="card-title text-warning"),
                    html.P(
                        f"The average accuracy rating of {df_with_accuracy['accuracy_rating'].mean():.1f}/10 "
                        "indicates that most media portrayals take significant creative liberties with snake "
                        "behavior, size, and capabilities, often for dramatic effect."
                    )
                ])
            ], className="mb-3")
        ], width=6),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Positive Representation", className="card-title text-success"),
                    html.P(
                        "Notable positive portrayals include Viper from Kung Fu Panda, various video game "
                        "characters like Solid Snake, and Kaa from the original Jungle Book (as an ally). "
                        "These help balance the narrative around snakes."
                    )
                ])
            ], className="mb-3")
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Cultural Significance", className="card-title text-info"),
                    html.P(
                        "Ancient mythologies (Egyptian Apophis, Norse Jörmungandr, Aztec Quetzalcoatl, Biblical "
                        "Serpent) show that snake symbolism has been deeply embedded in human culture for millennia, "
                        "often representing both danger and wisdom."
                    )
                ])
            ], className="mb-3")
        ], width=6),
    ], className="mb-4"),

    # Detailed appearances table
    html.H2("Notable Snake Appearances", className="mt-5 mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dash_table.DataTable(
                        data=df[['title', 'media_type', 'year', 'snake_character', 'role',
                                'protagonist_antagonist', 'cultural_impact', 'accuracy_rating']].to_dict('records'),
                        columns=[
                            {'name': 'Title', 'id': 'title'},
                            {'name': 'Type', 'id': 'media_type'},
                            {'name': 'Year', 'id': 'year'},
                            {'name': 'Character', 'id': 'snake_character'},
                            {'name': 'Role', 'id': 'role'},
                            {'name': 'Alignment', 'id': 'protagonist_antagonist'},
                            {'name': 'Cultural Impact', 'id': 'cultural_impact'},
                            {'name': 'Accuracy', 'id': 'accuracy_rating'},
                        ],
                        style_cell={
                            'textAlign': 'left',
                            'padding': '10px',
                            'font-family': 'sans-serif',
                            'whiteSpace': 'normal',
                            'height': 'auto',
                        },
                        style_header={
                            'backgroundColor': '#2C3E50',
                            'color': 'white',
                            'fontWeight': 'bold'
                        },
                        style_data_conditional=[
                            {
                                'if': {'column_id': 'protagonist_antagonist', 'filter_query': '{protagonist_antagonist} = "Antagonist"'},
                                'backgroundColor': '#FADBD8',
                                'color': '#C0392B'
                            },
                            {
                                'if': {'column_id': 'protagonist_antagonist', 'filter_query': '{protagonist_antagonist} = "Protagonist"'},
                                'backgroundColor': '#D5F4E6',
                                'color': '#27AE60'
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

], fluid=True)

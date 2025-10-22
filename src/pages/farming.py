"""
Snakeskin Farming Ethics Page
Explores snakeskin farming practices and their ethical implications
"""

from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from src.utils.data_loader import load_farming_data
import pandas as pd

# Load data
df = load_farming_data()

# Create visualizations
# Production by country
production_map = px.choropleth(
    df,
    locations='country',
    locationmode='country names',
    color='annual_production_skins',
    hover_name='country',
    hover_data=['primary_species_farmed', 'farming_method', 'ethical_score'],
    title="Annual Snakeskin Production by Country",
    color_continuous_scale='Reds',
    labels={'annual_production_skins': 'Annual Production (skins)'}
)
production_map.update_layout(height=500)

# Ethical scores by country
ethical_bar = px.bar(
    df.sort_values('ethical_score', ascending=True),
    y='country',
    x='ethical_score',
    orientation='h',
    title="Ethical Scores by Country (0-10 scale)",
    labels={'ethical_score': 'Ethical Score', 'country': 'Country'},
    color='ethical_score',
    color_continuous_scale='RdYlGn',
    range_color=[0, 10]
)
ethical_bar.update_layout(height=600)

# Farming methods distribution
method_counts = df['farming_method'].value_counts()
method_pie = px.pie(
    values=method_counts.values,
    names=method_counts.index,
    title="Distribution of Farming Methods",
    color_discrete_sequence=px.colors.qualitative.Set3
)
method_pie.update_layout(height=400)

# Animal welfare vs sustainability
welfare_sustainability = px.scatter(
    df[df['animal_welfare_rating'] != 'N/A (Wild)'],
    x='animal_welfare_rating',
    y='sustainability_rating',
    size='annual_production_skins',
    color='ethical_score',
    hover_data=['country', 'primary_species_farmed'],
    title="Animal Welfare vs Sustainability",
    labels={
        'animal_welfare_rating': 'Animal Welfare Rating',
        'sustainability_rating': 'Sustainability Rating',
        'ethical_score': 'Ethical Score'
    },
    color_continuous_scale='Viridis'
)
welfare_sustainability.update_layout(height=500)

# Regulation levels
regulation_counts = df['regulation_level'].value_counts()
regulation_bar = px.bar(
    x=regulation_counts.index,
    y=regulation_counts.values,
    title="Regulation Levels Across Countries",
    labels={'x': 'Regulation Level', 'y': 'Number of Countries'},
    color=regulation_counts.values,
    color_continuous_scale='Blues'
)
regulation_bar.update_layout(height=400)

# Production vs ethical score
production_ethics = px.scatter(
    df,
    x='annual_production_skins',
    y='ethical_score',
    size='annual_production_skins',
    color='farming_method',
    hover_data=['country', 'primary_species_farmed'],
    title="Production Volume vs Ethical Standards",
    labels={
        'annual_production_skins': 'Annual Production (skins)',
        'ethical_score': 'Ethical Score',
        'farming_method': 'Farming Method'
    },
    log_x=True
)
production_ethics.update_layout(height=500)

# Calculate aggregate statistics
total_production = df['annual_production_skins'].sum()
avg_ethical_score = df['ethical_score'].mean()
countries_with_certification = len(df[df['certification_available'] == 'Yes'])
banned_countries = len(df[df['regulation_level'] == 'Strict Ban'])

# Layout
layout = dbc.Container([
    html.H1("Snakeskin Farming Ethics", className="mt-4 mb-4 text-center"),

    # Introduction
    dbc.Row([
        dbc.Col([
            dbc.Alert([
                html.H5("Understanding the Snakeskin Trade", className="alert-heading"),
                html.P(
                    "The global snakeskin trade involves millions of snakes annually, sourced through both "
                    "farming and wild harvest. This page examines the ethical dimensions of this industry, "
                    "including animal welfare, sustainability, and the economic realities of snake farming "
                    "across different countries and regulatory environments."
                )
            ], color="info")
        ])
    ], className="mb-4"),

    # Summary statistics
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{total_production:,}", className="card-title text-center"),
                    html.P("Total Annual Skins", className="card-text text-center text-muted")
                ])
            ], color="primary", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{avg_ethical_score:.1f}/10", className="card-title text-center text-warning"),
                    html.P("Average Ethical Score", className="card-text text-center text-muted")
                ])
            ], color="warning", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{countries_with_certification}", className="card-title text-center text-success"),
                    html.P("With Certification", className="card-text text-center text-muted")
                ])
            ], color="success", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(f"{banned_countries}", className="card-title text-center"),
                    html.P("Countries Banned", className="card-text text-center text-muted")
                ])
            ], color="danger", outline=True)
        ], width=3),
    ], className="mb-4"),

    # Global production map
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Global Snakeskin Production", className="card-title"),
                    html.P(
                        "This map shows the distribution of snakeskin production globally. "
                        "Darker colors indicate higher production volumes.",
                        className="card-text text-muted"
                    ),
                    dcc.Graph(figure=production_map)
                ])
            ])
        ])
    ], className="mb-4"),

    # Ethical scores and farming methods
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=ethical_bar)
                ])
            ])
        ], width=8),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=method_pie)
                ])
            ])
        ], width=4),
    ], className="mb-4"),

    # Welfare vs sustainability
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Animal Welfare vs Environmental Sustainability", className="card-title"),
                    html.P(
                        "This chart compares animal welfare standards against environmental sustainability. "
                        "Bubble size represents production volume. Note: Wild harvest operations are excluded "
                        "as they don't have welfare ratings.",
                        className="card-text text-muted"
                    ),
                    dcc.Graph(figure=welfare_sustainability)
                ])
            ])
        ])
    ], className="mb-4"),

    # Regulation and production ethics
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=regulation_bar)
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Production vs Ethics", className="card-title"),
                    html.P(
                        "Examining whether high production correlates with lower ethical standards.",
                        className="card-text text-muted", style={'fontSize': '0.9rem'}
                    ),
                    dcc.Graph(figure=production_ethics)
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    # Key findings
    html.H2("Key Findings", className="mt-5 mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Wild Harvest Concerns", className="card-title text-danger"),
                    html.P(
                        "Countries relying on wild harvest (particularly in Southeast Asia) often have weak "
                        "regulation and lower ethical scores. This threatens wild python populations and "
                        "raises animal welfare concerns during capture and transport."
                    )
                ], className="h-100")
            ], className="mb-3")
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Intensive Farming Issues", className="card-title text-warning"),
                    html.P(
                        "Countries with intensive farming operations (China, Vietnam) produce high volumes but "
                        "frequently have poor animal welfare standards, including cramped enclosures, lack of "
                        "veterinary care, and inhumane slaughter methods."
                    )
                ], className="h-100")
            ], className="mb-3")
        ], width=6),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Successful Regulation Examples", className="card-title text-success"),
                    html.P(
                        "Australia demonstrates that strong regulation can enable sustainable wild harvest. "
                        "Their strict quotas, full traceability, and enforcement result in the highest ethical "
                        "scores while maintaining ecological balance."
                    )
                ], className="h-100")
            ], className="mb-3")
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Economic vs Ethical Balance", className="card-title text-info"),
                    html.P(
                        "Countries where snakeskin farming provides significant economic value (Indonesia, "
                        "Thailand, Colombia) are beginning to adopt better practices and certification programs, "
                        "showing that economic importance can drive improvement."
                    )
                ], className="h-100")
            ], className="mb-3")
        ], width=6),
    ], className="mb-4"),

    # Common issues and best practices
    html.H2("Issues and Best Practices", className="mt-5 mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("Common Issues", className="mb-0")),
                dbc.CardBody([
                    html.Ul([
                        html.Li(issue) for issue in df['common_issues'].dropna().unique()[:10]
                    ])
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("Best Practices", className="mb-0")),
                dbc.CardBody([
                    html.Ul([
                        html.Li(practice) for practice in df['best_practices'].dropna().unique()[:10]
                    ])
                ])
            ])
        ], width=6),
    ], className="mb-4"),

    # Detailed country data
    html.H2("Detailed Country Data", className="mt-5 mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dash_table.DataTable(
                        data=df[['country', 'primary_species_farmed', 'farming_method',
                                'annual_production_skins', 'ethical_score', 'animal_welfare_rating',
                                'sustainability_rating', 'regulation_level', 'conservation_impact']].to_dict('records'),
                        columns=[
                            {'name': 'Country', 'id': 'country'},
                            {'name': 'Primary Species', 'id': 'primary_species_farmed'},
                            {'name': 'Method', 'id': 'farming_method'},
                            {'name': 'Annual Production', 'id': 'annual_production_skins'},
                            {'name': 'Ethical Score', 'id': 'ethical_score'},
                            {'name': 'Welfare', 'id': 'animal_welfare_rating'},
                            {'name': 'Sustainability', 'id': 'sustainability_rating'},
                            {'name': 'Regulation', 'id': 'regulation_level'},
                            {'name': 'Conservation Impact', 'id': 'conservation_impact'},
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
                                'if': {
                                    'filter_query': '{ethical_score} < 4',
                                    'column_id': 'ethical_score'
                                },
                                'backgroundColor': '#FADBD8',
                                'color': '#C0392B'
                            },
                            {
                                'if': {
                                    'filter_query': '{ethical_score} >= 7',
                                    'column_id': 'ethical_score'
                                },
                                'backgroundColor': '#D5F4E6',
                                'color': '#27AE60'
                            },
                            {
                                'if': {
                                    'filter_query': '{conservation_impact} contains "Negative"',
                                    'column_id': 'conservation_impact'
                                },
                                'backgroundColor': '#FCF3CF'
                            },
                            {
                                'if': {
                                    'filter_query': '{conservation_impact} contains "Positive"',
                                    'column_id': 'conservation_impact'
                                },
                                'backgroundColor': '#D5F4E6'
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

    # Recommendations
    dbc.Row([
        dbc.Col([
            dbc.Alert([
                html.H5("Consumer Recommendations", className="alert-heading"),
                html.P("If purchasing snakeskin products:"),
                html.Ul([
                    html.Li("Look for certification from recognized wildlife trade organizations (CITES compliance)"),
                    html.Li("Prefer products from countries with strong regulation (Australia, certified operations in Malaysia/Thailand)"),
                    html.Li("Avoid products from countries with poor ethical scores or weak regulation"),
                    html.Li("Consider alternatives: many fashion brands now offer high-quality synthetic snake patterns"),
                    html.Li("Research the brand's supply chain transparency and animal welfare policies")
                ]),
            ], color="success")
        ])
    ], className="mb-4"),

], fluid=True)

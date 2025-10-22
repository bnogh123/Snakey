# Snakey - Interactive Snake Dashboard

A comprehensive, interactive web dashboard exploring snakes across the world with data visualizations on lethality, venom, size, endangerment, invasiveness, domestication, media representation, and snakeskin farming ethics.

## Features

### US Overview Page
- **Lethality Heatmap**: Interactive map showing average snake lethality by state
- **Species Distribution**: Visualizations of venomous vs. non-venomous species
- **Size Analysis**: Distribution of snake sizes across the United States
- **Invasive Species Alerts**: Tracking of invasive python and boa species in Florida
- **Conservation Status**: Breakdown of threatened and endangered species

### Global View Page
- **Continental Comparisons**: Compare snake characteristics across different continents
- **World's Most Lethal**: Ranking of the deadliest snakes globally
- **Largest Species**: Analysis of the world's biggest snake species
- **Venom Type Distribution**: Geographic distribution of different venom types
- **Conservation by Region**: Global conservation status overview

### Domesticated Snakes Page
- **Pet Snake Popularity**: Rankings of most popular pet snake species
- **Care Requirements**: Difficulty levels, costs, and lifespan information
- **Domestication History**: Timeline of when species became pets
- **Temperament Analysis**: Understanding snake behavior in captivity
- **Breeding Information**: Color morphs and breeding availability

### Snakes in Media Page
- **Protagonist vs Antagonist**: Analysis of snake portrayal in media
- **Cultural Impact**: Timeline of influential snake characters
- **Accuracy Ratings**: How realistic are movie/TV snake portrayals?
- **Mythology & Symbolism**: Ancient and modern cultural significance
- **Media Type Distribution**: Snakes across films, TV, books, and mythology

### Snakeskin Farming Ethics Page
- **Global Production Map**: Where snakeskin comes from worldwide
- **Ethical Scoring**: Country-by-country ethical practices analysis
- **Animal Welfare**: Comparison of farming methods and welfare standards
- **Sustainability Metrics**: Environmental impact of different practices
- **Consumer Guidance**: Recommendations for ethical purchasing

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Snakey.git
   cd Snakey
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Dashboard

```bash
python app.py
```

Then open your browser to `http://localhost:8050`

## Project Structure

```
Snakey/
├── data/
│   ├── raw/          # Original data sources
│   └── processed/    # Cleaned and processed datasets
├── src/
│   ├── pages/        # Dashboard page components
│   ├── components/   # Reusable UI components
│   └── utils/        # Helper functions and data processing
├── assets/
│   ├── images/       # Images and icons
│   └── styles/       # CSS stylesheets
├── docs/             # Documentation
├── app.py            # Main application entry point
└── requirements.txt  # Python dependencies
```

## Data Sources

Data compiled from:
- Global Reptile Database
- IUCN Red List
- Scientific literature and research papers
- Media databases
- Conservation organizations

## Deployment

This dashboard can be deployed to various platforms. See `docs/deployment.md` for detailed instructions.

### Quick Deploy Options:

#### Render (Recommended)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

1. Push your code to GitHub
2. Sign up at [render.com](https://render.com)
3. Create a new Web Service from your repository
4. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:server`

#### Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

1. Push to GitHub
2. Visit [railway.app](https://railway.app)
3. Click "Deploy from GitHub repo"

#### Docker
```bash
docker build -t snakey-dashboard .
docker run -p 8050:8050 snakey-dashboard
```

### GitHub Pages Integration

After deploying to Render/Railway, embed in your GitHub Pages site:

1. Copy `docs/github-pages-embed.html` to your GitHub Pages repository
2. Update the iframe URL with your deployed app URL
3. Commit and push to GitHub Pages

See `docs/deployment.md` for complete instructions.

## Technology Stack

- **Framework**: Dash (Plotly)
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly, Plotly Express
- **UI Components**: Dash Bootstrap Components
- **Deployment**: Gunicorn, Docker

## Contributing

Contributions are welcome! Areas for improvement:

- Additional snake species data
- More media appearances
- Updated farming practices information
- New visualizations
- Performance optimizations

To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Data Accuracy

This dashboard compiles data from various sources for educational and informational purposes. While effort has been made to ensure accuracy:

- Lethality scores are approximate and based on scientific literature
- Conservation statuses may change over time
- Media portrayals are subjective interpretations
- Farming practices vary and may change

Always consult professional sources for critical decisions.

## Acknowledgments

- Data compiled from Global Reptile Database, IUCN Red List, and various scientific publications
- Built with Dash by Plotly
- Inspired by the need to demystify and educate about snake species worldwide

## License

MIT License - See LICENSE file for details

## Contact

For questions, suggestions, or issues, please open an issue on GitHub.

---

**Note**: This dashboard is for educational purposes. If you encounter a snake in the wild, maintain a safe distance and contact local wildlife authorities if needed.

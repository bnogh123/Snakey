# Snakey Dashboard - Quick Start Guide

Get the Snakey Dashboard running in 5 minutes!

## Prerequisites

- Python 3.9 or higher
- Git
- 50MB of free disk space

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Snakey.git
cd Snakey
```

### 2. Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Dash (web framework)
- Plotly (visualizations)
- Pandas (data processing)
- And other required packages

### 4. Run the Dashboard

```bash
python app.py
```

You should see output like:
```
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'app'
 * Debug mode: on
```

### 5. Open in Browser

Navigate to: `http://localhost:8050`

You should now see the Snakey Dashboard!

## Exploring the Dashboard

### Available Pages

1. **US Overview** (`/`) - Default homepage
   - Interactive US state heatmap
   - Lethality and size distributions
   - Invasive species information

2. **Global View** (`/global`)
   - Continental comparisons
   - World's most lethal snakes
   - Global conservation status

3. **Domesticated Snakes** (`/domesticated`)
   - Pet snake rankings
   - Care requirements
   - Domestication history

4. **Snakes in Media** (`/media`)
   - Protagonist vs antagonist analysis
   - Cultural impact timeline
   - Accuracy ratings

5. **Farming Ethics** (`/farming`)
   - Global snakeskin production
   - Ethical scoring by country
   - Animal welfare comparisons

## Troubleshooting

### Port Already in Use

If port 8050 is in use, modify `app.py`:

```python
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8051)  # Change port
```

### Module Not Found Error

Make sure you've activated the virtual environment:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Then reinstall dependencies:
```bash
pip install -r requirements.txt
```

### CSV File Errors

Ensure all CSV files in `data/raw/` are present:
- `us_snake_species.csv`
- `global_snake_species.csv`
- `domesticated_snakes.csv`
- `snakes_in_media.csv`
- `snakeskin_farming.csv`

### Visualization Not Loading

1. Check browser console for errors (F12)
2. Verify CSV files have correct headers
3. Try refreshing the page
4. Clear browser cache

## Next Steps

### Customize the Dashboard

1. **Add More Data**: Edit CSV files in `data/raw/`
2. **Modify Visualizations**: Check `src/utils/visualizations.py`
3. **Change Colors**: Update `config.py`
4. **Add New Pages**: Create files in `src/pages/`

### Deploy to Production

See `docs/deployment.md` for deployment options:
- Render (free tier)
- Railway (free tier)
- Docker
- Heroku

### Learn More

- [Dash Documentation](https://dash.plotly.com/)
- [Plotly Graphing Library](https://plotly.com/python/)
- [Pandas User Guide](https://pandas.pydata.org/docs/)

## Common Tasks

### Update Data

1. Edit CSV files in `data/raw/`
2. Save changes
3. Refresh browser (changes auto-load in debug mode)

### Add a New Visualization

1. Create function in `src/utils/visualizations.py`
2. Import in relevant page file
3. Add to page layout

### Change Dashboard Theme

Edit in `app.py`:
```python
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],  # Try different themes
    ...
)
```

Available themes: BOOTSTRAP, CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, MORPH, PULSE, QUARTZ, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR

## Getting Help

- Check the [README.md](../README.md)
- Review [CONTRIBUTING.md](../CONTRIBUTING.md)
- Open an issue on GitHub
- Check existing issues for solutions

## Development Mode Features

When running in debug mode (`debug=True`):
- Auto-reload on code changes
- Detailed error messages
- Dev tools available

**Note**: Disable debug mode for production!

---

Happy exploring! If you encounter issues, please open an issue on GitHub.

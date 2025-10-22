# Deployment Guide

This guide covers multiple ways to deploy the Snakey dashboard.

## Option 1: Deploy to Render (Recommended - Free Tier Available)

Render offers free hosting for web services, perfect for Dash applications.

### Steps:

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and sign up
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Configure the service:
   - **Name**: snakey-dashboard
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:server`
6. Click "Create Web Service"

Your dashboard will be available at `https://snakey-dashboard.onrender.com`

### Embedding in GitHub Pages:

After deploying to Render, you can embed the dashboard in your GitHub Pages site using an iframe:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Snakey Dashboard</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }
        iframe {
            width: 100%;
            height: 100vh;
            border: none;
        }
    </style>
</head>
<body>
    <iframe src="https://your-app.onrender.com"></iframe>
</body>
</html>
```

## Option 2: Deploy to Railway

Railway also offers free tier hosting.

### Steps:

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "Start a New Project"
4. Select "Deploy from GitHub repo"
5. Select your Snakey repository
6. Railway will auto-detect Python and deploy

## Option 3: Docker Deployment

Use the included Dockerfile to deploy anywhere that supports containers.

```bash
docker build -t snakey-dashboard .
docker run -p 8050:8050 snakey-dashboard
```

## Option 4: Heroku Deployment

1. Install Heroku CLI
2. Create a Heroku app:
   ```bash
   heroku create snakey-dashboard
   git push heroku main
   ```

## Option 5: Local Deployment

For development and testing:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Access at `http://localhost:8050`

## GitHub Pages Integration

Since GitHub Pages only supports static sites, you have two options:

### Option A: Iframe Embed (Recommended)
Deploy the Dash app to Render/Railway/Heroku, then embed in GitHub Pages:

```html
<iframe src="https://your-deployed-app.onrender.com"
        width="100%"
        height="800px"
        frameborder="0">
</iframe>
```

### Option B: Link to Deployed App
Add a link in your GitHub Pages site:

```markdown
[View Snakey Dashboard](https://your-deployed-app.onrender.com)
```

## Environment Variables

If you need to set environment variables:

- `PORT`: Port to run the app (default: 8050)
- `DEBUG`: Set to `False` in production

## Updating the Deployment

After making changes:

1. Commit and push to GitHub
2. Most platforms will auto-deploy
3. For manual deployments, repeat the deployment steps

## Troubleshooting

### App won't start
- Check that all dependencies are in requirements.txt
- Verify Python version compatibility
- Check logs in your hosting platform

### Data not loading
- Ensure data files are included in git (check .gitignore)
- Verify file paths are correct
- Check CSV file formatting

### Slow performance
- Consider upgrading to a paid tier for more resources
- Optimize data loading (add caching)
- Reduce the number of visualizations per page

# Deployment & Website Integration Guide

## Step 1: Deploy to Render

1. **Push to GitHub**
   ```bash
   cd C:\Users\Bassem Noghnogh\Documents\GitHub\Snakey
   git init
   git add .
   git commit -m "Initial commit: Snakey Dashboard"
   git remote add origin https://github.com/bnogh123/Snakey.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to https://render.com and sign up/login
   - Click "New +" → "Web Service"
   - Connect your GitHub account
   - Select the "Snakey" repository
   - Render will auto-detect the `render.yaml` config
   - Click "Create Web Service"
   - Wait 3-5 minutes for deployment
   - You'll get a URL like: `https://snakey-dashboard.onrender.com`

## Step 2: Update Your Website

Once deployed, update `website/snakey.html`:

### Replace the deployment notice with an embedded dashboard:

Find this section (around line 177-195):
```html
<div class="deployment-notice">
    <h3>⚡ DEPLOYMENT IN PROGRESS</h3>
    ...
</div>
```

Replace it with:
```html
<div style="max-width: 1400px; margin: 40px auto; padding: 0 20px;">
    <div style="background: rgba(0, 255, 65, 0.05); border: 2px solid #00ff41; border-radius: 8px; overflow: hidden;">
        <div style="padding: 20px; text-align: center; border-bottom: 2px solid #00ff41;">
            <h3 style="font-family: 'VT323', monospace; color: #00ff41; font-size: 28px; margin: 0;">
                LIVE DASHBOARD
            </h3>
        </div>
        <iframe
            src="https://YOUR-APP-NAME.onrender.com"
            style="width: 100%; height: 100vh; border: none; display: block;"
            title="Snakey Interactive Dashboard">
        </iframe>
    </div>
</div>
```

**Important:** Replace `YOUR-APP-NAME.onrender.com` with your actual Render URL!

### Alternative: Add a "Launch Dashboard" button

If you prefer a button instead of embedding:
```html
<div style="text-align: center; margin: 40px 0;">
    <a href="https://YOUR-APP-NAME.onrender.com"
       target="_blank"
       style="display: inline-block; padding: 20px 40px; background: #00ff41; color: #0a0e27;
              text-decoration: none; font-family: 'VT323', monospace; font-size: 28px;
              border-radius: 8px; box-shadow: 0 0 20px #00ff41; transition: all 0.3s ease;">
        LAUNCH DASHBOARD →
    </a>
</div>
```

## Step 3: Test Everything

1. Open `website/index.html` in your browser
2. Click on the "Snakey Dashboard" project card
3. Verify the page loads correctly
4. Once deployed, test the embedded dashboard or link

## Step 4: Commit Website Changes

```bash
cd C:\Users\Bassem Noghnogh\Documents\GitHub\website
git add .
git commit -m "Add Snakey Dashboard project page"
git push
```

## Optional: Custom Domain

If you have a custom domain, you can:
1. Configure it in Render's dashboard settings
2. Update the iframe/link URL to your custom domain

## Troubleshooting

### Dashboard doesn't load in iframe
- Check browser console for errors
- Some hosting platforms block iframes - try the button approach instead
- Verify the Render URL is correct

### Render app sleeps after inactivity
- Free tier apps sleep after 15 minutes of no activity
- They wake up on first request (may take 30-60 seconds)
- Consider upgrading to paid tier for always-on service

### Dashboard loads slowly
- First load might be slow as data is processed
- Subsequent loads should be faster
- Consider adding loading indicator

## Success Checklist

- [ ] Snakey repo pushed to GitHub
- [ ] Dashboard deployed on Render
- [ ] Render URL obtained
- [ ] snakey.html updated with live URL
- [ ] Website changes committed
- [ ] Project accessible from portfolio
- [ ] Dashboard loads and functions correctly

---

Your dashboard is now live and integrated into your portfolio! 🎉

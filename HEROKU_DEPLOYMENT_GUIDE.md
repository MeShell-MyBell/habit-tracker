# Heroku Deployment Guide for Habit Tracker

## Issues Fixed
✅ Updated Python version to 3.11.10 (Heroku supported)  
✅ Fixed Django settings for proper production deployment  
✅ Improved database configuration  
✅ Enhanced static files handling  
✅ Added proper ALLOWED_HOSTS configuration  

## Step-by-Step Heroku Deployment

### 1. Prerequisites
- Heroku account created
- GitHub repository for your project (✅ Done)

### 2. Connect GitHub to Heroku
1. Log in to your Heroku dashboard at [https://dashboard.heroku.com/](https://dashboard.heroku.com/).
2. Create a new app by clicking **New → Create New App**.
3. Name your app (e.g., `power-of-change`) and select your region.
4. Go to the **Deploy** tab in your app dashboard.
5. Under **Deployment Method**, select **GitHub**.
6. Search for your GitHub repository (e.g., `habit_tracker`) and connect it.

### 3. Enable Automatic Deploys
1. In the **Deploy** tab, scroll to **Automatic Deploys**.
2. Select the branch you want to deploy (e.g., `main`).
3. Click **Enable Automatic Deploys**.

### 4. Set Environment Variables
1. Go to the **Settings** tab in your Heroku app dashboard.
2. Click **Reveal Config Vars**.
3. Add the following environment variables:
   - `SECRET_KEY`: Generate a secure key for Django.
   - `DEBUG`: Set to `False` for production.
   - `HEROKU_APP_NAME`: Set to your app name (e.g., `power-of-change`).

### 5. Add Heroku Postgres
1. In the **Resources** tab, search for **Heroku Postgres** under Add-ons.
2. Select the free **Hobby Dev** plan and attach it to your app.

### 6. Run Database Migrations
1. Go to the **More** dropdown in your Heroku app dashboard.
2. Select **Run Console**.
3. Run the following commands:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py create_default_categories
   ```

### 7. Open Your App
Your app will be live at `https://<your-app-name>.herokuapp.com`.

## Environment Variables Needed

Set these in your Heroku app dashboard (Settings → Config Vars):

| Variable | Value | Description |
|----------|-------|-------------|
| `SECRET_KEY` | Generate a secure key | Django secret key |
| `DEBUG` | `False` | Production mode |
| `HEROKU_APP_NAME` | Your app name | For ALLOWED_HOSTS |
| `DATABASE_URL` | Auto-set by Postgres addon | Database connection |

## Troubleshooting Common Issues

### Issue 1: App crashes immediately
**Solution**: Check logs in the **More → View Logs** section of your Heroku dashboard.

### Issue 2: Static files not loading
**Solution**: Run `python manage.py collectstatic --noinput` in the Heroku console.

### Issue 3: Database errors
**Solution**: Run migrations in the Heroku console:
```bash
python manage.py migrate --run-syncdb
```

### Issue 4: ALLOWED_HOSTS error
**Solution**: Ensure `HEROKU_APP_NAME` is set correctly in Config Vars.

## Security Notes
- Never commit your `env.py` file (✅ Already in .gitignore)
- Always use environment variables for sensitive data
- The fallback SECRET_KEY is only for initial deployment - replace it with a secure one

## Next Steps After Deployment
1. Test all functionality on the live site
2. Set up proper email backend for password resets
3. Configure custom domain (if needed)
4. Set up monitoring and backups

## Support
If you encounter issues, check:
1. Heroku logs in the dashboard
2. Django settings are correct
3. All environment variables are set
4. Database migrations have run successfully
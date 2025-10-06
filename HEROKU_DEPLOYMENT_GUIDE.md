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
- Heroku CLI installed on your machine
- Git repository pushed to GitHub (✅ Done)

### 2. Create Heroku App
```bash
# Login to Heroku
heroku login

# Create a new Heroku app (replace 'your-app-name' with desired name)
heroku create your-habit-tracker-app

# Set your app name as an environment variable
heroku config:set HEROKU_APP_NAME=your-habit-tracker-app
```

### 3. Set Environment Variables
```bash
# Set a secure secret key (generate a new one for production)
heroku config:set SECRET_KEY="your-super-secret-key-here"

# Set DEBUG to False for production
heroku config:set DEBUG=False

# Add database (Heroku Postgres)
heroku addons:create heroku-postgresql:mini
```

### 4. Deploy to Heroku
```bash
# Add Heroku remote (if not automatically added)
heroku git:remote -a your-habit-tracker-app

# Deploy your code
git push heroku main
```

### 5. Run Database Migrations
```bash
# Run migrations on Heroku
heroku run python manage.py migrate

# Create superuser (optional)
heroku run python manage.py createsuperuser

# Create default categories if you have the management command
heroku run python manage.py create_default_categories
```

### 6. Open Your App
```bash
heroku open
```

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
**Solution**: Check logs with `heroku logs --tail`

### Issue 2: Static files not loading
**Solution**: Run `heroku run python manage.py collectstatic --noinput`

### Issue 3: Database errors
**Solution**: 
```bash
heroku run python manage.py migrate --run-syncdb
```

### Issue 4: ALLOWED_HOSTS error
**Solution**: Ensure `HEROKU_APP_NAME` is set correctly:
```bash
heroku config:set HEROKU_APP_NAME=your-exact-app-name
```

## Security Notes
- Never commit your `env.py` file (✅ Already in .gitignore)
- Always use environment variables for sensitive data
- The fallback SECRET_KEY is only for initial deployment - replace it with a secure one

## Useful Heroku Commands
```bash
# View logs
heroku logs --tail

# Open Django shell
heroku run python manage.py shell

# Check dyno status
heroku ps

# Restart app
heroku restart
```

## Next Steps After Deployment
1. Test all functionality on the live site
2. Set up proper email backend for password resets
3. Configure custom domain (if needed)
4. Set up monitoring and backups

## Support
If you encounter issues, check:
1. Heroku logs: `heroku logs --tail`
2. Django settings are correct
3. All environment variables are set
4. Database migrations have run successfully
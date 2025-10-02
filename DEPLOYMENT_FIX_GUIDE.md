# Deployment Fix Guide - Heroku & GitHub

## 🚨 Common Issues Fixed

### 1. Django Version Mismatch ✅
- Updated requirements.txt to Django 5.2.4
- Updated crispy-forms versions for compatibility

### 2. Settings Configuration ✅
- Fixed SECRET_KEY handling for production
- Fixed DEBUG setting for Heroku
- Updated ALLOWED_HOSTS for Heroku subdomains
- Fixed WhiteNoise static files configuration

### 3. Runtime Specification ✅
- Added runtime.txt with Python 3.12.4

## 🚀 Step-by-Step Deployment Fix

### Phase 1: GitHub Setup

1. **Initialize Git Repository (if not done)**
```bash
cd "/Users/shellie/Code institute/habit_tracker"
git init
git add .
git commit -m "Initial commit"
```

2. **Create GitHub Repository**
- Go to github.com → New Repository
- Name: `habit-tracker`
- Don't initialize with README (you have one)
- Make it public for assessment

3. **Connect Local to GitHub**
```bash
git remote add origin https://github.com/YOUR_USERNAME/habit-tracker.git
git branch -M main
git push -u origin main
```

### Phase 2: Heroku Deployment

1. **Install Heroku CLI** (if not installed)
- Download from: https://devcenter.heroku.com/articles/heroku-cli

2. **Login to Heroku**
```bash
heroku login
```

3. **Create Heroku App**
```bash
heroku create your-habit-tracker-app-name
```

4. **Set Environment Variables**
```bash
heroku config:set SECRET_KEY="your-super-secret-key-here"
heroku config:set DEBUG=False
```

5. **Add PostgreSQL Database**
```bash
heroku addons:create heroku-postgresql:mini
```

6. **Deploy to Heroku**
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

7. **Run Migrations on Heroku**
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## 🔧 Troubleshooting Common Errors

### Error: "SECRET_KEY not set"
**Solution:**
```bash
heroku config:set SECRET_KEY="django-insecure-your-key-here"
```

### Error: "App crashed" or "H10 error"
**Check logs:**
```bash
heroku logs --tail
```
**Common fixes:**
- Ensure requirements.txt is correct
- Check Procfile format: `web: gunicorn habit_tracker.wsgi`

### Error: Static files not loading
**Solution:** Already fixed in settings.py with WhiteNoise

### Error: Database connection issues
**Check database URL:**
```bash
heroku config:get DATABASE_URL
```

## 📋 Pre-Deployment Checklist

- [x] requirements.txt updated
- [x] runtime.txt created
- [x] settings.py configured for production
- [x] Procfile exists
- [x] Static files configured
- [ ] Environment variables set on Heroku
- [ ] Database migrations run
- [ ] Superuser created

## 🎯 Quick Commands Reference

**Local Development:**
```bash
python manage.py runserver
```

**Deploy Updates:**
```bash
git add .
git commit -m "Update description"
git push origin main
git push heroku main
```

**Check Heroku Status:**
```bash
heroku ps
heroku logs --tail
```

**Reset Heroku Database (if needed):**
```bash
heroku pg:reset DATABASE_URL --confirm your-app-name
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## 🆘 If Still Having Issues

1. **Check Heroku logs:** `heroku logs --tail`
2. **Verify environment variables:** `heroku config`
3. **Test locally first:** `python manage.py runserver`
4. **Check git status:** `git status`

Your habit tracker should now deploy successfully to both GitHub and Heroku!
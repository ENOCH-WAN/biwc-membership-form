# Deployment Guide - BIWC-Kwabenya Membership Website

## Quick Start - Deploy on Render.com (FREE)

### Step 1: Prepare Your Code
✅ **Already Done!** Your code is ready with:
- `requirements.txt` - Python dependencies
- `wsgi.py` - Server configuration
- `app.py` - Flask application
- `database.py` - Database setup
- `templates/` - HTML templates
- `static/css/` - Styling

### Step 2: Push Code to GitHub
1. Create a GitHub account (if you don't have one): https://github.com/signup
2. Create a new repository called "biwc-membership"
3. Upload your membership folder to GitHub:
   - Copy all files from your membership folder
   - Upload them to the GitHub repository

### Step 3: Deploy on Render.com
1. Go to https://render.com
2. Click "Get Started" or Sign up
3. Connect your GitHub account
4. Select your repository
5. Choose "Web Service"
6. Fill in these settings:
   - **Name**: biwc-membership (or any name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:app`
   - Leave other settings as default
7. Click "Create Web Service"

### Step 4: Get Your Public Link
- After deployment (2-3 minutes), Render will give you a URL like:
  - `https://biwc-membership.onrender.com`
- This is your public website link! 🎉

---

## Alternative Hosting Options

### Option 2: PythonAnywhere (Also FREE)
- Website: https://www.pythonanywhere.com
- Good for Python/Flask apps
- Easy web-based interface

### Option 3: Railway.app
- Website: https://railway.app
- Modern deployment platform
- Simple GitHub integration

---

## Important Notes

⚠️ **Database**: 
- Currently uses SQLite (church_members.db)
- Works fine for moderate traffic
- For larger scale, consider upgrading to PostgreSQL

📝 **Environment Variables**:
- Secret key is hardcoded in app.py
- Before production deployment, set:
  ```
  FLASK_SECRET_KEY=your-secure-key-here
  ```

🔒 **Security**:
- Change the secret key in app.py for production
- Never share database files publicly

---

## Summary
1. **Push to GitHub** → 10 minutes
2. **Deploy on Render** → 5 minutes
3. **Get Public URL** → Instant!

Your website will be live for everyone to access! 🚀

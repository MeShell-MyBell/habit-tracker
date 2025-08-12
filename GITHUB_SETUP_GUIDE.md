# GitHub Project Board Setup Instructions

## Step-by-Step Guide to Create Your Project Board

### 1. Navigate to Your GitHub Repository
- Go to: `https://github.com/MeShell-MyBell/habit-tracker`
- If you don't have this repository yet, create it first

### 2. Create the Project Board
- Click on the **"Projects"** tab in your repository
- Click **"New project"**
- Choose **"Board"** template
- Name it: **"Habit Tracker Development"**
- Description: **"Agile development board for habit tracker application"**
- Set visibility to **"Public"** (important for assessment)

### 3. Set Up Columns
Create these 4 columns in order:
1. **📋 Backlog** - Future features and ideas
2. **📝 To Do** - Ready for development
3. **🔄 In Progress** - Currently working on
4. **✅ Done** - Completed features

### 4. Create Issues from User Stories

Copy these as GitHub Issues (Issues tab → New issue):

#### MUST HAVE ISSUES

**Issue 1: User Authentication System**
```
Title: User Registration and Login System
Labels: Must Have, Authentication
Description: 
As a site user, I want to register and log in so that only I can access my habits.

Acceptance Criteria:
- [x] Users can register with email and password
- [x] Users can log in and log out  
- [x] Only authenticated users can access habits
- [x] Proper session management

Status: Done ✅
```

**Issue 2: Basic Habit CRUD**
```
Title: Create, Read, Update, Delete Habits
Labels: Must Have, Core Feature
Description:
As a site user, I want to create habits in different categories so that I can organize my goals.

Acceptance Criteria:
- [x] Users can create new habits
- [x] Users can view their habits
- [x] Users can edit existing habits
- [x] Users can delete habits

Status: Done ✅
```

**Issue 3: Progress Tracking**
```
Title: Mark Habits as Complete
Labels: Must Have, Progress
Description:
As a site user, I want to mark habits as complete so that I can track my daily progress.

Acceptance Criteria:
- [x] Users can mark habits as completed
- [x] Visual indication of completed habits
- [x] Progress is saved to database

Status: Done ✅
```

**Issue 4: Habit Dashboard**
```
Title: View All Habits Dashboard
Labels: Must Have, UI
Description:
As a site user, I want to view my habits so that I can see what I need to accomplish.

Acceptance Criteria:
- [x] Clean dashboard showing all user habits
- [x] Organized by categories
- [x] Shows completion status

Status: Done ✅
```

#### SHOULD HAVE ISSUES

**Issue 5: Edit Habits**
```
Title: Edit Existing Habits
Labels: Should Have, Enhancement
Description:
As a site user, I want to edit my habits so that I can update my goals as they evolve.

Acceptance Criteria:
- [x] Edit form pre-populated with current data
- [x] All habit fields can be updated
- [x] Changes are saved properly

Status: Done ✅
```

**Issue 6: Delete Habits**
```
Title: Delete Habits with Confirmation
Labels: Should Have, Safety
Description:
As a site user, I want to delete habits so that I can remove goals I no longer want to pursue.

Acceptance Criteria:
- [x] Delete button available on habits
- [x] Confirmation dialog before deletion
- [x] Habit and related progress removed

Status: Done ✅
```

#### COULD HAVE ISSUES

**Issue 7: Password Reset**
```
Title: Password Reset Functionality
Labels: Could Have, Security
Description:
As a site user, I want to reset my password so that I can regain access if I forget it.

Acceptance Criteria:
- [x] Password reset form
- [x] Email with reset token
- [x] Secure token validation

Status: Done ✅
```

**Issue 8: Category System**
```
Title: Habit Categories
Labels: Could Have, Organization
Description:
As a site user, I want to categorize my habits so that I can organize them by type.

Acceptance Criteria:
- [x] Predefined categories available
- [x] Habits can be assigned to categories
- [x] Filter habits by category

Status: Done ✅
```

#### TECHNICAL TASKS

**Issue 9: Deployment Setup**
```
Title: Deploy to Heroku
Labels: Technical, Deployment
Description:
Set up production deployment on Heroku

Acceptance Criteria:
- [x] App deployed and accessible
- [x] Database configured
- [x] Environment variables set

Status: Done ✅
```

**Issue 10: Database Setup**
```
Title: PostgreSQL Database Configuration
Labels: Technical, Database
Description:
Configure PostgreSQL for production

Acceptance Criteria:
- [x] PostgreSQL addon added
- [x] Migrations run successfully
- [x] Database populated with default data

Status: Done ✅
```

#### FUTURE ENHANCEMENTS (for Backlog)

**Issue 11: Streak Tracking**
```
Title: Habit Streak Counter
Labels: Enhancement, Future
Description:
Add visual streak counters for motivation

Status: Backlog 📋
```

**Issue 12: Analytics Dashboard**
```
Title: Detailed Progress Charts
Labels: Enhancement, Analytics
Description:
Add detailed progress charts and statistics

Status: Backlog 📋
```

### 5. Organize Issues in Project Board
- Move completed issues (1-10) to **✅ Done** column
- Move future enhancements (11-12) to **📋 Backlog** column

### 6. Add Labels
Create these labels in your repository (Settings → Labels):
- **Must Have** (red)
- **Should Have** (orange) 
- **Could Have** (yellow)
- **Enhancement** (blue)
- **Technical** (purple)
- **Future** (gray)

### 7. Final Check
- Ensure project board is set to **Public**
- All issues are properly labeled
- Issues are in correct columns
- Project board link works: `https://github.com/MeShell-MyBell/habit-tracker/projects`

## Quick Setup Summary
1. Go to GitHub → Your Repository → Projects → New Project
2. Create "Board" template named "Habit Tracker Development" 
3. Add 4 columns: Backlog, To Do, In Progress, Done
4. Create 12 issues from the templates above
5. Set appropriate labels and move to correct columns
6. Make project board public
7. Test the link from your README

This will show assessors your complete development journey and agile methodology!
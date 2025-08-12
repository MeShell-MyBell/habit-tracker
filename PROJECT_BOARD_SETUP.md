# Project Board Issues for Habit Tracker

## Must Have Issues (Priority: High)

### User Authentication
- **Title**: User Registration and Login System
- **Description**: As a site user, I want to register and log in so that only I can access my habits.
- **Acceptance Criteria**:
  - Users can register with email and password
  - Users can log in and log out
  - Only authenticated users can access habits
- **Labels**: Must Have, Authentication
- **Status**: Done

### Basic Habit CRUD
- **Title**: Create, Read, Update, Delete Habits
- **Description**: As a site user, I want to create habits in different categories so that I can organize my goals.
- **Acceptance Criteria**:
  - Users can create new habits
  - Users can view their habits
  - Users can edit existing habits
  - Users can delete habits
- **Labels**: Must Have, Core Feature
- **Status**: Done

### Progress Tracking
- **Title**: Mark Habits as Complete
- **Description**: As a site user, I want to mark habits as complete so that I can track my daily progress.
- **Acceptance Criteria**:
  - Users can mark habits as completed for today
  - Visual indication of completed habits
  - Progress is saved to database
- **Labels**: Must Have, Progress
- **Status**: Done

### Habit Dashboard
- **Title**: View All Habits Dashboard
- **Description**: As a site user, I want to view my habits so that I can see what I need to accomplish.
- **Acceptance Criteria**:
  - Clean dashboard showing all user habits
  - Organized by categories
  - Shows completion status
- **Labels**: Must Have, UI
- **Status**: Done

## Should Have Issues (Priority: Medium)

### Edit Habits
- **Title**: Edit Existing Habits
- **Description**: As a site user, I want to edit my habits so that I can update my goals as they evolve.
- **Acceptance Criteria**:
  - Edit form pre-populated with current data
  - All habit fields can be updated
  - Changes are saved properly
- **Labels**: Should Have, Enhancement
- **Status**: Done

### Delete Habits
- **Title**: Delete Habits with Confirmation
- **Description**: As a site user, I want to delete habits so that I can remove goals I no longer want to pursue.
- **Acceptance Criteria**:
  - Delete button available on habits
  - Confirmation dialog before deletion
  - Habit and related progress removed
- **Labels**: Should Have, Safety
- **Status**: Done

### Progress History
- **Title**: View Progress Over Time
- **Description**: As a site user, I want to see my progress over time so that I can stay motivated.
- **Acceptance Criteria**:
  - History of completed habits
  - Visual progress indicators
  - Motivational feedback
- **Labels**: Should Have, Analytics
- **Status**: In Progress

## Could Have Issues (Priority: Low)

### Password Reset
- **Title**: Password Reset Functionality
- **Description**: As a site user, I want to reset my password so that I can regain access if I forget it.
- **Acceptance Criteria**:
  - Password reset form
  - Email with reset token
  - Secure token validation
- **Labels**: Could Have, Security
- **Status**: Done

### Category System
- **Title**: Habit Categories
- **Description**: As a site user, I want to categorize my habits so that I can organize them by type.
- **Acceptance Criteria**:
  - Predefined categories available
  - Habits can be assigned to categories
  - Filter habits by category
- **Labels**: Could Have, Organization
- **Status**: Done

## Technical Tasks

### Deployment Setup
- **Title**: Deploy to Heroku
- **Description**: Set up production deployment on Heroku
- **Acceptance Criteria**:
  - App deployed and accessible
  - Database configured
  - Environment variables set
- **Labels**: Technical, Deployment
- **Status**: Done

### Database Setup
- **Title**: PostgreSQL Database Configuration
- **Description**: Configure PostgreSQL for production
- **Acceptance Criteria**:
  - PostgreSQL addon added
  - Migrations run successfully
  - Database populated with default data
- **Labels**: Technical, Database
- **Status**: Done

### UI/UX Polish
- **Title**: Bootstrap 5 Styling
- **Description**: Implement responsive design with Bootstrap 5
- **Acceptance Criteria**:
  - Mobile-friendly responsive design
  - Consistent styling across pages
  - Good user experience
- **Labels**: Technical, UI/UX
- **Status**: Done

## Future Enhancements (Backlog)

### Streak Tracking
- **Title**: Habit Streak Counter
- **Description**: Add visual streak counters for motivation
- **Labels**: Enhancement, Future
- **Status**: Backlog

### Analytics Dashboard
- **Title**: Detailed Progress Charts
- **Description**: Add detailed progress charts and statistics
- **Labels**: Enhancement, Analytics
- **Status**: Backlog

### Social Features
- **Title**: Share Achievements
- **Description**: Allow users to share achievements with friends
- **Labels**: Enhancement, Social
- **Status**: Backlog

### Mobile App
- **Title**: Native Mobile Application
- **Description**: Create native mobile app version
- **Labels**: Enhancement, Mobile
- **Status**: Backlog

### Notifications
- **Title**: Email Reminders
- **Description**: Send email or push notifications for habits
- **Labels**: Enhancement, Notifications
- **Status**: Backlog
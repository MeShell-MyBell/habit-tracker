# The Power of Change - Habit Tracker

## Overview
This project is a habit tracker web application built with the python-based framework Django. The front-end is HTML & CSS, Javascript & also incorporates the Bootstrap 5 framework. There is full CRUD functionality as users can create, read, update, and delete their habits. This application is named the Power of Change and is designed to be user-friendly and visually appealing.

The live project can be found here: [Live Project](https://shellies-habit-tracker-640f97fbfff2.herokuapp.com/)

## Table of Contents
- [Overview](#overview)
- [Agile Development](#agile-development)
- [UX Design](#ux-design)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Colors](#colors)
  - [Fonts](#fonts)
  - [Logo Design](#logo-design)
- [Features](#features)
  - [User Authentication](#user-authentication)
  - [Habit Management](#habit-management)
  - [Category System](#category-system)
  - [Progress Tracking](#progress-tracking)
  - [Password Reset](#password-reset)
- [Database Design](#database-design)
- [Testing](#testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Accessibility Testing](#accessibility-testing)
- [AI Implementation](#ai-implementation)
- [Deployment](#deployment)
  - [Heroku Deployment](#heroku-deployment)
  - [Local Development](#local-development)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

## Agile Development

I used an agile approach to build this project, which means I broke the work down into small, manageable tasks. This helped me stay organized and make steady progress on the habit tracker.

**🔗 [View my Project Board](https://github.com/MeShell-MyBell/habit-tracker/projects)**

I organized my work using GitHub's project board, which is like a digital to-do list. I moved tasks through different stages:
- **Backlog**: Ideas and features I might add later
- **To Do**: Tasks ready to work on next  
- **In Progress**: What I'm currently building
- **Done**: Completed features

I divided the project into three main phases:

**Phase 1 - Getting Started**
- Set up the basic Django project
- Created user login and registration
- Built the main habit features (add, view, edit, delete)
- Got the app working on Heroku

**Phase 2 - Adding Features**
- Added categories to organize habits
- Built the progress tracking system
- Made the app look good with Bootstrap
- Fixed bugs and improved forms

**Phase 3 - Final Touches**
- Added password reset feature
- Polished the design and user experience
- Set up the admin area
- Tested everything thoroughly

I used the MoSCoW method to decide what was most important:
- **Must Have**: Essential features needed for the app to work
- **Should Have**: Important features that make the app better
- **Could Have**: Nice extras if I had time

This approach helped me focus on building a working app first, then adding improvements. It also meant I always had something functional to show, even if all features weren't complete yet.

## UX Design

### User Stories
I used an agile workflow for the project. First I created user stories to set up small, achievable and precise tasks. The MoSCoW system was helpful for me to focus on getting an MVP created by focusing on getting the must-haves done.

Here are the user stories:

**Must Have:**
- As a site user, I want to register and log in so that only I can access my habits.
- As a site user, I want to create habits in different categories so that I can organize my goals.
- As a site user, I want to mark habits as complete so that I can track my daily progress.
- As a site user, I want to view my habits so that I can see what I need to accomplish.

**Should Have:**
- As a site user, I want to edit my habits so that I can update my goals as they evolve.
- As a site user, I want to delete habits so that I can remove goals I no longer want to pursue.
- As a site user, I want to see my progress over time so that I can stay motivated.

**Could Have:**
- As a site user, I want to reset my password so that I can regain access if I forget it.
- As a site user, I want to categorize my habits so that I can organize them by type.

### Wireframes
*[Add your wireframes here]*

### Colors
*[Add your color palette and accessibility considerations here]*

### Fonts
*[Add your typography choices here]*

### Logo Design
*[Add your logo design process here]*

## Features

This section showcases the key features of the habit tracker application with visual examples.

### User Authentication

![Login Page](screenshots/login.png)

The application includes a comprehensive authentication system:
- **User Registration**: Clean signup form with validation
- **Secure Login**: Custom login form with error handling
- **Password Reset**: Email-based password recovery system
- **User Session Management**: Proper session handling and security

![Registration Form](screenshots/registration.png)

### Habit Management

![Dashboard Overview](screenshots/dashboard.png)

Core CRUD functionality for habit management:
- **Create**: Users can add new habits with titles, descriptions, and categories
- **Read**: View all habits in an organized dashboard with habit counts
- **Update**: Edit existing habits to modify goals or details
- **Delete**: Remove habits with confirmation dialog for safety

![Add Habit Form](screenshots/add-habit.png)

### Category System

![Categories Display](screenshots/categories.png)

Eight pre-defined categories help users organize their habits:
- Health & Fitness
- Learning & Education
- Productivity
- Personal Development
- Social & Relationships
- Hobbies & Creativity
- Finance & Career
- Mindfulness & Wellness

### Progress Tracking

![Progress View](screenshots/progress.png)

- **Daily Completion**: Mark habits as complete with visual feedback
- **Status Indicators**: Clear visual distinction between pending and completed habits
- **Instant Feedback**: Success messages and notifications for user actions

### Password Reset

![Password Reset](screenshots/password-reset.png)

- **Secure Reset Flow**: Token-based password reset system
- **Email Integration**: Password reset links sent via email
- **Security Measures**: Time-limited tokens for enhanced security

### Responsive Design

![Mobile View](screenshots/mobile-responsive.png)

- **Mobile Friendly**: Fully responsive design using Bootstrap 5
- **Cross-Device Compatibility**: Works seamlessly on desktop, tablet, and mobile
- **Touch-Friendly Interface**: Optimized buttons and forms for touch devices

## Database Design

The application uses four main models:

1. **Category**: Organizes habits into themed groups
2. **Habit**: Core model storing habit information and user relationships
3. **Progress**: Tracks daily completion status for each habit
4. **PasswordResetToken**: Manages secure password reset functionality

## Testing

This section documents the comprehensive testing approach used to ensure the habit tracker meets quality standards.

### HTML Validation

All HTML templates have been validated using the W3C Markup Validator:

![HTML Validation Results](screenshots/html-validation.png)

- **Homepage**: ✅ No errors or warnings
- **Login Page**: ✅ No errors or warnings  
- **Registration Page**: ✅ No errors or warnings
- **Dashboard**: ✅ No errors or warnings
- **Edit Habit Form**: ✅ No errors or warnings

### CSS Validation

CSS stylesheets validated using W3C CSS Validation Service (Jigsaw):

![CSS Validation Results](screenshots/css-validation.png)

- **style.css**: ✅ No errors found
- **Bootstrap Integration**: ✅ Properly integrated without conflicts

### Manual Testing

Comprehensive manual testing was conducted across different browsers and devices:

#### Browser Compatibility
- **Chrome**: ✅ Full functionality confirmed
- **Firefox**: ✅ Full functionality confirmed
- **Safari**: ✅ Full functionality confirmed
- **Edge**: ✅ Full functionality confirmed

#### Device Testing
- **Desktop**: ✅ Responsive layout works perfectly
- **Tablet**: ✅ Touch-friendly interface confirmed
- **Mobile**: ✅ Mobile-optimized experience

#### User Authentication Testing
- **Registration**: ✅ Form validation and account creation work correctly
- **Login**: ✅ Authentication and redirect functionality verified
- **Logout**: ✅ Session termination and redirect confirmed
- **Password Reset**: ✅ Email flow and token validation tested

#### CRUD Functionality Testing
- **Create Habits**: ✅ Form submission and database storage verified
- **Read Habits**: ✅ Habit display and organization confirmed
- **Update Habits**: ✅ Edit functionality and data persistence tested
- **Delete Habits**: ✅ Confirmation dialog and safe deletion verified

### Automated Testing

Django's built-in testing framework was used for automated testing:

```python
# Example test cases implemented:
- Model validation testing
- View response testing
- Form validation testing
- User authentication testing
- Database integrity testing
```

### Accessibility Testing

Accessibility features have been tested to ensure inclusive design:

![Accessibility Audit](screenshots/accessibility-audit.png)

- **Color Contrast**: ✅ WCAG AA compliance verified
- **Keyboard Navigation**: ✅ Full keyboard accessibility confirmed
- **Screen Reader Compatibility**: ✅ Proper ARIA labels and semantic HTML
- **Font Scaling**: ✅ Text remains readable at 200% zoom

## AI Implementation

This section documents how AI tools were used during the development of this habit tracker application.

### AI-Assisted Development Process

During the development of this habit tracker, I used GitHub Copilot and other AI tools to enhance productivity and code quality:

#### Code Generation and Completion
- **Django Models**: AI assisted in generating the initial model structures for Habit, Category, and Progress models
- **Form Creation**: Auto-completion helped create comprehensive Django forms with proper validation
- **Template Structure**: AI suggestions provided Bootstrap-compatible HTML template layouts

#### Problem Solving and Debugging
- **Error Resolution**: When encountering Django-specific errors, AI tools provided contextual solutions
- **Best Practices**: AI suggestions helped implement Django security best practices and proper authentication flows
- **Code Optimization**: Received suggestions for more efficient database queries and view structures

#### Documentation and Comments
- **Code Comments**: AI assisted in writing clear, descriptive comments for complex functions
- **README Content**: AI tools helped structure and improve the documentation you're reading now
- **User Story Refinement**: AI feedback helped refine user stories to be more specific and testable

### AI Tools Used

1. **GitHub Copilot**: Primary coding assistant for:
   - Auto-completing Django view functions
   - Generating form validation logic
   - Creating template structures
   - Writing test cases

2. **Claude/ChatGPT**: Used for:
   - Planning project architecture
   - Debugging complex issues
   - Refining documentation
   - Code review and suggestions

3. **AI-Powered Code Analysis**: For:
   - Identifying potential security vulnerabilities
   - Suggesting performance improvements
   - Code style and PEP8 compliance checking

### Human Oversight and Validation

While AI tools were valuable throughout development, all AI-generated code was:
- **Manually Reviewed**: Every suggestion was carefully evaluated before implementation
- **Tested Thoroughly**: All AI-assisted code went through the same testing process
- **Customized**: AI suggestions were adapted to fit the specific needs of this project
- **Validated**: Functionality was verified to meet user requirements and project goals

### Learning Outcomes

Using AI tools during development provided valuable learning experiences:
- **Faster Development**: Reduced time spent on boilerplate code
- **Best Practices**: Learned Django patterns and conventions through AI suggestions
- **Problem-Solving Skills**: Improved ability to debug and optimize code with AI assistance
- **Code Quality**: Enhanced code readability and maintainability

This project demonstrates how AI can be effectively used as a development tool while maintaining human oversight and decision-making in the creative and architectural aspects of software development.

## Deployment

### Heroku Deployment

The application is deployed on Heroku with the following configuration:

1. **Platform**: Heroku with PostgreSQL database
2. **Environment Variables**: 
   - `SECRET_KEY`: Django secret key for security
   - `DEBUG`: Set to False in production
   - `DATABASE_URL`: PostgreSQL connection string (auto-generated)

3. **Build Configuration**:
   - `Procfile`: Defines web process using Gunicorn
   - `requirements.txt`: Lists all Python dependencies
   - `runtime.txt`: Specifies Python version (3.12.4)

4. **Static Files**: Served using WhiteNoise for efficient delivery

### Local Development

To run the project locally:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `env.py`
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Start development server: `python manage.py runserver`

## Technologies Used

**Backend:**
- Python 3.12.4
- Django 5.1.1
- PostgreSQL (Production)
- SQLite (Development)

**Frontend:**
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Crispy Forms for form styling

**Deployment & Tools:**
- Heroku (Hosting)
- Git & GitHub (Version Control)
- WhiteNoise (Static Files)
- Gunicorn (WSGI Server)

## Future Enhancements

- **Streak Tracking**: Add visual streak counters for motivation
- **Habit Analytics**: Detailed progress charts and statistics
- **Social Features**: Share achievements with friends ---=----ADD FAcebook links in
- **Mobile App**: Native mobile application
- **Reminder System**: Email or push notifications


## Credits

- Django Documentation
- Bootstrap 5 Documentation
- Heroku Documentation
- Code Institute Learning Materials
- Stack Overflow Community

---

[Back to Top](#habit-tracker---power-of-change)



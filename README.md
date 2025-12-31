# Grace Community Church Membership System

A Flask-based web application for managing church membership registrations and viewing member directories.

## Project Structure

```
membership/
├── app.py                 # Flask application main file
├── database.py           # Database management and functions
├── templates/            # HTML templates for Flask
│   ├── index.html       # Home page
│   ├── register.html    # Registration form
│   └── members.html     # Member directory
├── static/
│   └── css/
│       └── style.css    # Application styling
└── church_members.db    # SQLite database (created on first run)
```

## Features

- **Member Registration**: Comprehensive form for church membership applications
- **Member Directory**: View all registered members with their details
- **Dashboard**: Home page displaying member count statistics
- **Form Validation**: Client-side and server-side validation
- **Responsive Design**: Mobile-friendly interface

## Requirements

- Python 3.7+
- Flask 2.0+
- SQLite3 (included with Python)

## Installation

1. **Install Flask**:
   ```bash
   pip install flask
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

### Home Page (/)
- Displays total member count
- Links to registration and member directory

### Registration (/register)
- Fill out the membership application form
- Required fields are marked with *
- Includes:
  - Personal Information
  - Contact Information
  - Additional Information
  - Emergency Contact
  - Spiritual Information

### Member Directory (/members)
- View all registered members
- See member details including name, email, phone, city, and spiritual status
- Members are sorted by join date (newest first)

## Database

The application uses SQLite3 to store member information. The database is automatically initialized on first run with a `members` table containing:

- Personal details (name, email, phone, DOB, gender)
- Address information (street, city, state, postal code)
- Family information (marital status, emergency contacts)
- Spiritual information (spiritual status, baptism date, previous church)
- Skills and interests for ministry involvement
- Automatic join date timestamp

## Notes

- The default secret key should be changed for production use
- The database file `church_members.db` is created in the application root directory
- Email addresses must be unique
- The application runs in debug mode by default (disable in production)

## Future Enhancements

- User authentication and admin panel
- Email notifications
- Member profile editing
- Search and filtering functionality
- Export member data to CSV
- Member activity tracking

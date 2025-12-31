from flask import Flask, render_template, request, redirect, url_for, flash
import database
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this for production

@app.route('/')
def index():
    """Home page"""
    member_count = database.get_member_count()
    return render_template('index.html', member_count=member_count)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Membership registration form"""
    if request.method == 'POST':
        try:
            member_data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'phone': request.form['phone'],
                'date_of_birth': request.form['date_of_birth'],
                'gender': request.form['gender'],
                'address': request.form['address'],
                'city': request.form['city'],
                'state': request.form['state'],
                'postal_code': request.form['postal_code'],
                'marital_status': request.form['marital_status'],
                'occupation': request.form['occupation'],
                'emergency_contact_name': request.form['emergency_contact_name'],
                'emergency_contact_phone': request.form['emergency_contact_phone'],
                'spiritual_status': request.form['spiritual_status'],
                'baptism_date': request.form['baptism_date'] if request.form['baptism_date'] else None,
                'previous_church': request.form['previous_church'],
                'skills_interests': request.form['skills_interests']
            }
            
            member_id = database.add_member(member_data)
            flash(f'Registration successful! Your member ID is {member_id}. Welcome to our church family!', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            flash(f'Registration failed: {str(e)}', 'error')
    
    return render_template('register.html')

@app.route('/members')
def members():
    """View all registered members"""
    all_members = database.get_all_members()
    return render_template('members.html', members=all_members)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import InputRequired, Email, ValidationError
from twilio.rest import Client
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = ''

# Twilio credentials
account_sid = ''
auth_token = ''
twilio_whatsapp_number = 'whatsapp:+14155238886'  # Twilio WhatsApp sandbox number

# Recipient number
recipient_number = ''  # Recipient number provided

# Initialize Twilio client
client = Client(account_sid, auth_token)

# MySQL database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dileepdivya@456",
    database="whatsapp_data"
)
db_cursor = db_connection.cursor()

# Define form for data collection
class DataForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    mobile_number = StringField('Mobile Number', validators=[InputRequired()])
    pdf_file = FileField('PDF File')

    def validate_mobile_number(form, field):
        if not field.data.isdigit() or len(field.data) != 10:
            raise ValidationError('Invalid mobile number')

# Function to send WhatsApp message
def send_whatsapp_message(name, email, number):
    try:
        # Format the recipient's number
        recipient_number_formatted = f'whatsapp:+91{recipient_number}'  # Assuming the number is Indian and adding the country code
        
        # Construct the message body
        message_body = f"Name: {name}\nEmail: {email}\nNumber: {number}"

        # Send the WhatsApp message
        message = client.messages.create(
            from_=twilio_whatsapp_number,
            body=message_body,
            to=recipient_number_formatted
        )

        # Print the message SID for reference
        print("Message SID:", message.sid)
        return True
    except Exception as e:
        print("Error sending WhatsApp message:", str(e))
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        mobile_number = form.mobile_number.data
        pdf_file = request.files.get('pdf_file')

        # Save data to MySQL database
        sql = "INSERT INTO user_data (name, email, mobile_number, pdf_filename) VALUES (%s, %s, %s, %s)"
        if pdf_file:
            pdf_filename = pdf_file.filename
            pdf_file.save(pdf_filename)
            val = (name, email, mobile_number, pdf_filename)
        else:
            val = (name, email, mobile_number, None)  # If no PDF file is uploaded, set pdf_filename to None

        db_cursor.execute(sql, val)
        db_connection.commit()

        # Send WhatsApp message
        send_whatsapp_message(name, email, mobile_number)

        flash('Your data has been successfully sent to WhatsApp!', 'success')
        return redirect(url_for('index'))  # Redirect to the same page after form submission
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

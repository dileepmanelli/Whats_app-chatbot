# Whats_app-chatbot

The WhatsApp Chatbot for Data Collection is a web application designed to streamline the process of collecting user information via WhatsApp. The chatbot allows users to submit their details conveniently through a user-friendly interface, and the submitted information is automatically sent to a designated WhatsApp number using Twilio's API.

# Key Features
User-Friendly Interface: The web application provides a simple and intuitive form for users to input their details, including name, email, and mobile number.<br>
Validation: Data validation ensures that the user inputs are accurate and properly formatted, providing a seamless user experience.<br>
WhatsApp Integration: The chatbot seamlessly integrates with WhatsApp using Twilio's API, enabling automatic sending of user-submitted details to a specified WhatsApp number.<br>
Feedback Messages: Users receive immediate feedback messages on the web interface confirming whether their details have been successfully sent to WhatsApp.<br>
Flash Messages: Flash messages are displayed on the web page to provide real-time notifications to users regarding the status of their data submission.<br>

# Technologies Used
Flask: Python-based web framework for developing the backend server.<br>
HTML/CSS: Frontend development for designing the user interface.<br>
Twilio API: Integration with Twilio's WhatsApp API for sending messages.<br>
MySQL: Database management system for storing user data (optional).<br>
Python: Programming language used for backend logic and integration with Twilio.<br>

# Usage
Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.<br>
Update the Twilio credentials and WhatsApp number in the app.py file.<br>
Run the Flask application using python app.py.<br>
Access the web application through the provided URL and fill out the data collection form.<br>
Upon submission, receive immediate feedback on the web interface regarding the status of your data submission.<br>
# Contributing
Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.


# Acknowledgements
This project was inspired by the need for a simple and efficient way to collect user data via WhatsApp.
Special thanks to Twilio for providing the WhatsApp API and documentation for seamless integration.

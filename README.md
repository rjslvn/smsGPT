# SMS Chatbot with Twilio and OpenAI

A chatbot application that integrates Twilio for SMS communication and OpenAI for natural language processing. The chatbot can engage in conversations and provide responses to incoming SMS messages.

## 📝 Features

- Receives incoming SMS messages using Twilio's webhooks.
- Stores conversation history in a MySQL database.
- Uses the OpenAI API to generate chatbot responses based on conversation history.
- Sends SMS replies using Twilio.

## ⚙️ Technologies Used

- Python
- Flask (web framework)
- Twilio (for SMS communication)
- MySQL (database)
- OpenAI API (natural language processing)

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/chatbot-with-twilio-and-openai.git
   ```

2. Navigate to the project directory:

   ```bash
   cd chatbot-with-twilio-and-openai
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure Twilio:

   - Create a Twilio account and obtain your Account SID and Auth Token.
   - Purchase a phone number from Twilio for sending and receiving SMS.
   - Update the `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` constants in the code with your respective values.

5. Configure the MySQL database:

   - Install MySQL and create a database for the project.
   - Update the `get_mysql_connection()` function in the code with your MySQL connection details.

6. Configure OpenAI:

   - Create an OpenAI account and obtain your API key.
   - Update the code with your OpenAI API key.

7. Start the application:

   ```bash
   python app.py
   ```

8. Expose the application to the internet using a tool like ngrok to receive incoming webhooks from Twilio.

9. Configure Twilio webhook:

   - In your Twilio account settings, set the webhook for incoming SMS messages to `http://your-ngrok-url/sms`.

10. The application is now ready to receive incoming SMS messages and respond with generated chatbot responses.

## 🚀 Usage

1. Send an SMS to your Twilio phone number.

2. The chatbot will process the incoming message and generate a response using OpenAI.

3. The chatbot's response will be sent back as an SMS reply.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize and use the code for your own projects!
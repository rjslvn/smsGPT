import mysql.connector
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

print("Connected to the database")

# Twilio configuration
TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'
TO_PHONE_NUMBER = 'RECIPIENT_PHONE_NUMBER'

app = Flask(__name__)
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="text_memory"
    )


def send_sms(to, body):
    message = twilio_client.messages.create(
        body=body,
        from_=TWILIO_PHONE_NUMBER,
        to=to
    )
    return message.sid


def generate_response(prompt, conversation_id):
    cnx = get_mysql_connection()
    cursor = cnx.cursor()

    # Retrieve conversation history from the database
    cursor.execute("SELECT user_input, bot_response FROM conversations WHERE id = %s", (conversation_id,))
    conversation_history = cursor.fetchall()

    # Add the latest user input to the conversation history
    conversation_history.append((prompt, None))

    # Convert conversation_history into a prompt string
    prompt_with_history = " ".join([f"{row[0]} {row[1]}" for row in conversation_history if row[1] is not None])

    # Remove 'None' from the prompt string
    prompt_with_history = prompt_with_history.replace(" None", "")

    # Use the OpenAI API to generate a response
    # Make sure to add your OpenAI API key here
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_with_history,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Store the latest bot response in the database
    cursor.execute(
        "INSERT INTO conversations (id, user_input, bot_response) VALUES (%s, %s, %s)",
        (conversation_id, prompt, response.choices[0].text.strip())
    )
    cnx.commit()

    cursor.close()
    cnx.close()

    return response.choices[0].text.strip()


@app.route('/sms', methods=['POST'])
def sms():
    user_input = request.form.get('Body')
    from_number = request.form.get('From')

    # Process the user input with the GPT chatbot while maintaining context history
    response = generate_response(user_input, from_number)

    # Create a Twilio MessagingResponse object to reply to the message
    twilio_response = MessagingResponse()
    twilio_response.message(response)

    return str(twilio_response)


if __name__ == '__main__':
    # Send a test SMS
    send_sms(TO_PHONE_NUMBER, "This is a test message from Twilio!")

    # Start the Flask application to handle incoming messages
    app.run(port=5000)

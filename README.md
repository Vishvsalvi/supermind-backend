# Flask Chat Bot Application

This is a Flask-based web application that interacts with a chat bot API. The application allows users to send questions to the chat bot and receive responses.

## Requirements

Ensure you have the following dependencies installed:

```
blinker==1.9.0
certifi==2024.12.14
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
Flask==3.1.0
Flask-Cors==5.0.0
gunicorn==23.0.0
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.5
MarkupSafe==3.0.2
packaging==24.2
python-dotenv==1.0.1
requests==2.32.3
urllib3==2.3.0
Werkzeug==3.1.3
```

You can install these dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory of the project and add your application token:

```
APPLICATION_TOKEN=<YOUR_APPLICATION_TOKEN>
```

## Running the Application

To run the application locally, use the following command:

```bash
python app.py
```

The application will be available at `http://0.0.0.0:5000`.

## API Endpoint

### `/call_function`

- **Method:** POST
- **Description:** Sends a question to the chat bot and returns the response.
- **Request Body:** JSON object containing the question.
  ```json
  {
    "question": "Your question here"
  }
  ```
- **Response:** JSON object containing the result.
  ```json
  {
    "result": "Chat bot response"
  }
  ```

## Deployment

To deploy the application using Gunicorn, use the following command:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

This will start the application with 4 worker processes.

## License

This project is licensed under the MIT License.
```
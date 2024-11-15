from flask import Flask, render_template_string
from datetime import datetime
import pytz
import os

app = Flask(__name__)
VISITS_FILE = "visits.txt"

def get_visit_count():
    try:
        with open(VISITS_FILE, "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0

def increment_visit_count():
    count = get_visit_count() + 1
    with open(VISITS_FILE, "w") as file:
        file.write(str(count))
    return count

@app.route('/')
def show_moscow_time():
    # Get the current time in Moscow
    moscow_time_zone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_time_zone).strftime("%Y-%m-%d %H:%M:%S")
    
    visit_count = increment_visit_count()

    # Define HTML template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Time in Moscow</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
            }
            .time-container {
                text-align: center;
            }
            h1 {
                font-size: 2rem;
                color: #333;
            }
            img {
                max-width: 600px;
                height: auto;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="time-container">
            <img src="{{ url_for('static', filename='moscow.jpg') }}"
                alt="Picture of Moscow">
            <h1>Current Time in Moscow:</h1>
            <p>{{ moscow_time }}</p>
            <p>This page has been visited {{ visit_count }} times.</p>
        </div>
    </body>
    <link rel="icon"
        type="image/x-icon"
        href="{{ url_for('static', filename='favicon.ico') }}">
    </html>
    """

    return render_template_string(html_template, moscow_time=moscow_time, visit_count=visit_count)

@app.route('/visits')
def visits():
    count = get_visit_count()
    return f"Total visits: {count}"

if __name__ == '__main__':
    app.run(debug=True)

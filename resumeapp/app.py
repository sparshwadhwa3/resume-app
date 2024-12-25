# resume.py
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    resume = {
        "name": "Sparsh Wadhwa",
        "email": "sparshwadhwa@example.com",
        "phone": "(123) 456-7890",
        "education": "B.Sc. in Computer Science",
        "skills": ["Python", "Django", "Docker", "Azure", "Kubernetes"],
        "experience": [
            {"title": "Software Engineer", "company": "XYZ Corp", "years": "2020-2023"},
            {"title": "Junior Developer", "company": "ABC Ltd", "years": "2018-2020"}
        ]
    }

    html_template = """
    <html>
    <head><title>Resume</title></head>
    <body>
        <h1>{{ resume['name'] }}</h1>
        <p>Email: {{ resume['email'] }}</p>
        <p>Phone: {{ resume['phone'] }}</p>
        <h2>Education</h2>
        <p>{{ resume['education'] }}</p>
        <h2>Skills</h2>
        <ul>
            {% for skill in resume['skills'] %}
                <li>{{ skill }}</li>
            {% endfor %}
        </ul>
        <h2>Experience</h2>
        <ul>
            {% for job in resume['experience'] %}
                <li>{{ job['title'] }} at {{ job['company'] }} ({{ job['years'] }})</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    
    return render_template_string(html_template, resume=resume)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)


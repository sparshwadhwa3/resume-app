# resume.py
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    resume = {
        "name": "Sparsh Wadhwa",
        "email": "sparshwadhwadevops@gmail.com",
        "phone": "+91-8928699025",
        "summary": """
        Around 6.5 years of IT experience with expertise in AWS, Azure, DevOps, Azure-DevOps, Linux and Shell Scripting.
        """,
        "certifications": [
            "AWS Certified Solutions Architect Associate",
            "Azure Certified DevOps Engineer",
            "Red Hat Certified Engineer"
        ],
        "skills": {
            "Cloud Platforms": "AWS, Azure",
            "DevOps Tools": "Git, Jenkins, Docker, Dockerhub, Ansible, Kubernetes, Terraform, ArgoCD, Prometheus, Grafana",
            "Scripting": "Bash Shell Scripting",
            "Operating Systems": "Linux (Configuration, Troubleshooting, and Administration)"
        },
        "experience": [
            {
                "title": "DevOps Engineer",
                "company": "ISO New England",
                "years": "May 2021 – Present",
                "responsibilities": [
                    "Implemented CI/CD solution using Azure DevOps (AzureRepo, AzurePipeline, ACR, SelfHosted Agent, AKS, ArgoCD).",
                    "Implemented CI/CD pipelines with GitHub, Jenkins, Docker, ECR, EKS, ArgoCD, Prometheus, Grafana.",
                    "Automated deployments to EKS using GitOps and ArgoCD, enhancing rollback capabilities.",
                    "Integrated Prometheus and Grafana for Kubernetes (EKS) performance monitoring and dashboarding.",
                    "Implemented MLOps solution using AWS services (CodeCommit, CodeBuild, Lambda, EMR, S3, SNS, CloudWatch, KedroPipeline).",
                ]
            },
            {
                "title": "System Engineer",
                "company": "ISO New England",
                "years": "June 2018 – April 2021",
                "responsibilities": [
                    "Built and maintained Linux-based systems in AWS cloud environments.",
                    "Configured servers with Ansible, managed IAM roles, users, and security groups.",
                    "Monitored EC2, S3, EBS, and CloudWatch for system health, alarms, and metrics.",
                    "Automated system maintenance with cron jobs, OS hardening, and patching."
                ]
            }
        ],
        "education": "Bachelor of Engineering, First Class – Mumbai University",
    }

    html_template = """
    <html>
    <head>
        <title>Resume</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #ff6f61, #6a11cb);
                color: #333;
                margin: 0;
                padding: 0;
                height: 100vh;
            }

            .container {
                max-width: 900px;
                margin: 0 auto;
                padding: 30px;
                background-color: #fff;
                box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
                border-radius: 8px;
                margin-top: 40px;
                border-top: 10px solid #3498db;
            }

            h1 {
                text-align: center;
                font-size: 2.5em;
                color: #3498db;
                margin-bottom: 0;
                text-transform: uppercase;
            }

            p.contact-info {
                text-align: center;
                font-size: 1.1em;
                font-weight: bold;
                color: #555;
                margin-bottom: 20px;
            }

            p.contact-info span {
                display: inline-block;
                margin-right: 20px;
            }

            .section {
                margin-bottom: 30px;
            }

            .section-title {
                background-color: #3498db;
                color: #fff;
                padding: 10px;
                font-size: 1.2em;
                border-radius: 5px;
                text-align: center;
            }

            .section-content {
                padding: 15px;
                background-color: #f9f9f9;
                border-radius: 5px;
                margin-top: 10px;
                box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
            }

            ul {
                padding: 0;
                list-style-type: none;
            }

            li {
                margin-bottom: 10px;
                font-size: 1.1em;
            }

            .skill-list {
                display: flex;
                flex-wrap: wrap;
                gap: 15px;
                margin-top: 15px;
            }

            .skill-item {
                background-color: #ecf0f1;
                padding: 8px 20px;
                border-radius: 25px;
                font-size: 1.1em;
                transition: background-color 0.3s ease;
            }

            .skill-item:hover {
                background-color: #3498db;
                color: white;
            }

            .experience-title {
                font-weight: bold;
                font-size: 1.3em;
                color: #3498db;
            }

            .responsibilities {
                margin-left: 20px;
            }

            footer {
                text-align: center;
                margin-top: 40px;
                font-size: 1.2em;
                color: #555;
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }

            @media (max-width: 768px) {
                .container {
                    padding: 20px;
                }

                h1 {
                    font-size: 2em;
                }

                .section-title {
                    font-size: 1.1em;
                }

                .section-content {
                    padding: 10px;
                }
            }

        </style>
    </head>
    <body>
        <div class="container">
            <h1>{{ resume['name'] }}</h1>
            <p class="contact-info">
                <span>Email: {{ resume['email'] }}</span>
                <span>Phone: {{ resume['phone'] }}</span>
            </p>

            <div class="section">
                <h2 class="section-title">Summary</h2>
                <div class="section-content">
                    <p>{{ resume['summary'] }}</p>
                </div>
            </div>

            <div class="section">
                <h2 class="section-title">Certifications</h2>
                <div class="section-content">
                    <ul>
                        {% for certification in resume['certifications'] %}
                            <li>{{ certification }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>

            <div class="section">
                <h2 class="section-title">Technical Skills</h2>
                <div class="section-content">
                    <div class="skill-list">
                        <div class="skill-item"><strong>Cloud Platforms:</strong> {{ resume['skills']['Cloud Platforms'] }}</div>
                        <div class="skill-item"><strong>DevOps Tools:</strong> {{ resume['skills']['DevOps Tools'] }}</div>
                        <div class="skill-item"><strong>Scripting:</strong> {{ resume['skills']['Scripting'] }}</div>
                        <div class="skill-item"><strong>Operating Systems:</strong> {{ resume['skills']['Operating Systems'] }}</div>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2 class="section-title">Experience</h2>
                <div class="section-content">
                    {% for job in resume['experience'] %}
                        <h3 class="experience-title">{{ job['title'] }} at {{ job['company'] }} ({{ job['years'] }})</h3>
                        <ul class="responsibilities">
                            {% for responsibility in job['responsibilities'] %}
                                <li>{{ responsibility }}</li>
                            {% endfor %}
                        </ul>
                    {% endfor %}
                </div>
            </div>

            <div class="section">
                <h2 class="section-title">Education</h2>
                <div class="section-content">
                    <p>{{ resume['education'] }}</p>
                </div>
            </div>
        </div>

        <footer>
            <p>&copy; 2024 Sparsh Wadhwa</p>
        </footer>
    </body>
    </html>
    """

    return render_template_string(html_template, resume=resume)

# Health check route for readiness and liveness probes
@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)


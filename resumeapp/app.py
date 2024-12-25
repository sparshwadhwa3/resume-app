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
                "company": "Ekaggata Technologies",
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
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
            h1, h2, h3 { margin-bottom: 5px; color: #2c3e50; }
            p, ul { margin-top: 5px; margin-bottom: 15px; }
            ul { list-style-type: none; padding: 0; }
            li { margin-bottom: 8px; }
            .container { max-width: 900px; margin: 0 auto; padding: 10px; }
            .section { margin-bottom: 30px; }
            .section-title { background-color: #3498db; color: #fff; padding: 8px; text-align: center; }
            .contact-info { font-weight: bold; }
            .responsibilities { margin-left: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{{ resume['name'] }}</h1>
            <p class="contact-info">Email: {{ resume['email'] }} | Phone: {{ resume['phone'] }}</p>

            <div class="section">
                <h2 class="section-title">Summary</h2>
                <p>{{ resume['summary'] }}</p>
            </div>

            <div class="section">
                <h2 class="section-title">Certifications</h2>
                <ul>
                    {% for certification in resume['certifications'] %}
                        <li>{{ certification }}</li>
                    {% endfor %}
                </ul>
            </div>

            <div class="section">
                <h2 class="section-title">Technical Skills</h2>
                <h3>Cloud Platforms</h3>
                <p>{{ resume['skills']['Cloud Platforms'] }}</p>
                <h3>DevOps Tools</h3>
                <p>{{ resume['skills']['DevOps Tools'] }}</p>
                <h3>Languages</h3>
                <p>{{ resume['skills']['Languages'] }}</p>
                <h3>Operating Systems</h3>
                <p>{{ resume['skills']['Operating Systems'] }}</p>
            </div>

            <div class="section">
                <h2 class="section-title">Experience</h2>
                {% for job in resume['experience'] %}
                    <h3>{{ job['title'] }} at {{ job['company'] }} ({{ job['years'] }})</h3>
                    <ul class="responsibilities">
                        {% for responsibility in job['responsibilities'] %}
                            <li>{{ responsibility }}</li>
                        {% endfor %}
                    </ul>
                {% endfor %}
            </div>

            <div class="section">
                <h2 class="section-title">Education</h2>
                <p>{{ resume['education'] }}</p>
            </div>
        </div>
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


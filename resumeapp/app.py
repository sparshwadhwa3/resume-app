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
        Around 6.5 years of IT experience with expertise in AWS, Azure, DevOps, Azure-DevOps, Linux, Shell Scripting, MLOps, and Python.
        """,
        "certifications": [
            "AWS Certified Solutions Architect Associate",
            "Azure Certified DevOps Engineer",
            "Azure Certified Data Engineer",
            "Azure Certified AI Engineer",
            "Red Hat Certified Engineer"
        ],
        "technical_skills": {
            "Cloud Platforms": ["AWS", "Azure"],
            "DevOps Tools": ["Git", "Jenkins", "Docker", "Dockerhub", "Ansible", "Kubernetes", "Terraform", "ArgoCD", "Prometheus", "Grafana", "Loki"],
            "AWS Services": [
                "CloudFormation", "CodeCommit", "CodeBuild", "ECR", "CodeDeploy", "CodePipeline", "EMR", "Sagemaker", "IAM", "S3", "EC2", "EBS", 
                "EFS", "CloudFront", "Route 53", "CloudWatch", "ELB", "Auto Scaling", "VPC", "Bastion Hosts", "VPC Endpoints", "NAT Gateway", "Lambda", "RDS", "SNS"
            ],
            "Azure Services": [
                "Azure Repo", "Pipelines", "Artifacts", "Virtual Machines", "App Services", "Azure Functions", "Container Instances", "Container Registry", "Azure Kubernetes Service (AKS)"
            ],
            "Languages": ["Bash Shell Scripting", "Python"],
            "Operating Systems": ["Linux (Configuration, Troubleshooting, and Administration)"]
        },
        "experience": [
            {
                "title": "Sr. DevOps Engineer",
                "company": "Ekaggata Technologies",
                "years": "May 2021 – Present",
                "responsibilities": [
                    "Implemented MLOps solution using AWS services such as CodeCommit, CodeBuild, Lambda, EMR, S3, SNS, CloudWatch, KedroPipeline, and Sagemaker.",
                    "Implemented CI/CD pipelines using GitHub, Jenkins, Docker, ECR, EKS, ArgoCD, Prometheus, Grafana, and Loki.",
                    "Automated deployment processes to EKS using ArgoCD, implementing GitOps practices for seamless application delivery and rollback.",
                    "Utilized Prometheus for performance and resource monitoring in Kubernetes (EKS) and integrated Grafana for real-time dashboards and alerting.",
                    "Implemented Loki for centralized log aggregation, improving application observability and troubleshooting."
                ]
            },
            {
                "title": "System Engineer",
                "company": "Ekaggata Technologies",
                "years": "June 2018 – April 2021",
                "responsibilities": [
                    "Built and maintained Linux-based systems in AWS cloud environments using EC2, S3, EBS, and VPC.",
                    "Configured servers using Ansible and managed users, groups, roles, and security groups using IAM.",
                    "Performed OS hardening, patching, and scheduled cron jobs for system maintenance.",
                    "Managed AWS services including EC2, S3, EFS, and CloudWatch for monitoring, alarms, and notifications."
                ]
            }
        ],
        "education": "Bachelor of Engineering, First Class – Mumbai University",
        "personal_skills": [
            "Excellent troubleshooting and problem-solving skills.",
            "Self-motivated and disciplined, with a strong work ethic.",
            "Good team player with the ability to work in fast-paced environments.",
            "Passionate about continuous learning and professional growth."
        ]
    }

    html_template = """
    <html>
    <head><title>Resume</title></head>
    <body>
        <h1>{{ resume['name'] }}</h1>
        <p>Email: {{ resume['email'] }}</p>
        <p>Phone: {{ resume['phone'] }}</p>
        
        <h2>Summary</h2>
        <p>{{ resume['summary'] }}</p>
        
        <h2>Professional Certifications</h2>
        <ul>
            {% for certification in resume['certifications'] %}
                <li>{{ certification }}</li>
            {% endfor %}
        </ul>

        <h2>Technical Skills</h2>
        <h3>Cloud Platforms</h3>
        <ul>
            {% for platform in resume['technical_skills']['Cloud Platforms'] %}
                <li>{{ platform }}</li>
            {% endfor %}
        </ul>
        
        <h3>DevOps Tools</h3>
        <ul>
            {% for tool in resume['technical_skills']['DevOps Tools'] %}
                <li>{{ tool }}</li>
            {% endfor %}
        </ul>
        
        <h3>AWS Services</h3>
        <ul>
            {% for service in resume['technical_skills']['AWS Services'] %}
                <li>{{ service }}</li>
            {% endfor %}
        </ul>
        
        <h3>Azure Services</h3>
        <ul>
            {% for service in resume['technical_skills']['Azure Services'] %}
                <li>{{ service }}</li>
            {% endfor %}
        </ul>
        
        <h3>Languages</h3>
        <ul>
            {% for language in resume['technical_skills']['Languages'] %}
                <li>{{ language }}</li>
            {% endfor %}
        </ul>
        
        <h3>Operating Systems</h3>
        <ul>
            {% for os in resume['technical_skills']['Operating Systems'] %}
                <li>{{ os }}</li>
            {% endfor %}
        </ul>

        <h2>Experience</h2>
        {% for job in resume['experience'] %}
            <h3>{{ job['title'] }} at {{ job['company'] }} ({{ job['years'] }})</h3>
            <ul>
                {% for responsibility in job['responsibilities'] %}
                    <li>{{ responsibility }}</li>
                {% endfor %}
            </ul>
        {% endfor %}
        
        <h2>Education</h2>
        <p>{{ resume['education'] }}</p>

        <h2>Personal Skills</h2>
        <ul>
            {% for skill in resume['personal_skills'] %}
                <li>{{ skill }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """

    return render_template_string(html_template, resume=resume)

# Health check route for readiness and liveness probes
@app.route("/health")
def health():
    # This is a simple check, returning a 200 OK response
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)


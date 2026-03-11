# DevOps Project: Deploy a Flask Application to Azure Linux VM with Terraform

This project demonstrates how to deploy a simple web application to an Azure Linux Virtual Machine using Terraform, Git, and GitHub.

The goal of this project is to simulate a real-world DevOps workflow including:

- Infrastructure provisioning using Terraform
- Source control using Git and GitHub
- Application deployment on a Linux server
- Remote management using SSH
- Running the application as a Linux service

---

# Architecture

Windows 11 Machine  
→ Visual Studio Code  
→ Git / GitHub  
→ Terraform  

Azure Cloud  
→ Resource Group  
→ Virtual Network  
→ Subnet  
→ Network Security Group  
→ Public IP  
→ Linux Virtual Machine  

Linux VM  
→ Python Flask Application  
→ systemd service

---

# Technologies Used

- Azure
- Terraform
- Linux (Ubuntu)
- Git
- GitHub
- Python
- Flask
- SSH
- Visual Studio Code

---

# Project Architecture

User Browser
↓
Azure Public IP
↓
Azure Linux VM
↓
Flask Application (Port 5000)


---

# Step 1: Clone Repository

git clone https:https://github.com/tevinbisuali/azure-flask-devops-project.git

cd azure-flask-devops-project

# Step 2: Login to Azure

Navigate to the Terraform folder:

cd terraform

terraform init

# Step 4: Review Terraform Plan

terraform plan

# Step 5: Deploy Infrastructure

terraform apply

Type **yes** when prompted.

This will create:

- Resource Group
- Virtual Network
- Subnet
- Network Security Group
- Public IP
- Linux Virtual Machine

---

# Step 6: Connect to the Linux VM

After Terraform finishes, it will output the public IP.

Connect using SSH:

ssh azureuser@PUBLIC_IP

# Step 7: Install Dependencies on the VM

Update packages:

sudo apt update

Install required software:

sudo apt install -y git python3 python3-pip python3-venv

# Step 8: Clone Application Repository

git clone https:https://github.com/tevinbisuali/azure-flask-devops-project.git

cd azure-flask-devops-project.git/app

# Step 9: Create Python Virtual Environment

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# Step 10: Run the Application

python app.py

The application will run on:

http://PUBLIC_IP:5000

# Step 11: Run the App as a Linux Service

Create service file:

sudo nano /etc/systemd/system/flaskapp.service

Add the following configuration:

[Unit]
Description=Flask App
After=network.target

[Service]
User=azureuser
WorkingDirectory=/home/azureuser/azure-terraform-linux-devops-project/app
ExecStart=/home/azureuser/azure-terraform-linux-devops-project/app/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target

Save and exit

Reload systemd:

sudo systemctl daemon-reload

Enable the service:

sudo systemctl enable flaskapp

Start the service:

sudo systemctl start flaskapp

Check status:

sudo systemctl status flaskapp

# Application Output

Open in browser:

http://PUBLIC_IP:5000

Expected output:

Hello from Azure Linux VM!

# Destroy Infrastructure (Important)

To avoid Azure charges:

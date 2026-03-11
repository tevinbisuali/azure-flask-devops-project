from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Azure Linux VM! This app was deployed using Terraform, GitHub, and Linux."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
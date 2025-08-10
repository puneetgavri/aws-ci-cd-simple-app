from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, AWS DEVOPS DEMO!'

if __name__ == '__main__':
    # Bind to all network interfaces inside the container
    app.run(host='0.0.0.0', port=5000)

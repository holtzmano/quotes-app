from flask import Flask
from backend.routes.quotes import quotes_bp

app = Flask(__name__)
app.register_blueprint(quotes_bp)

if __name__ == "__main__":
    app.run(port=5000)

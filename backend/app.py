from flask import Flask
from routes.quest_routes import quest_blueprint
from utils.security import secure_headers

app = Flask(__name__)

# Apply security headers
@app.after_request
def apply_security_headers(response):
    secure_headers(response)
    return response

# Register blueprints
app.register_blueprint(quest_blueprint, url_prefix='/quests')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


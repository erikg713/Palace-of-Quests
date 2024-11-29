# Entry point for the application
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
import sys
sys.path.insert(0, '/home/Dev713/PalaceOfQuests')

from app import app as application  # Replace 'app' with your Flask app file name.

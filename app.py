# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class ...oloo
app = Flask(__name__)  # '__name__' is the name of the current module

# Define a route for the home page ('/')
@app.route('/')
def hello_world():
    """This function returns a simple 'Hello, World!' message."""
    return 'Hello, World!'

# Run the Flask app when the script is executed directly
if __name__ == '__main__':
    app.run()  # Start the development server with debugging enabled
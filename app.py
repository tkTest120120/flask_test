from flask import Flask, jsonify


app = Flask(__name__)

@app.get("/")
def home():
    return "API is working fine"

# if __name__ == "__main__":
#     app.run()
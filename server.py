
"""Flask server to detect emotions."""

from flask import Flask, jsonify, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def root():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Detect emotions from the supplied text."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return jsonify({"error": "Please enter a text to analyze."}), 400

    response = emotion_detector(text_to_analyze)

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

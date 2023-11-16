import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_texts = [item['text'] for item in transcript_list]
        return jsonify(transcript_texts)
    except TranscriptsDisabled:
        return jsonify({"error": "Transcripts are disabled for this video"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

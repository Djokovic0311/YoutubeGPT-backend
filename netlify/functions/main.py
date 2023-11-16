from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

app = Flask(__name__)


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
    app.run(host='', port=8000)
# netlify/functions/get_transcript.py

from youtube_transcript_api import YouTubeTranscriptApi

def handler(event, context):
    video_id = event['queryStringParameters']['video_id']
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_texts = [item['text'] for item in transcript_list]
        return {
            'statusCode': 200,
            'body': transcript_texts
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

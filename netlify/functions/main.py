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

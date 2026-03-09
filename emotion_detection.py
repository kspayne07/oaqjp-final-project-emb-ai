import requests
import json

def emotion_detector(text_to_analyze):

    # call api endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    json_response = json.loads(response.text)
    emotions = json_response['emotionPredictions'][0]['emotion']

    # find dominant emotion
    dominant_emotion = ''
    m = 0.0
    for emotion, value in emotions.items():
        if value > m:
            m = value
            dominant_emotion = emotion

    emotions['dominant_emotion'] = dominant_emotion

    return emotions 
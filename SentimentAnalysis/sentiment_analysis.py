import requests
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

authenticator = IAMAuthenticator('b2GhucMwzU7Pp131eLvW2ZvvH3VF-ZwgA4VHzCGCQs7G')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/1cd88e19-aef4-4606-b7fc-abdfad735206')

def sentiment_analyzer(text_to_analyse): # POST request
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = natural_language_understanding.analyze(
        url = 'https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/1cd88e19-aef4-4606-b7fc-abdfad735206',
        json = myobj, headers=header, features=Features(sentiment=SentimentOptions(model='bert'))).get_result()
    formatted_response = json.loads(response.text) # convert text into a dictionary
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {'label': label, 'score': score}
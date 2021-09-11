import os
import dialogflow
from google.api_core.exceptions import InvalidArgument


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/shunkingsiu/Desktop/djangochatbot/reactpageagent-rehl-e8f6c376b8ef.json'
DIALOGFLOW_PROJECT_ID = 'reactpageagent-rehl'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'hi'

#text_to_be_analyzed = "hi"

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
#text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)

def get_input(text_to_be_analyzed="hi"):
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input) # dialogflow database

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        #print(response)
    except InvalidArgument as e:
        print(e)
        raise
    return response

def get_output(response):
    print("input text:", response.query_result.query_text)
    print("intent:", response.query_result.intent.display_name)
    print("intent's confidence:", response.query_result.intent_detection_confidence)
    print("response:", response.query_result.fulfillment_text)


while True:
    response = get_input(input("Say something to the chat bot:"))
    get_output(response)

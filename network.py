import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/shunkingsiu/Desktop/djangochatbot/reactpageagent-rehl-e8f6c376b8ef.json'
DIALOGFLOW_PROJECT_ID = 'reactpageagent-rehl'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'hi'  

text_to_be_analyzed = "bye"

session_client = dialogflow.SessionsClient()
print("line 13")
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
print("line 15")
text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
print("line 17")
query_input = dialogflow.types.QueryInput(text=text_input)
print("line 19")

try:
    response = session_client.detect_intent(session=session, query_input=query_input)
    #print(response)
except InvalidArgument as e:
    print(e)
    raise

print(response)

print("輸入文字:", response.query_result.query_text)
print("得到的 intent:", response.query_result.intent.display_name)
print("偵測到 intent 的 confidence:", response.query_result.intent_detection_confidence)
print("回應的話:", response.query_result.fulfillment_text)
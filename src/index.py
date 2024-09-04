
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import WATSON_ASSISTANT_API_KEY, WATSON_ASSISTANT_URL

def setup_assistant():
    authenticator = IAMAuthenticator(WATSON_ASSISTANT_API_KEY)
    assistant = AssistantV2(
        version='2021-06-14',
        authenticator=authenticator
    )
    assistant.set_service_url(WATSON_ASSISTANT_URL)
    return assistant

if __name__ == "__main__":
    assistant = setup_assistant()
    print("Assistant setup complete.")

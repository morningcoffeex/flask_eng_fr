import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']



# Set some variables for the translator


MODEL_TO_ENGLISH = 'fr-en'
MODEL_TO_FRENCH = 'en-fr'


# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# Translate to french
def english_to_french(english_text):
    french_text = language_translator.translate(
    text=english_text,
    model_id=MODEL_TO_FRENCH).get_result()
    return french_text['translations'][0]['translation']

    # Translate to english
def french_to_english(french_text):
    english_text = language_translator.translate(
    text=french_text,
    model_id=MODEL_TO_ENGLISH).get_result()
    return english_text['translations'][0]['translation']

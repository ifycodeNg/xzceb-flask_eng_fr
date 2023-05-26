"""
This modules trnaslates text to vaious languages
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()


APIKEY = os.environ['apikey']
URL = os.environ['url']


authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    #write the code here
    """
    Translates engilsh to french
    """
    if english_text is None:
        return False
    if len(english_text) < 1:
        return False
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return translation["translations"][0]["translation"]

def french_to_english(french_text):
    #write the code here
    """
    Translates french to english
    """
    if french_text is None:
        return False
    if len(french_text) < 1:
        return False
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return translation["translations"][0]["translation"]

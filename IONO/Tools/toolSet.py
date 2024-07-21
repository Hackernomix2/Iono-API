import os
from dotenv import load_dotenv
import google.generativeai as gemini_embedder
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


load_dotenv() #loading the .env file
GOOGLE_API_KEY = os.getenv('GEMNI_API_KEY') 


#this is a method that makes embeddings/the vectors 
#we call this when we save the models
def embed(object):
    result = (gemini_embedder.embed_content(
        model="models/embedding-001",
        content= object,
        task_type="retrieval_document",))
    
    return result['embedding']

############################################################################################################
'''
below are the methods that we will use to interact with google sheets

walk throgh of usage
1. start_service()
2. read_sheet_data(service, spreadsheet_id, range_name)
3. do something with the data

'''


CLIENT_SECRETS_PATH = os.getenv('CLIENT_SECRETS_PATH')
TOKEN_PATH = os.getenv('TOKEN_PATH')
SCOPES = os.getenv('SCOPES').split(',')


def authenticate_google():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for future use
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    
    return creds


def build_service(creds):
    try:
        service = build('sheets', 'v4', credentials=creds)
        return service
    except HttpError as err:
        print(err)
        return None

def read_sheet_data(service, spreadsheet_id, range_name):
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return []

        return values
    except HttpError as err:
        print(err)
        return []

    
def start_service():
    creds = authenticate_google()
    service = build_service(creds)
    return service




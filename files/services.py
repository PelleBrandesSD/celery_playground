import time
from typing import Any

import requests

    

    
def call_callback(*, result: dict, callback_url: str, callback_data: dict[str, Any] = {}) -> dict:
    callback_payload = {
        'status': 'success',
        'result': result,
        'callback_data': callback_data
    }
    
    # call the callback url
    response = requests.post(callback_url, json=callback_payload)
    return response.json()

def transcribe(*, audio_url: str):
    # download the audio
    audio = download_audio(audio_url=audio_url)
    # check that the audio is not empty
    if not audio:
        raise ValueError("Audio is empty")
    
    time.sleep(4)
    
    return "transcription: lorem ipsum"
    

def summarize(*, text: str):
    time.sleep(2)
    return f"summary of lorem ipsum. original text: {text}" 

def download_audio(*, audio_url: str) -> bytes:
    return b"lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit voluptate velit esse cillum dolore fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim id est laborum"
    
    
def upload_audio(*, audio_url: str, audio: bytes) -> str:
    pass
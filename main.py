# Import necessary modules
from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

# Create a FastAPI instance
app = FastAPI()

# Pydantic model to accept text input
class TextInput(BaseModel):
    text: str

# Function to generate SHA-256 checksum from input text
def generate(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

# Root endpoint with a welcome message
@app.get("/")
def welcome():
    return {"message": "Welcome to the Token Generator API! - Created by Manali"}

# POST endpoint to generate checksum from given text
@app.post("/generate-checksum")
def generate_checksum(data: TextInput):
    """
    This endpoint receives a JSON object with a 'text' field and returns
    the SHA-256 checksum of the text.
    """
    checksum = generate(data.text)
    return {"checksum": checksum}

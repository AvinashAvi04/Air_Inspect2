import PIL.Image

# img = PIL.Image.open('image.jpg')

import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
import random
def generate_gemini_response(img):
    print("into gemini")
    while True:
        load_dotenv()  # Load environment variables from .env file
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        print(gemini_api_key)
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-pro-vision')
        prompt="""You are an expert Aircraft safety technichian.You are provided with an image of an component of a aircraft. Perform a faulty wiring detection.
        Return the response as a JSON ub=nder the following format. Just send JSON and nothing else.The format is as follows {'Fault_Detected':true/false,'Component_Name':....,'Fault':....,'Description':...}
        Always return some content in the fields above.
        """
        
        response = model.generate_content([prompt,img])
        try:
            response_dict = json.loads(response.text)
            print(response_dict)
            return response_dict
        except Exception as e:
            print("Error:", e)
            continue



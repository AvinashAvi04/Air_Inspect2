import PIL.Image

# img = PIL.Image.open('image.jpg')

import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
import random
def generate_gemini_response(img):
    # print("into gemini")
    # while True:
    #     load_dotenv()  # Load environment variables from .env file
    #     gemini_api_key = os.getenv("GEMINI_API_KEY")
    #     print(gemini_api_key)
    #     genai.configure(api_key=gemini_api_key)
    #     model = genai.GenerativeModel('gemini-pro-vision')
    #     prompt="""You are an expert Aircraft safety technichian.You are provided with an image of an component of a aircraft. Perform a faulty wiring detection.
    #     Return the response as a JSON ub=nder the following format. Just send JSON and nothing else.The format is as follows {'Fault_Detected':true/false,'Component_Name':....,'Fault':....,'Description':...}
    #     Always return some content in the fields above.
    #     """
        
    #     response = model.generate_content([prompt,img])
    #     try:
    #         response_dict = json.loads(response.text)
    #         print(response_dict)
    #         return response_dict
    #     except Exception as e:
    #         print("Error:", e)
    #         continue


# Set up weighted choices for fault detection
    fault_detected_choices = [True, False]
    fault_detected_weights = [0.7, 0.3]

    # Set up weighted choices for component names
    component_names = ["Router", "Controller", "Communication"]
    component_weights = [0.5, 0.3, 0.2]

    # Faults and descriptions for each component type
    component_faults = {
        "Router": [
            ("IP Conflict", "Two devices are assigned the same IP address."),
            ("No Internet", "Router is not connected to the internet."),
            ("Slow Connectivity", "Router connectivity is slower than usual.")
        ],
        "Controller": [
            ("Overheating", "Controller temperature exceeds safe operating limits."),
            ("Firmware Bug", "Controller firmware contains a critical bug affecting operations."),
            ("Power Failure", "Controller is not receiving power due to a faulty power supply.")
        ],
        "Communication": [
            ("Signal Loss", "Intermittent signal loss observed."),
            ("Hardware Failure", "Communication hardware has failed and needs replacement."),
            ("Encryption Error", "Encryption protocols are not functioning correctly.")
        ]
    }

    # Choose whether a fault is detected
    fault_detected = random.choices(fault_detected_choices, fault_detected_weights)[0]
    
    if fault_detected:
        # Choose the component name
        component_name = random.choices(component_names, component_weights)[0]
        
        # Choose fault and description based on the component
        fault, description = random.choice(component_faults[component_name])
    else:
        # If no fault is detected, set other fields to None
        component_name, fault, description = None, None, None
    
    return {
        'Fault_Detected': fault_detected,
        'Component_Name': component_name,
        'Fault': fault,
        'Description': description
    }


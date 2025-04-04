import subprocess

from openai import OpenAI

import time

API_KEY = "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"


def generate_response(user_input):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY,
    )
    
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": 
'''You are a command-line assistant. Your only task is to generate valid and executable command-line commands for Windows or Ubuntu.  
When I ask for a command, you should return *only* the command without any explanation, formatting, or extra text.  

For example:  
🟢 *User Input:* Open Task Manager  
✅ *Response:* taskmgr  

🟢 *User Input:* List all files in the current directory (Ubuntu)  
✅ *Response:* ls  

🟢 *User Input:* Search "AI in India" on Google (Windows)  
✅ *Response:* start "" "https://www.google.com/search?q=AI+in+India"  

🟢 *User Input:* Show network configuration (Ubuntu)  
✅ *Response:* ifconfig  

Return *only* the command. No explanations, no extra text.  
If multiple commands exist, return the most common one.  
If OS-specific, assume Windows unless I specify otherwise.
'''},
            {"role": "user", "content": user_input}
        ]
    )  
    
    response = completion.choices[0].message.content
    print(response)
    return response
def run_command(command):
    """Runs a command and prints output/errors if any."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()

    if output:
        print("OUTPUT:\n", output)
    if error:
        print("ERROR:\n", error)
        
        
        
run_command(generate_response("google search about ai"))   


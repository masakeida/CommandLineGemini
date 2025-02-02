#!/usr/bin/env python
import os
import sys
import google.generativeai as genai

def main():
    input = []
    for line in sys.stdin:
        input.append(line)

    # Set Google API Key
    GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
    genai.configure(api_key=GOOGLE_API_KEY)

    # Use gemini-2.0-flash model
    gemini_flash = genai.GenerativeModel("gemini-2.0-flash-exp")
    prompt = ''.join(input)
    response = gemini_flash.generate_content(prompt)
    print('----- From Gemini 2.0 Flash -----')
    print(response.text)


if __name__ == "__main__":
    main()

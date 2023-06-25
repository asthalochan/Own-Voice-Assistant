from output_audio import *
import openai
import speech_recognition as sr

listner = sr.Recognizer()

wlc= audio_out("hello , Welcome to Aastthaa AI ")
openai.api_key = "*********************************"

print("-: Welcome to Astha's AI:- ")
while True:
    with sr.Microphone() as source:
        print("speak now ......")
        voice = listner.listen(source)
        prompt= listner.recognize_google(voice)
    
    model_engine = "text-davinci-003"
    
    if 'exit' in prompt or 'quit' in prompt:
        break

    
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    
    
    print(response)
    res=audio_out(response)
  
    print("\n")
    

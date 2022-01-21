def predict_audio(audio):
	import speech_recognition as sr
	r = sr.Recognizer()
	try:
#		print("Recognizing...")    
		query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
#		print(f"User said: {query}\n")  #User query will be printed.

	except Exception as e:
        # print(e)    
		print("Say that again please...")   #Say that again will be printed in case of improper voice 
		return "None" #None string will be returned
	print(query)
	return query



morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '
}
import speech_recognition as sr 


r = sr.Recognizer()


with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

    try:
       
        said = r.recognize_google(audio)
        print("You said:", said)
    except Exception as e:
        print("Error recognizing speech:", str(e))

def text_to_morse_code(text):
    
    text = text.upper()
    
    morse_code = []
    
    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(char)  
    return ' '.join(morse_code)


input_text = said
morse_code_result = text_to_morse_code(input_text)

print("Morse Code:")
print(morse_code_result)



from gpiozero import Buzzer 

from time import sleep

buzzer = Buzzer(17) 

for i in morse_code_result:
    if i == "-":
        buzzer.on()
        sleep(1.25)
        buzzer.off()
    if i == ".":
        buzzer.on()
        sleep(0.5)
        buzzer.off()
    if i == " ":
        sleep(1.5)
    sleep(0.5)

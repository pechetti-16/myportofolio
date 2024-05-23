import wikipedia
import pyttsx3
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('VOICE COMMAND')
root.resizable(False,False)
root.geometry("1000x500+250+150")
attributes=('Segoe UI Emoji',30,'bold')
frame=Frame(root,width=1000,height=500,bg='white')
frame.place(x=0,y=0)
voice=pyttsx3.init()
# Set the language of Wikipedia (optional, defaults to English)
wikipedia.set_lang("en")
l1=Label(frame,text='Topic',font=attributes,fg='black',bg='white')
l1.place(x=10,y=20)
e1=Entry(frame,fg='black',width=20)
e1.place(x=30,y=20)
e2=e1.get()

try:
    # Specify the Wikipedia page title
    page_title = e2.encode('utf-8')

    # Get the summary of the Wikipedia page
    page_summary = wikipedia.summary(page_title)

    # Print and use the summary
    print(f"Summary of '{page_title.decode()}':")
    print(page_summary)
    voice.say(page_summary)
    voice.runAndWait()

except wikipedia.exceptions.DisambiguationError as e:
    # Handle disambiguation error (suggesting titles)
    print("DisambiguationError: Please choose a more specific title:")
    print(e.options)
except wikipedia.exceptions.HTTPTimeoutError:
    # Handle HTTP timeout error
    print("Error: Wikipedia API request timed out. Please try again later.")
except wikipedia.exceptions.WikipediaException as e:
    # Handle other Wikipedia exceptions
    print(f"Error: {e}")

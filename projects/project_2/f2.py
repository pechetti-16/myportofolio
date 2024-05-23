import wikipedia
import pyttsx3

# Set the language of Wikipedia to Telugu
wikipedia.set_lang("en")

# Initialize text-to-speech engine
voice = pyttsx3.init()

try:
    # Specify the Wikipedia page title
    page_title = input("Enter the Wikipedia page title: ")

    # Get the summary of the Wikipedia page
    page_summary = wikipedia.summary(page_title)

    # Print the summary
    print(f"Summary of '{page_title}':")
    print(page_summary)

    # Set the voice language to Telugu
    voice.setProperty('rate', 100)  # You can adjust the speaking rate
    voice.setProperty('voice', 'te-in')  # Telugu (India) voice

    # Speak the Telugu text
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


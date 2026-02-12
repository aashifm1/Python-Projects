
# install pyspellchecker package --> pip install pyspellchecker
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
    
    def correct_text(self,text):
        words = text.split() # it will split the words
        corrected_words = []
        changed = False # the typed word is already correct

        for word in words:
            corrected_word = self.spell.correction(word)

            if corrected_word != word.lower():
                print(f"Correcting {word} to {corrected_word}")
                changed = True # the typed word is not already correct

            corrected_words.append(corrected_word) # it will store the corrected word
        
        if not changed:
            print("The text is already correct.")

        return ' '.join(corrected_words) # returns the value
    
    def runapp(self):
        print("\n =========== Spell Checker ===========")
        while True:
            text = input('Enter text to check (or type "terminate" to quit): ').strip().lower()
            possible_quit = self.spell.correction(text) # what if "termiante" word has spelling mistake

            if possible_quit == "terminate":
                confirm = input("Did you mean to terminate the program? (yes/no): ").strip().lower()

                if confirm == "yes":
                    print("Terminating the program...")
                    break
                else:
                    print("Continuing program...\n")
                    continue

            corrected_text = self.correct_text(text)
            print(f'Corrected text: {corrected_text}\n')

if __name__ == "__main__":
    SpellCheckerApp().runapp()
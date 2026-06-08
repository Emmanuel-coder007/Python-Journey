

    
def translator(language):
    translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'} }
    
    def translate_word(word):
        word = word.lower()  # Convert to lowercase for case-insensitive matching
        if language in translations:
            if word in translations[language]:
                return translations[language][word]
            else:
                return f"'{word}' not found in any supported languages."
        else:
            return f"Language '{language}' not supported."

    return translate_word

#Example usage
translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello')) # Output: hola

 
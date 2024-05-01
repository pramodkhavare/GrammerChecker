from textblob import TextBlob
from spellchecker import SpellChecker
# from gingerit.gingerit import GingerIt 
from grammarbot import GrammarBotClient


class CheckSpell:
    def __init__(self):
        pass 

    def correct_spelling(self ,sentance):
        spell = SpellChecker()
        words = sentance.split()
        corrected_words = []
        for word in words:
            if word not in spell:
                corrected_word = spell.correction(word=word)
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)
        correct_sentance = " ".join(corrected_words)


        return correct_sentance
    def correct_grammer(self,sentence):
        client = GrammarBotClient()

        result = client.check(sentence)

        if not result.matches:
            return sentence
        
        corrected_sentence = sentence 
        for match in result.matches:
            # Replace the incorrect text with the suggested correction
            corrected_sentence = corrected_sentence[:match.offset] + match.replacements[0]['value'] + corrected_sentence[match.offset + match.length:]

        return corrected_sentence


if __name__  == "__main__":
    obj = CheckSpell()
    message = "Hello world. I like mashine learning. appple. bananana"
    print(obj.correct_spelling(message))
    print(obj.correct_grammer(message))

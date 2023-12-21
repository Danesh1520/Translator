from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from googletrans import Translator
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import random

def home(request):
    return render(request, 'index.html')
def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
    return translated_text

'''def paraphrase_sentence(sentence):
    words = word_tokenize(sentence)
    paraphrased_words = []

    for word in words:
        synonyms = get_synonyms(word)
        if synonyms:
            paraphrased_words.append(random.choice(synonyms))
        else:
            paraphrased_words.append(word)

    paraphrased_sentence = ' '.join(paraphrased_words)
    return paraphrased_sentence

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def paraphrase(request):
    if request.method == 'POST':
        original_text = request.POST.get('paraphraseInput', '')
        paraphrased_text = paraphrase_sentence(original_text)
        return render(request, 'index.html', {'paraphrased_text': paraphrased_text})
    return render(request, 'index.html')'''


def translate(request):
    if request.method == 'POST':
        original_text = request.POST.get('translateInput', '')
        input_language = request.POST.get('input_language', '')  # Corrected variable name
        translator_language = request.POST.get('translator_language', '')  # Corrected variable name

        # Translate text using the correct language codes
        translated_text = translate_text(original_text, input_language, translator_language)

        return render(request, 'index1.html', {'translated_text': translated_text,'original_text':original_text})
    return render(request, 'index.html')
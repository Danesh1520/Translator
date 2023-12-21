from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from googletrans import Translator
import random

def home(request):
    return render(request, 'index.html')
    
def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
    return translated_text

def translate(request):
    if request.method == 'POST':
        original_text = request.POST.get('translateInput', '')
        input_language = request.POST.get('input_language', '')  # Corrected variable name
        translator_language = request.POST.get('translator_language', '')  # Corrected variable name

        # Translate text using the correct language codes
        translated_text = translate_text(original_text, input_language, translator_language)

        return render(request, 'index1.html', {'translated_text': translated_text,'original_text':original_text})
    return render(request, 'index.html')

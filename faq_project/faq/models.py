# faq/models.py

from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(text, dest_lang):
    if not text:  # If the text is empty, return an empty string
        return ""
    try:
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text  # Fallback to the original text

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_hi = RichTextField(blank=True, null=True)  # Hindi
    answer_bn = RichTextField(blank=True, null=True)  # Bengali

    # Method to get translated question
    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)

    # Method to get translated answer
    def get_translated_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer)

    def save(self, *args, **kwargs):
        # Automatically translate question and answer if not provided
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)
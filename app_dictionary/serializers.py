from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Dictionary, Word

class DictionarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Dictionary
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    word_lang = SerializerMethodField(method_name='get_word_lang', read_only=True)

    class Meta:
        model = Word
        fields = '__all__'

    def get_word_lang(self, obj):
        try:
            if self.context['request']['lang'] == 'ru':
                return obj.word_description_ru
            elif self.context['request']['lang'] == 'en':
                return obj.word_description_en
            elif self.context['request']['lang'] == 'tk':
                return obj.word_description_tk
            return obj.word_description_uz
        except:
            return obj.word_description_uz
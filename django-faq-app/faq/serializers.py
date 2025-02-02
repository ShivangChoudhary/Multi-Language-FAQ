from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'translated_question']

    def get_translated_question(self, obj):
        lang = self.context.get('request').query_params.get('lang', 'en')
        return obj.get_translated_question(lang)

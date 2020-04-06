from rest_framework import serializers

from polls.models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')
        read_only_fields = ('votes',)

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True, required=False)
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices')
    def create(self, validated_data):
        choices_data = validated_data.pop('choices', None)
        question = Question.objects.create(**validated_data)
        if choices_data:
            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)
        return question

class WriteableQuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices')
    def create(self, validated_data):
        choices_data = validated_data.pop('choices', None)
        question = Question.objects.create(**validated_data)
        if choices_data:
            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)
        return question

class AddChoiceToQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes', 'question')
        read_only_fields = ('votes', 'question')
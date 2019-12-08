from .models import Quiz, Question, Answer, FundedQuiz
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['content', 'correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['youtube_url', 'question_text', 'order', 'answers']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'description', 'questions']
        depth = 3


class FundedQuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = FundedQuiz
        fields = ['quiz', 'id', 'complete', 'percent_correct', 'amount',
                  'lightning_gift_order_id', 'redeemed']

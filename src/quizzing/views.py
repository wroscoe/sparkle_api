from .models import Quiz, Question, Answer, FundedQuiz
from rest_framework import viewsets
from .serializers import QuestionSerializer, QuizSerializer, FundedQuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class FundedQuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FundedQuiz.objects.all()
    serializer_class = FundedQuizSerializer
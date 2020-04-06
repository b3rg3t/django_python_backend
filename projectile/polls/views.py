from rest_framework import generics, views, response, status
from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, WriteableQuestionSerializer, ChoiceSerializer, AddChoiceToQuestionSerializer
class QuestionGenric:
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
class QuestionList(QuestionGenric, generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WriteableQuestionSerializer
        return QuestionSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return response.Response(QuestionSerializer(instance).data, status=status.HTTP_201_CREATED)    
class QuestionDetail(QuestionGenric, generics.RetrieveAPIView, generics.DestroyAPIView):
    pass
class QuestionVote(views.APIView):
    def post(self, request, *args, **kwargs):
        question_pk = kwargs.get('pk', None)
        questions = Question.objects.filter(pk=question_pk)
        payload = request.data
        if questions.exists():
            question = questions.first()
            choice_pk = payload.get('choice', None)
            possible_choices = question.choice_set.filter(pk=choice_pk)
            if possible_choices.exists():
                choice = possible_choices.first()
                choice.votes += 1
                choice.save()
                serializer = QuestionSerializer(question)
                print(serializer.data)
                return response.Response(serializer.data,status=status.HTTP_200_OK)
        return response.Response(
            'Not a valid choice or question',
            status=status.HTTP_400_BAD_REQUEST
        )
class ChoiceList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddChoiceToQuestionSerializer
        return ChoiceSerializer
    def perform_create(self, serializer):
        serializer.save(question=Question.objects.get(id=self.kwargs.pop("question_pk", None)))

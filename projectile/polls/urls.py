from django.urls import path, include
from polls.views import QuestionList, QuestionDetail, QuestionVote, ChoiceList
urlpatterns = [
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('questions/<int:question_pk>/choices/', ChoiceList.as_view(), name='choice-list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    path('questions/<int:pk>/vote/', QuestionVote.as_view(), name='question-vote')
]

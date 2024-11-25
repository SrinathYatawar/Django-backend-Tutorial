
from django.urls import path
from .views import questionCreateView,questionListView,questionRetriveView,CreatorCreateView,CreatorRetriveView,CreatorListView, CustomToken


urlpatterns = [
    path('v1/auth',CustomToken.as_view(),name='authentication'),
    path('v1/creator/create',CreatorCreateView.as_view(),name='creatorcreate'),
    path('v1/creator/<int:pk>',CreatorRetriveView.as_view(),name='creatorretrive'),
    path('v1/creator/all',CreatorListView.as_view(),name='creatorlist'),
    path('v1/question/create',questionCreateView.as_view(),name='questionCreate'),
    path('v1/question/<int:pk>',questionRetriveView.as_view(),name='retriveques'),
    path('v1/question/all',questionListView.as_view(),name='lisstallquestion')
]
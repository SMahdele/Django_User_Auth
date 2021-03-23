from django.urls import path
from django.views.generic import TemplateView
from .views import UserProjectView,UserProjectDetails ,UserExperienceView,UserExperienceDetails,UserEducationView,UserEducationDetails

urlpatterns = [   path('get-project/<str:pk>/',UserProjectDetails.as_view(), name="get-del-project"),
                  path('post-project/<str:pk>/', UserProjectView.as_view(), name="create-project"),
                  path('get-exp/<str:pk>/', UserExperienceDetails.as_view(), name="get-del-exp"),
                  path('post-exp/<str:pk>/',UserExperienceView.as_view(), name="create-exp"),
                  path('get-edu/<str:pk>/',UserEducationDetails.as_view(), name="get-del-edu"),
                  path('post-edu/<str:pk>/', UserEducationView.as_view(), name="create-edu"),


]

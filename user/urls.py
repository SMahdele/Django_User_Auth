from django.urls import path
from django.views.generic import TemplateView
from .views import UserProjectView,UserProjectDetails ,UserExperienceView,UserExperienceDetails,UserEducationView,UserEducationDetails

urlpatterns = [   path('get-project/<str:id>/',UserProjectDetails.as_view(), name="get-up-del-project"),
                  path('list-project/', UserProjectView.as_view(), name="create/list-project"),
                  path('get-exp/<str:id>/', UserExperienceDetails.as_view(), name="get-up-del-exp"),
                  path('list-exp/',UserExperienceView.as_view(), name="create/list-exp"),
                  path('get-edu/<str:id>/',UserEducationDetails.as_view(), name="get-up-del-edu"),
                  path('list-edu/', UserEducationView.as_view(), name="create/list-edu"),

]

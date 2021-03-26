# from .views import  ReadPostAPIView
# from .serializers import UserProjectSerializer
# from .models import  UserProject
# from .pagination import UserProjectViewPagination
#
# class UserProjectView(ReadPostAPIView):
#     serializer_class = UserProjectSerializer
#     model_class = UserProject
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
#     pagination_class = UserProjectViewPagination
#
#     def get_queryset(self):
#         queryset = self.UserProject.fil
#         serializer_class = UserSerializer
#         filter_backends = [filters.SearchFilter]
#         search_fields = ['username', 'email']

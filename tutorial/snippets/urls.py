from django.urls import path,include
from rest_framework.routers import DefaultRouter
from snippets import (
     views, 
     views_example_01,
     views_example_02_with_function,
     views_example_03_with_single_class,
     views_example_04_with_mixins,
     views_example_05_with_generic_class_based,
     views_example_authentication_permissions,
     views_example_hyperlinked,
     views_example_viewsets
)
from rest_framework.urlpatterns import format_suffix_patterns
router = DefaultRouter()
router.register(r'snippets', views_example_viewsets.SnippetViewSet,basename="snippets")
router.register(r'users', views_example_viewsets.UserViewSet,basename="users")

urlpatterns = [
     
     path('snippets/', views.snippet_list),
     path('snippets/<int:pk>', views.snippet_detail),
     path('snippets/ex1/', views_example_01.snippet_list),
     path('snippets/ex1/<int:pk>', views_example_01.snippet_detail),
     path('snippets/ex2/', views_example_02_with_function.snippet_list),
     path('snippets/ex2/<int:pk>', views_example_02_with_function.snippet_detail),
     path('snippets/ex3/', views_example_03_with_single_class.SnippetList.as_view()),
     path('snippets/ex3/<int:pk>', views_example_03_with_single_class.SnippetDetail.as_view()),
     path('snippets/ex4/', views_example_04_with_mixins.SnippetList.as_view()),
     path('snippets/ex4/<int:pk>', views_example_04_with_mixins.SnippetDetail.as_view()),
     path('snippets/ex5/', views_example_05_with_generic_class_based.SnippetList.as_view()),
     path('snippets/ex5/<int:pk>', views_example_05_with_generic_class_based.SnippetDetail.as_view()),
     path('snippets/ex6/users/', views_example_authentication_permissions.UserList.as_view()),
     path('snippets/ex6/users/<int:pk>', views_example_authentication_permissions.UserDetail.as_view()),
     path('snippets/ex6/', views_example_authentication_permissions.SnippetList.as_view()),
     path('snippets/ex6/<int:pk>', views_example_authentication_permissions.SnippetDetail.as_view()),
     path('snippets/ex7/users/', views_example_hyperlinked.UserList.as_view(), name='user-list'),
     path('snippets/ex7/users/<int:pk>', views_example_hyperlinked.UserDetail.as_view(), name='user-detail'),
     path('snippets/ex7/', views_example_hyperlinked.SnippetList.as_view(), name='snippet-list'),
     path('snippets/ex7/<int:pk>', views_example_hyperlinked.SnippetDetail.as_view(),name='snippet-detail'),
     path('', views_example_hyperlinked.api_root),
     path('snippets/ex7/<int:pk>/highlight/', views_example_hyperlinked.SnippetHighlight.as_view(),name='snippet-highlight'),
     # path('viewset/', include(router.urls)),
]
#format is optional
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
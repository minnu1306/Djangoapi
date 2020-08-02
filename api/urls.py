
from django.urls import path,include
from .views import article_list, ArticleList, GenericV, ArticleView, ModelView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleView,basename='article')
router.register('model',ModelView,basename='m')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),

    #path('article/',article_list ),
    path('article/',ArticleList.as_view() ),
    path('generic/<int:id>/',GenericV.as_view() ),

]

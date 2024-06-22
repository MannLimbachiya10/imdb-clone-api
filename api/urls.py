from django.contrib import admin
from django.urls import path
from django.contrib import auth
#from .views import movie_list, movie_details
from .views import djangoInbuildfilter ,filterUsingRatings,WatchListAV , WatchListDetailAV , StreamPlatfromAV, StreamPlatformDetailAV,ReviewListAV,ReviewDetailsAV,ReviewCreateAV, UserReviewAV
from .testdataScript import generate_watchlist_data
urlpatterns = [
    # path('watchlist/', movie_list),
    # path('watchlist/<int:pk>/',movie_details),
    path('watchlist/',WatchListAV.as_view(), name='watch'),
    path('watchlist/<int:pk>/',WatchListDetailAV.as_view(), name='watchdetails'),
    path('streamplatforms/', StreamPlatfromAV.as_view(), name='stream'),
    path('streamplatforms/<int:pk>/',StreamPlatformDetailAV.as_view(), name='streamdetails'),
    path('<int:pk>/review',ReviewListAV.as_view(), name='review-list'),
    path('<int:pk>/review-create',ReviewCreateAV.as_view(), name='review-create'),
    path('review/<int:pk>/',ReviewDetailsAV.as_view(), name='reviews_specific'),
    path('review/<str:username>/',UserReviewAV.as_view(), name='review_user'),
    path('review/',filterUsingRatings.as_view(), name='review_ratings'),
    path('watchlist/djangofilter/',djangoInbuildfilter.as_view(), name='django-filter'),
    path('watchlist/generate/', generate_watchlist_data.as_view()),
    #path('reviews/',ReviewListAV.as_view() , name='reviews_list'),
]
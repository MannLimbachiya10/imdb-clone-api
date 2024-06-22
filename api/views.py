from django.shortcuts import render
from .models import WatchList,StreamPlatfrom,Review
from .serializers import WatchListSerializers,StreamPlatfromSerializer, ReviewSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from api.custompermissions import AdminorReadonly, AllowReviewUserOnly
from .throttling import ReviewCreatethrottle, ReviewListthrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import *
from drf_spectacular.utils import extend_schema
from rest_framework import renderers


class djangoInbuildfilter(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializers
    #use below when you wanted to use filters
    # filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['title', 'StreamingPlatform__name','avg_rating']
    #use below when you wanted to use search filter.
    # filter_backends =[filters.SearchFilter]
    # search_fields = ['title', 'StreamingPlatform__name']
    #use below for ordering.
    filter_backends=[filters.OrderingFilter]
    ordering_fields= ['avg_rating','number_Of_Ratings']

class filterUsingRatings(mixins.ListModelMixin , generics.GenericAPIView):
    serializer_class = ReviewSerializers

    def get_queryset(self):
        rating = self.request.query_params.get('rating')
        return Review.objects.filter(rating=rating)

    def get(self , request , *args ,**kwargs):
        return self.list(request , *args , **kwargs)

class UserReviewAV(mixins.ListModelMixin , generics.GenericAPIView):
    serializer_class =ReviewSerializers

    def get_queryset(self):
        username = self.kwargs['username']
        return Review.objects.filter(review_user__username = username)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class WatchListAV(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):

    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes=[AdminorReadonly]

    def get(self , request):
        movies = WatchList.objects.all()
        paginator= PageNumberPagination()
        paginator.page_size=4
        result_page = paginator.paginate_queryset(movies,request)
        serializer = WatchListSerializers(result_page ,many=True)
        #return Response(serializer.data)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self , request):
        serializer = WatchListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors)


class WatchListDetailAV(APIView):

    permission_classes=[AdminorReadonly]
    def get(self, request , pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"message":"Movie doesnot exists"})

        serializer = WatchListSerializers(movie)
        return Response(serializer.data)
    
    def put(self , request ,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"message":"Movie doesnot exists"})
        
        seriaizer = WatchListSerializers(movie, data=request.data)
        if seriaizer.is_valid():
            seriaizer.save()
            return Response(seriaizer.data , status.HTTP_200_OK)
        return Response(seriaizer.errors)
    
    def delete(self, request ,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExits:
            return Response({"message":"Movie doesnot exists"})
        
        movie.delete()
        return Response({"message":"This item is deleted"},status.HTTP_200_OK)
    
class StreamPlatfromAV(APIView):
    permission_classes=[AdminorReadonly]
    def get(self,request):
        stream = StreamPlatfrom.objects.all()
        serializer = StreamPlatfromSerializer(stream, many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StreamPlatfromSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
class StreamPlatformDetailAV(APIView):
    permission_classes=[AdminorReadonly]

    def get(self,request,pk):
        try:
            stream = StreamPlatfrom.objects.get(pk=pk)
        except StreamPlatfrom.DoesNotExist:
            return Response({"message":"Streaming platform does not exists!!"})
        
        serializer = StreamPlatfromSerializer(stream)
        return Response(serializer.data)
    
    def put(self, request , pk):
        try:
            stream = StreamPlatfrom.objects.get(pk=pk)
        except StreamPlatfrom.DoesNotExist:
            return Response({"message":"Streaming platform does not exists!!"})
        
        serializer = StreamPlatfromSerializer(stream,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors)
    
    def delete(self, request , pk):
        try:
            stream = StreamPlatfrom.objects.get(pk=pk)
        except StreamPlatfrom.DoesNotExist:
            return Response({"message":"Streaming platform does not exists!!"})
        
        stream.delete()
        return Response({"message":"Streaming Plaform Deleted successfully!!"}, status.HTTP_200_OK)
    

class ReviewListAV(mixins.ListModelMixin , generics.GenericAPIView):

    #queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    #permission_classes = [permissions.IsAuthenticated]
    #throttle_classes = [ReviewListthrottle]

    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class ReviewCreateAV(mixins.CreateModelMixin , generics.GenericAPIView):
    # serializer_class =ReviewSerializers

    # def get_queryset(self):
    #     return Review.objects.all()

    # def perform_create(self, serializer):
    #     pk = self.kwargs.get('pk')
    #     watchlist=WatchList.objects.get(pk=pk)
    #     review_queryset = Review.objects.filter(watchlist=watchlist, review_user=self.request.user)
    #     if review_queryset.exists():
    #        # print(Review.objects.filter(watchlist=watchlist and review_user=self.request.user))
    #         raise ValidationError("You have already reviewed this error!!")
    #     serializer.save(watchlist=watchlist ,review_user=self.request.user)
       
    serializer_class = ReviewSerializers
    queryset= Review.objects.all()
    permission_classes =[permissions.IsAuthenticated]
    #throttle_classes =[ReviewCreatethrottle] #include this when you require throttling, i.e, restrict number of resquests.
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        user_queryset = Review.objects.filter(watchlist=watchlist,review_user=review_user)
        if user_queryset.exists():
            raise ValidationError("You have already reviewed this show!!")
        if watchlist.number_Of_Ratings==0:
            watchlist.avg_rating=serializer.validated_data['rating']
        else:
            watchlist.avg_rating=(watchlist.avg_rating + serializer.validated_data['rating'] )/2
        watchlist.number_Of_Ratings=watchlist.number_Of_Ratings+1
        watchlist.save()
        serializer.save(review_user=review_user,watchlist=watchlist)

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ReviewDetailsAV(mixins.RetrieveModelMixin ,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset =Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [AllowReviewUserOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# @api_view(['GET','POST'])

# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializers(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    

# @api_view(['GET','PUT','DELETE'])

# def movie_details(request,pk):
    
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except movie.DoesNotExist:
#         return Response(status.HTTP_404_NOT_FOUND , {"Error":"Movie Dosenot exists!!"})
#     if request.method == 'GET':
#         serializer = MovieSerializers(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer= MovieSerializers(movie,data=request.data)
#         if serializer.is_valid():
    #         serializer.save()
    #         return Response(status.HTTP_201_CREATED,serializer.data)
    #     return Response(serializer.data)
    # if request.method == 'DELETE':
    #     movie.delete()
    #     return Response({"messgae":"Object deleted successfully!"},status.HTTP_200_OK )
        


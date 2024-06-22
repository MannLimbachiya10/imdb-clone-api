import random
from faker import Faker
from rest_framework.decorators import api_view,APIView
from .serializers import WatchListSerializers
from rest_framework.response import Response
from .models import WatchList ,StreamPlatfrom
from django.views.decorators.csrf import csrf_exempt

fake=Faker()

class generate_watchlist_data(APIView):
    def post(self, request):

        title = fake.sentence()
        storyline = fake.paragraph()
        streamingplatform = random.choice(['Netflix','Disney+','Hulu'])
        active=True
        sp=StreamPlatfrom.objects.all()
        if not sp.exists():
            return Response({'message':'first add streaming platform'})
        sp_individaul = random.choice(sp)
        my_dict={
            'title':title,
            'storyline':storyline,
            'StreamingPlatform':sp_individaul.id,
            'active':active
        }
        
        # my_dict=WatchList.objects.create(title=title,
        #     storyline=storyline,
        #     StreamingPlatform=sp_individaul,
        #     active=active             
        #     )
            
        serializer=WatchListSerializers(data=my_dict)
       
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(my_dict)
        return Response(serializer.errors)



#@csrf_exempt
# @api_view(['POST'])
# def generate_watchlist_data(request):
#     title = fake.sentence()
#     storyline = fake.paragraph()
#     streamingplatform = random.choice(['Netflix','Disney+','Hulu'])
#     my_dict={
#         'title':title,
#         'storyline':storyline,
#         'StreamingPlatform':streamingplatform
#     }
#     serializer=WatchListSerializers(data=my_dict)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(my_dict)
#     return Response(serializer.errors)

# @api_view(['POST'])
# def Generate_Random_data_for_watchlist(request):
#     serializer= WatchListSerializers(data=generate_watchlist_data)
#     if serializer.is_valid():
#         serializer.save()
#         Response(serializer.data)
#     return Response(serializer.errors)


from rest_framework import serializers
from .models import WatchList , StreamPlatfrom ,Review
from rest_framework import validators

class ReviewSerializers(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ['watchlist']

class WatchListSerializers(serializers.ModelSerializer):
    #show_length= serializers.SerializerMethodField()
    #reviews = ReviewSerializers(many=True ,read_only=True)
    #StreamingPlatform=serializers.CharField(source='StreamingPlatform.name', read_only=True) #Uncomment this line when you don't want to run test cases.

    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatfromSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializers(many=True ,read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #watchlist = serializers.HyperlinkedRelatedField(many=True , read_only=True , view_name='watchdetails')
    class Meta:
        model = StreamPlatfrom
        fields = '__all__'

    # def get_show_length(self , data):
    #     return len(data.name)

    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Please enter atleast two alphabets in name field")
    #     return value
    
    # def validate(self,data):
    #     if data['name']==data['description']:
    #         raise serializers.ValidationError("Name and Description should not be same")
    #     return data

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short it must have atleast 2 alphabets in it!!")
#     return value

# class MovieSerializers(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    # Below is field level validation
    # def validate_name(self, value):
    #     if len(value)<=1:
    #         raise serializers.ValidationError("Name is too sort!!")
    #     return value
    
    # below is object level validation
    # def validate(self, data):
    #     if data['name']==data['description']:
    #         raise serializers.ValidationError("Title and Description should not be same!!")
    #     return data
        
        
    
from rest_framework import serializers
from .models import Creator, Question, Choices









class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    



class ChoicesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Choices
        fields = ['id', 'choice_text', 'voteCount']





class questionSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializers(many=True,read_only = True)
    # creator = serializers.PrimaryKeyRelatedField(queryset=Creator.objects.all())  #
    
    class Meta:
        model = Question
        fields = ['id','creator','question_text','publish_date','choices']





class CreatorSerializer(serializers.ModelSerializer):
    questions = questionSerializer(many=True,read_only = True)
    
    class Meta:
        model = Creator
        fields = ['id','created_by','questions']
    
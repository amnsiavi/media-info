from rest_framework import serializers 
from django.utils import timezone

from watch_list.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        exclude = ['created','updated']
    
    def get_created_at(self,object):
        
       return object.created.strftime("%Y-%m-%d-%H:%M:%S")
    
    def get_updated_at(self,object):
        return object.updated.strftime("%Y-%m-%d-%H:%M:%S")
                
    
    def update(self,instance,validated_data):
        instance = super().update(instance,validated_data)
        instance.save(update_fields=['updated'])
        return instance

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    
    class Meta:
        model = StreamPlatform
        exclude = ['created','updated']
    
    def get_created_at(self,object):
        return object.created.strftime("%Y-%m-%d-%H:%M:%S")
    
    def get_updated_at(self, object):
        return object.updated.strftime("%Y-%m-%d-%H:%M:%S")
    
    
    def update(self,instance,validated_data):
        instance = super().update(instance,validated_data)
        instance.save(update_fields=['updated'])
        return instance
    
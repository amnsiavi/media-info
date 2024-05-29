from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from watch_list.models import WatchList, StreamPlatform
from watch_list.api.serialzers import WatchListSerializer,StreamPlatformSerializer



class WatchListAV(APIView):
    
    def get(self, request):
        
        try:
            if WatchList.objects.exists():
                watch_list = WatchList.objects.all()
                serialzed = WatchListSerializer(watch_list,many=True)
                return Response({
                    'data':serialzed.data
                },status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self,request):
        
        try:
            if len(request.data) == 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = WatchListSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'data':serializer.data
                    },status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WatchListDetails(APIView):
    
    def get(self, request,pk):
        
        try:
            watch_list = WatchList.objects.get(pk=pk)
            serialized = WatchListSerializer(watch_list)
            return Response({
                'data':serialized.data
            },status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,pk):
        
        try:
            watch_list = WatchList.objects.get(pk=pk)
            watch_list.delete()
            return Response({
                'message':'Reccord Deleted'
            },status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request,pk):
        try:
            if len(request.data) == 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            watch_list = WatchList.objects.get(pk=pk)
            serialized = WatchListSerializer(watch_list,data=request.data)
            if serialized.is_valid():
                serialized.save()
                return Response({
                    'data':serialized.data
                },status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self,request,pk):
        
        try:
            if len(request.data) == 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                watch_list = WatchList.objects.get(pk=pk)
                serialized = WatchListSerializer(watch_list,data=request.data,partial=True)
                if serialized.is_valid():
                    serialized.save()
                    return Response({
                        'data':serialized.data
                    },status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StreamPlatformList(APIView):
    
    def get(self,request):
        
        try:
            if StreamPlatform.objects.exists():
                platform = StreamPlatform.objects.all()
                serialized = StreamPlatformSerializer(platform,many=True)
                return Response({
                    'data':serialized.data
                },status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self,request):
        
        try:
            if len(request.data) == 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                serialized = StreamPlatformSerializer(data=request.data)
                if serialized.is_valid():
                    serialized.save()
                    return Response({
                        'data':serialized.data
                    },status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StreamPlatformDetail(APIView):
    pass
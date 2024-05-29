from django.urls import path


from watch_list.api.views import WatchListAV,WatchListDetails,StreamPlatformList,StreamPlatformDetail



urlpatterns = [
    path('list/',WatchListAV.as_view(),name='watch-list'),
    path('<int:pk>/',WatchListDetails.as_view(),name='watchlist-details'),
    path('stream-platform/list',StreamPlatformList.as_view(),name='streamplatform-list'),
    path('stream-platform/<int:pk>', StreamPlatformDetail.as_view(),name='streamplatform-details')
    
]

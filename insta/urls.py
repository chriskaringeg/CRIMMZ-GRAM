from django.conf.urls import url
''' 
This is to allow us to connect the PROJECT's  url with this APP's url 
it will then allow us to define paths here as we had included (grams urls)
in the PROJECT.
'''

from . import views
'''
Here we are importing the views as we shall connect templates from there 
'''

from django.conf import settings
'''
This is importing the settings configurations to (gramapp)
'''

from django.conf.urls.static import static
'''
This is to import static-files in urls
'''
from django.shortcuts import render, redirect


'''End Of Import'''
#---------------------------------------------------------------------#

urlpatterns=[




#################################################################################################################################################################################
#URL FOR  HOME PAGE
#################################################################################################################################################################################

    #HOME Page url!

    #This is the home page url pattern 
    url(r'^$',views.index, name='index'),
     url(r'^feeds/$',views.feeds, name='feeds'),

#################################################################################################################################################################################
#URL FOR EXPLORE-PAGE
#################################################################################################################################################################################

    #EXPLORE-Page url!
    
    #This is the Explore page url 
    url(r'^explore/',views.explore,name ='explore'),

#################################################################################################################################################################################
#URL FOR NOTIFICATION_PAGE
#################################################################################################################################################################################

    #NOTIFICATION-Page url!
    
    #This is the Notification page url 
    url(r'^notification',views.notification,name ='notification'),

#################################################################################################################################################################################
#URL FOR PROFILE-PAGE
##################################################################################################################################################################################

    #PROFILE-Page url!
    
    #This is the Profile page url 
    url(r'^profile/$',views.profile,name ='profile'),

#################################################################################################################################################################################
#URL FOR LOGIN-PAGE
##################################################################################################################################################################################

    #LOGIN-Page url!
    
    #This is the Login page url 
 

#################################################################################################################################################################################
#URL FOR LOG-OUT PAGE
##################################################################################################################################################################################

    #LOG-OUT-Page url!
    
    #This is the Login-Out page url 

#################################################################################################################################################################################
#URL FOR UPLOADING-PAGE
#################################################################################################################################################################################

    #POST_PIC-Page url!
    
    #This is the Post page url 
    url(r'^upload/',views.upload,name ='upload'),

##################################################################################################################################################################################
##################################################################################################################################################################################
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
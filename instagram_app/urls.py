
from django.urls import path
from .views import home, login, signup, logout_view, post, update_post, delete_post



urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    
    path('logout/', logout_view, name='logout'),

    path('post/', post, name="post"),

    path('update/<int:post_id>/', update_post, name='update'),


    path('delete/<int:post_id>/', delete_post, name="delete")


]

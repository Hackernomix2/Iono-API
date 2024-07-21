from django.urls import path
from . import views

urlpatterns = [
    # get methods 
    path('projects/', views.get_project, name='get_all_projects'),
    path('research/', views.get_research, name='get_all_research'),
    path('collected-data/', views.get_collected_data, name='get_all_collected_data'),

    path('projects/<int:pk>/', views.get_one_project, name='get_one_project'),
    path('research/<int:pk>/', views.get_one_research, name='get_one_research'),
    path('collected-data/<int:pk>/', views.get_one_collected_data, name='get_one_collected_data'),

    path('user/projects/', views.get_user_projects, name='get_user_projects'),
    path('user/research/', views.get_user_research, name='get_user_research'),


    path('projects/<int:pk>/data/', views.get_project_data, name='get_project_data'),

    path('research/<int:pk>/project/', views.get_research_project, name='get_research_project'),

    # Create methods
    path('projects/create/', views.create_project, name='create_project'),
    path('research/create/', views.create_research, name='create_research'),
    path('collected-data/create/', views.create_collected_data, name='create_collected_data'),

    # AI related methods
    path('projects/<int:pk>/ask-ai/', views.ask_ai, name='ask_ai'),
    path('projects/<int:pk>/request-data-analysis/', views.request_data_analysis, name='request_data_analysis'),

    # Update method
    path('projects/<int:pk>/update/', views.update_project, name='update_project'),
]

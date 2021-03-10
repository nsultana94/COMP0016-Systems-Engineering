from django.urls import path
from . import views
from .views import (HomeProjectListView, 
                PostDetailView,
                PostCreateView, 
                PostUpdateView, 
                PostDeleteView, 
                UserPostListView,
                OrganisationListView,
                OrganisationDetailView,
                OrganisationUpdateView,
                OrganisationDeleteView,
                ReviewsListView, 
                ReviewDetailView, 
                UsersListView,
                ProjectsListView, 
                ProjectDetailView,
                ReviewsDisplayListView,
                Trial)


urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name = 'blog-about'),
    path('displayOrganisations/', OrganisationListView.as_view() , name= 'organisations'),
    path('reviews/', ReviewsListView.as_view() , name= 'reviews'),
    path('trial/', Trial.as_view() , name= 'trial'),
    path('reviewDisplay/', ReviewsDisplayListView.as_view() , name= 'review-display'), #review grid

    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # feedback sheet
    # path('review/<int:review_id>/', ReviewDetailView.as_view(), name = 'review-detail'),
    path('review/<int:review_id>/', views.review, name = 'review-detail'), # VIEW ONE REVIEW
    path('reviewdetail/<int:project_id>/', views.projectreviewdetail , name= 'reviewdetail'),

    path('organisation/<int:pk>/', OrganisationDetailView.as_view(), name = 'organisation-detail'),
    path('project/<int:pk>/', views.projectdetail, name = 'project-detail'),

    path('project/<int:project_id>/review/<int:review_id>/', views.detail, name='detail'),
    
    
    # path('markAndReview/project/<int:pk>/', MarkProjectDetail.as_view(), name = 'mark-project-detail'),
    path('markAndReview/project/<int:pk>/', views.markprojectdetail, name = 'mark-project-detail'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('organisation/<int:pk>/update/', OrganisationUpdateView.as_view(), name = 'organisation-update'),
    path('organisation/<int:pk>/delete/', OrganisationDeleteView.as_view(), name = 'organisation-delete'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),

    path('users/', UsersListView.as_view(), name = 'users' ),
    path('projects/', views.projectgrid, name = 'projects' ),
    path('projects/list', views.projectlistview, name = 'projectslist' ),
    path('acceptedprojects', views.acceptedprojects, name = 'acceptedprojects' ),
    path('rejectedprojects', views.rejectedprojects, name = 'rejectedprojects' ),


    path('SubmissionPortal/', views.SubmissionPortal, name= 'SubmissionPortal'),
    path('ReviewPortal/<int:project_id>/', views.ReviewPortal, name= 'ReviewPortal'),
    # path('ReviewPortal/', views.ReviewPortal, name= 'ReviewPortal'),

    
   
]
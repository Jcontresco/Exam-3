from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('jobs/<int:jobs_id>', views.viewStats),
    path('jobs/new',views.create_job),
    path('jobs/edit/<int:jobs_id>', views.editJob),
    path('delete/<int:jobs_id>', views.deleteJob),
    path('add_job/<int:jobs_id>', views.add_Job),
]
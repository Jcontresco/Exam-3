from django.shortcuts import redirect, render
from apps.user.models import User
from apps.wall.models import Jobs
from datetime import date
from django.contrib import messages

# Create your views here.

def viewStats(request, jobs_id):
    id = request.session['user_id']
    user = User.objects.get(id=id)
    job_desc = Jobs.objects.get(id=jobs_id)

    if user:
        context = {
            'job_desc': job_desc,
            'user': user
        }
        return render(request, 'wall/stats.html', context)
    

def dashboard(request):

    if 'user_id' in request.session:
        id = request.session['user_id']

        user = User.objects.get(id=id)
        user_jobs = Jobs.objects.filter(user=user)
        all_jobs = Jobs.objects.all()
        context = {
            'user_jobs': user_jobs,
            'all_jobs' : all_jobs,
            'user': user
        }
        return render(request, 'wall/dashboard.html', context=context)    
    return redirect('/')

def create_job(request):
    if request.method == 'GET':
        return render(request, 'wall/jobadd.html')
        
    elif request.method == 'POST':
        errors = Jobs.objects.basic_validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard/jobs/new')
        else:
            id = request.session['user_id']
            user = User.objects.get(id=id)
            title = request.POST['title']
            descr = request.POST['description']
            location = request.POST['location']
            new_job = Jobs.objects.create(title=title, description=descr, user=user, location=location)
        
        return redirect('/dashboard') 

def editJob(request, jobs_id):
    job = Jobs.objects.get(id=jobs_id)
    if request.method == 'GET':
        if job:
            context = {
                'job_info': job
            }
            return render(request, 'wall/jobedit.html', context)

        else: 
            return redirect('/dashboard')
    
    elif request.method == 'POST':
        if job:
            job.title = request.POST['jobs-title']
            job.description = request.POST['jobs-description']
            job.location = request.POST['jobs-location']
            job.save()
            return redirect('/dashboard')

def deleteJob(request, jobs_id):
    id = request.session['user_id']
    user = User.objects.get(id=id)
    job = Jobs.objects.get(id=jobs_id)

    if job:
        job.delete()
        print('deleting job')
        return redirect('/dashboard')
        

    return redirect('/dashboard')

def add_Job(request, jobs_id):
    id = request.session['user_id']
    user = User.objects.get(id=id)

    jobs = Jobs.objects.get(id=jobs_id)
    jobs.join.add(user)
    print(jobs.join.all())
    return redirect('/dashboard')



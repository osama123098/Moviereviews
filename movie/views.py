from django.shortcuts import render,get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Movie, Review
from .forms import ReviewForm

# Create your views here.
def home(request):
    # this is home page
    search_term = request.GET.get('search_movie')
    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:    
        movies = Movie.objects.all()
    return render(request, 'home.html', {'search_term':search_term,'movies': movies})

def about(request):
    # this is about page
    return HttpResponse('<h1>Welcome to about Page</h1>')

def signup(request):
    # forwarding to the sign_up page here. 
    email = request.GET.get('email')
    return render(request, 'signup.html',{'email': email})

def detail(request,movie_id):
    #detail acces to movie
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie = movie)
    return render(request, 'detail.html',{'movie':movie,'reviews':reviews})

@login_required
def createreview(request,movie_id):
    """Function to manage reviews of the movie add by user"""
    movie = get_object_or_404(Movie,pk=movie_id)
    # user is navigating to create review page
    if request.method == 'GET':
        return render(request,'create_review.html',{'form':ReviewForm(),'movie':movie})

    else:
        try:
            form = ReviewForm(request.POST)
            newReview= form.save(commit = False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('detail',newReview.movie_id)

        except ValueError:
            return render(request,'create_review.html',{'form':ReviewForm(),'error':'bad data passed in'})
@login_required
def updatereview(request,review_id):
    # Update the review of the movie 
    review= get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance= review)
        return render(request,'updatereview.html',{'review':review,'form':form})

    else:
        try:
            form = ReviewForm(request.POST,instance=review)
            form.save()
            return redirect('detail',review.movie.id)
        except ValueError:
            return render(request,'updatereview.html',{'review':review,'form':form ,'error':'Bad data in form'})

@login_required
def deletereview(request,review_id):
    #Delete the review when user is log in
    review = get_object_or_404(Review, pk=review_id,
    user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)
    


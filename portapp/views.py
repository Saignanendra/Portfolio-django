from django.shortcuts import render, redirect
from django.contrib import messages 

#* Models 
from .models import User_Profile, Contact, about, Fact, Skill,ContactInfo,PortfolioItem,Service,Testimonial,Resume,Education,Experience
from .models import social_media_links

# TODO Create your views here.



def home(request):

    userprofile = User_Profile.objects.all()
    about_user = about.objects.all()
    fact = Fact.objects.all()
    skill = Skill.objects.all()
    contact = ContactInfo.objects.all()
    image = PortfolioItem.objects.all()
    service = Service.objects.all()
    review = Testimonial.objects.all()
    resume = Resume.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    links = social_media_links.objects.all()

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contacts = Contact.objects.create(name=name, email=email, subject=subject,message=message)
        contacts.save()

        messages.success(request, "We've received your information and will reach out to you soon. Thank you!")
        


    context = {"userprofile":userprofile,
                "about":about_user,
                "fact":fact,
                "skill":skill,
                "contact":contact,
                "image":image,
                "service":service,
                "review":review,
                "resume":resume,
                "education":education,
                "experience":experience,
                "links":links,}

    return render(request, 'portapp/index.html', context)

'''
def blogs(request):

    userprofile = User_Profile.objects.all()


    blogs = Blogs.objects.all().order_by('-time_stamp')

    context = {'blogs':blogs, "userprofile":userprofile}

    return render(request, "portapp/blogs.html", context)

def about(request):

    userprofile = User_Profile.objects.all()


    context = {"userprofile":userprofile}

    return render(request, "portapp/about.html", context)


def contact(request):
    
    userprofile = User_Profile.objects.all()


    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        phonenum = request.POST['num']
        desc = request.POST['desc']

        contact = Contact.objects.create(name=name, email=email, phone_num=phonenum,description=desc)
        contact.save()

        messages.success(request, "We've received your information and will reach out to you soon. Thank you!")
        

    context = {"userprofile":userprofile}
    return render(request, "portapp/contact.html", context) '''
    

def error_404(request, exception):

    return render(request, "portapp/error_404.html", status=404)

def error_500(request):

    return render(request, "portapp/error_500.html", status=500)

def error_400(request,exception):

    return render(request, "portapp/error_400.html", status=400)

def error_403(request,exception):

    return render(request, "portapp/error_403.html", status=403)    
from django.db import models
import os

# Create your models here.

    #path for user uploaded profile images
def upload_to_portfolio_home_images(instance, filename):
    # Media file upload path: media/<user_id>/profileimage/<filename>
    return f'static/media/homeimage/{filename}'

def upload_to_portfolio_profile_images(instance, filename):
    # Media file upload path: media/<user_id>/profileimage/<filename>
    return f'static/media/profileimage/{filename}'


class User_Profile(models.Model):
    home_image = models.ImageField(upload_to=upload_to_portfolio_home_images)
    name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to=upload_to_portfolio_profile_images)
    job1 = models.CharField(max_length=150,null=True, blank=True)
    job2 = models.CharField(max_length=150,null=True, blank=True)
    job3 = models.CharField(max_length=150,null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    
class social_media_links(models.Model):
    
    facebook = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return " Add Social Media Links"  

    class Meta:
        verbose_name="Add Social Media links"
        verbose_name_plural = "Add Social Media links"
         

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField(null=True)
    time_stamp = models.DateTimeField(auto_now=True, blank=True)
      
    def __str__(self):
        return (
                 f"{self.email}"
                 f"{self.subject}"
                 f"({self.time_stamp:%Y-%m-%d %H:%M})"
        )

    class Meta:
        verbose_name = "Contacts from Portfolio"
        verbose_name_plural = "Contacts from Portfolio"


class about(models.Model):
    birthday = models.DateField(null=True, blank=True)
    website = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    is_freelance = models.CharField(max_length=50, blank=True, default="available")
    time_stamp = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return (
                 f"{self.email}"
        )

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"    

class Fact(models.Model):
    description = models.TextField(null=True, blank=True)
    happy_clients = models.CharField(max_length=10,null=True, blank=True)
    projects = models.CharField(max_length=10,null=True, blank=True)
    hours_of_support = models.CharField(max_length=10,null=True, blank=True)
    hard_workers = models.CharField(max_length=100,null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return (
                 f"{self.time_stamp}"
        )
    class Meta:
        verbose_name = "Fact"
        verbose_name_plural = "Fact"    

class Skill(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    percentage = models.PositiveIntegerField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return (
                 f"{self.name}"
        )
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "write your skill"  

class Resume(models.Model):

    full_name = models.CharField(max_length=100,null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=250,null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    email = models.EmailField()
    time_stamp = models.DateTimeField(auto_now=True, blank=True)
    def __str__(self):
        return (
                 f"{self.full_name}"
        ) 
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume"      
    
class Education(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    degree = models.CharField(max_length=250,null=True, blank=True)
    school = models.CharField(max_length=250,null=True, blank=True)
    location = models.CharField(max_length=250,null=True, blank=True)
    year_start = models.CharField(max_length=50,null=True, blank=True)
    year_end = models.CharField(max_length=50,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return (
                f"{self.degree}"
        )   
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"     


class Experience(models.Model):
    
        resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
        job_title = models.CharField(max_length=250,null=True, blank=True)
        company = models.CharField(max_length=250,null=True, blank=True)
        location = models.CharField(max_length=250,null=True, blank=True)
        year_start = models.CharField(max_length=50,null=True, blank=True)
        year_end = models.CharField(max_length=50,null=True, blank=True)
        description = models.TextField(null=True, blank=True)
    

        def __str__(self):
            return (
                    f"{self.job_title}"
            )      

        class Meta:
            verbose_name = "Experience"
            verbose_name_plural = "Experience"  

def upload_to_portfolio_images(instance, filename):
    # Get the project type and image name from the instance
    project_type = instance.project_type.lower().replace(" ", "_")
    # Media file upload path: media/<user_id>/profileimage/<filename>
    return f'static/media/{project_type}/{filename}'

class PortfolioItem(models.Model):
    PROJECT_TYPES = [
        ('Design', 'Design'),
        ('Digital', 'Digital'),
        ('Graphics', 'Graphics'),
    ]

    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES,null=True, blank=True)
    image = models.ImageField(upload_to=upload_to_portfolio_images,null=True, blank=True)
    video = models.FileField(upload_to=upload_to_portfolio_images,null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now=True, blank=True)

    # You can add more fields such as a link to the project or any other relevant information.

    def __str__(self):
        return (
                 f"{self.project_type}"
        )  

    class Meta:
        verbose_name = "Images and Videos"
        verbose_name_plural = "Images and Videos"  

class Service(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now=True, blank=True)


    def __str__(self):
        return (
                 f"{self.title}"
        )  
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Service"  

class ContactInfo(models.Model):
    location = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15,blank=True)
    time_stamp = models.DateTimeField(auto_now=True, blank=True)


    def __str__(self):
        return (
                 f"{self.email}"
        )      
    class Meta:
        verbose_name = "ContactInfo"
        verbose_name_plural = "Contact-Information"    

class Testimonial(models.Model):
    name = models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=100,blank=True)
    testimonial_text = models.TextField(blank=True)
    time_stamp = models.DateTimeField(auto_now=True, blank=True)


    def __str__(self):
        return (
                 f"{self.name}"
        ) 
    class Meta:
        verbose_name = "Testimonail"
        verbose_name_plural = "Testimonail"      
from django.contrib import admin

from .models import Education,Experience


# Register your models here.


#* TO Display detail view in admin site



class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'id','name', 'subject','time_stamp')


from .models import social_media_links

admin.site.register(social_media_links)

from .models import User_Profile

class User_ProfileAdmin(admin.ModelAdmin):

    list_display = ('name', 'id','time_stamp')

admin.site.register(User_Profile,User_ProfileAdmin)


from .models import ContactInfo

class ContactInfoAdmin(admin.ModelAdmin):

    list_display = ('email','phone','time_stamp')

admin.site.register(ContactInfo, ContactInfoAdmin)


from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):

    list_display = ('name', 'title','time_stamp')

admin.site.register(Testimonial, TestimonialAdmin)


from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','time_stamp')
admin.site.register(Service, ServiceAdmin)

from .models import PortfolioItem

class PortfolioAdmin(admin.ModelAdmin):

    list_display = ('project_type', 'id','time_stamp')

admin.site.register(PortfolioItem,PortfolioAdmin)


from .models import Skill

class SkillAdmin(admin.ModelAdmin):

    list_display = ('name', 'percentage','time_stamp')

admin.site.register(Skill, SkillAdmin)

from .models import Fact

class FactAdmin(admin.ModelAdmin):

    list_display = ('id','time_stamp')

admin.site.register(Fact,FactAdmin)


from .models import about

class AboutAdmin(admin.ModelAdmin):

    list_display = ('email', 'id','time_stamp')

admin.site.register(about,AboutAdmin)


from .models import Contact

admin.site.register(Contact, ContactAdmin)


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

from .models import Resume
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'phone', 'email')
    inlines = [EducationInline, ExperienceInline]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ( 'degree', 'school', 'year_start', 'year_end')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'year_start', 'year_end')

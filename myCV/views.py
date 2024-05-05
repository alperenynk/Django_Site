from django.shortcuts import render
from myCV.models import GeneralSetting, ImageSetting, Skill, SocialMedia

# Create your views here.
def index(request):

    # General
    site_title = GeneralSetting.objects.get(name="site_title").parameter
    site_keywords = GeneralSetting.objects.get(name="site_keywords").parameter
    site_description = GeneralSetting.objects.get(name="site_description").parameter
    home_banner_title = GeneralSetting.objects.get(name="home_banner_title").parameter
    home_banner_name = GeneralSetting.objects.get(name="home_banner_name").parameter
    about_myself_welcome = GeneralSetting.objects.get(name="about_myself_welcome").parameter
    testimonial1_name = GeneralSetting.objects.get(name="testimonial1_name").parameter
    testimonial2_name = GeneralSetting.objects.get(name="testimonial2_name").parameter
    testimonial1_think = GeneralSetting.objects.get(name="testimonial1_think").parameter
    testimonial2_think = GeneralSetting.objects.get(name="testimonial2_think").parameter

    # Image
    site_favicon = ImageSetting.objects.get(name="site_favicon").file
    home_banner_image = ImageSetting.objects.get(name="home_banner_image").file
    testimonial1_image = ImageSetting.objects.get(name="testimonial1_image").file
    testimonial2_image = ImageSetting.objects.get(name="testimonial2_image").file

    # Skill
    skills = Skill.objects.all()

    # Social Media
    social_medias = SocialMedia.objects.all()

    context = {
        "site_title": site_title,
        "site_keywords": site_keywords,
        "site_description": site_description,
        "home_banner_title": home_banner_title,
        "home_banner_name": home_banner_name,
        "about_myself_welcome": about_myself_welcome,
        "site_favicon": site_favicon,
        "home_banner_image": home_banner_image,
        "testimonial1_image": testimonial1_image,
        "testimonial2_image": testimonial2_image,
        "testimonial1_name": testimonial1_name,
        "testimonial2_name": testimonial2_name,
        "testimonial1_think": testimonial1_think,
        "testimonial2_think": testimonial2_think,
        "skills": skills,
        "social_medias": social_medias,
    }

    return render(request, "index.html", context=context)
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
    education_hs = GeneralSetting.objects.get(name="education_hs").parameter
    education_uni = GeneralSetting.objects.get(name="education_uni").parameter
    mail = GeneralSetting.objects.get(name="mail").parameter
    number = GeneralSetting.objects.get(name="number").parameter
    location = GeneralSetting.objects.get(name="location").parameter
    testimonial1_name = GeneralSetting.objects.get(name="testimonial1_name").parameter
    testimonial2_name = GeneralSetting.objects.get(name="testimonial2_name").parameter
    testimonial3_name = GeneralSetting.objects.get(name="testimonial3_name").parameter
    testimonial4_name = GeneralSetting.objects.get(name="testimonial4_name").parameter
    testimonial5_name = GeneralSetting.objects.get(name="testimonial5_name").parameter
    testimonial6_name = GeneralSetting.objects.get(name="testimonial6_name").parameter
    testimonial1_think = GeneralSetting.objects.get(name="testimonial1_think").parameter
    testimonial2_think = GeneralSetting.objects.get(name="testimonial2_think").parameter
    testimonial3_think = GeneralSetting.objects.get(name="testimonial3_think").parameter
    testimonial4_think = GeneralSetting.objects.get(name="testimonial4_think").parameter
    testimonial5_think = GeneralSetting.objects.get(name="testimonial5_think").parameter
    testimonial6_think = GeneralSetting.objects.get(name="testimonial6_think").parameter

    # Image
    site_favicon = ImageSetting.objects.get(name="site_favicon").file
    home_banner_image = ImageSetting.objects.get(name="home_banner_image").file
    testimonial1_image = ImageSetting.objects.get(name="testimonial1_image").file
    testimonial2_image = ImageSetting.objects.get(name="testimonial2_image").file
    testimonial3_image = ImageSetting.objects.get(name="testimonial3_image").file
    testimonial4_image = ImageSetting.objects.get(name="testimonial4_image").file
    testimonial5_image = ImageSetting.objects.get(name="testimonial5_image").file
    testimonial6_image = ImageSetting.objects.get(name="testimonial6_image").file

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
        "education_hs": education_hs,
        "education_uni": education_uni,
        "mail": mail,
        "number": number,
        "location": location,
        "site_favicon": site_favicon,
        "home_banner_image": home_banner_image,
        "testimonial1_image": testimonial1_image,
        "testimonial2_image": testimonial2_image,
        "testimonial3_image": testimonial3_image,
        "testimonial4_image": testimonial4_image,
        "testimonial5_image": testimonial5_image,
        "testimonial6_image": testimonial6_image,
        "testimonial1_name": testimonial1_name,
        "testimonial2_name": testimonial2_name,
        "testimonial3_name": testimonial3_name,
        "testimonial4_name": testimonial4_name,
        "testimonial5_name": testimonial5_name,
        "testimonial6_name": testimonial6_name,
        "testimonial1_think": testimonial1_think,
        "testimonial2_think": testimonial2_think,
        "testimonial3_think": testimonial3_think,
        "testimonial4_think": testimonial4_think,
        "testimonial5_think": testimonial5_think,
        "testimonial6_think": testimonial6_think,
        "skills": skills,
        "social_medias": social_medias,
    }

    return render(request, "index.html", context=context)
from django.db import models

# Create your models here.

# Home Model
class HomeModel(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=300)
    profession=models.CharField(max_length=150)

    def __str__(self):
        return self.title

# About Model
class AboutModel(models.Model):
    about_image=models.ImageField(upload_to='About/')
    description=models.TextField()
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=20)
    job_title=models.CharField(max_length=200)
    location=models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Skill Model
class SkillModel(models.Model):
    logo=models.ImageField(upload_to='skill/')
    title=models.TextField()
    progress_bar=models.IntegerField(default=70)

    def __str__(self):
        return self.title


# Services Model
class ServicesModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title

# Handel Model
class HandelModel(models.Model):
    total=models.IntegerField(default=70)
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title


# Portfolio Model
class PortfolioModel(models.Model):
    portfolio_image=models.ImageField(upload_to='Portfolio/')
    title=models.CharField(max_length=100)
    profession=models.CharField(max_length=200)
    category=models.ForeignKey("PortfolioCategoryModel",on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Portfolio Category Model
class PortfolioCategoryModel(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name


# Client Model
class ClientModel(models.Model):
    client_image=models.ImageField(upload_to='Client/')
    title=models.CharField(max_length=100)
    profession=models.CharField(max_length=200)
    description=models.TextField()
   
    def __str__(self):
        return self.title

    
# Team Model
class TeamModel(models.Model):
    team_img=models.ImageField(upload_to='Team/')
    title=models.CharField(max_length=100)
    profession=models.CharField(max_length=200)
   
    def __str__(self):
        return self.title

# CompamyBrand Model
class CompamyBrandModel(models.Model):
    brand_image=models.ImageField(upload_to='Brand/')
   
    def __str__(self):
        return self.title


# Blog Model
class BlogModel(models.Model):
    blog_img=models.ImageField(upload_to='Blog/')
    published=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=300)
    description=models.TextField()
    read_more=models.URLField(max_length=900)
   
    def __str__(self):
        return self.title

# Contact Model
class ContactModel(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=300)
    message=models.TextField()

    def __str__(self):
        return self.email


# Footer Model
class FooterModel(models.Model):
    number=models.CharField(max_length=300)
    email=models.EmailField(max_length=254)
    location=models.CharField(max_length=300)
    Copy_right=models.TextField()
    fb_link=models.URLField(max_length=900)
    twitter_link=models.URLField(max_length=900)
    linkdin_link=models.URLField(max_length=900)
    googleplus_link=models.URLField(max_length=900)

    def __str__(self):
        return self.email


# python manage.py migrate
# python manage.py makemigrations
# python manage.py runserver
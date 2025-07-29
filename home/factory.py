import factory
from django.contrib.auth.models import User
from . models import Blog, Profile
from faker import Faker
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
import requests
from django.core.files.base import ContentFile

def generate_img_file(name='image.jpg', size=(100,100), color= (73,109,137)):
    image = Image.new('RGB',size,color)
    buffer = BytesIO()
    image.save(buffer, format= 'JPEG')
    return SimpleUploadedFile(name, buffer.getvalue(),content_type='image/jpeg')


faker = Faker()

class Userfactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('user_name')

class Profilefactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
    user = factory.SubFactory(Userfactory)     
    bio = factory.Faker('text', max_nb_chars= 100)   
    profile_pic = factory.LazyFunction(lambda: generate_img_file(name='profile_pic'))

class Blogfactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog
    title = factory.Faker('name')    
    desc = factory.Faker ("sentence", nb_words= 50)
    author = factory.SubFactory(Userfactory)

    @factory.lazy_attribute
    def img(self):
        url = 'https://picsum.photos/id/16/2500/1667'
        resp = requests.get(url)
        return ContentFile(resp.content, name='blog.jpg')
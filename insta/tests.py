from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User
 # Create your tests here.


class ProfileTestCase(TestCase):


    
    # SetUp method
    def setUp(self):
        
        #creating a user instance
        self.user = User(username="chris",email="ckaringe@gmail.com",password="blackpool005")
        self.image = Profile(user=self.user,profile_avatar="ben_H62Kawu.jpeg",bio="Rolls-Royce Wraith")

        def tearDown(self):
            User.objects.all().delete()
            Image.objects.all().delete()
            
        # Testing Instance
        def test_instance(self):
            self.assertTrue(isinstance(self.image,Image))
            
    def test_save_profile(self):
        new_user = User(id=1,username="chris",email="ckaringe@gmail.com",password="blackpool005")
        new_user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>=1)
        
    def test_delete_profile(self):
        new_user = User(id=1,username="chris",email="ckaringe@gmail.com",password="blackpool005")
        new_user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)<=0)
class ImageTestCase(TestCase):
    
    # SetUp method
    def setUp(self):
        #creating a user instance
        self.user = User(username="chris",email="ckaringeg@gmail.com",password="blackpool005")
        self.image = Image(image="default.jpg",tag_someone="ben2_2HRlWyC.jpeg",image_caption="ai at its best")

    def tearDown(self):
        User.objects.all().delete()
        Image.objects.all().delete()
        
    # Testing Instance

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
            
    def test_save_image(self):
        new_image =Image(image="default.jpg",tag_someone="ben2_2HRlWyC.jpeg",image_caption="ai at its best")
        new_image.save()
        images = Image.objects.all()
        self.assertTrue(len(images)>=1)
        
    def test_delete_image(self):
       new_image =Image(id=1,image="default.jpg",tag_someone="ben2_2HRlWyC.jpeg",image_caption="ai at its best")
       new_image.delete()
       images = Image.objects.all()
       self.assertTrue(len(images)==0)
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CV, Comment, Education, Experience, Skill, UserRegular
from .serializers import (CommentSerializer, CVSerializer, EducationSerializer,
                          ExperienceSerializer, SkillSerializer,
                          UserProfileSerializer, UserRegularSerializer)
from django.views.decorators.csrf import csrf_protect


class DisplayPages:
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def login(request):
        return render(request, 'login.html')

    def register(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            return redirect('http://127.0.0.1:8000/login')
        else:
            return render(request,'register.html')


    def login_page(request):
        error_message = None  
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('http://127.0.0.1:8000/homepage/')
            else:
                error_message = "Hatalı kullanıcı adı veya şifre. Lütfen tekrar deneyin."

            return render(request, 'error.html', {'error_message': error_message})
        else:
            return redirect('http://127.0.0.1:8000')

    def homepage(request):
        return render(request, 'homepage.html')

    def cv_adjust(request):
        return render(request, 'adjustment.html')

    def cv_create(request):
        return render(request, 'create.html')

    def cv_detail(request, cv_id):
        cvs = CV.objects.get(pk=cv_id)
        cv_serializer = CVSerializer(cvs)

        experiences = Experience.objects.get(pk=cv_id)
        experience_serializer = ExperienceSerializer(experiences)

        educations = Education.objects.get(pk=cv_id)
        educations_serializer = EducationSerializer(educations)

        skills = Skill.objects.get(pk=cv_id)
        skills_serializer = SkillSerializer(skills)

        context = {
            'about_me': cv_serializer.data,
            'experience': experience_serializer.data,
            'education': educations_serializer.data,
            'skill': skills_serializer.data,
        }

        return render(request, 'base.html', context)

    def cvall(request):
        cvs = CV.objects.all()
        cv_serializer = CVSerializer(cvs, many=True)

        context = {
            'about_me': cv_serializer.data,
        }

        return render(request, 'cvall.html', context)

    def submit_comment(request):
        if request.method == 'POST':
            form = CommentSerializer(data=request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'homepage.html', {'form': form, 'success_message': 'Yorumunuz başarıyla gönderildi.'})
            else:
                form = CommentSerializer()
        return render(request, 'homepage.html', {'form': form})

    def update_cv(request, cv_id):
        if request.method == 'POST':
            full_name = request.POST.get('full_name')
            telephone = request.POST.get('telephone')
            location = request.POST.get('location')
            about_me = request.POST.get('about_me')
            email = request.POST.get('e_mail')

            cv_instance = CV.objects.get(pk=cv_id)
            cv_instance.full_name = full_name
            cv_instance.phone_number = telephone
            cv_instance.address = location
            cv_instance.additional_information = about_me
            cv_instance.email = email

            cv_instance.save()

            skills = request.POST.get('skills')
            skill_instance = Skill.objects.get(pk=cv_id)
            skill_instance.name = skills

            skill_instance.save()

            degree = request.POST.get('degree')
            institution = request.POST.get('institution')
            educate_location = request.POST.get('educate_location')
            graduation_date = request.POST.get('graduation_date')

            education_instance = Education.objects.get(pk=cv_id)
            education_instance.degree = degree
            education_instance.institution = institution
            education_instance.location = educate_location
            education_instance.graduation_date = graduation_date

            education_instance.save()

            title = request.POST.get('title')
            company = request.POST.get('company')
            experience_location = request.POST.get('experience_location')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            description = request.POST.get('description')

            experience_instance = Experience.objects.get(pk=cv_id)
            experience_instance.title = title
            experience_instance.company = company
            experience_instance.location = experience_location
            experience_instance.start_date = start_date
            experience_instance.end_date = end_date
            experience_instance.description = description

            experience_instance.save()
            print("asdas")
            return redirect('http://127.0.0.1:8000/cv_all')
        else:
            context = {
                'id': cv_id
            }
            return render(request, 'adjustment.html', context)

    def cvcreate(request):
        if request.method == 'POST':
            full_name = request.POST.get('full_name')
            telephone = request.POST.get('telephone')
            location = request.POST.get('location')
            about_me = request.POST.get('about_me')
            email = request.POST.get('e_mail')
            skills = request.POST.get('skills')

            cv_instance = CV(
                full_name=full_name,
                phone_number=telephone,
                address=location,
                additional_information=about_me,
                email=email
            )
            cv_instance.save()

            skill_instance = Skill(
                name=skills,
            )
            skill_instance.save()

            degree = request.POST.get('degree')
            institution = request.POST.get('institution')
            educate_location = request.POST.get('educate_location')
            graduation_date = request.POST.get('graduation_date')

            education_instance = Education(
                degree=degree,
                institution=institution,
                location=educate_location,
                graduation_date=graduation_date,
            )
            education_instance.save()

            title = request.POST.get('title')
            company = request.POST.get('company')
            experience_location = request.POST.get('experience_location')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            description = request.POST.get('description')

            experience_instance = Experience(
                title=title,
                company=company,
                location=experience_location,
                start_date=start_date,
                end_date=end_date,
                description=description,
            )
            experience_instance.save()

            return redirect('http://127.0.0.1:8000/cv_all')
        else:
            return HttpResponse("Invalid request method", status=405)

    def comments(request):
        comments = Comment.objects.all()
        comments_serializer = CommentSerializer(comments, many=True)

        return render(request, 'comments.html', {'comments': comments_serializer.data})

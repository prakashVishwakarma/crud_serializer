from django.contrib import admin
from App.models import Task, CrudUser, UserProfile, Author, Book, Student, Course, Enrollment

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'created_at', 'updated_at']

@admin.register(CrudUser)
class CrudUserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'email', 'created_at', 'updated_at']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'bio', 'website', 'created_at', 'updated_at']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'bio', 'created_at', 'updated_at']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'book_name', 'content', 'created_at', 'updated_at']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'created_at', 'updated_at']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'start_date', 'created_at', 'updated_at']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id','student', 'course', 'enrollment_date', 'grade', 'created_at', 'updated_at']
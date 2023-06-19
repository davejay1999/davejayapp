import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_package",
    version="v0.0.1",
    install_requires=[
        "Django==3.2.4",
        "django-extensions==3.0.3",
        "django-filter==2.3.0",
        "djangorestframework==3.11.2",
        "django-storages==1.9.1",
        "django-environ==0.4.5",
        "django-cors-headers==3.3.0",
        "django-summernote==0.8.11.6",
        "django-model-utils==4.0.0",
        "django-redis==4.12.1",
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'corsheaders',
        'rest_framework',
        'todo',
    ],
    author="Jay Dave",
    author_email="davejay1999@gmail.com",
    description="Django project",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.9",
    scripts=["manage.py"],
)
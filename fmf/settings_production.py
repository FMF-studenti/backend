"""
Django settings for fmf project - production overrides.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from fmf.settings import *

DEBUG = False
ALLOWED_HOSTS = ['.fmf.si']

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework_ember.renderers.JSONRenderer',
)

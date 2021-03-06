import os

# ROOT_DIR/PROJ_DIR/SITE_DIR
SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.dirname(SITE_DIR)
ROOT_DIR = os.path.dirname(PROJ_DIR)

ALLOWED_HOSTS = [
	'*',
]

# Application definition

INSTALLED_APPS = (
    # Django default apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Wagtail app dependancies.
    'taggit',
    'compressor',
    'modelcluster',
    # Wagtail default apps.
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtailsearch',
    'wagtail.wagtailimages',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailembeds',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    # Make forms pretty.
    'crispy_forms',
    # 
    'django_markup',
    #
    'team',
    #
    'wagtail_blog',
)

MIDDLEWARE_CLASSES = (
    # Django default.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # Wagtail.
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'rjsw.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rjsw.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(ROOT_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')
MEDIA_URL = '/media/'

# Wagtail Settings.

WAGTAIL_SITE_NAME = "RJS"

# Wagtail Blog

WAGTAIL_BLOG_AUTHOR_PAGE = 'team.TeamMemberPage' # your wagtail page model with author information
WAGTAIL_BLOG_POSTS_PER_PAGE = 10 # posts per page on the post listing page
WAGTAIL_BLOG_FEED_TITLE = 'RJS Feed' # RSS / Atom feed custom title, defaults to RSS Feed / Atom Feed
WAGTAIL_BLOG_FEED_DESCRIPTION = 'RJS Feed' # RSS 2.0 / Atom feed custom description, defaults to Blog Post Feed
WAGTAIL_BLOG_FEED_LENGTH = 50 # How many articles are included in the feed, defaults to 50

# Crispy Forms.

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Logging to stderr should end up in "/var/log/apache/error.log".

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            # 'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}


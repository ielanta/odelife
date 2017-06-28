DEBUG = True
ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'odelifedb1',
        'USER': 'postgres',
        'PASSWORD': 'landbreeze',
        'HOST': 'pgdb',
        'PORT': 5432,
    }
}

# ---- COMMON ----

SECRET_KEY = '9$l2tuimb7@*5^3on!0!4nx1+td2h7!=gmw_*t9pd&9&^9v7n8'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = {
	'development': {
		'DEBUG': True,
		'ALLOWED_HOSTS': ['localhost'],
		'STATIC_ROOT': os.path.join(BASE_DIR, 'staticfiles')
	},
	'production': {
		'DEBUG': False,
		'ALLOWED_HOSTS': ['18.188.98.228'],
		'STATIC_ROOT': '/var/www/ayushi/static/'
	}
}
from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=1.00, doc="",
    mturk_hit_settings={'keywords': 'bonus, study', 'title': 'Experiment 2 Part B (few minutes to complete, additional bonus for completion)', 'description': 'Receive an additional bonus for completion.',
                        'frame_height': 500, 'template': 'global/mturk_template.html',
                        'minutes_allotted_per_assignment': 60, 'expiration_hours': 5 * 24,
                        'qualification_requirements': [
                            # Testläufe ausschließen
                            {
                                'QualificationTypeId': "30TX348SI5MJEMQUUDY0XUUD19Q85N",
                                'Comparator': "DoesNotExist",
                                'ActionsGuarded': "DiscoverPreviewAndAccept",
                            },
                            {
                                'QualificationTypeId': "3P1HXW38ULF39NSV32V3NZ34W9K5K3",
                                'Comparator': "DoesNotExist",
                                'ActionsGuarded': "DiscoverPreviewAndAccept",
                            },
                            # Only US
                            # {
                            #     'QualificationTypeId': "00000000000000000071",
                            #     'Comparator': "EqualTo",
                            #     'LocaleValues': [{'Country': "US"}]
                            # },
                            # At least 500 HITs approved
                            {
                                'QualificationTypeId': "00000000000000000040",
                                'Comparator': "GreaterThanOrEqualTo",
                                'IntegerValues': [500]
                            },
                            # At least 95% of HITs approved
                            {
                                'QualificationTypeId': "000000000000000000L0",
                                'Comparator': "GreaterThanOrEqualTo",
                                'IntegerValues': [95]
                            },
                            # Experiment 2 Part A Participation: INCLUDE ONLY FORMER PARTICIPANTS
                            {
                                'QualificationTypeId': "30IMA0M1DBV3KT3P2VV42SCTFVOOUP",
                                'Comparator': "Exists",
                                'ActionsGuarded': "DiscoverPreviewAndAccept",
                            },
                            # Experiment 2 Part B Participation: EXCLUDE RETAKERS
                            {
                                'QualificationTypeId': "3BIT4H6AA7JC3S273ZARAJOR45X5IU",
                                'Comparator': "DoesNotExist",
                                'ActionsGuarded': "DiscoverPreviewAndAccept",
                            },
                        ],
                        # Experiment 2 Part B Participation
                        'grant_qualification_id': '3BIT4H6AA7JC3S273ZARAJOR45X5IU'}
)


SESSION_CONFIGS = [
    dict(
        name='Experiment2',
        display_name="Experiment 2 (Behavior) Part B",
        num_demo_participants=100,
        app_sequence=['Introduction', 'Main']
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'ECU'

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '#hjd89#!rzgt$lp**+!3go*m@-u%y&l--_rhjitxeh2w0-@-rd'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
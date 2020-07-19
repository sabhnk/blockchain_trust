from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


class Constants(BaseConstants):
    name_in_url = 'Filler_task'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(label='What is your age?', min=13, max=125)

    gender = models.IntegerField(
        choices=[[1, 'Female'],
                 [2, 'Male'],
                 [3, 'Other'],
                 [4, 'Prefer not to say']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    education = models.IntegerField(
        choices=[[1, 'Less than high school diploma'],
                 [2, 'High school degree or equivalent'],
                 [3, 'Bachelors degree'],
                 [4, 'Masters degree'],
                 [5, 'Doctorate'],
                 [6, 'Other']],
        label='What is the highest educational degree you have completed?',
        widget=widgets.RadioSelect,
    )

    employment = models.IntegerField(
        label='What is your current employment?',
        choices=[[1, 'Full-time (38 hours/week or more)'],
                 [2, 'Part-time (less than 38 hours/week)'],
                 [3, 'Unemployed'],
                 [4, 'Self-employed'],
                 [5, 'Student'],
                 [6, 'Retired'],
                 [7, 'Unable to work'],
                 [8, 'Other']],
        widget=widgets.RadioSelect,
    )

    income = models.IntegerField(
        label='What is your yearly household income?',
        choices=[[1, 'below 10,000$'],
                 [2, '10,000$ - 24,999$'],
                 [3, '25,000$ - 49,999$'],
                 [4, '50,000$ - 74,999$'],
                 [5, '75,000$ - 99,999$'],
                 [6, '100,000$ - 149,999$'],
                 [7, '150,000$ and above']
                 ],
        widget=widgets.RadioSelect,
    )

    crt_bat = models.IntegerField(
        label='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )

    crt_widget = models.IntegerField(
        label='''
        "If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?"
        '''
    )

    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )

    teaser1 = models.IntegerField(
        label='''
        Add together three of the following numbers, so that they score 30. Each number can be used multiple times.
        How many combinations are there to achieve this?
        
        1 | 2 | 4 | 6 | 8 | 20 | 22 | 24 | 25 '''
    )

    teaser2 = models.StringField(
        label='''Which letter is missing in the following sequence?
        
        O | U | ? | H | R | A | U '''
    )
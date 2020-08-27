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
import random

author = 'Sabrina Hinkerohe'

doc = """
Experiment 2 (Behavior) : Part A
"""


class Constants(BaseConstants):
    name_in_url = 'Introduction'
    players_per_group = None
    num_rounds = 1


# Treatment / Control Group
class Subsession(BaseSubsession):

    def creating_session(self):
        # self.get_players(): Returns a list of all the players in the subsession.
        for player in self.get_players():
            # attribute will be kept for multiple rounds, because it is couples with participant not player
            player.participant.vars['transparent_PartA'] = random.choice([True, False])
            player.participant.vars['correct_confirmatory_questions_PartA'] = False
            player.participant.vars['intimeB'] = True


class Group(BaseGroup):
    pass


def likert7(label):
    return models.IntegerField(
        # users see choice options and answers will be stored as integers
        label=label,
        choices=[
            [1, 'I strongly disagree'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'I strongly agree'],
        ],
        widget=widgets.RadioSelect
    )


def likert_lowhigh(label):
    return models.IntegerField(
        # users see choice options and answers will be stored as integers
        label=label,
        choices=[
            [1, 'Very low'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'Very high'],
        ],
        widget=widgets.RadioSelect
    )


class Player(BasePlayer):
    manipulation = likert_lowhigh('Please rate how you see the level of transparency in this study.')

    confirm_1 = models.IntegerField(
        label='You are Player A. When you sent 300 ECU to Player B, how much will Player B receive?',
        choices=[
            [1, '300 ECU'],
            [2, '900 ECU'],
            [3, '100 ECU'],
        ],
        widget=widgets.RadioSelect
    )

    confirm_2 = models.IntegerField(
        label='You are Player B. When you receive 300 ECU from Player A, how much did Player A send?',
        choices=[
            [1, '300 ECU'],
            [2, '900 ECU'],
            [3, '100 ECU'],
        ],
        widget=widgets.RadioSelect
    )

    confirm_3 = models.IntegerField(
        label='Your transaction details will be visible for…?',
        choices=[
            [1, '...myself only'],
            [2, '...myself and my partner'],
            [3, '...myself, my partner and all other participants (publicly visible)'],
        ],
        widget=widgets.RadioSelect
    )

    confirm_4 = models.IntegerField(
        label='Your payoff directly depends on…?',
        choices=[
            [1, '...my own decisions only'],
            [2, '...my partners decisions only'],
            [3, '...my own and my partners decision'],
        ],
        widget=widgets.RadioSelect
    )

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
Experiment 2 (Behavior) : Part B
"""


class Constants(BaseConstants):
    name_in_url = 'PartB_Introduction'
    players_per_group = None
    num_rounds = 1


# Treatment / Control Group
class Subsession(BaseSubsession):

    def creating_session(self):
        # if self.round_number == 1:
        for player in self.get_players():
            # attribute will be kept for multiple rounds, because it is couples with participant not player
            player.participant.vars['transparent_PartB'] = random.choice([True, False])
            player.participant.vars['correct_confirmatory_questions_PartB'] = False


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

# def likert7(label):
#     return models.IntegerField(
#         label=label,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         widget=widgets.RadioSelect
#     )


class Player(BasePlayer):

    manipulation = likert7('The setting of this financial transaction makes me feel transparent.')

    confirm_1 = models.IntegerField(
        label='When you sent 90 ECU to Player B, how much will Player B receive?',
        choices=[
            [1, '90 ECU'],
            [2, '270 ECU'],
            [3, '30 ECU'],
        ],
        widget=widgets.RadioSelect
    )

    confirm_2 = models.IntegerField(
        label='When you receive 90 ECU from Player A, how much did Player A send?',
        choices=[
            [1, '90 ECU'],
            [2, '270 ECU'],
            [3, '30 ECU'],
        ],
        widget=widgets.RadioSelect
    )

    confirm_3 = models.IntegerField(
        label='My pay-out directly depends on…?',
        choices=[
            [1, '...my own decisions only'],
            [2, '...my partners decisions only'],
            [3, '...my own and my partners decision'],
        ],
        widget=widgets.RadioSelect
    )

    confirm_4 = models.IntegerField(
        label='My transaction details will be visible for…?',
        choices=[
            [1, '...myself only'],
            [2, '...myself and my partner'],
            [3, '...myself, my partner and all other participants'],
        ],
        widget=widgets.RadioSelect
    )

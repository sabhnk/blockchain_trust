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
Experiment 1 (Intention) : Part B
"""


class Constants(BaseConstants):
    name_in_url = 'PartB'
    players_per_group = None
    num_rounds = 1

    endowment = c(50)
    completion_payoff = c(10)


# Treatment / Control Group
class Subsession(BaseSubsession):

    def creating_session(self):
        # self.get_players(): Returns a list of all the players in the subsession.
        for player in self.get_players():
            # attribute will be kept for multiple rounds, because it is couples with participant not player
            if player.participant.vars['transparent_PartA']:
                player.participant.vars['transparent_PartB'] = False
            else:
                player.participant.vars['transparent_PartB'] = True


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
#         # users see choice options and answers will be stored as integers
#         label=label,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         widget=widgets.RadioSelect
#     )


class Player(BasePlayer):

    manipulation = likert7('The setting of this financial transaction makes me feel transparent.')

    intention = models.BooleanField(
        label='Would you conclude a transaction on the blockchain network?',
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ],
        widget=widgets.RadioSelect
    )

    intention_amount = models.CurrencyField(
        label="What amount would you use to transact and send to Player B?",
    )

    pc_1 = likert7('I am concerned that the information I provide to the blockchain network could be misused.')
    pc_2 = likert7(
        'I am concerned that anyone will be able to find private information about me on the blockchain network.')
    pc_3 = likert7(
        'I am concerned about submitting information on the blockchain network, because it could be used in a way I did not foresee.')

    benefit_1 = likert7('Transacting on the blockchain network offers benefits for me.')
    benefit_2 = likert7('Transacting on the blockchain network will lead to economic benefits for me.')
    benefit_3 = likert7('I expect financial benefit form transacting on the blockchain network.')

    attention = models.IntegerField(
        label='What would be your ideal holiday destination?',
        blank=True,
        choices=[
            [1, 'Beach vacation'],
            [2, 'City trip'],
            [3, 'Cultural tour'],
            [4, 'Adventure holiday'],
            [5, 'Skiing holiday'],
            [6, 'Cruise'],
            [7, 'Other'],
        ],
        widget=widgets.RadioSelect
    )

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
        label='Your pay-out directly depends on…?',
        choices=[
            [1, '...my own decisions only'],
            [2, '...my partners decisions only'],
            [3, '...my own and my partners decision'],
        ],
        widget=widgets.RadioSelect
    )

    confirm_4 = models.IntegerField(
        label='Your transaction details will be visible for…?',
        choices=[
            [1, '...myself only'],
            [2, '...myself and my partner'],
            [3, '...myself, my partner and all other participants (publicly visible)'],
        ],
        widget=widgets.RadioSelect
    )

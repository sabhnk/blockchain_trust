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
    completion_payoff = c(100)

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
    code_confirmation = models.BooleanField(
        label='I understand that without the code I cannot collect my payoff.',
        choices=[
            [True, 'Yes']
        ],
        widget=widgets.RadioSelect
    )
    transparent = models.BooleanField()
    manipulation = likert_lowhigh('Please rate how you see the level of transparency in this situation.')

    intention = models.BooleanField(
        label='Would you conclude a transaction in the described situation?',
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ],
        widget=widgets.RadioSelect
    )

    intention_amount = models.CurrencyField(
        label="What amount would you send to Player B? (If you answered 'No' above, please set the amount to 0)",
    )

    pc_1 = likert7('I am concerned that the information I provide in this situation could be misused.')
    pc_2 = likert7(
        'I am concerned that anyone will be able to find private information about me in this situation.')
    pc_3 = likert7(
        'I am concerned about submitting information in this situation, because it could be used in a way I did not foresee.')

    benefit_1 = likert7('Transacting in this situation offers benefits for me.')
    benefit_2 = likert7('Transacting in this situation will lead to economic benefits for me.')
    benefit_3 = likert7('I expect financial benefit form transacting in this situation.')

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
    )

    # confirm_1 = models.IntegerField(
    #     label='You are Player A. When you send 300 ECU to Player B, how much will Player B receive?',
    #     choices=[
    #         [1, '300 ECU'],
    #         [2, '900 ECU'],
    #         [3, '100 ECU'],
    #     ],
    #     widget=widgets.RadioSelect
    # )
    #
    # confirm_2 = models.IntegerField(
    #     label='You are Player B. When you receive 300 ECU from Player A, how much did Player A send?',
    #     choices=[
    #         [1, '300 ECU'],
    #         [2, '900 ECU'],
    #         [3, '100 ECU'],
    #     ],
    #     widget=widgets.RadioSelect
    # )

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

    confirm_5 = models.IntegerField(
        label='What is the multiplier that is applied to every amount, that Player A sends to Player B?',
        choices=[
            [1, 'The amount is doubled ( x2 )'],
            [2, 'The amount is tripled ( x3 )'],
            [3, 'The amount stays the same ( x1 )'],
        ],
        widget=widgets.RadioSelect
    )

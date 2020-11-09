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
Experiment 2 (Behavior)
"""


class Constants(BaseConstants):
    name_in_url = 'Experiment2_PartA'
    players_per_group = 2
    num_rounds = 1

    completion_payoff = c(100)
    endowment = c(50)
    multiplication_factor = 3


# Treatment / Control Group
class Subsession(BaseSubsession):

    # creating_session gets executed for each round independently
    def creating_session(self):
        for group in self.get_groups():
            group.transparent = random.choice([True, False])
        # self.get_players(): Returns a list of all the players in the subsession.
        for player in self.get_players():
            player.correct_confirmatory_questions = False


class Group(BaseGroup):
    transparent = models.BooleanField()

    sent_amount = models.CurrencyField(
        label="How much do you want to send to Player B?"
    )
    sent_back_amount = models.CurrencyField(
        label="How much do you want to send back to Player A?"
    )

    def sent_back_amount_choices(self):
        return currency_range(
            c(0),
            self.sent_amount * Constants.multiplication_factor,
            c(1)
        )

    def set_payoffs(self):
        playerA = self.get_player_by_id(1)
        playerB = self.get_player_by_id(2)
        playerA.participant.payoff += Constants.endowment - self.sent_amount + self.sent_back_amount
        playerB.participant.payoff += self.sent_amount * Constants.multiplication_factor - self.sent_back_amount




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
    transparent = models.BooleanField()
    correct_confirmatory_questions = models.BooleanField
    manipulation = likert_lowhigh('Please rate how you see the level of transparency in this situation.')

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

    def role(self):
        if self.id_in_group == 1:
            return 'sender'
        else:
            return 'recipient'

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

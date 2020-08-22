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
    name_in_url = 'PartB'
    players_per_group = 2
    num_rounds = 1

    endowment = c(50)
    multiplication_factor = 3


# Treatment / Control Group
class Subsession(BaseSubsession):
    # is executed each time, a player arrives on the wait page

    def group_by_arrival_time_method(self, waiting_players):
        # put waiting players onto two separate lists according to attribute transparent_PartB
        transparent_players_role1 = [player for player in waiting_players if player.participant.vars['transparent_PartB'] == True and player.participant.vars['id_in_group_PartA'] == 1]
        transparent_players_role2 = [player for player in waiting_players if player.participant.vars['transparent_PartB'] == True and player.participant.vars['id_in_group_PartA'] == 2]
        nontransparent_players_role1 = [player for player in waiting_players if player.participant.vars['transparent_PartB'] == False and player.participant.vars['id_in_group_PartA'] == 1]
        nontransparent_players_role2 = [player for player in waiting_players if
                                        player.participant.vars['transparent_PartB'] == False and
                                        player.participant.vars['id_in_group_PartA'] == 2]

        # put first player of each list together in one group
        if len(transparent_players_role1) > 0 and len(transparent_players_role2) > 0:
            # create group
            return [transparent_players_role1[0], transparent_players_role2[0]]
        elif len(nontransparent_players_role1) > 0 and len(nontransparent_players_role2) > 0:
            # create group
            return [nontransparent_players_role1[0], nontransparent_players_role2[0]]


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        label="How much do you want to send to participant B?"
    )
    sent_back_amount = models.CurrencyField(
        label="How much do you want to send back?"
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
        playerA.payoff += Constants.endowment - self.sent_amount + self.sent_back_amount
        playerB.payoff += self.sent_amount * Constants.multiplication_factor - self.sent_back_amount


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

    def role(self):
        if self.id_in_group == 1:
            return 'sender'
        else:
            return 'recipient'

    manipulation = likert7('The setting of this financial transaction makes me feel transparent.')
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
    )

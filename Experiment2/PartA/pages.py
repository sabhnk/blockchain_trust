from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class ShuffleWaitPage(WaitPage):
    # only for players with correct answers to confirmatory questions
    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']

    group_by_arrival_time = True



    # TODO: for PartB: shuffle partner, but A stays A
    # shuffle players between groups but keep players in fixed roles: aus Subsession
    # self.group_randomly(fixed_id_in_group=True)
    #
    #
    # after_all_players_arrive = 'do_my_shuffle'


class Experimental_Part_Send(Page):
    # condition-specific
    form_model = 'player'
    form_fields = ['sent_amount']

    def is_displayed(self):
        # exclude player with incorrect answers to confirmaotry questions & only show to Player A of group
        return self.participant.vars['correct_confirmatory_questions_PartA'] and self.player.id_in_group == 1


class Wait_for_PlayerA(WaitPage):
    def is_displayed(self):
        # do not show for player that did not get sorted into groups due to incorrect answers
        return self.participant.vars['correct_confirmatory_questions_PartA']
    pass


class Experimental_Part_SendBack(Page):

    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.correct_confirmatory_questions and self.player.id_in_group == 2

    def vars_for_template(self):
        return dict(
            tripled_amount=self.group.sent_amount * Constants.multiplication_factor
        )


class Wait_for_PlayerB(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Attention_Check(Page):
    # same for each participant
    form_model = 'player'
    form_fields = ['attention']

    def is_displayed(self):
        return self.player.correct_confirmatory_questions


class Survey(Page):
    # condition-specific
    form_model = 'player'
    form_fields = ['pc_1', 'pc_2', 'pc_3', 'benefit_1', 'benefit_2', 'benefit_3', ]

    def is_displayed(self):
        return self.player.correct_confirmatory_questions

    # calculate payoff
    def before_next_page(self):
        self.participant.payoff += self.player.current_balance
        self.player.current_balance -= self.player.current_balance



class Results(Page):
    pass


page_sequence = [ShuffleWaitPage, Experimental_Part_Send, Wait_for_PlayerA, Experimental_Part_SendBack, Wait_for_PlayerB, Attention_Check, Survey, Results]

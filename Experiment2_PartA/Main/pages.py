from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ShuffleWaitPage(WaitPage):
    body_text = "Please wait for the other Player to arrive."

    # only for players with correct answers to confirmatory questions
    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']

    group_by_arrival_time = True

    def before_next_page(self):
        # if self.timeout_happened:
        self.participant.vars['intimeB'] = True


class Experimental_Part_Send(Page):
    # condition-specific
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        # exclude player with incorrect answers to confirmatory questions & only show to Player A of group
        return self.participant.vars['correct_confirmatory_questions_PartA'] and self.player.id_in_group == 1


class Wait_for_PlayerA(WaitPage):
    body_text = "Please wait for the other Player to make their choice."

    def is_displayed(self):
        # do not show for player that did not get sorted into groups due to incorrect answers
        return self.participant.vars['correct_confirmatory_questions_PartA']


class Experimental_Part_SendBack(Page):
    timeout_seconds = 60

    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        # exclude player with incorrect answers to confirmatory questions & only show to Player B of group
        return self.participant.vars['correct_confirmatory_questions_PartA'] and self.player.id_in_group == 2

    def vars_for_template(self):
        return dict(
            tripled_amount=self.group.sent_amount * Constants.multiplication_factor
        )

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['intimeB'] = False


class Attention_Check(Page):

    # same for each participant
    form_model = 'player'
    form_fields = ['attention']

    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA'] and self.participant.vars['intimeB']


class Survey(Page):

    # condition-specific
    form_model = 'player'
    form_fields = ['pc_1', 'pc_2', 'pc_3', 'benefit_1', 'benefit_2', 'benefit_3', ]

    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA'] and self.participant.vars['intimeB']


class Wait_for_PlayerB(WaitPage):
    body_text = "Please wait for the other Player. Information from the other Player is needed to calculate your payoff."

    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA'] and self.participant.vars['intimeB']

    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [ShuffleWaitPage, Experimental_Part_Send, Wait_for_PlayerA, Experimental_Part_SendBack,
                 Attention_Check, Survey, Wait_for_PlayerB, Results]

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class ShuffleWaitPage(WaitPage):
    group_by_arrival_time = True

class Welcome(Page):
    def before_next_page(self):
        if self.group.transparent:
            self.player.transparent = True
        else:
            self.player.transparent = False


class Instructions(Page):
    # condition-specific
    # same questions, but answers are condition specific
    form_model = 'player'
    form_fields = ['confirm_3', 'confirm_4', 'confirm_5']

    # 3 Questions Fields
    def before_next_page(self):
        if self.player.transparent:
            # alle Antworten sind richtig
            if (self.player.confirm_3 == 3 and self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                self.participant.payoff += Constants.completion_payoff
                self.player.correct_confirmatory_questions = True
            else:
                self.player.correct_confirmatory_questions = False
                # self.participant.payoff = c(0)
        else:
            # alle Antworten sind richtig
            if (self.player.confirm_3 == 2 and self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                self.participant.payoff += Constants.completion_payoff
                self.player.correct_confirmatory_questions = True
            else:
                self.player.correct_confirmatory_questions = False
                # self.participant.payoff = c(0)

class Confirmatory_Results(Page):
    pass


class Manipulation_Check(Page):
    # same for each participant
    form_model = 'player'
    form_fields = ['manipulation']


class Experimental_Part_Send(Page):
    # condition-specific
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        # only show to Player A of group
        return self.player.id_in_group == 1


class Wait_for_PlayerA(WaitPage):
    pass

class Experimental_Part_SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        # only show to Player B of group
        return self.player.id_in_group == 2

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


class Survey(Page):
    # condition-specific
    form_model = 'player'
    form_fields = ['pc_1', 'pc_2', 'pc_3', 'benefit_1', 'benefit_2', 'benefit_3', ]


class Results(Page):
    form_model = 'player'
    form_fields = ['code_confirmation']


page_sequence = [ShuffleWaitPage, Welcome, Instructions, Confirmatory_Results, Manipulation_Check, Experimental_Part_Send, Wait_for_PlayerA, Experimental_Part_SendBack,
                 Wait_for_PlayerB, Attention_Check, Survey, Results]

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass


class Instructions(Page):
    # condition-specific
    form_model = 'player'

    def before_next_page(self):
        self.player.correct_confirmatory_questions = False


class Confirmatory_Questions(Page):
    # same questions, but answers are condition specific
    form_model = 'player'
    form_fields = ['confirm_1', 'confirm_2', 'confirm_3', 'confirm_4']

    # if answers are wrong, set payout to 0

    def before_next_page(self):
        if self.player.transparent:
            if (self.player.confirm_1 != 2) or (self.player.confirm_2 != 3) or (self.player.confirm_3 != 3) or (
                    self.player.confirm_4 != 3):
                self.participant.payoff = c(0)
        else:
            if (self.player.confirm_1 != 2) or (self.player.confirm_2 != 3) or (self.player.confirm_3 != 3) or (
                    self.player.confirm_4 != 2):
                self.participant.payoff = c(0)


class Confirmatory_Wrong(Page):
    form_model = 'player'

    def is_displayed(self):
        if self.player.transparent:
            if (self.player.confirm_1 != 2) or (self.player.confirm_2 != 3) or (self.player.confirm_3 != 3) or (
                    self.player.confirm_4 != 3):
                return True
            else:
                return False
        else:
            if (self.player.confirm_1 != 2) or (self.player.confirm_2 != 3) or (self.player.confirm_3 != 3) or (
                    self.player.confirm_4 != 2):
                return True
            else:
                return False



class Manipulation_Check(Page):
    # same for each participant
    form_model = 'player'
    form_fields = ['manipulation']

    def is_displayed(self):
        if self.player.transparent:
            if (self.player.confirm_1 == 2) and (self.player.confirm_2 == 3) and (self.player.confirm_3 == 3) and (
                    self.player.confirm_4 == 3):
                return True
            else:
                return False
        else:
            if (self.player.confirm_1 == 2) and (self.player.confirm_2 == 3) and (self.player.confirm_3 == 3) and (
                    self.player.confirm_4 == 2):
                return True
            else:
                return False


    def before_next_page(self):
        # exit experiment
        self.player.current_balance = 10
        self.player.correct_confirmatory_questions = True


class Experimental_Part(Page):
    # condition-specific
    form_model = 'player'
    form_fields = ['intention', 'intention_amount']

    def is_displayed(self):
        return self.player.correct_confirmatory_questions

    def error_message(self, values):
            if values['intention_amount'] < c(0):
                return 'The amount cannot be negative.'
            else:
                if values['intention']:
                    if values['intention_amount'] > self.player.current_balance:
                        return 'The amount cannot be higher than your current balance.'
                    elif values['intention_amount'] == c(0):
                        return 'You cannot simultaneously state "Yes" and set the amount to 0.'
                else:
                    if values['intention_amount'] != c(0):
                        return 'You cannot state "No" and set an amount different than 0.'


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


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Welcome, Instructions, Confirmatory_Questions, Confirmatory_Wrong, Manipulation_Check,
                 Experimental_Part, Attention_Check, Survey, Results]

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass


class Instructions(Page):
    # condition-specific
    pass


class Confirmatory_Questions(Page):
    # same questions, but answers are condition specific
    form_model = 'player'
    form_fields = ['confirm_1', 'confirm_2', 'confirm_3', 'confirm_4']

    # if answers are wrong, set payout to 0
    def before_next_page(self):
        if self.participant.vars['transparent_PartA']:
            if (self.player.confirm_1 != 2) or (self.player.confirm_2 != 3) or (self.player.confirm_3 != 3) or (
                    self.player.confirm_4 != 3):
                self.participant.payoff = c(0)
                self.participant.vars['correct_confirmatory_questions_PartA'] = False
            else:
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
        else:
            if (self.player.confirm_1 != 2) or (self.player.confirm_2 != 3) or (self.player.confirm_3 != 3) or (
                    self.player.confirm_4 != 2):
                self.participant.payoff = c(0)
                self.participant.vars['correct_confirmatory_questions_PartA'] = False
            else:
                self.participant.vars['correct_confirmatory_questions_PartA'] = True


class Confirmatory_Results(Page):
    pass


class Manipulation_Check(Page):
    # same for each participant
    form_model = 'player'
    form_fields = ['manipulation']

    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']



class Experimental_Part(Page):
    # condition-specific
    form_model = 'player'
    form_fields = ['intention', 'intention_amount']

    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']

    def error_message(self, values):
            if values['intention_amount'] < c(0):
                return 'The amount cannot be negative.'
            else:
                if values['intention']:
                    if values['intention_amount'] > Constants.endowment:
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
        return self.participant.vars['correct_confirmatory_questions_PartA']


class Survey(Page):
    # condition-specific
    form_model = 'player'
    form_fields = ['pc_1', 'pc_2', 'pc_3', 'benefit_1', 'benefit_2', 'benefit_3', ]

    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']


class Results(Page):
    pass


page_sequence = [Welcome, Instructions, Confirmatory_Questions, Confirmatory_Results, Manipulation_Check,
                 Experimental_Part, Attention_Check, Survey, Results]

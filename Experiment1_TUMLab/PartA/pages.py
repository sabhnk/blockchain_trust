from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    def before_next_page(self):
        if self.participant.vars['transparent_PartA']:
            self.player.transparent = True


class Instructions(Page):
    # condition-specific
    # same questions, but answers are condition specific
    form_model = 'player'
    form_fields = ['confirm_3', 'confirm_4', 'confirm_5']

    # 3 Questions Fields
    def before_next_page(self):
        if self.participant.vars['transparent_PartA']:
            # alle Antworten sind richtig
            if (self.player.confirm_3 == 3 and self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                self.participant.payoff += Constants.completion_payoff
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # # Antworten 3,4 richtig
            # elif (self.player.confirm_3 == 3 and self.player.confirm_4 == 3):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # # Antworten 3,5 richtig
            # elif (self.player.confirm_3 == 3 and self.player.confirm_5 == 2):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # # Antworten 4,5 richtig
            # elif (self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartA'] = True
            else:
                self.participant.vars['correct_confirmatory_questions_PartA'] = False
                # self.participant.payoff = c(0)
        else:
            # alle Antworten sind richtig
            if (self.player.confirm_3 == 2 and self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                self.participant.payoff += Constants.completion_payoff
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # # Antworten 3,4 richtig
            # elif (self.player.confirm_3 == 2 and self.player.confirm_4 == 3):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # # Antworten 3,5 richtig
            # elif (self.player.confirm_3 == 2 and self.player.confirm_5 == 2):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # # Antworten 4,5 richtig
            # elif (self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartA'] = True
            else:
                self.participant.vars['correct_confirmatory_questions_PartA'] = False
                # self.participant.payoff = c(0)



class Confirmatory_Results(Page):
    pass


class Manipulation_Check(Page):
    # same for each participant
    form_model = 'player'
    form_fields = ['manipulation']

    # def is_displayed(self):
    #     return self.participant.vars['correct_confirmatory_questions_PartA']


class Experimental_Part(Page):
    # condition-specific
    form_model = 'player'
    form_fields = ['intention', 'intention_amount']

    # def is_displayed(self):
    #     return self.participant.vars['correct_confirmatory_questions_PartA']

    def error_message(self, values):
        if values['intention_amount'] < c(0):
            return 'The amount cannot be negative.'
        else:
            if values['intention']:
                if values['intention_amount'] > Constants.endowment:
                    return 'The amount cannot be higher than your current balance.'
                # elif values['intention_amount'] == c(0):
                #     return 'You cannot simultaneously state "Yes" and set the amount to 0.'
            else:
                if values['intention_amount'] != c(0):
                    return 'You cannot simultaneously state "No" and set an amount different than 0.'


class Attention_Check(Page):
    # same for each participant
    form_model = 'player'
    form_fields = ['attention']

    # def is_displayed(self):
    #     return self.participant.vars['correct_confirmatory_questions_PartA']


class Survey(Page):
    # condition-specific
    form_model = 'player'
    form_fields = ['pc_1', 'pc_2', 'pc_3', 'benefit_1', 'benefit_2', 'benefit_3', ]

    # def is_displayed(self):
    #     return self.participant.vars['correct_confirmatory_questions_PartA']

    # def before_next_page(self):
    #     self.participant.payoff += Constants.completion_payoff


class Results(Page):
    pass
    # def is_displayed(self):
    #     return self.participant.vars['correct_confirmatory_questions_PartA']


page_sequence = [Welcome, Instructions, Confirmatory_Results, Manipulation_Check,
                 Experimental_Part, Attention_Check, Survey, Results]
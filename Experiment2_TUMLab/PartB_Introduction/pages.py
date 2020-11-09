from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    def before_next_page(self):
        if self.participant.vars['transparent_PartB']:
            self.player.transparent = True


class Instructions(Page):
    # condition-specific
    # same questions, but answers are condition specific
    form_model = 'player'
    form_fields = ['confirm_3', 'confirm_4', 'confirm_5']

    # 3 Questions Fields
    def before_next_page(self):
        if self.participant.vars['transparent_PartB']:
            # alle Antworten sind richtig
            if (self.player.confirm_3 == 3 and self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                self.participant.payoff += Constants.completion_payoff
                self.participant.vars['correct_confirmatory_questions_PartB'] = True
            # # Antworten 3,4 richtig
            # elif (self.player.confirm_3 == 3 and self.player.confirm_4 == 3):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartB'] = True
            # # Antworten 3,5 richtig
            # elif (self.player.confirm_3 == 3 and self.player.confirm_5 == 2):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartB'] = True
            # # Antworten 4,5 richtig
            # elif (self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartB'] = True
            else:
                self.participant.vars['correct_confirmatory_questions_PartB'] = False
                # self.participant.payoff = c(0)
        else:
            # alle Antworten sind richtig
            if (self.player.confirm_3 == 2 and self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                self.participant.payoff += Constants.completion_payoff
                self.participant.vars['correct_confirmatory_questions_PartB'] = True
            # # Antworten 3,4 richtig
            # elif (self.player.confirm_3 == 2 and self.player.confirm_4 == 3):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartB'] = True
            # # Antworten 3,5 richtig
            # elif (self.player.confirm_3 == 2 and self.player.confirm_5 == 2):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartB'] = True
            # # Antworten 4,5 richtig
            # elif (self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
            #     # self.participant.payoff = c(10)
            #     self.participant.vars['correct_confirmatory_questions_PartB'] = True
            else:
                self.participant.vars['correct_confirmatory_questions_PartB'] = False
                # self.participant.payoff = c(0)

class Confirmatory_Results(Page):
    pass


class Manipulation_Check(Page):
    # same for each participant
    form_model = 'player'
    form_fields = ['manipulation']

    # def is_displayed(self):
    #     return self.participant.vars['correct_confirmatory_questions_PartA']


page_sequence = [Welcome, Instructions, Confirmatory_Results, Manipulation_Check]

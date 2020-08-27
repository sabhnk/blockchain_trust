from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    def before_next_page(self):
        if self.participant.vars['transparent_PartA']:
            self.player.transparent = True
        else:
            self.player.transparent = False


class Instructions(Page):

    # condition-specific
    # same questions, but answers are condition specific
    form_model = 'player'
    form_fields = ['confirm_1', 'confirm_2', 'confirm_3', 'confirm_4']

    # if answers are wrong, set payout to 10
    def before_next_page(self):
        if self.participant.vars['transparent_PartA']:
            # alle Antworten sind richtig
            if (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_3 == 3 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 1,2,3 richtig
            elif (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_3 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 1,2,4 richtig
            elif (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 1,3,4 richtig
            elif (self.player.confirm_1 == 2 and self.player.confirm_3 == 3 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 2,3,4 richtig
            elif (self.player.confirm_2 == 3 and self.player.confirm_3 == 3 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            else:
                self.participant.vars['correct_confirmatory_questions_PartA'] = False
        else:
            # alle Antworten sind richtig
            if (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_3 == 2 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 1,2,3 richtig
            elif (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_3 == 2):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 1,2,4 richtig
            elif (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 1,3,4 richtig
            elif (self.player.confirm_1 == 2 and self.player.confirm_3 == 2 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 2,3,4 richtig
            elif (self.player.confirm_2 == 3 and self.player.confirm_3 == 2 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            else:
                self.participant.vars['correct_confirmatory_questions_PartA'] = False


class Confirmatory_Results(Page):
    pass


class Manipulation_Check(Page):
    # same for each participant
    form_model = 'player'
    form_fields = ['manipulation']

    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']


page_sequence = [Welcome, Instructions, Confirmatory_Results, Manipulation_Check]

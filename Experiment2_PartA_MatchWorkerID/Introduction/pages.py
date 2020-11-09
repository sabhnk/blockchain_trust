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
    form_fields = ['confirm_5', 'confirm_3', 'confirm_4']

    # 3 Questions Fields
    def before_next_page(self):
        if self.participant.vars['transparent_PartA']:
            # alle Antworten sind richtig
            if (self.player.confirm_3 == 3 and self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 3,4 richtig
            elif (self.player.confirm_3 == 3 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 3,5 richtig
            elif (self.player.confirm_3 == 3 and self.player.confirm_5 == 2):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 4,5 richtig
            elif (self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            else:
                self.participant.vars['correct_confirmatory_questions_PartA'] = False
                self.participant.payoff = c(0)
        else:
            # alle Antworten sind richtig
            if (self.player.confirm_3 == 2 and self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 3,4 richtig
            elif (self.player.confirm_3 == 2 and self.player.confirm_4 == 3):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 3,5 richtig
            elif (self.player.confirm_3 == 2 and self.player.confirm_5 == 2):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            # Antworten 4,5 richtig
            elif (self.player.confirm_4 == 3 and self.player.confirm_5 == 2):
                # self.participant.payoff = c(10)
                self.participant.vars['correct_confirmatory_questions_PartA'] = True
            else:
                self.participant.vars['correct_confirmatory_questions_PartA'] = False
                self.participant.payoff = c(0)

    # 4 question fields
    # if answers are wrong, set payout to 10
    # def before_next_page(self):
    #     if self.participant.vars['transparent_PartA']:
    #         # alle Antworten sind richtig
    #         if (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_3 == 3 and self.player.confirm_4 == 3):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         # Antworten 1,2,3 richtig
    #         elif (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_3 == 3):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         # Antworten 1,2,4 richtig
    #         elif (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_4 == 3):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         # Antworten 1,3,4 richtig
    #         elif (self.player.confirm_1 == 2 and self.player.confirm_3 == 3 and self.player.confirm_4 == 3):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         # Antworten 2,3,4 richtig
    #         elif (self.player.confirm_2 == 3 and self.player.confirm_3 == 3 and self.player.confirm_4 == 3):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         else:
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = False
    #     else:
    #         # alle Antworten sind richtig
    #         if (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_3 == 2 and self.player.confirm_4 == 3):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         # Antworten 1,2,3 richtig
    #         elif (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_3 == 2):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         # Antworten 1,2,4 richtig
    #         elif (self.player.confirm_1 == 2 and self.player.confirm_2 == 3 and self.player.confirm_4 == 3):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         # Antworten 1,3,4 richtig
    #         elif (self.player.confirm_1 == 2 and self.player.confirm_3 == 2 and self.player.confirm_4 == 3):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         # Antworten 2,3,4 richtig
    #         elif (self.player.confirm_2 == 3 and self.player.confirm_3 == 2 and self.player.confirm_4 == 3):
    #             # self.participant.payoff = c(10)
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = True
    #         else:
    #             self.participant.vars['correct_confirmatory_questions_PartA'] = False


class Confirmatory_Results(Page):
    # last_char = player.participant.mturk_worker_id
    def before_next_page(self):
        last_char = str(self.participant.mturk_worker_id)[-1]
        # if last_char is even, Player A else Player B
        if last_char.isnumeric():
            if (last_char % 2) == 0:
                self.participant.vars['PlayerA'] == True
                self.player.playerA = True
            else:
                self.participant.vars['PlayerA'] == False
                self.player.playerA = False
        # last_char is not a number
        # print(ord('a'))  # 97
        else:
            if ((ord(last_char)) % 2) == 0:
                self.participant.vars['PlayerA'] == True
                self.player.playerA = True
            else:
                self.participant.vars['PlayerA'] == False
                self.player.playerA = False




class Manipulation_Check(Page):
    # same for each participant
    form_model = 'player'
    form_fields = ['manipulation']

    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']


page_sequence = [Welcome, Instructions, Confirmatory_Results, Manipulation_Check]

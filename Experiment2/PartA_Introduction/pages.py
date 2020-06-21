from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    template_name = 'global/Welcome.html'


class Instructions(Page):
    template_name = 'global/Instructions.html'
    # condition-specific


class Confirmatory_Questions(Page):
    template_name = 'global/Confirmatory_Questions.html'
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
    template_name = 'global/Confirmatory_Results.html'


class Manipulation_Check(Page):
    template_name = 'global/Manipulation_Check.html'
    # same for each participant
    form_model = 'player'
    form_fields = ['manipulation']

    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']


page_sequence = [Welcome, Instructions, Confirmatory_Questions, Confirmatory_Results, Manipulation_Check]

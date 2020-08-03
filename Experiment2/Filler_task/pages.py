from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'employment', 'income']
    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']


class FillerTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'teaser1', 'crt_widget']
    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']

class FillerTest2(Page):
    form_model = 'player'
    form_fields = ['teaser2', 'crt_lake', 'teaser3']
    def is_displayed(self):
        return self.participant.vars['correct_confirmatory_questions_PartA']

    def before_next_page(self):
        self.participant.payoff += Constants.completion_payoff


page_sequence = [FillerTest, FillerTest2, Demographics]

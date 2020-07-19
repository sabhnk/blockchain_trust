from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'employment', 'income']


class FillerTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'teaser1', 'crt_widget']

class FillerTest2(Page):
    form_model = 'player'
    form_fields = ['teaser2', 'crt_lake']


page_sequence = [FillerTest, FillerTest2, Demographics]

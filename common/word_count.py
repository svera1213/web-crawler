from django.db.models import Func, IntegerField


class WordCount(Func):
    function = 'CHAR_LENGTH'
    name = 'word_count'
    template = "(%(function)s(%(expressions)s) - CHAR_LENGTH(REPLACE(%(expressions)s, ' ', '')))"
    output_field = IntegerField()

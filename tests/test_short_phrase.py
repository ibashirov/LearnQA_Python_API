import pytest
class TestShortPhrase:

    def test_short_phrase(self):
        phrase ="sdfgsd" #input("Введите фразу короче 15 символов:")
        assert len(phrase) < 15, "Фраза длинее 15 символов"

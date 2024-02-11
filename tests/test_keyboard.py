from src.keyboard import Keyboard, MixinSavelanguage
import pytest

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_default_lang():
    assert kb.language == 'EN'


def test_change_lang():
    kb.change_lang()
    assert kb.language == 'RU'
    kb.change_lang()
    assert kb.language == 'EN'
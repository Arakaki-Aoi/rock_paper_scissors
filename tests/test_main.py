import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import builtins
import main
import pytest


def test_generate_cpu_hand(monkeypatch):
    monkeypatch.setattr("main.random.choice", lambda values: "rock")
    assert main.generate_cpu_hand() == "rock"


@pytest.mark.parametrize(
    "cpu_hand,user_hand,expected",
    [
        ("rock", "rock", "tie"),
        ("rock", "scissors", "lose"),
        ("rock", "paper", "win"),
        ("paper", "paper", "tie"),
        ("paper", "rock", "lose"),
        ("paper", "scissors", "win"),
        ("scissors", "scissors", "tie"),
        ("scissors", "paper", "lose"),
        ("scissors", "rock", "win"),
    ],
)
def test_compare_hands(cpu_hand, user_hand, expected):
    assert main.compare_hands(cpu_hand, user_hand) == expected


def test_outcome_message():
    assert main.outcome_message("tie") == "We're Even!"
    assert main.outcome_message("lose") == "You lose!"
    assert main.outcome_message("win") == "You win"


class DummyRoot:
    instance = None

    def __init__(self):
        DummyRoot.instance = self
        self._button = None
        self._destroyed = False

    def title(self, _):
        pass

    def update_idletasks(self):
        pass

    def winfo_screenwidth(self):
        return 1920

    def winfo_screenheight(self):
        return 1080

    def winfo_width(self):
        return 200

    def winfo_height(self):
        return 100

    def geometry(self, geometry_str):
        self.geometry_str = geometry_str

    def mainloop(self):
        if self._button:
            self._button.command()

    def destroy(self):
        self._destroyed = True


class DummyStringVar:
    def __init__(self, master=None):
        self._value = "rock"

    def get(self):
        return self._value


class DummyCombobox:
    def __init__(self, root, values, textvariable, state, width):
        self.root = root
        self.textvariable = textvariable

    def pack(self, **kwargs):
        pass


class DummyButton:
    def __init__(self, root, text, command):
        self.command = command
        root._button = self

    def pack(self, **kwargs):
        pass


def test_create_game_window(monkeypatch):
    monkeypatch.setattr(main, "generate_cpu_hand", lambda: "scissors")
    monkeypatch.setattr(main.tk, "Tk", DummyRoot)
    monkeypatch.setattr(main.tk, "StringVar", DummyStringVar)
    monkeypatch.setattr(main.ttk, "Combobox", DummyCombobox)
    monkeypatch.setattr(main.tk, "Button", DummyButton)
    monkeypatch.setattr(builtins, "print", lambda *args, **kwargs: None)

    main.create_game_window()

    assert DummyRoot.instance._destroyed is True
    assert DummyRoot.instance.geometry_str == "200x100+860+490"

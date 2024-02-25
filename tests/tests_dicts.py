from utils.dicts import get_val
import pytest


def test_get_val():
    assert get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert get_val({}, "vcs") == "git"
    assert get_val({"vcs": "mercurial"}, "hdd") == 'git'
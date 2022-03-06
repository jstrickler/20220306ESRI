#!/usr/bin/env python
import pytest  # <1>
import re  # <2>

class SpamSearch():  # <3>
    def __init__(self, search_string, target_string):
        self.search_string = search_string
        self.target_string = target_string


    def findit(self):  # <4>
        return re.search(self.search_string, self.target_string)

def test_spam_search_calls_re_search(mocker):   # <5>
    mocker.patch('re.search')  # <6>
    s = SpamSearch('bug', 'lightning bug')  # <7>
    _ = s.findit()   # <8>
    re.search.assert_called_once_with('bug', 'lightning bug')  # <9>

if __name__ == '__main__':
    pytest.main([__file__, '-s'])   # <10>

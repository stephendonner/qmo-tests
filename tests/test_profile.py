#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.author import AuthorPage


class TestAuthorProfilePage:

    @pytest.mark.nondestructive
    def test_that_accessing_author_profile_works(self, mozwebqa):
        author_page = AuthorPage(mozwebqa, author_name=u'rbillings')
        author_page.go_to_author_page()

        Assert.greater(len(author_page.posted_by), 0)

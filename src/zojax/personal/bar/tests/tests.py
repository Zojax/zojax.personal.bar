##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
import os.path
import unittest, doctest
from zope import interface
from zope.app.testing import setup
from zope.app.testing.functional import ZCMLLayer
from zojax.cache.testing import setUpCache, tearDownCache

personalbar = ZCMLLayer(
    os.path.join(os.path.split(__file__)[0], 'ftesting.zcml'),
    __name__, 'personalbar', allow_teardown=True)


def test_suite():
    test = doctest.DocFileSuite(
        "tests.txt",
        setUp=setUpCache, tearDown=tearDownCache,
        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)
    test.layer = personalbar

    portlet = doctest.DocFileSuite(
        "portlet.txt",
        setUp=setUpCache, tearDown=tearDownCache,
        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)
    portlet.layer = personalbar

    return unittest.TestSuite((test, portlet))

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
from zope import interface, schema
from zojax.pageelement.interfaces import IPageElement


class IPersonalBar(IPageElement):
    """ personal bar viewlet manager """

    principal = interface.Attribute('principal')

    portal = interface.Attribute('portal')
    portal_url = interface.Attribute('portal_url')

    isAnonymous = interface.Attribute('isAnonymous')


class IPersonalBarPortlet(interface.Interface):
    """ Personal Bar portlet """

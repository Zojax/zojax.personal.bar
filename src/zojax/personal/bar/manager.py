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
from zope import interface
from zope.component import getUtility
from zope.app.component.hooks import getSite
from zope.traversing.browser import absoluteURL
from zope.viewlet.manager import WeightOrderedViewletManager
from zope.app.security.interfaces import IAuthentication
from zope.app.security.interfaces import IUnauthenticatedPrincipal
from zojax.principal.profile.interfaces import IPersonalProfile

from interfaces import IPersonalBar


class PersonalBar(WeightOrderedViewletManager):

    def update(self):
        context = self.context
        request = self.request
        principal = request.principal

        self.isAnonymous = IUnauthenticatedPrincipal.providedBy(principal)

        self.portal = getSite()
        self.portal_url = absoluteURL(self.portal, request)
        self.principal = principal
        self.profile = IPersonalProfile(principal)

        super(PersonalBar, self).update()

        viewlets = []
        for viewlet in self.viewlets:
            if hasattr(viewlet, 'isAvailable'):
                if viewlet.isAvailable():
                    viewlets.append(viewlet)
            else:
                viewlets.append(viewlet)
        self.viewlets = viewlets

    def render(self):
        return self.template()

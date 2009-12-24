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
from zope import component
from zope.app.component.interfaces import ISite
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from zojax.cache.view import cache
from zojax.cache.tag import SiteTag
from zojax.principal.profile.interfaces import IPersonalProfile


PersonalBarTag = SiteTag('personalbar')


def Principal(object, instance, *args, **kw):
    profile = IPersonalProfile(instance.request.principal)

    return {'principal': instance.request.principal.id,
            'modified': profile.modified}


class PersonalBar(object):

    @cache('pegeelement.personalbar', PersonalBarTag, Principal)
    def updateAndRender(self):
        return super(PersonalBar, self).updateAndRender()


@component.adapter(ISite, IObjectModifiedEvent)
def siteModified(site, ev):
    PersonalBarTag.update(site)

# -*- coding: utf-8 -*-

import unittest2 as unittest

from plone.testing import z2
from plone.app.testing.layers import IntegrationTesting
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from zope.component import getAdapter
from Products.CMFCore.utils import getToolByName

from zope.configuration import xmlconfig

from plone.contentratings.browser.interfaces import ICategoryContainer


class UpDownLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # load ZCML
        import acentoweb.updown
        xmlconfig.file('configure.zcml', acentoweb.updown,
                       context=configurationContext)
        z2.installProduct(app, 'acentoweb.updown')

    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'acentoweb.updown:default')

UPDOWN_FIXTURE = UpDownLayer()

UPDOWN_INTEGRATION_TESTING = IntegrationTesting(bases=(UPDOWN_FIXTURE,), name="LibreOrganizacion:Integration")
UPDOWN_FUNCTIONAL_TESTING = FunctionalTesting(bases=(UPDOWN_FIXTURE,), name="LibreOrganizacion:Functional")

class TestProductInstall(unittest.TestCase):
    layer = UPDOWN_INTEGRATION_TESTING


    def testPloneContentratingsInstalled(self):
        """Check that plone.contentratings is installed."""
        qi = getToolByName(self.layer['portal'], 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled('plone.contentratings'))

    def testCategoryInstalled(self):
        """Check that our UpDown rating category is registered."""
        manager = getAdapter(self.layer['portal'], ICategoryContainer)
        categories = manager.acquired_categories
        categories_titles = [c.title for c in categories]
        self.assertTrue(u'UpDown' in categories_titles)


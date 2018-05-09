# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from qidejt.theme.testing import QIDEJT_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that qidejt.theme is properly installed."""

    layer = QIDEJT_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if qidejt.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'qidejt.theme'))

    def test_browserlayer(self):
        """Test that IQidejtThemeLayer is registered."""
        from qidejt.theme.interfaces import (
            IQidejtThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IQidejtThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = QIDEJT_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['qidejt.theme'])

    def test_product_uninstalled(self):
        """Test if qidejt.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'qidejt.theme'))

    def test_browserlayer_removed(self):
        """Test that IQidejtThemeLayer is removed."""
        from qidejt.theme.interfaces import \
            IQidejtThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IQidejtThemeLayer, utils.registered_layers())

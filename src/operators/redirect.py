"""This module provides the operators achieving redirection to web browsers"""

from urllib.parse import urljoin
import logging
import bpy
from src.config.api import API_CONFIG, MODE
from src.config.langs import TRADUCTOR, CONFIG_LANG


# pylint: disable=too-few-public-methods

class RedirectorOperator(bpy.types.Operator):
    """Base class for redirection operators. DON'T REGISTER."""

    def __init__(self):
        self.logger = logging.getLogger('Redirector')

    def execute(self, unused_ctx):
        """On click function"""
        del unused_ctx
        import webbrowser

        try:
            webbrowser.open_new_tab(self.url)
        except webbrowser.Error as err:
            self.logger.error(err)
            return {'CANCELLED'}

        return {'FINISHED'}


class TresorioRedirectForgotPasswordOperator(RedirectorOperator):
    """This operator redirects to the password recovery page on Tresorio's website."""
    __doc__ = TRADUCTOR['desc']['forgot_password'][CONFIG_LANG]

    bl_idname = 'tresorio.redirect_forgot_password'
    bl_label = 'Forgot password'

    def __init__(self):
        super().__init__()
        self.url = urljoin(API_CONFIG[MODE]['frontend'],
                           API_CONFIG['routes']['forgot_password'])


class TresorioRedirectGetCreditsOperator(RedirectorOperator):
    """This operator redirects to the get credits page on Tresorio's website."""
    __doc__ = TRADUCTOR['desc']['get_credits'][CONFIG_LANG]

    bl_idname = 'tresorio.redirect_get_credits'
    bl_label = 'Get credits'

    def __init__(self):
        super().__init__()
        self.url = urljoin(API_CONFIG[MODE]['frontend'],
                           API_CONFIG['routes']['get_credits'])


class TresorioRedirectRegisterOperator(RedirectorOperator):
    """This operator redirects to the registration page on the Tresorio's website."""
    __doc__ = TRADUCTOR['desc']['create_account'][CONFIG_LANG]

    bl_idname = 'tresorio.redirect_register'
    bl_label = 'Register'

    def __init__(self):
        super().__init__()
        self.url = urljoin(API_CONFIG[MODE]['frontend'],
                           API_CONFIG['routes']['register'])


class TresorioRedirectHomeOperator(RedirectorOperator):
    """This operator redirects to the main page on the Tresorio's website."""
    __doc__ = TRADUCTOR['desc']['redirect_tresorio'][CONFIG_LANG]

    bl_idname = 'tresorio.redirect_home'
    bl_label = 'Tresorio Home'

    def __init__(self):
        super().__init__()
        self.url = API_CONFIG[MODE]['homepage']

class TresorioRedirectDownloadAddon(RedirectorOperator):
    """This operator redirects to the download plugin page."""
    ___doc___ = TRADUCTOR['desc']['redirect_download'][CONFIG_LANG]

    bl_idname = 'tresorio.download_addon'
    bl_label = 'Tresorio Addon'

    def __init__(self):
        super().__init__()
        self.url = API_CONFIG[MODE]['frontend'] + API_CONFIG['routes']['download_addon']
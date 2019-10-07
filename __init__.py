bl_info = {
    'name': 'WIP Tresorio cloud rendering',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'category': 'Render',
    'file': '/$HOME/.config/blender/2.80/scripts/addons/tresorio',
    'location': 'Properties: Render > Tresorio Rendering',
    'description': 'Cloud distributed rendering for Blender, by Tresorio',
    'wiki_url': 'http://192.168.15.20:3000',
}

import os
import bpy
import sys
from importlib import reload
from types import ModuleType

user_path = bpy.utils.resource_path('USER')
addon_path = os.path.join(user_path, 'scripts', 'addons', 'tresorio')
modules_path = os.path.join(user_path, 'scripts', 'addons', 'tresorio', 'bundle_modules')
sys.path.append(addon_path)
sys.path.append(modules_path)

def reload_all(module: ModuleType, layers: int):
    if layers == 0: return
    for key in module.__dict__:
        if key == 'bpy':
            continue
        attr = module.__dict__[key]
        if type(attr) is not ModuleType:
            continue
        reload_all(attr, layers - 1)
        reload(attr)

if 'src' not in locals():
    import src
    reload_all(src, 2)

# Properties
from src.properties.user_props import TresorioUserProps
from src.properties.report_props import TresorioReportProps
from src.properties.render_form import TresorioRenderFormProps
from src.properties.renders import TresorioRendersDetailsProps
from src.properties.render_packs import TresorioRenderPacksProps

# UI
from src.ui.main_panel import TresorioMainPanel
from src.ui.account_panel import TresorioAccountPanel
from src.ui.new_render_panel import TresorioNewRenderPanel
from src.ui.selected_render_panel import TresorioSelectedRenderPanel
from src.ui.user_renders_panel import TresorioRendersPanel, TresorioRendersList

# Operators
from src.operators.login import TresorioLoginOperator
from src.operators.logout import TresorioLogoutOperator
from src.operators.render import TresorioRenderFrameOperator
from src.operators.redirect import TresorioRedirectHomeOperator
from src.operators.stop_render import TresorioStopRenderOperator
from src.operators.redirect import TresorioRedirectRegisterOperator
from src.operators.delete_render import TresorioDeleteRenderOperator
from src.operators.redirect import TresorioRedirectGetCreditsOperator
from src.operators.redirect import TresorioRedirectForgotPasswordOperator
from src.operators.download_render_results import TresorioDownloadRenderResultsOperator
from src.services.async_loop import AsyncLoopModalOperator

to_register_classes = (
                       # Properties 
                       TresorioUserProps,
                       TresorioReportProps,
                       TresorioRenderPacksProps,
                       TresorioRenderFormProps,
                       TresorioRendersDetailsProps,

                       # Operators
                       TresorioLoginOperator,
                       TresorioLogoutOperator,
                       TresorioRedirectForgotPasswordOperator,
                       TresorioRedirectRegisterOperator,
                       TresorioRedirectHomeOperator,
                       TresorioRenderFrameOperator,
                       TresorioDownloadRenderResultsOperator,
                       TresorioStopRenderOperator,
                       TresorioDeleteRenderOperator,
                       TresorioRedirectGetCreditsOperator,
                       AsyncLoopModalOperator,

                       # UI
                       TresorioMainPanel,
                       TresorioRendersPanel,
                       TresorioNewRenderPanel,
                       TresorioAccountPanel,
                       TresorioRendersList,
                       TresorioSelectedRenderPanel,
                      )

from src.operators.logout import logout
import asyncio

def unregister():
    logout(erase_loop=True) # this stops the loop
    loop = asyncio.get_event_loop()
    loop.close()
    for cls in reversed(to_register_classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError as exc:
            print(exc)


def register():
    asyncio.set_event_loop(asyncio.new_event_loop())
    for cls in to_register_classes:
        ## Add description with language translation
        set_doc = getattr(cls, 'set_doc', None)
        if callable(set_doc):
            cls.set_doc()
        bpy.utils.register_class(cls)


if __name__ == '__main__':
    register()

# -*- coding: UTF-8 -*-

import nuke

nuke.pluginAddPath('cryptomatte/nuke')
nuke.pluginAddPath('mamoworld')
nuke.pluginAddPath('tabtabtab')
nuke.pluginAddPath('ofx')
# nuke.pluginAddPath('batchrender', addToSysPath=False)
nuke.pluginAddPath('olm_smoother')
nuke.pluginAddPath('custom_env')
nuke.pluginAddPath('tomas_lefebvre')
nuke.pluginAddPath('//server/Scripts/NukePlugins/EE')
if nuke.env['NukeVersionString'].startswith('10.5v'):
    nuke.pluginAddPath('optical_flares')

# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

import os
from sos.report.plugins import Plugin, IndependentPlugin

class DrmInfo(Plugin, IndependentPlugin):

    short_desc = 'GPU drm infomation'

    plugin_name = 'gpu_drminfo'
    profiles = ('system', 'hardware')
    packages = ('drm-info',)
    commands = ('drm_info',)

    def setup(self):
        self.add_cmd_output("drm_info")

# vim: set et ts=4 sw=4 :

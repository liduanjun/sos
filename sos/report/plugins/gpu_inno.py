# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.report.plugins import Plugin, IndependentPlugin

class Inno(Plugin, IndependentPlugin):
    """收集芯动的显卡信息
    """

    short_desc = 'Inno GPU drm driver infomation'

    plugin_name = 'gpu_inno'
    profiles = ('system', 'hardware')
    files = ('/sys/bus/platform/drivers/sysdbg/sysdbg.0/develop_mode',)

    def setup(self):
        self.add_cmd_output([
            "echo -n inno@123456 > /sys/bus/platform/drivers/sysdbg/sysdbg.0/develop_mode",
            "find /usr/lib/`dpkg-architecture -q DEB_HOST_GNU_TYPE` -name innogpu_drv*", # check vaapi lib
            "ffmpeg -version",
            "mpv -version"
        ])
        self.add_copy_spec([
            "/sys/bus/platform/drivers/sysdbg/sysdbg.0/driver_info",
            "/sys/bus/platform/drivers/sysdbg/sysdbg.0/gpu_static_info",
            "/sys/bus/platform/drivers/sysdbg/sysdbg.0/gpu_dynamic_info",
            "/sys/kernel/debug/inno",
            "/sys/kernel/debug/pvr",
            "/sys/module/innogpu/parameters",
            "/lib/firmware/innogpu/",
            "/sys/kernel/debug/innogpu0/"
        ])
        self.add_cmd_output("echo -n hwinfo > /sys/bus/platform/devices/sysdbg.0/hwinfo_idx")
        self.add_copy_spec([
            "/sys/bus/platform/devices/sysdbg.0/hwinfo"
        ], tag="hwinfo")
        self.add_cmd_output("echo -n custom > /sys/bus/platform/devices/sysdbg.0/hwinfo_idx")
        self.add_copy_spec([
            "/sys/bus/platform/devices/sysdbg.0/hwinfo"
        ], tag="custom")

# vim: set et ts=4 sw=4 :

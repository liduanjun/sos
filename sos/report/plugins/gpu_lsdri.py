# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.report.plugins import Plugin, IndependentPlugin

class Lsdri(Plugin, IndependentPlugin):

    short_desc = 'GPU direct render infomation'

    plugin_name = 'gpu_lsdri'
    profiles = ('system', 'hardware')

    def setup(self):
        self.add_copy_spec([
            "/etc/os-release",
            "/usr/share/drirc.d",
            "/sys/kernel/debug/dri",
            "/sys/class/drm",
            "/sys/class/backlight",
            "/sys/module/drm",
            "/sys/bus/platform/devices",
            "/sys/kernel/debug/dma_buf"
        ])

        self.add_cmd_output([
            "ls -lh /dev/dri/*",
            "cat /proc/sys/kernel/printk",
            "cat /proc/devices",
            "i2cdetect -l",
            "find /usr/lib/ -name libcodec*",
            "find /usr/lib/ -name libva*",
            "find /usr/lib/ -name libav*",
        ])

# vim: set et ts=4 sw=4 :

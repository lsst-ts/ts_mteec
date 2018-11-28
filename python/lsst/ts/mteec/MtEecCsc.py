# This file is part of ts_scriptqueue.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import lsst.ts.salobj as salobj

__all__ = ["MtEecCsc"]

import SALPY_MTEEC


class MtEecCsc(salobj.BaseCsc):
    """CSC  for the Environment Enclousure Control """

    def __init__(self):
        """ not indexed - call up to super """
        super().__init__(SALPY_MTEEC, 0)

    def do_applyTemperatureSetpoint(self, id_data):
        """ Check temp and see if we need to move up or downcaseTokens"""
        self.assert_enabled("setTemeratureSetPoint")
# Should have some model ..

    def do_disableControl(self, id_data):
        """ Check temp and see if we need to move up or downcaseTokens"""
        self.assert_enabled("setTemeratureSetPoint")

    def do_setToDayTime(self, id_data):
        """ Check temp and see if we need to move up or downcaseTokens"""
        self.assert_enabled("setToDayTime")

    def do_setToNightTime(self, id_data):
        """ Check temp and see if we need to move up or downcaseTokens"""
        self.assert_enabled("setToNightTIme")

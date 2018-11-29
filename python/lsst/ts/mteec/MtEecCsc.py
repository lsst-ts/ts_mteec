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
import SALPY_MTEEC
import lsst.ts.salobj as salobj
import enum


__all__ = ["MtEecCsc"]


class MtEecState(enum.IntEnum):
    """State constants. Should get these from SALPY?
    """
    NOTSET = SALPY_MTEEC.detailedState_NotSetState
    """  detailed state not set  cannot be run."""
    DAY = SALPY_MTEEC.detailedState_DaySetState
    """Script is configured and so can be run."""
    NIGHT = SALPY_MTEEC.detailedState_NightSetState


class MtEecCsc(salobj.BaseCsc):
    """CSC  for the Environment Enclousure Control """

    _state = MtEecState

    def __init__(self):
        """ not indexed - call up to super """
        super().__init__(SALPY_MTEEC, 0)

    def do_applyTemperatureSetpoint(self, id_data):
        """ Check temp and see if we need to move up or downcaseTokens"""
        self.assert_enabled("setTemeratureSetPoint")
# Should talk to something here .. .

    def do_disableControl(self, id_data):
        """ Check temp and see if we need to move up or downcaseTokens"""
        self.assert_enabled("disableControl")
        self._state.setState(MtEecState.NOTSET)

    def do_setToDayTime(self, id_data):
        """ Check temp and see if we need to move up or downcaseTokens"""
        self.assert_enabled("setToDayTime")
        self.assert_state(MtEecState.NOTSET)
        self._state.setState(MtEecState.DAY)

    def do_setToNightTime(self, id_data):
        """ Check temp and see if we need to move up or downcaseTokens"""
        self.assert_enabled("setToNightTIme")
        self.assert_state(MtEecState.NOTSET)
        self._state.setState(MtEecState.NIGHT)

    @property
    def state(self):
        """Get the current state.
        * ``state``: the current state; a `MtEecState`
        """
        return self._state

    @property
    def state_name(self):
        """Get the current `state`.state as a name.
        """
        try:
            return MtEecState(self.state.state).name
        except ValueError:
            return f"UNKNOWN({self.state.state})"

    @property
    def final_state_future(self):
        """Get an asyncio.Future that returns the final state
        of the script.
        """
        return self._final_state_future

    def set_state(self, state=None):
        """Set the script state.

        Parameters
        ----------
        state : `MtEecState` (optional)
            New state, or None if no change
        """
        if state is not None:
            if state not in MtEecState:
                raise ValueError(f"{state} is not in MtEecState")
            self._state.state = state

    def assert_state(self, state):
        """Assert that the  state is as expected or throw an exception

        Parameters
        ----------
        state :  `MtEecState`
            The required state.
        """
        if self._state != state:
            raise salobj.ExpectedError(
                f"Unexpected state={self.state_name} instead of {MtEecState(state).name}")

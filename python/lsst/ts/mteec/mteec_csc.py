# This file is part of ts_mteec.
#
# Developed for the LSST Data Management System.
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

__all__ = ["MtEecCsc"]

import pathlib

from lsst.ts import salobj


class MtEecCsc(salobj.ConfigurableCsc):
    """Commandable SAL Component for the MTEEC (Main Telescope Enclosure
    Environment Control).

    Parameters
    ----------
    config_dir : `string`
        The configuration directory
    initial_state : `salobj.State`
        The initial state of the CSC
    simulation_mode : `int`
        Simulation mode (1) or not (0)
    """

    def __init__(
        self, config_dir=None, initial_state=salobj.State.STANDBY, simulation_mode=0,
    ):
        schema_path = pathlib.Path(__file__).resolve().parents[4].joinpath("schema", "mteec.yaml")
        self.config = None
        self._config_dir = config_dir
        super().__init__(
            name="MTEEC",
            index=0,
            schema_path=schema_path,
            config_dir=config_dir,
            initial_state=initial_state,
            simulation_mode=simulation_mode,
        )
        self.log.info("__init__")

    async def connect(self):
        """Start the MTEEC MQTT client or start the mock client, if in
        simulation mode.
        """
        self.log.info("Connecting")
        self.log.info(self.config)
        self.log.info(f"self.simulation_mode = {self.simulation_mode}")
        if self.config is None:
            raise RuntimeError("Not yet configured")
        if self.connected:
            raise RuntimeError("Already connected")
        if self.simulation_mode == 1:
            # TODO Add code for simulation case
            pass
        else:
            # TODO Add code for non-simulation case
            pass

    async def disconnect(self):
        """Disconnect the MTEEC CSC, if connected.
        """
        self.log.info("Disconnecting")

    async def do_applyTemperatureSetpoint(self, data):
        self.assert_enabled()
        raise salobj.ExpectedError("Not implemented yet.")

    async def do_disableControl(self, data):
        self.assert_enabled()
        raise salobj.ExpectedError("Not implemented yet.")

    async def do_setToDayTime(self, data):
        self.assert_enabled()
        raise salobj.ExpectedError("Not implemented yet.")

    async def do_setToNightTime(self, data):
        self.assert_enabled()
        raise salobj.ExpectedError("Not implemented yet.")

    async def handle_summary_state(self):
        """Override of the handle_summary_state function to connect or
        disconnect to the MTEEC CSC (or the mock client) when needed.
        """
        self.log.info(f"handle_summary_state {salobj.State(self.summary_state).name}")
        if self.disabled_or_enabled:
            if not self.connected:
                await self.connect()
        else:
            await self.disconnect()

    async def configure(self, config):
        self.config = config

    async def implement_simulation_mode(self, simulation_mode):
        if simulation_mode not in (0, 1):
            raise salobj.ExpectedError(f"Simulation_mode={simulation_mode} must be 0 or 1")

    @property
    def connected(self):
        # TODO Add code to determine if the CSC is connected or not.
        return True

    @staticmethod
    def get_config_pkg():
        return "ts_config_ocs"

    @classmethod
    def add_arguments(cls, parser):
        super(MtEecCsc, cls).add_arguments(parser)
        parser.add_argument("-s", "--simulate", action="store_true", help="Run in simuation mode?")

    @classmethod
    def add_kwargs_from_args(cls, args, kwargs):
        super(MtEecCsc, cls).add_kwargs_from_args(args, kwargs)
        kwargs["simulation_mode"] = 1 if args.simulate else 0

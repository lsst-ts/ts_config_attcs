# This file is part of ts_config_attcs.
#
# Developed for Vera C. Rubin Observatory Telescope and Site Systems.
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

import pathlib
import unittest

from lsst.ts import salobj


class ConfigTestCase(salobj.BaseConfigTestCase, unittest.TestCase):
    def setUp(self):
        self.config_package_root = pathlib.Path(__file__).parents[1]

    def test_ATAOS(self):
        self.check_standard_config_files(
            sal_name="ATAOS",
            module_name="lsst.ts.ataos",
            config_package_root=self.config_package_root,
        )

    def test_ATDome(self):
        self.check_standard_config_files(
            sal_name="ATDome",
            module_name="lsst.ts.atdome",
            config_package_root=self.config_package_root,
        )

    def test_ATDomeTrajectory(self):
        self.check_standard_config_files(
            sal_name="ATDomeTrajectory",
            module_name="lsst.ts.atdometrajectory",
            config_package_root=self.config_package_root,
        )

    def test_ATHexapod(self):
        self.check_standard_config_files(
            sal_name="ATHexapod",
            module_name="lsst.ts.athexapod",
            config_package_root=self.config_package_root,
        )

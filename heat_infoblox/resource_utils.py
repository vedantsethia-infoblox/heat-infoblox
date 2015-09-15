# Copyright (c) 2015 Infoblox Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from heat.common.i18n import _
from heat.engine import constraints
from heat.engine import properties

from heat_infoblox import config as cfg
from heat_infoblox import connector
from heat_infoblox import ibexceptions as exc
from heat_infoblox import object_manipulator

"""Utilities for specifying resources."""


def port_schema(port_name, is_required):
    return properties.Schema(
        properties.Schema.STRING,
        _('ID of an existing port to associate with the %s port.')
        % port_name,
        constraints=[
            constraints.CustomConstraint('neutron.port')
        ],
        required=is_required
    )


def connect_to_infoblox():
    config = cfg.CONF['infoblox']

    reqd_opts = ['wapi_url', 'username', 'password']

    for opt in reqd_opts:
        if not getattr(config, opt, None):
            raise exc.InfobloxIsMisconfigured(option=opt)

    return object_manipulator.InfobloxObjectManipulator(
        connector.Infoblox({"url": config.wapi_url,
                            "username": config.username,
                            "password": config.password,
                            "sslverify": config.sslverify}))

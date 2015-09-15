# Copyright 2015 Infoblox Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_config import cfg

CONF = cfg.CONF

CONF.register_group(cfg.OptGroup(
    name='infoblox', title="Configuration for Infoblox Client"
))

OPTS = [
    cfg.StrOpt('wapi_url'),
    cfg.StrOpt('username'),
    cfg.StrOpt('password'),
    cfg.BoolOpt('sslverify', default=False),
    cfg.IntOpt('http_pool_connections', default=100),
    cfg.IntOpt('http_pool_maxsize', default=100),
]

CONF.register_opts(OPTS, group='infoblox')

#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2020 Evgeni Golov
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = '''
---
module: status_info
version_added: 1.3.0
short_description: Get status info
description:
  - Get status information from the server
author:
  - "Evgeni Golov (@evgeni)"
extends_documentation_fragment:
  - redhat.satellite.foreman
'''

EXAMPLES = '''
- name: status
  redhat.satellite.status_info:
    server_url: "https://satellite.example.com"
    username: "admin"
    password: "changeme"
'''

RETURN = '''
status:
  description: Basic status of the server.
  returned: always
  type: dict
ping:
  description: Detailed service status.
  returned: if supported by server
  type: dict
'''

from ansible_collections.redhat.satellite.plugins.module_utils.foreman_helper import ForemanAnsibleModule


def main():
    module = ForemanAnsibleModule()

    with module.api_connection():
        status = module.status()

        if 'ping' in module.foremanapi.resources:
            if 'ping' in module.foremanapi.resource('ping').actions:
                ping_action = 'ping'
            else:
                ping_action = 'index'
            ping = module.foremanapi.resource('ping').call(ping_action)
        else:
            ping = None

        module.exit_json(status=status, ping=ping)


if __name__ == '__main__':
    main()

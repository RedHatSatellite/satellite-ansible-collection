#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2021 Eric Helms
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
module: content_view_version_info
version_added: 2.1.0
short_description: Fetch information about Content Views
description:
  - Fetch information about Content Views
author:
  - "Eric Helms (@ehelms)"
options:
  content_view:
    description:
      - Content View to which the Version belongs
    required: true
    type: str
extends_documentation_fragment:
  - redhat.satellite.foreman
  - redhat.satellite.foreman.katelloinfomodule
  - redhat.satellite.foreman.infomodulewithoutname
'''

EXAMPLES = '''
- name: "Show a content view version"
  redhat.satellite.content_view_version_info:
    username: "admin"
    password: "changeme"
    server_url: "https://satellite.example.com"
    content_view: "CentOS 8 View"
    search: 'version = "4.0"'

- name: "Show all content view_versions for a content view"
  redhat.satellite.content_view_version_info:
    username: "admin"
    password: "changeme"
    server_url: "https://satellite.example.com"
    content_view: "CentOS 8 View"
'''

RETURN = '''
content_view_versions:
  description: List of all found content_view_versions and their details
  returned: success and I(search) was passed
  type: list
  elements: dict
'''

from ansible_collections.redhat.satellite.plugins.module_utils.foreman_helper import (
    KatelloInfoAnsibleModule,
)


class KatelloContentViewVersionInfo(KatelloInfoAnsibleModule):
    pass


def main():
    module = KatelloContentViewVersionInfo(
        foreman_spec=dict(
            content_view=dict(type='entity', scope=['organization'], required=True),
            name=dict(invisible=True),
        ),
    )

    with module.api_connection():
        module.run()


if __name__ == '__main__':
    main()

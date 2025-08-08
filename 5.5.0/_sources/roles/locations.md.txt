redhat.satellite.locations
===================================

This role creates and manages locations.

Role Variables
--------------

This role supports the [Common Role Variables](https://github.com/theforeman/foreman-ansible-modules/blob/develop/README.md#common-role-variables).

The main data structure for this role is the list of `satellite_locations`. Each `location` requires the following fields:

- `name`: The name of the location.

For all other fields, see the `location` module.

Example Playbook
----------------

Create the 'UK' location and set its parent to EMEA.

```yaml
- hosts: localhost
  roles:
    - role: redhat.satellite.locations
      vars:
        satellite_server_url: https://satellite.example.com
        satellite_username: "admin"
        satellite_password: "changeme"
        satellite_locations:
          - name: UK
            organisations: 
              - RedHat
            parent: EMEA
            parameters:
              - name: system_location
                value: UK
```

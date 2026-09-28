redhat.satellite.settings
===========================

This role creates and manages Settings.

Role Variables
--------------

This role supports the [Common Role Variables](https://github.com/theforeman/foreman-ansible-modules/blob/develop/README.md#common-role-variables).

The main data structure for this role is the list of `satellite_settings`. Each `setting` must contain the field `name` and may contain the optional field `value` which if empty will reset the setting to the default value.

Example Playbook
----------------

Enable *Destroy associated VM on host delete* and disable *Clean up failed deployment*:

```yaml
- hosts: localhost
  roles:
    - role: redhat.satellite.settings
      vars:
        satellite_server_url: https://satellite.example.com
        satellite_username: "admin"
        satellite_password: "changeme"
        satellite_settings:
          - name: destroy_vm_on_host_delete
            value: true
          - name: clean_up_failed_deployment
            value: false
```

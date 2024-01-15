redhat.satellite.domains
==========================

This role creates and manages Domains.

Role Variables
--------------

This role supports the [Common Role Variables](https://github.com/theforeman/foreman-ansible-modules/blob/develop/README.md#common-role-variables).

The main data structure for this role is the list of `satellite_domains`. Each `domain` requires the following fields:

- `name`: The name of the domain.

The following fields are optional and will be omitted by default:

- `description`: Description of the domain.
- `dns_proxy`: DNS proxy to use within this domain for managing A records.
- `parameters`: Domain specific host parameters.

Example Playbook
----------------

Create a domain `example.org`.

```yaml
- hosts: localhost
  roles:
    - role: redhat.satellite.domains
      vars:
        satellite_server_url: https://satellite.example.com
        satellite_username: "admin"
        satellite_password: "changeme"
        satellite_domains:
          - name: "example.org"
            description: "Example Domain"
            locations:
              - "Uppsala"
            organizations:
              - "ACME"
```

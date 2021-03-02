redhat.satellite.manifest
===========================

Upload Subscription Manifest

Role Variables
--------------

This role supports the [Common Role Variables](https://github.com/theforeman/foreman-ansible-modules/blob/develop/README.md#common-role-variables).

- `satellite_manifest_path`: Path to subscription Manifest file on Ansible target host. When using `manifest_download`, it is first downloaded to this location from the Red Hat Customer Portal before being uploaded to the Foreman server.
- `satellite_manifest_download`: Whether to first download the Manifest from the Red Hat Customer Portal. Defaults to `False`.
- `satellite_manifest_uuid`: UUID of the Manifest to download, corresponding to a [Subscription Allocation](https://access.redhat.com/management/subscription_allocations) defined on your Red Hat account. Required when `manifest_download` is `True`.
- `satellite_rhsm_username`: Your username for the Red Hat Customer Portal. Required when `satellite_manifest_download` is `true`.
- `satellite_rhsm_password`: Your password for the Red Hat Customer Portal. Required when `satellite_manifest_download` is `true`.

Example Playbooks
-----------------

Use a Subscription Manifest which has already been downloaded on localhost at `~/manifest.zip`:

```yaml
- hosts: localhost
  roles:
    - role: redhat.satellite.manifest
      vars:
        satellite_server_url: https://satellite.example.com
        satellite_username: "admin"
        satellite_password: "changeme"
        satellite_organization: "Default Organization"
        satellite_manifest_path: "~/manifest.zip"
```

Download the Subscription Manifest from the Red Hat Customer Portal to localhost before uploading to Foreman server:

```yaml
- hosts: localhost
  roles:
    - role: redhat.satellite.manifest
      vars:
        satellite_server_url: https://satellite.example.com
        satellite_username: "admin"
        satellite_password: "changeme"
        satellite_organization: "Default Organization"
        satellite_manifest_path: "~/manifest.zip"
        satellite_manifest_download: True
        satellite_rhsm_username: "happycustomer"
        satellite_rhsm_password: "$ecur3p4$$w0rd"
        satellite_manifest_uuid: "01234567-89ab-cdef-0123-456789abcdef"
```

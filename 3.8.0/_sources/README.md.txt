# Red Hat Satellite Ansible Collection

Ansible modules for interacting with the Satellite API.

## Support

For support questions around this collection, please open a ticket on the [Red Hat Customer Portal](https://access.redhat.com).

## Installation

You can install this collection directly from Automation Hub or via RPMs provided by Red Hat.

The GitHub repository serves as the source for the release and should not be used for direct installation and consumption of the collection.

### Installation from Automation Hub

You can install the collection with `ansible-galaxy collection install redhat.satellite`.

See the Ansible documentation how to configure `ansible-galaxy` to be able to [download a collection from Automation Hub](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#downloading-a-collection-from-automation-hub).

You will need to install the Python `requests` library manually, e.g. from the RPM provided by Red Hat (`python-requests` on Red Hat Enterprise Linux 7, `python3-requests` on Red Hat Enterprise Linux 8).

### Installation via RPM

The collection is also available as `ansible-collection-redhat-satellite` in the Satellite repository.

## Satellite Documentation

The official Satellite documentation can be found in the [Product Documentation section of the Red Hat Customer Portal](https://access.redhat.com/documentation/en-us/red_hat_satellite/).

## Upstream

This collection is based on the [`theforeman.foreman`](https://github.com/theforeman/foreman-ansible-modules) community collection for Foreman and Katello.
If possible, any contributions should go directly to `theforeman.foreman` from where they will flow back into this collection.

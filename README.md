# Red Hat Satellite Ansible Collection

Ansible modules for interacting with the Satellite API.

## Support

For support questions around this collection, please open a ticket on the [Red Hat Customer Portal](https://access.redhat.com).

## Installation

You can install this collection directly from Automation Hub.

The GitHub repository serves as the source for the release and should not be used for direct installation and consumption of the collection.

### Installation from Automation Hub

You can install the collection with `ansible-galaxy collection install redhat.satellite` (Ansible 2.9 and later).
You will require the `python-requests` RPM provided in the Red Hat Enterprise Linux repositories.

## Satellite Documentation

The official Satellite documentation can be found in the [Product Documentation section of the Red Hat Customer Portal](https://access.redhat.com/documentation/en-us/red_hat_satellite/).

## Upstream

This collection is based on the [`theforeman.foreman`](https://github.com/theforeman/foreman-ansible-modules) community collection for Foreman and Katello.
If possible, any contributions should go directly to `theforeman.foreman` from where they will flow back into this collection.

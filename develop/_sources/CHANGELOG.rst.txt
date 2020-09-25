================================
redhat.satellite Release Notes
================================

.. contents:: Topics

This changelog describes changes after version 0.8.1.

v1.3.0
======

Minor Changes
-------------

- external_usergroup - rename the ``auth_source_ldap`` parameter to ``auth_source`` (``auth_source_ldap`` is still supported via an alias)
- server URL and credentials can now also be specified using environment variables (https://github.com/theforeman/foreman-ansible-modules/issues/837)
- subnet - add support for external IPAM (https://github.com/theforeman/foreman-ansible-modules/issues/966)

Bugfixes
--------

- content_view - remove CVs from lifecycle environments before deleting them (https://bugzilla.redhat.com/show_bug.cgi?id=1875314)
- external_usergroup - support non-LDAP external groups (https://github.com/theforeman/foreman-ansible-modules/issues/956)
- host - properly scope image lookups by the compute resource (https://bugzilla.redhat.com/show_bug.cgi?id=1878693)
- inventory plugin - include empty parent groups in the inventory (https://github.com/theforeman/foreman-ansible-modules/issues/919)

New Modules
-----------

- redhat.satellite.status_info - Get status info

v1.2.0
======

Minor Changes
-------------

- compute_resource - added ``caching_enabled`` option for VMware compute resources
- domain, host, hostgroup, operatingsystem, subnet - manage parameters in a single API call (https://bugzilla.redhat.com/show_bug.cgi?id=1855008)
- host - add ``compute_attributes`` parameter to module (https://bugzilla.redhat.com/show_bug.cgi?id=1871815)
- provisioning_template - update list of possible template kinds (https://bugzilla.redhat.com/show_bug.cgi?id=1871978)
- repository - update supported parameters (https://github.com/theforeman/foreman-ansible-modules/issues/935)

Bugfixes
--------

- image - fix quoting of search values (https://github.com/theforeman/foreman-ansible-modules/issues/927)

v1.1.0
======

Minor Changes
-------------

- activation_key - add ``description`` parameter (https://github.com/theforeman/foreman-ansible-modules/issues/915)
- callback plugin - add reporter to report logs sent to Foreman (https://github.com/theforeman/foreman-ansible-modules/issues/836)
- document return values of modules (https://github.com/theforeman/foreman-ansible-modules/pull/901)
- inventory plugin - allow to control batch size when pulling hosts from Foreman (https://github.com/theforeman/foreman-ansible-modules/pull/865)
- subnet - Require mask/cidr only on ipv4 (https://github.com/theforeman/foreman-ansible-modules/issues/878)

Bugfixes
--------

- inventory plugin - fix want_params handling (https://github.com/theforeman/foreman-ansible-modules/issues/847)

New Modules
-----------

- redhat.satellite.http_proxy - Manage HTTP Proxies

v1.0.1
======

Release Summary
---------------

Documentation fixes to reflect the correct module names.


v1.0.0
======

Release Summary
---------------

This is the first stable release of the ``redhat.satellite`` collection.


Breaking Changes / Porting Guide
--------------------------------

- All modules were renamed to drop the ``foreman_`` and ``katello_`` prefixes.
  Additionally to the prefix removal, the following modules were further ranamed:

  * katello_upload to content_upload
  * katello_sync to repository_sync
  * katello_manifest to subscription_manifest
  * foreman_search_facts to resource_info
  * foreman_ptable to partition_table
  * foreman_model to hardware_model
  * foreman_environment to puppet_environment

New Modules
-----------

- redhat.satellite.activation_key - Manage Activation Keys
- redhat.satellite.architecture - Manage Architectures
- redhat.satellite.auth_source_ldap - Manage LDAP Authentication Sources
- redhat.satellite.bookmark - Manage Bookmarks
- redhat.satellite.compute_attribute - Manage Compute Attributes
- redhat.satellite.compute_profile - Manage Compute Profiles
- redhat.satellite.compute_resource - Manage Compute Resources
- redhat.satellite.config_group - Manage (Puppet) Config Groups
- redhat.satellite.content_credential - Manage Content Credentials
- redhat.satellite.content_upload - Upload content to a repository
- redhat.satellite.content_view - Manage Content Views
- redhat.satellite.content_view_filter - Manage Content View Filters
- redhat.satellite.content_view_version - Manage Content View Versions
- redhat.satellite.domain - Manage Domains
- redhat.satellite.external_usergroup - Manage External User Groups
- redhat.satellite.global_parameter - Manage Global Parameters
- redhat.satellite.hardware_model - Manage Hardware Models
- redhat.satellite.host - Manage Hosts
- redhat.satellite.host_collection - Manage Host Collections
- redhat.satellite.host_power - Manage Power State of Hosts
- redhat.satellite.hostgroup - Manage Hostgroups
- redhat.satellite.image - Manage Images
- redhat.satellite.installation_medium - Manage Installation Media
- redhat.satellite.job_template - Manage Job Templates
- redhat.satellite.lifecycle_environment - Manage Lifecycle Environments
- redhat.satellite.location - Manage Locations
- redhat.satellite.operatingsystem - Manage Operating Systems
- redhat.satellite.organization - Manage Organizations
- redhat.satellite.os_default_template - Manage Default Template Associations To Operating Systems
- redhat.satellite.partition_table - Manage Partition Table Templates
- redhat.satellite.product - Manage Products
- redhat.satellite.provisioning_template - Manage Provisioning Templates
- redhat.satellite.puppet_environment - Manage Puppet Environments
- redhat.satellite.realm - Manage Realms
- redhat.satellite.redhat_manifest - Interact with a Red Hat Satellite Subscription Manifest
- redhat.satellite.repository - Manage Repositories
- redhat.satellite.repository_set - Enable/disable Repositories in Repository Sets
- redhat.satellite.repository_sync - Sync a Repository or Product
- redhat.satellite.resource_info - Gather information about resources
- redhat.satellite.role - Manage Roles
- redhat.satellite.scap_content - Manage SCAP content
- redhat.satellite.scap_tailoring_file - Manage SCAP Tailoring Files
- redhat.satellite.scc_account - Manage SUSE Customer Center Accounts
- redhat.satellite.scc_product - Subscribe SUSE Customer Center Account Products
- redhat.satellite.setting - Manage Settings
- redhat.satellite.smart_class_parameter - Manage Smart Class Parameters
- redhat.satellite.snapshot - Manage Snapshots
- redhat.satellite.subnet - Manage Subnets
- redhat.satellite.subscription_manifest - Manage Subscription Manifests
- redhat.satellite.sync_plan - Manage Sync Plans
- redhat.satellite.templates_import - Sync Templates from a repository
- redhat.satellite.user - Manage Users
- redhat.satellite.usergroup - Manage User Groups

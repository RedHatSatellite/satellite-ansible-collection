# How to Update Repository

This repository is a branded version of the [foreman-ansible-modules](https://github.com/theforeman/foreman-ansible-modules) and requires some consideration when updating.
The basic update is to merge in upstream changes from a target release version and then apply branding.

```
git checkout -b update-to-<target tag>
git remote add upstream https://github.com/theforeman/foreman-ansible-modules
git fetch upstream
git merge <target tag>
make branding
```

Now inspect the changes that are made and manually fix any irregularities.

# How to Release Repository

After making local changes for branding:

   * Create a pull request with the changes

   * After merging, tag the merge commit with `<version number>` (i.e. 3.3.0).
     Please use signed tags.

   * Generate a copy of the source tarball locally: `make dist`

   * Visit the UI for the tag (e.g. [3.3.0](https://github.com/RedHatSatellite/satellite-ansible-collection/releases/tag/3.3.0) and click the "Create release from tag" button

   * Edit the release title to the name of the tag (e.g. 3.3.0) and upload the generated source tarball, then click `Publish Release`

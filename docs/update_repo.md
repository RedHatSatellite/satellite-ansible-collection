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

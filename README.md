# check_certs
Check TLS certificates of sites for their expiration dates. Send notifications if configured to do so.

## Plugins

The script uses plugins to send out notifications. The file name of a notification plugin should be `<plugin_name>_notifier.py`, and should be put in the `plugins/` directory.

## Configuration File

The script looks for a certs.yaml file as its configuration in the following locations,

* current work directory, i.e. `./`
* `~/.check_certs/` directory
* `/etc/check_certs/` directory

The configuration file has two main sections, `defaults` and `sites`.

The `defaults` section lists the default values of known settings to the script and its plugins. In the `defaults[notifiers]` section, each key should be a plugin name, which should match the prefix of the file name of the actual plugin module.

The `sites` section lists all the sites the script checks and their individual configurations if needed. Every default configuration can be overridden in this section.

There is [an example configuration file](examples/certs.yaml) in the examples directory.

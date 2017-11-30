Role Name
=========

This is the base common system related setup for all systems in use in XVT.

Requirements
------------

Support on existing Ubuntu 16.04 and RedHat OS.

Role Variables
--------------

* `ami_search_tags` - used by `lookup_ec2_ami` role to find the AMI on which to base the instance
* `system_common_timezone` - Set the system timezone
* `system_common_packages` - List of common system packages that we should install.
* `system_common_python_packages` - List of common python packages (installed by pip command) to be installed.
* `system_common_ntp_service` - The name of the system service that provide time server sync using ntp protocol.
* `system_common_ntp_config_path` - File path of the time server package
* `system_common_ntp_server` - The NTP server to be used when templating the time server configuration files.
   Default value is au.pool.ntp.org.

Dependencies
------------

None
Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: xvt-system-common
           system_common_ntp_service: chrony

License
-------

BSD

Author Information
------------------


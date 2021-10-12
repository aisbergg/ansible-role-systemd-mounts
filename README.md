# Ansible Role: `aisbergg.systemd_mounts`

This Ansible role adds or removes Systemd mounts on Linux systems.

## Requirements

- System needs to be managed with Systemd

## Role parameters

**Bold** variables are required.

| Variable | Default | Comments |
|----------|---------|----------|
| `systemd_mounts` | `[]` | List of Systemd mounts to be created. |
| `systemd_mounts[].after` |  | Refer to official documentation on _[After](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#After=)_. |
| `systemd_mounts[].before` |  | Refer to official documentation on _[Before](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#Before=)_. |
| `systemd_mounts[].default_dependencies` | `true` | Refer to official documentation on _[DefaultDependencies](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#DefaultDependencies=)_. |
| `systemd_mounts[].description` | `'mount ' ~ mount.where` | Refer to official documentation on _[Description](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#Description=)_. 
| `systemd_mounts[].force_unmount` |  | Refer to official documentation on _[ForceUnmount](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#ForceUnmount=)_. |
| `systemd_mounts[].lazy_unmount` |  | Refer to official documentation on _[LazyUnmount](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#LazyUnmount=)_. |
| `systemd_mounts[].mode` |  | Refer to official documentation on _[DirectoryMode](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#DirectoryMode=)_. |
| `systemd_mounts[].options` |  | Refer to official documentation on _[Options](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#Options=)_. |
| `systemd_mounts[].read_write_only` |  | Refer to official documentation on _[ReadWriteOnly](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#ReadWriteOnly=)_. |
| `systemd_mounts[].requires` |  | Refer to official documentation on _[Requires](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#Requires=)_. |
| `systemd_mounts[].sloppy_options` |  | Refer to official documentation on _[SloppyOptions](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#SloppyOptions=)_. |
| `systemd_mounts[].timeout` |  | Refer to official documentation on _[TimeoutSec](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#TimeoutSec=)_. |
| `systemd_mounts[].type` |  | Refer to official documentation on _[Type](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#Type=)_. |
| `systemd_mounts[].wants` |  | Refer to official documentation on _[Wants](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#Wants=)_. |
| **`systemd_mounts[].what`** |  | Refer to official documentation on _[What](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#What=)_. |
| **`systemd_mounts[].where`** |  | Refer to official documentation on _[Where](https://www.freedesktop.org/software/systemd/man/systemd.mount.html#Where=)_. |
| `systemd_mounts[].auto_mount` | `false` | Add also an automount unit. |
| `systemd_mounts_clear` | `false` | Remove undefined mount points from `/etc/systemd/system`. Only mounts managed with Ansible will remain. |


## Example Playbook

```yaml
- hosts: all
  vars:
    systemd_mounts_clear: false
    systemd_mounts:
      - what: "172.16.24.192:/mnt/things"
        where: /mnt/things
        type: nfs
        options: auto

  roles:
    - aisbergg.systemd_mounts
```

## License

MIT

## Author Information

Andre Lehmann (aisberg@posteo.de)

import subprocess
from pathlib import Path

from ansible.errors import AnsibleFilterError


class FilterModule(object):

    def filters(self):
        return {
            'systemd_mount_file_name': self.systemd_mount_file_name,
            'excessive_mount_files': self.excessive_mount_files,
        }

    def systemd_mount_file_name(self, path, suffix='mount'):
        cmd = ['systemd-escape', '-p', '--suffix', suffix, path]
        try:
            return subprocess.check_output(cmd, encoding='utf-8').strip()
        except subprocess.CalledProcessError as e:
            raise AnsibleFilterError('Failed to create mount file name: ' + str(e)) from e

    def _systemd_unescape(self, path):
        cmd = ['systemd-escape', '-p', '-u', path]
        try:
            return subprocess.check_output(cmd, encoding='utf-8').strip()
        except subprocess.CalledProcessError as e:
            raise AnsibleFilterError('Failed to unescape mount name: ' + str(e)) from e

    def excessive_mount_files(self, defined_mounts, existing_mount_service_files):
        existing_mount_service_files = set(existing_mount_service_files)

        # create service file paths for defined mounts
        defined_mount_service_files = {
            '/etc/systemd/system/' + self.systemd_mount_file_name(mnt['where']) for mnt in defined_mounts
        }

        # create difference
        diff = existing_mount_service_files.difference(defined_mount_service_files)

        # turn mount service file names into service names
        excessive_mounts = [{'where': self._systemd_unescape(Path(p).stem)} for p in diff]

        return excessive_mounts

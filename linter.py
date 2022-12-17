from SublimeLinter.lint import Linter
from shutil import which
import sublime


class Shellcheck(Linter):
    cmd = 'tldr ${args}'
    if sublime.platform() == 'windows' and not which('tldr') and which('wsl'):
        cmd = 'wsl ' + cmd

    regex = (r'^.+?:(?P<line>[0-9]+): (?<message>.+)$')

    defaults = {
    }

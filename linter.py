#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Joshua Hagins
# Copyright (c) 2015 Joshua Hagins
#
# License: MIT
#

"""This module exports the RubyLint plugin class."""

from SublimeLinter.lint import RubyLinter


class RubyLint(RubyLinter):

    """Provides an interface to ruby-lint."""

    syntax = ('ruby', 'ruby on rails', 'rspec')
    cmd = 'ruby-lint@ruby'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 2.0.0'
    regex = (
        r'^.+?: (?:(?P<warning>warning)|(?P<error>error)): '
        r'line (?P<line>\d+), column (?P<col>\d+): '
        r'(?P<message>.+)'
    )
    tempfile_suffix = 'rb'
    config_file = ('--config', 'ruby-lint.yml')

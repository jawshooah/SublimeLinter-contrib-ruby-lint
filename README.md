SublimeLinter-contrib-ruby-lint
================================

[![Build Status](https://travis-ci.org/jawshooah/SublimeLinter-contrib-ruby-lint.svg?branch=master)](https://travis-ci.org/jawshooah/SublimeLinter-contrib-ruby-lint)
[![Codacy Badge](https://www.codacy.com/project/badge/fe2c9325e1f34ecfb8dbc79012e2c719)](https://www.codacy.com/public/haginsjosh/SublimeLinter-contrib-ruby-lint)

This linter plugin for [SublimeLinter][docs] provides an interface to [ruby-lint](https://github.com/YorickPeterse/ruby-lint). It will be used with files that have the “Ruby” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `ruby-lint` is installed on your system. To install `ruby-lint`, do the following:

1. Install [Ruby](http://www.ruby-lang.org).

1. Install `ruby-lint` by typing the following in a terminal:
   ```
   [sudo] gem install ruby-lint
   ```

1. If you are using `rbenv` or `rvm`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#shell-startup-files) for more information.


**Note:** This plugin requires `ruby-lint` 2.0.0 or later.

### Linter configuration
In order for `ruby-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `ruby-lint`, you can proceed to install the SublimeLinter-contrib-ruby-lint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `ruby-lint`. Among the entries you should see `SublimeLinter-contrib-ruby-lint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

By default, the linter plugin looks for a config file called `ruby-lint.yml` in the current directory and its parents. To override the config file path, you would add this to the linter settings:

```json
"ruby-lint": {
    "args": ["--config", "path/to/ruby-lint.yml"]
}
```

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

##### IMPORTANT!
Also note that this repository uses [overcommit](https://github.com/causes/overcommit) as a validation tool. Before making any changes, please [install overcommit](https://github.com/causes/overcommit#installation) in your local repository.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings

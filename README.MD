# Early Development

This software is not tested yet and this are very early code that i don't even know if it works. I'll test it in the future on a VM

## Objectives

- Learn more about python
- Learn how to interact with package managers
- Re-Design the Interface of my previous tool
- Try to improve this tool over time

## Testing Builds Available

- Testing builds for Windows now available (expect most of them to not work at all)

## Dependencies

This tool tries to install all the things needed to work but anyway this are de dependencies

- Scoop (Commands in install instructions)
- Chocolatey (Commands in install instructions)
- Winget (Will be installed automatically as a dependency)

## Why Python?

Because i like python and it's easy

## Tkinter

Tkinter is a basic Graphical User Interface builder for python and i used it for some error messages and information boxes.

## CustomTkinter

With CustomTkinter you can create modern looking user interfaces in python with tkinter. CustomTkinter is a tkinter extension which provides extra ui-elements like the CTkButton, which can be used like a normal tkinter.Button, but can be customized with a border and round edges.


## Scoop

Scoop installs programs you know and love, from the command line with a minimal amount of friction. It:

- Eliminates permission popup windows
- Hides GUI wizard-style installers
- Prevents PATH pollution from installing lots of programs
- Avoids unexpected side-effects from installing and uninstalling programs
- Finds and installs dependencies automatically
- Performs all the extra setup steps itself to get a working program

## Chocolatey

Chocolatey is a software management solution that allows you to manage 100% of your software, anywhere you have Windows, with any endpoint management tool. No other solution (including newly announced solutions) reach this level of management - most only can manage to software in Programs and Features.

## Winget

Windows Package Manager winget command-line tool is bundled with Windows 11 and modern versions of Windows 10 by default as the App Installer.

If you are running an earlier version of Windows and the App Installer is not installed, you can get App Installer from the Microsoft Store. If it's already installed, make sure it is updated with the latest version.

### Microsoft prevented scripts for installing winget automatically so you just need to update your Application Installer from the store to get winget working. 

## How to Download and update this tool (Windows)

- You can download it directly here and install each version (Please only install stable releases)
- You can add my scoop bucket to your Windows and download it with scoop that will be easier to update. (Only stable releases will be availabe)

<!-- 

### Install Scoop

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

```

### Install Chocolatey

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

```

### Install Sudo

```
choco install sudo

```

### Install Git

```
scoop install git

```

### Add my scoop bucket

```
scoop bucket add filmabem https://github.com/FilmaBem2/applications.git

```

### Install FB-Install-Tool

```
scoop install fb-install-tool

``` -->


### Pre-configuration

You can configure all the packages you want to install in the 'windowspackages.json' in the list that corresponds to the package managers it is available (use the template from this repo. The file is not shipped by default, if the file exists the ui will not be loaded)

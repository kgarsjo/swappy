# Swappy
> Creates Save Profiles for non-supporting games using git and Python

## What does Swappy do?
Swappy leverages git to partition the contents of a directory into namespaced branches, and to switch between those branches when needed.

## Why is that useful?
My wife and I both play PC games. However, some of the games we play do not provide switchable profiles for saves. My saves and hers are all in the same save-folder bucket, and we have to manage them carefully.

With swappy, we can swap our saves in and out of the save-folder bucket, effectively creating save profiles. This is done by describing namespaces (git branches), and persisting saves to those namespaces when switching.

## Installation
You will need:
  - `git v2.x`
  - `python v2.x`
  - A clone or download of this repo

## Usage
```bash
python save_folder_swappy_driver.py <folder-to-partition> <partition namespace>
```

## How can I quickly use Swappy via Steam?
Check out the [Steam quick-use guide](steam_quick_setup.md).

## How does it work?
Let's take **The Elder Scrolls V: Skyrim** as an example. It has one save folder, `path/to/skyrim/saves`, and no in-game means of separating saves for multiple players.

Using Swappy, we can create a profile for myself:
```bash
python save_folder_swappy_driver.py path/to/skyrim/saves saves/kgarsjo
```
This will initialize a git project in the skyrim saves directory, and create a new empty branch named `saves/kgarsjo` for my saves to reside in.

I can then create a profile for my wife:
```bash
python save_folder_swappy_driver.py path/to/skyrim/saves saves/the-wife
```
This will check in any saves I've made since creating my profile into my branch, and then create a new empty branch named `saves/the-wife` for her saves to reside in.

Switching back to my profile is exactly the same:
```bash
python save_folder_swappy_driver.py path/to/skyrim/saves saves/kgarsjo
```
This will check in any saves my wife has made since creating her profile into her branch. It will then switch to my existing branch named `saves/kgarsjo` with all of my existing saves.

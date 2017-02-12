# Swappy Fast Profile Switch with Steam

Running python scripts to switch profiles before play can be a pain. However, we can creatively use Steam's Non-Steam Game links to make the process easy.

We can create scripts that switch profiles, and then attach those scripts as Non-Steam Games. In Windows, those will be Batch files. In Linux and Mac OSX, those will be bash scripts.

This guide will assume Windows for simplicity.

## Step 1: Creating Batch scripts for profile switching
For every profile you intend to make switchable, create a `.bat` file that executes the switch.

As an example, here is `kgarsjo_skyrim_profile.bat`:
```bash
python path/to/save_folder_swappy_driver.py path/to/skyrim/saves saves/kgarsjo
```

## Step 2: Create a Non-Steam Game Link
As [this thread describes](http://forums.steampowered.com/forums/showthread.php?t=2658249), Steam will only let you select executables as non-steam-game links. However, you can link to anything via steam with some indirection.

1. In Steam, navigate to **Games > Add a Non-Steam Game to My Library**.
1. Select any executable from the pre-populated list
1. After it's created, find the link in your list of games, right-click, and select **Properties**
  - Edit the name to be what you want. In my example, the name becomes **The Elder Scrolls V: Skyrim - kgarsjo's profile**
  - Edit the target to point to your batch file, `kgarsjo_skyrim_profile.bat`
  - Edit the Start In to point to the directory containing your batch file

Afterwards you can set a custom icon and steam tile, and you have an in-steam link for switching profiles.

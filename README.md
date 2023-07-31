# Flexium
Lite web-based rolling release Linux distro, based on Arch Linux and the `Flexed` modular DE. 
Inspired as a Arch Linux flavour that allows for a Chrome OS-like experience, with access to a real Linux-based OS.

It can be used by anybody (Calamarium installer and browser-focused experience for beginners, in order to make Flexium an Ubuntu alternative; powerusers can use the preinstalled `kitty` in order to access the Arch Linux package manager and the Runtime Scripts Collection)

## I. What does it contain?
- `pacman` and `yay` for managing packages. (Same repositories as Arch Linux)
- The Linux Zen kernel
- GRUB bootloader
- Web Browser (at the moment, there are editions for [Firefox](https://www.mozilla.org/it/firefox/new/) and [Chromium](https://www.chromium.org/chromium-projects/))
- [`kitty`](https://sw.kovidgoyal.net/kitty/) terminal emulator
- Minimalistic custom Desktop Environments (avaiable both on X11 and Wayland, independent from the rest of Flexium)
- Fully-sandboxed environments (for better security)
- [`calamares`](https://calamares.io/) installation tool
- Runtime Scripts Collection:
    - Scripts for rebuilding Flexium itself
    - Scripts for auto-installing `rg` and `fd` as alternatives to `grep` and `find`
    - Scripts for installing [`thermald`](https://github.com/intel/thermal_daemon) and [`auto-cpufreq`](https://github.com/AdnanHodzic/auto-cpufreq) for better CPU frequency scaling
    - Script for installing the Container Android Subsystem (based on [waydroid](https://waydro.id/))
    - Script to use `cpulimit` in order to make the Web Browser smoother limiting the rest of the OS
- Building Scripts Collection:
    - Build ISO images (Bootstrap, ISO or Netboot)
    - Select X11 or Wayland, Firefox or Chromium, Flexed or KDE.

## II. How to build

Required dependencies: `archiso`, `bash`-compatible shell.  
After you clone the Git repository:

1. `git submodule sync && cd flexed && cargo build --release && cd ..` (Only if you want to build the OS with Flexed)
2. `cd build_scripts`
3. Run one of the `select_X.sh` if you want to customize the image
4. `./build_iso.sh interactive`
5. Congratulations! You have built your own image of Flexium.

## III. How to install

### III.I. Get the ISO

Either:

- Download from Github Releases
- Build following the instruction above

### III.II. Flash drive

Flash your drive using something like Balena Etcher.

### III.III. Run the Live OS

Plug your drive into your computer, boot it up, select the drive and enter the Live environment.
From there you can try Flexium or can launch the "Installer" application in order to install on the drive.

## IV. Missing features

- Grafico GUI Suite:
    - Optional GUI installer (`yay` frontend).
    - Optional GUI for accessing the Runtime Scripts Collection
    - Optional GUI for customizing Flexed
- Installing Flexed without having to compile each time (as Arch package)

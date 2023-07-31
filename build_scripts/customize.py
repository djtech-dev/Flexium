#!/bin/python

def select_x11():
	pass
def select_wayland():
	pass
def select_firefox():
	_packages_rm("chromium")
	_packages_add("firefox")
def select_chromium():
	_packages_add("chromium")
	_packages_rm("firefox")
def enable_flexed():
	_packages_rm("plasma-desktop")
	if 'wayland' in _all_packages:
		depends = _flexed_config_dependencies('../flexed/default/minima_wayland.json')
	elif 'xorg' in _all_packages:
		depends = _flexed_config_dependencies('../flexed/default/minima_xorg.json')
	else:
		select_x11()
		depends = _flexed_config_dependencies('../flexed/default/minima_xorg.json')
	for pkg in depends:
		_packages_add(pkg)
def enable_kde():
	_packages_add("plasma-desktop")
	if 'wayland' in _all_packages:
		depends = _flexed_config_dependencies('../flexed/default/minima_wayland.json')
	elif 'xorg' in _all_packages:
		depends = _flexed_config_dependencies('../flexed/default/minima_xorg.json')
	else:
		select_x11()
		depends = _flexed_config_dependencies('../flexed/default/minima_xorg.json')
	for pkg in depends:
		_packages_rm(pkg)
def enable_vm():
	_packages_add("virtualbox-guest-utils-nox")
	_packages_add("qemu-guest-agent")
	_packages_add("open-vm-tools")
	_packages_add("hyperv")

def disable_vm():
	_packages_rm("virtualbox-guest-utils-nox")
	_packages_rm("qemu-guest-agent")
	_packages_rm("open-vm-tools")
	_packages_rm("hyperv")

def disable_all():
	disable_vm()
	_packages_rm("plasma-desktop")
	_packages_rm("firefox")
	_packages_rm("chromium")
	if 'wayland' in _all_packages:
		depends = _flexed_config_dependencies('../flexed/default/minima_wayland.json')
	elif 'xorg' in _all_packages:
		depends = _flexed_config_dependencies('../flexed/default/minima_xorg.json')
	else:
		select_x11()
		depends = _flexed_config_dependencies('../flexed/default/minima_xorg.json')
	for pkg in depends:
		_packages_rm(pkg)
def menu():
	print("[1] Enable/disable VM integrations ")
	print("[2] Use X11")
	print("[3] Use Wayland")
	print("[4] Use KDE for Desktop")
	print("[5] Use Flexed for Desktop")
	print("[6] Use Firefox as Web Browser")
	print("[7] Use Chromium as Web Browser")
	print("[8] Change Flexed JSON configuration")
	print("[L] List Flexed configuration's dependencies")
	print("[R] Reset to the NoArch configuration")
	print("[Q] Quit ")

if __name__ == "__main__":
	menu()

# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device RMX3852
%define vendor realme
%define vendor_pretty Realme
%define device_pretty GT Neo 6
%define rpm_device RMX3852
%define installable_zip 1

%define droid_target_aarch64 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries / /odm /product /system /system_ext /vendor /vendor_dlkm /system_dlkm


%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"


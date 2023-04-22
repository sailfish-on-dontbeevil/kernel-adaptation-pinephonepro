# Device details
%define device pinephonepro

# Kernel target architecture
%define kernel_arch arm64

# Crossbuild toolchain to use
%define crossbuild aarch64

# RPM target architecture, remove to leave it unaffected
# You should have a good reason to change the target architecture
# (like building on aarch64 targeting an armv7hl repository)
%define device_target_cpu aarch64

# Defconfig to pick-up
%define defconfig pinephone_pro_defconfig

# Linux kernel source directory
%define source_directory linux/

# Build modules
%define build_modules 1

# Build Image
%define build_Image 1

# Apply Patches
%define apply_patches 1

# Build uImage
##define build_uImage 1

# Build zImage
##define build_zImage 1

# Build and pick-up the following devicetrees
%define devicetrees rockchip/rk3399-pinephone-pro.dtb

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc

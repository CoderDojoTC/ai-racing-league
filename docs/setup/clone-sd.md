# Cloning a microSD Card using UNIX `dd` Command

This guide explains how to clone a microSD card using the `dd` command on UNIX and UNIX-like systems.

---

## Table of Contents

- [Cloning a microSD Card using UNIX `dd` Command](#cloning-a-microsd-card-using-unix-dd-command)
  - [Table of Contents](#table-of-contents)
  - [Identify the microSD Card Device](#identify-the-microsd-card-device)
  - [Unmount the microSD Card](#unmount-the-microsd-card)
  - [Create a Backup Image](#create-a-backup-image)
  - [Copy the Backup Image to New microSD Cards](#copy-the-backup-image-to-new-microsd-cards)
  - [Expand the Filesystem (Optional)](#expand-the-filesystem-optional)

---

## Identify the microSD Card Device

1. First, identify the device name for your microSD card. Use either `lsblk` or `df` to list devices and their mount points.

    ```bash
    lsblk
    ```

    Or:

    ```bash
    df -h
    ```

2. Look for the device corresponding to your microSD card. It's generally something like `/dev/sdX` or `/dev/mmcblkX`, where `X` is a letter.

    ⚠️ **Caution**: Be very careful to identify the correct device, as choosing the wrong one could result in data loss.

---

## Unmount the microSD Card

1. Before copying data, unmount the partitions of the microSD card to ensure that no data is being read or written during the cloning process.

    ```bash
    sudo umount /dev/sdX*
    ```

---

## Create a Backup Image

1. Use the `dd` command to create an image file of the microSD card.

    ```bash
    sudo dd if=/dev/sdX of=raspberrypi_backup.img bs=4M status=progress
    ```

    - `if`: Input File — the device you are copying from (your microSD card).
    - `of`: Output File — the image file you are creating.
    - `bs`: Block Size — specifies how much data should be read at each iteration. `4M` is usually a good size.
    - `status=progress`: shows the progress during the copy.

---

## Copy the Backup Image to New microSD Cards

1. To clone the image onto a new microSD card, insert the new card and identify it just like you did in the first step.

    ```bash
    sudo dd if=raspberrypi_backup.img of=/dev/sdY bs=4M status=progress
    ```

    Replace `/dev/sdY` with the device name of your new microSD card.

    ⚠️ **Caution**: Again, be very careful to identify the correct device to avoid data loss.

---

## Expand the Filesystem (Optional)

1. If your new microSD card is larger than the original, you might need to expand the filesystem to use the additional space. You can do this using `raspi-config` on the Raspberry Pi.

    ```bash
    sudo raspi-config
    ```

    Navigate to `Advanced Options` > `Expand Filesystem`.

After following these steps, you should have successfully cloned your Raspberry Pi's microSD card.

---

**Note**: The `dd` command can be very dangerous if misused. Always double-check your device names and ensure you understand the commands you're running.

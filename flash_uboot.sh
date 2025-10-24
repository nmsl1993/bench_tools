#! /bin/bash

TFTP_DIR=/srv/tftp
IMAGES_DIR=/home/noah/Development/buildroot/output/images

rsync -av --progress ${IMAGES_DIR}/u-boot-dtb.imx ${TFTP_DIR}/u-boot-dtb.imx
rsync -av --progress ${IMAGES_DIR}/imx6ull-ninefives-poe.dtb ${TFTP_DIR}/imx6ull-ninefives-poe.dtb
rsync -av --progress ${IMAGES_DIR}/zImage ${TFTP_DIR}/zImage


BUILDROOT_DIR=/home/noah/Development/buildroot
python3 /home/noah/Development/bench_tools/ch1_off.py
sleep 0.5
python3 /home/noah/Development/bench_tools/ch1_on.py
ls -ltrah ${BUILDROOT_DIR}/output/images/*.imx
uuu -v ${TFTP_DIR}/u-boot-dtb.imx



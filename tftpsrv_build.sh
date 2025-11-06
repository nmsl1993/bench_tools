#! /bin/bash

TFTP_DIR=/srv/tftp
IMAGES_DIR=/home/noah/Development/buildroot/output/images

rsync -av --progress ${IMAGES_DIR}/u-boot-dtb.imx ${TFTP_DIR}/u-boot-dtb.imx
rsync -av --progress ${IMAGES_DIR}/imx6ull-ninefives-poe.dtb ${TFTP_DIR}/imx6ull-ninefives-poe.dtb
rsync -av --progress ${IMAGES_DIR}/zImage ${TFTP_DIR}/zImage

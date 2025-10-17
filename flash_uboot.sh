#! /bin/bash

BUILDROOT_DIR=/home/noah/Development/buildroot
python3 /home/noah/Development/bench_tools/ch1_off.py
sleep 0.5
python3 /home/noah/Development/bench_tools/ch1_on.py
ls -ltrah ${BUILDROOT_DIR}/output/images/*.imx
uuu -v ${BUILDROOT_DIR}/output/images/u-boot-dtb.imx


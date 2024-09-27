# Splitkb Kyria

## Components

Kyria Acrylic Plate Case Clear
Kailh Low Profile Choc Switches - Silver (linear)
Kailh Choc Transparent Keycaps
Elite-C Low Profile (rev4) Microcontroller
Kyria PCB Kit - Black
Kyria rev2 PCB Kit
SSD1306 OLED Display 128x64

## Firmware

Assuming QMK MSYS is configured (`qmk setup`) and has the latest clone of `qmk/qmk_firmware` I compiled the firmware with this command:

``` sh
qmk compile -kb splitkb/kyria/rev1 -km default
```

The result should look like this:

``` sh
Ψ Compiling keymap with make -r -R -f builddefs/build_keyboard.mk -s KEYBOARD=splitkb/kyria/rev1/base KEYMAP=default KEYBOARD_FILESAFE=splitkb_kyria_rev1_base TARGET=splitkb_kyria_rev1_base_default VERBOSE=false COLOR=true SILENT=false QMK_BIN="qmk"


Generating: .build/obj_splitkb_kyria_rev1_base_default/src/info_deps.d                              [OK]
avr-gcc.exe (GCC) 12.2.0
Copyright (C) 2022 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Generating: .build/obj_splitkb_kyria_rev1_base_default/src/info_config.h                            [OK]
Generating: .build/obj_splitkb_kyria_rev1_base_default/src/default_keyboard.c                       [OK]
Generating: .build/obj_splitkb_kyria_rev1_base_default/src/default_keyboard.h                       [OK]
Compiling: keyboards/splitkb/kyria/kyria.c                                                          [OK]
Compiling: keyboards/splitkb/kyria/rev1/rev1.c                                                      [OK]
Compiling: .build/obj_splitkb_kyria_rev1_base_default/src/default_keyboard.c                        [OK]
Compiling: quantum/keymap_introspection.c                                                           [OK]
Compiling: quantum/quantum.c                                                                        [OK]
Compiling: quantum/bitwise.c                                                                        [OK]
Compiling: quantum/led.c                                                                            [OK]
Compiling: quantum/action.c                                                                         [OK]
Compiling: quantum/action_layer.c                                                                   [OK]
Compiling: quantum/action_tapping.c                                                                 [OK]
Compiling: quantum/action_util.c                                                                    [OK]
Compiling: quantum/eeconfig.c                                                                       [OK]
Compiling: quantum/keyboard.c                                                                       [OK]
Compiling: quantum/keymap_common.c                                                                  [OK]
Compiling: quantum/keycode_config.c                                                                 [OK]
Compiling: quantum/sync_timer.c                                                                     [OK]
Compiling: quantum/logging/debug.c                                                                  [OK]
Compiling: quantum/logging/sendchar.c                                                               [OK]
Compiling: quantum/matrix_common.c                                                                  [OK]
Compiling: quantum/matrix.c                                                                         [OK]
Compiling: quantum/debounce/sym_defer_g.c                                                           [OK]
Compiling: quantum/split_common/split_util.c                                                        [OK]
Compiling: quantum/split_common/transport.c                                                         [OK]
Compiling: quantum/split_common/transactions.c                                                      [OK]
Compiling: quantum/main.c                                                                           [OK]
Assembling: platforms/avr/xprintf.S                                                                 [OK]
Compiling: platforms/avr/printf.c                                                                   [OK]
Compiling: quantum/color.c                                                                          [OK]
Compiling: quantum/rgblight/rgblight.c                                                              [OK]
Compiling: quantum/rgblight/rgblight_drivers.c                                                      [OK]
Compiling: quantum/process_keycode/process_rgb.c                                                    [OK]
Compiling: quantum/led_tables.c                                                                     [OK]
Compiling: drivers/oled/oled_driver.c                                                               [OK]
Compiling: quantum/encoder.c                                                                        [OK]
Compiling: drivers/encoder/encoder_quadrature.c                                                     [OK]
Compiling: platforms/avr/drivers/ws2812_bitbang.c                                                   [OK]
Compiling: quantum/crc.c                                                                            [OK]
Compiling: quantum/process_keycode/process_grave_esc.c                                              [OK]
Compiling: quantum/process_keycode/process_magic.c                                                  [OK]
Compiling: quantum/send_string/send_string.c                                                        [OK]
Compiling: quantum/process_keycode/process_space_cadet.c                                            [OK]
Compiling: tmk_core/protocol/host.c                                                                 [OK]
Compiling: tmk_core/protocol/report.c                                                               [OK]
Compiling: tmk_core/protocol/usb_device_state.c                                                     [OK]
Compiling: tmk_core/protocol/usb_util.c                                                             [OK]
Compiling: platforms/suspend.c                                                                      [OK]
Compiling: platforms/synchronization_util.c                                                         [OK]
Compiling: platforms/timer.c                                                                        [OK]
Compiling: platforms/avr/hardware_id.c                                                              [OK]
Compiling: platforms/avr/platform.c                                                                 [OK]
Compiling: platforms/avr/suspend.c                                                                  [OK]
Compiling: platforms/avr/timer.c                                                                    [OK]
Compiling: platforms/avr/bootloaders/dfu.c                                                          [OK]
Compiling: platforms/avr/drivers/i2c_master.c                                                       [OK]
Archiving: .build/obj_splitkb_kyria_rev1_base_default/i2c_master.o                                  [OK]
Compiling: platforms/avr/drivers/i2c_slave.c                                                        [OK]
Archiving: .build/obj_splitkb_kyria_rev1_base_default/i2c_slave.o                                   [OK]
Compiling: platforms/avr/drivers/serial.c                                                           [OK]
Archiving: .build/obj_splitkb_kyria_rev1_base_default/serial.o                                      [OK]
Compiling: tmk_core/protocol/lufa/lufa.c                                                            [OK]
Compiling: tmk_core/protocol/usb_descriptor.c                                                       [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Class/Common/HIDParser.c                                       [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/AVR8/Device_AVR8.c                                        [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/AVR8/EndpointStream_AVR8.c                                [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/AVR8/Endpoint_AVR8.c                                      [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/AVR8/Host_AVR8.c                                          [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/AVR8/PipeStream_AVR8.c                                    [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/AVR8/Pipe_AVR8.c                                          [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/AVR8/USBController_AVR8.c                                 [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/AVR8/USBInterrupt_AVR8.c                                  [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/ConfigDescriptors.c                                       [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/DeviceStandardReq.c                                       [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/Events.c                                                  [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/HostStandardReq.c                                         [OK]
Compiling: lib/lufa/LUFA/Drivers/USB/Core/USBTask.c                                                 [OK]
Compiling: tmk_core/protocol/lufa/usb_util.c                                                        [OK]
Linking: .build/splitkb_kyria_rev1_base_default.elf                                                 [OK]
Creating load file for flashing: .build/splitkb_kyria_rev1_base_default.hex                         [OK]
Copying splitkb_kyria_rev1_base_default.hex to qmk_firmware folder                                  [OK]
Checking file size of splitkb_kyria_rev1_base_default.hex                                           [OK]
 * The firmware size is fine - 27000/28672 (94%, 1672 bytes free)
```

The file `splitkb_kyria_rev1_base_default.hex` is now in the `qmk_firmware` folder. Type `pwd` and look for a folder named `qmk_firmware` in that path. The `*.hex` file should be located there.

Time to flash the firmware using `QMK Toolbox`. Load the firmware and selet `ATmega32U4` as MCU, then connect the Microcontroller and press `Flash`.

The result should look like this:

```sh
Atmel DFU device connected (WinUSB): Atmel Corp. ATm32U4DFU (03EB:2FF4:0000)
Attempting to flash, please don't remove device
> dfu-programmer.exe atmega32u4 erase --force
> Erasing flash...  Success
> Checking memory from 0x0 to 0x6FFF...  Empty.
> dfu-programmer.exe atmega32u4 flash --force "C:\Users\0xfab1\qmk_firmware\splitkb_kyria_rev1_base_default.hex"
> Programming 0x6980 bytes...
> Success
> Reading 0x7000 bytes...
> Success
> Validating...  Success
> 0x6980 bytes written into 0x7000 bytes memory (94.20%).
> dfu-programmer.exe atmega32u4 reset
Flash complete
Atmel DFU device disconnected (WinUSB): Atmel Corp. ATm32U4DFU (03EB:2FF4:0000)
```

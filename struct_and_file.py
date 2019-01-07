#!/usr/bin/python3
import struct
import binascii

FLASH_AREA_CODE=0x7c05e516
BOOT_CONFIG_STR='BOOT_CONFIG'
APP_CODE_STR='APP_CODE'
F35_APP_CODE_STR='F35_APP_CODE'
APP_CONFIG_STR='APP_CONFIG'
DISPLAY_CONFIG_STR='DISPLAY'

def get_int_from_bytes(num_byte):
    return int.from_bytes(num_byte, byteorder='little')

img_file = open('firmware.img', 'rb')
img_file_str = img_file.read()

header_format = struct.Struct('4s4s')
header_size = header_format.size
(magic, num_area) = header_format.unpack_from(img_file_str, 0)
print(binascii.hexlify(magic))

magic_num = get_int_from_bytes(magic)
area_num = get_int_from_bytes(num_area)
print(hex(magic_num), area_num)
for i in range(1, area_num + 1):
    print('\n\n')
    offset = img_file_str[header_size:header_size+4]
    offset = get_int_from_bytes(offset)

    area_description_format = struct.Struct('4s16s4s4s4s4s')
    (magic_value, id_string, flags, flash_addr_words, length, checksum) = area_description_format.unpack_from(img_file_str, offset)
    print(id_string, magic_value)
    header_size = header_size + 4
    length = get_int_from_bytes(length)
    checksum = get_int_from_bytes(checksum)
    flash_addr_words = get_int_from_bytes(flash_addr_words) * 2


    content_start_addr = offset + area_description_format.size
    content_end_addr = content_start_addr + length
    content = img_file_str[content_start_addr:content_end_addr]
    crc_value = binascii.crc32(content)
    if (get_int_from_bytes(magic_value) != FLASH_AREA_CODE):
        continue
    else:
        if (crc_value == checksum):
            print("find a valid flash area description")
            if (BOOT_CONFIG_STR == id_string[0:len(BOOT_CONFIG_STR)].decode(encoding='utf-8')):
                print("find boot config")
                print('boot config length is %x, start addr %x, checksum:%x'%(length, flash_addr_words, checksum))
            if (DISPLAY_CONFIG_STR == id_string[0:len(DISPLAY_CONFIG_STR)].decode(encoding='utf-8')):
                print("find display config")
                print('display length is %x, start addr %x, checksum:%x'%(length, flash_addr_words, checksum))
            if (APP_CODE_STR == id_string[0:len(APP_CODE_STR)].decode(encoding='utf-8')):
                print("find app_code")
                print('app code length is %x, start addr %x, checksum:%x'%(length, flash_addr_words, checksum))
            if (APP_CONFIG_STR == id_string[0:len(APP_CONFIG_STR)].decode(encoding='utf-8')):
                print("find app config")
                print('app config length is %x, start addr %x, checksum:%x'%(length, flash_addr_words, checksum))
            if (F35_APP_CODE_STR == id_string[0:len(F35_APP_CODE_STR)].decode(encoding='utf-8')):
                print("find app_code")
                print('app code length is %x, start addr %x, checksum:%x'%(length, flash_addr_words, checksum))

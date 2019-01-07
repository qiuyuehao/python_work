#!/usr/bin/python3

a = "qiuyuehao"
print(a[2])
c = a.join("hello")
print(a + "hello")
a = [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1]
b = [str(i) for i in a]
print(b)
c = ''.join(b)
print(c)
print(type(c))
d = c.split('0')
print(d)
e = bytearray(a)
print(type(e))
print(e)
f = e.split(b'\x00')
print(f)
print(type(f))
#  output
#  u
#  qiuyuehaohello
#  ['1', '1', '0', '0', '1', '1', '1', '0', '0', '1', '1', '1', '1']
#  1100111001111
#  <class 'str'>
#  ['11', '', '111', '', '1111']
#  <class 'bytearray'>
#  bytearray(b'\x01\x01\x00\x00\x01\x01\x01\x00\x00\x01\x01\x01\x01')
#  [bytearray(b'\x01\x01'), bytearray(b''), bytearray(b'\x01\x01\x01'), bytearray(b''), bytearray(b'\x01\x01\x01\x01')]
#  <class 'list'>

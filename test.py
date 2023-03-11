from pwn import *

target = remote("github.com", 9000)
target = process("./challenge")
gdb.attach(target)
gdb.attach(target, gdbscript='b *main')
target.send(x)
target.sendline(x)
print target.recvline()
print target.recvuntil("out")
p64(x)
p32(x)
u64(x)
u32(x)
target.interactive()

.data

a:
.word 100
b:
.word 0
x:
.word 1
y:
.word 0
z:
.word 0
c:
.word 0
i:
.word 0

.text

la x1, x
la x2, y
lw x3, 0(x1)
lw x4, 0(x2)
and x5, x3, x4
la x1, x
lw x2, 0(x1)
or x3, x5, x2
la x1, x
lw x2, 0(x1)
and x4, x3, x2
la x1, z
sw x4, 0(x1)
li x1, 1
la x2, b
sw x1, 0(x2)
la x1, a
la x2, b
lw x3, 0(x1)
lw x4, 0(x2)
sub x5, x3, x4
la x1, c
sw x5, 0(x1)
li x1, 1
la x2, a
li x3, 2
lw x4, 0(x2)
sub x5, x4, x3
add x2, x1, x5
la x1, b
la x3, b
lw x4, 0(x1)
lw x5, 0(x3)
div x6, x4, x5
li x1, 4
li x3, 2
add x4, x1, x3
mul x1, x6, x4
sub x3, x2, x1
li x1, 3
li x2, 1
la x4, a
lw x5, 0(x4)
sub x6, x2, x5
add x2, x1, x6
sub x1, x3, x2
la x2, c
sw x1, 0(x2)
la x1, a
li x2, 4000
lw x3, 0(x1)
xor x4, x3, x2
seqz x4, x4
la x1, b
li x2, 1000
lw x3, 0(x1)
slt x5, x3, x2
and x1, x4, x5
beqz x1, else0
li x11, 97
addi x10, x0, 11
ecall
li x11, 32
addi x10, x0, 11
ecall
li x11, 61
addi x10, x0, 11
ecall
li x11, 32
addi x10, x0, 11
ecall
la x12, a
lw x11, 0(x12)
addi x10, x0, 1
ecall
li x11, 10
addi x10, x0, 11
ecall
j endif0
else0:
li x11, 333
addi x10, x0, 1
ecall
li x11, 10
addi x10, x0, 11
ecall
endif0:
startwhile0:
la x1, b
li x2, 10
lw x3, 0(x1)
slt x4, x3, x2
beqz x4, endwhile0
li x11, 98
addi x10, x0, 11
ecall
li x11, 32
addi x10, x0, 11
ecall
li x11, 61
addi x10, x0, 11
ecall
li x11, 32
addi x10, x0, 11
ecall
la x12, b
lw x11, 0(x12)
addi x10, x0, 1
ecall
li x11, 10
addi x10, x0, 11
ecall
la x1, b
li x2, 1
lw x3, 0(x1)
add x5, x3, x2
la x1, b
sw x5, 0(x1)
j startwhile0
endwhile0:
startfor0:
la x1, i
lw x2, 0(x1)
addi x2, x2, -5
beq x2, x0, endfor0 
li x11, 105
addi x10, x0, 11
ecall
li x11, 32
addi x10, x0, 11
ecall
li x11, 61
addi x10, x0, 11
ecall
li x11, 32
addi x10, x0, 11
ecall
la x12, i
lw x11, 0(x12)
addi x10, x0, 1
ecall
li x11, 10
addi x10, x0, 11
ecall
la x1, i
lw x2, 0(x1)
addi x2, x2, 1
sw x2, 0(x1)
j startfor0
endfor0:

addi a0, x0, 10
ecall
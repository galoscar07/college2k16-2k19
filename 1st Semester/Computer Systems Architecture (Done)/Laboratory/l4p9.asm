;9. The word A and the byte B are given. Obtain the byte C in the following way:
;- the bits 0-3 of C are the same as the bits 6-9 of A
;- the bits 4-5 of C have the value 1
;- the bits 6-7 of C are the same as the bits 1-2 of B
assume cs:code,ds:data
data segment
	a dw 1000111111111111b
	b db 10101010b
	c db ?
data ends
code segment
start:
	mov ax, data
	mov ds,ax

	mov ax,a
	and ax,0000001111000000b
	mov cl,6
	shr ax,cl
	mov c,al
	
	or c,00110000b
	
	and b,00000110b
	ror b,3
	mov ah,b
	or c, ah
	mov dx,0
	mov dl, c
	
	
	mov ax,4c00h
	int 21h
code ends
end start
	
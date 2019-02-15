assume cs:code,ds:data
data segment
	buffer db 12,?, 10 dup(?)
	ten db 10
	number1 dw ?
data ends
code segment
start:
	push data
	pop ds
	
	mov ah,0Ah
	lea dx,buffer
	int 21h
	
	mov bx,0
	mov ax,0
	repeta:
		cmp bl,buffer[1]
		je save1
		
		mov dl,buffer[bx+2]
		sub dl,'0'
		xor dh,dh
		
		mul ten
		add ax,dx
		
		inc bx
		jmp repeta
		
	save1:
		mov number1,ax
	
	mov ax,number1
	
	mov ah,09h
	mov dx,offset number1
	int 21
	
	mov ax,4c00h
	int 21h
	
code ends
end start
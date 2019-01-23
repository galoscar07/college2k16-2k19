;citeste in baza 10 pune in registru si scrie in fisier valoare registrului ax in baza 2
assume cs:code,ds:data
data segment
	buffer db 12,?, 10 dup(?)
	ten db 10
	number dw ?
	filename db 'test.txt','0'
	binary db 16 dup(?)
	len equ $-binary
	handle dw ?
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
		je save
	
		mov dl,buffer[bx+2]
		sub dl,'0'
		xor dh,dh
		mul ten
		add ax,dx
		inc bx
		jmp repeta
		
	save:
		mov number,ax
	
	mov ax,number
	mov bx,16
	convertbinary:
		cmp bx,0
		je print
		shr ax,1
		jc one
		
		mov binary[bx-1],'0'
		dec bx
		jmp convertbinary
		
		one:
			mov binary[bx-1],'1'
			dec bx
			jmp convertbinary
			
	print:
		clc
		mov ah, 3dh
		mov al,1
		mov dx, offset filename
		int 21h
		
		mov handle,ax
		
		mov ah,40h
		mov bx,handle
		mov cx,len
		mov dx,offset binary
		int 21h
	
		mov ah, 3eh
		mov bx, handle
		int 21h
		
		mov ax,4c00h
		int 21h
		
code ends
end start
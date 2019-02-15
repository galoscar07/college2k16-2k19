;Nota 5
;Citesc de la tastatura un nr in baza 10 max 65335
;Si il punem intr-un registru sau o variabila
;Il pun in fisier in alta baza decat baza 10
assume cs:code,ds:data

data segment
	buffer db 12,?, 10 dup(?)
	ten db 10
	number1 dw ?
	file_name db "file.txt",0
	buffer_output db 16 dup(?)
	len equ $ - buffer_output
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
	.while:
		cmp bl,buffer[1]
		je .save1
		
		mov dl,buffer[bx+2]
		sub dl,'0'
		xor dh,dh
		
		mul ten
		add ax,dx
		
		inc bx
		jmp .while
		
	.save1:
		mov number1,ax
		
	mov ah,0Ah
	lea dx,buffer
	int 21h
	
	mov bx,0
	mov ax,0
	.while2:
		cmp bl,buffer[1]
		je .save2
		
		mov dl,buffer[bx+2]
		sub dl,'0'
		xor dh,dh
		
		mul ten
		add ax,dx
		
		inc bx
		jmp .while2
		
	.save2:
		add ax,number1
		
	;Convert to other base
	mov bx,16
	.while_binary:
		cmp bx,0
		je .print_file
		
		shr ax,1
		jc .one
		
		;Otherwise it's zero
		mov buffer_output[bx-1],'0'
		dec bx
		jmp .while_binary
		
		.one:
			mov buffer_output[bx-1],'1'
			dec bx
			jmp .while_binary
	
	.print_file:
		
		;Open file
		mov ah,3dh
		mov al,1
		mov dx,offset file_name
		int 21h
		jc .end
		
		;Otherwise is not an error and save handle
		mov handle,ax
		
		;Write in file
		mov ah,40h
		mov bx,handle
		mov cx,len
		mov dx,offset buffer_output
		int 21h
		jc .end
		
	
	.end:
		mov ax,4c00h
		int 21h
	

code ends
end start
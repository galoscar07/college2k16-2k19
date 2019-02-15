assume cs:code,ds:data
data segment
	msg1 db 'Give a file: $'
	msg2 db 'Give a number: $'
	filename db 12,?,13 dup(?)
	number dw ?
	handler dw 0
data ends
code segment
start:
	push data
	pop ds
	
	mov ah,09h
	mov dx, offset msg1
	int 21
	
	mov ah,0ah
	mov dx,offset filename
	int 21
	
	mov ah,09h
	mov dx,offset msg2
	int 21
	
	mov ah,0ah
	mov dx, offset number
	int 21
	
	mov bl,filename[1]
	mov bh,0
	add bx, offset filename
	add bx,2
	mov byte ptr[bx],0
	
	mov ah,3dh
	mov al,0
	mov dx, offset filename+2
	int 21
	
	mov handler,ax
	
	mov ah,40h
	mov bx,handler
	mov cx,100
	mov dx,offset number+2
	int 21
	
	mov ax, 4c00h
	int 21
code ends
end start
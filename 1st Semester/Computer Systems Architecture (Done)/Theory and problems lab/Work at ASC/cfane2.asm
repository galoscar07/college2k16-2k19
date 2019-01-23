assume cs:code,ds:data
data segment
	filename db 'file.txt'
data ends
code segment
start:
	mov ax,data
	mov ds,ax
	
	add bx,offset filename
	
	mov byte ptr [bx],0
	
	mov ah, 3dh
	mov al,0
	mov dx,offset filename
	int 21h
	
	
	mov ax,4c00h
	int 21h
code ends
end start
	
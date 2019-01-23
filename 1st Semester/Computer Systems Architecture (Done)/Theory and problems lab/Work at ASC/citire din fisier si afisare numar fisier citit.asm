assume cs:code,ds:data
data segment
	message db 'Numele fisiersului: $'
	filename db 12,?,13 dup (?)
	handler dw 0
	string db 100 dup(?),'$'
data ends
code segment
start:
	mov ax,data
	mov ds,ax
	

	mov ah,09h			
	mov dx,offset message			
	int 21h
	

	mov ah,0Ah			
	mov dx,offset filename			
	int 21h
	

	mov bl,filename[1]
	mov bh,0
	add bx, offset filename
	add bx,2
	mov byte ptr[bx],0
	

	mov ah,3Dh       
	mov al,0				
	mov dx, offset filename+2    
	int 21h
	
	mov handler,ax		
		
	readfromfile:
		;the function that reads from the file
		mov ah,3Fh
		mov bx,handler
		mov dx,offset string
		mov cx,100
		int 21h
		
		
		mov si,ax
		mov string[si],'$'
		mov ah,09h
		int 21h
		
		
		cmp si,100
		je readfromfile
		jmp closefile
		
	closefile:
		mov ah,3Eh
		int 21h
		mov ax,4C00h
		int 21
		
code ends
end start
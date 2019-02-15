assume ds:data, cs:code
data segment
	a db 'abc$'  ;a $ terminated string
data ends
code segment
start:
	mov ax,data
	mov ds,ax

	;printing a character
	mov dl, 1100001b
	mov ah,02h
	int 21h

	;printing the “new line” character
	mov dl,10
	mov ah,02h
	int 21h
	;printing the “carriage return” character
	;mov dl,13
	;mov ah,02h
	;int 21h

	;printing a string
	lea dx,a
	mov ah,09h
	int 21h

	mov ah,4ch
	mov al,00h
	int 21h

code ends
end start
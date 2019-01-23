assume cs:code,ds:data
data segment
	msg db 'da un numar: $'
	numar db 12,?,12 dup(?)
	putere db 1
	zece db 10
data ends
code segment
start:
	mov ax, data
	mov ds,ax
	
	mov ah,09h
	mov dx,offset msg
	int 21h
	
	mov ah,0Ah
	mov dx,offset numar
	int 21h
	
	mov si,offset numar+2
	cld
	mov dx,0
	repeta:
		lodsb
		cmp ah,'0'
		jl final
		cmp ah,'9'
		jg final
		continua:
			mul putere
			add dx,ax
			mov al,putere
			mul zece
			mov putere,ax
			loop repeta
			
	final:
		mov ax,4c00h
		int 21
code ends
end start
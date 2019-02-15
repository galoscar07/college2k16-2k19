assume cs:code,ds:data
data segment
	s1 db 1,2,3,4
	len_s1 equ ($-s1)
	s2 db 5,6,7,8
	len_s2 equ($-s2)
	d db len_s1 dup(?)
data ends
code segment
start:
	mov ax,data
	mov ds, ax
	mov es, ax
	
	lea si,s1
	lea di,d
	mov cx,len_s1
	repeta:
		lodsb
		stosb
		loop repeta
	
	lea si,s2
	mov cx,len_s2
	lea di,d
	repet:
		lodsb		
		test DI, 1
		jz evn
		odd:
			sub d[DI], AL
			inc DI
			loop repet
			jmp terminate
		evn:
			add d[DI], AL
			inc DI
			loop repet
	terminate:		
		mov ax,4c00h
		int 21h
		
code ends
end start
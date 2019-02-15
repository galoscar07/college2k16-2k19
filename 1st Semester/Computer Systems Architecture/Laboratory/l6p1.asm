;1. Two byte strings S1 and S2 are given. Obtain the string D by concatenating the elements of 
;S1 from the left hand side to the right hand side and the elements of S2 from the right hand side 
;to the left hand side.
;Exemple:
;S1: 1, 2, 3, 4
;S2: 5, 6, 7
;D: 1, 2, 3, 4, 7, 6, 5
assume cs:code, ds:data
data segment
	s1 db 1,2,3,4
	len_s1 equ $-s1
	s2 db 5,6,7
	len_s2 equ $-s2
	d db len_s1+len_s2 dup(?)
data ends
code segment
start:
	mov ax,data
	mov ds,ax
	mov es, ax

	cld
	lea si,s1
	lea di,d
	mov cx,len_s1
	repeta:
		lodsb
		stosb
		loop repeta
	std
	lea si,s2
	mov cx,len_s2
	repet:
		lodsb
		cld
		stosb
		std
		loop repet
	
	mov ax,4c00h
	int 21h
code ends
end start
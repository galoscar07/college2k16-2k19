;Being given a string of words, compute the longest substring of ordered words (in increasing 
;order) from this string.
assume cs:code,ds:data
data segment
	sir dw 1,2,1,2,3,4,1,7,2,3
	len equ ($-sir)/2
	sir_fin dw dup(?)
	max db 0
	cr db 0
	in db 0
	fi db 0
data ends
code segment
start:
	mov ax,data
	mov ds,ax
	mov es,ax

	lea si, sir
	mov cx, len
	repata:
	lodsw
	jmp detsir
	
	
	detsir:
		
		
		
	
	mov ax,4c00h
	int 21h
code ends
end start
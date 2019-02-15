;4. A byte string S of length l is given. Obtain the string D of length l-1 so that the elements of 
;represent the difference between every two consecutive elements of S.
;Exemple:
;S: 1, 2, 4, 6, 10, 20, 25
;D: 1, 2, 2, 4, 10, 5
assume cs:code,ds:data
data segment
	s db 1,2,4,6,10,20,25
	len_s equ $-s
	d db len_s-1 dup(?)
data ends
code segment
start:
	mov ax,data
	mov ds,ax
	mov es,ax
	
	lea si,s
	lea di,d
	mov cx, len_s-1
	lodsb
	repeta:
		mov bl,al
		lodsb
		mov dl,al
		sub al,bl
		stosb
		mov al,dl
	loop repeta
	
	
	mov ax,4c00h
	int 21h
code ends
end start

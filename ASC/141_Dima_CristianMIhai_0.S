.data
	a: .space 1600     #matrice
	m: .space 4        #nr linii
	n: .space 4        #nr coloane
	p: .space 4        #nr perechi 
	i: .space 4
	j: .space 4
	k: .space 4         #nr de stari prin care trece matricea
	m2: .space 4
	n2: .space 4
	nr_celula: .space 4
	contor: .space 4
	nr_vecini_vii: .space 4
	formatScanf: .asciz "%d"
	formatPrintf: .asciz "%d "
	linie_noua: .asciz "\n"
	
	verificare1: .asciz "a intrat la vecini a %d oara\n"
	verificare2: .asciz "a iesit din sus/jos\n"
	cati_vecini: .asciz "celula %d %d are %d vecini\n"
	afisare_i_j: .asciz "i este %d  j este %d\n"
	va_murii: .asciz "celula %d %d va muri\n"
	va_inviaa: .asciz "celula %d %d va invia\n"
.text
.global main
main:
	#citire m
	pushl $m
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	
	#citire n
	pushl $n
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	#citire p
	pushl $p
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx

movl $0, contor	

movl m, %eax
movl %eax, m2
movl n, %eax
movl %eax, n2
incl m2
incl n2		#m2=m+1   n2=n+1    m=m+2   n=n+2

addl $2, m		
addl $2, n				
		

et_for:
	movl contor, %ecx
	cmp %ecx, p
	je citeste_k           
	
	#citesc coordonatele celulei (i, j)
	pushl $i
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	pushl $j
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	incl i
	movl i, %eax
	movl $0, %edx
	mull n			#eax=(i+1)*(n+2)
	
	incl j
	addl j, %eax		#eax=(i+1)*(n+2)+(j+1)
	
	lea a, %edi
	movl $1, (%edi, %eax, 4)
	
	incl contor
	jmp et_for
	
citeste_k:
	pushl $k
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	
#afisare matrice	
#for(i=1; i<m+1; i++
#{
#   for(j=1; j<n+1; j++)
#       cout<<a[i][j]<<' ';
#   cout<<endl;
#}	

/*
afisare_matrice:
	movl $1, i
	for_linii:
		movl i, %ecx
		
		cmp m2, %ecx
		
		je for_transformari
		
		movl $1, j
		for_coloane:
			movl j, %ecx
			
			cmp n2, %ecx
			
			je continuare_for_linii
			
			movl i, %eax
			movl $0, %edx
			mull n			#eax=(i+1)*(n+2)
			addl j, %eax		#eax=(i+1)*(n+2)+(j+1)
			
			lea a, %edi
			movl (%edi, %eax, 4), %ebx
	
			pushl %ebx
			pushl $formatPrintf
			call printf
			popl %ebx
			popl %ebx
			
			pushl $0
			call fflush
			popl %ebx
	
			incl j
			jmp for_coloane
	continuare_for_linii:
		movl $4, %eax
		movl $1, %ebx
		movl $linie_noua, %ecx
		movl $2, %edx
		int $0x80
		
		incl i
		jmp for_linii
*/
movl $0, nr_celula

for_transformari:
	movl $0, contor
	
	for_contor:
		movl contor, %ecx
		cmp %ecx, k
		je et_afisare
		
		movl $1, i
		
		for_liniute:
			movl i, %ecx
			cmp %ecx, m2
			je omorare_sau_inviere_efectiva
			
			movl $1, j
				
			for_columns:
				
				movl j, %ecx
				cmp %ecx, n2
				je continuare_for_liniute
				
				movl $0, nr_vecini_vii
				
				vecin_stg_sus:
				decl i
				decl j
				movl i, %eax
				movl $0, %edx
				mull n
				addl j, %eax
				mov (%edi, %eax, 4), %ebx
				cmp $1, %ebx
				jne comp_stg_sus_minus1
				jmp stg_sus_viu
				comp_stg_sus_minus1:
				cmp $-1, %ebx
				jne vecin_deasupra
				
				stg_sus_viu:
				incl nr_vecini_vii
				
				vecin_deasupra:
				incl %eax
				mov (%edi, %eax, 4), %ebx
				cmp $1, %ebx
				jne comp_deasupra_minus1
				jmp deasupra_viu
				comp_deasupra_minus1:
				cmp $-1, %ebx
				jne vecin_dr_sus
				
				deasupra_viu:
				incl nr_vecini_vii
				
				vecin_dr_sus:
				incl %eax
				mov (%edi, %eax, 4), %ebx
				cmp $1, %ebx
				jne comp_dr_sus_minus1
				jmp dr_sus_viu
				comp_dr_sus_minus1:
				cmp $-1, %ebx
				jne vecin_stg
				dr_sus_viu:
				incl nr_vecini_vii
				
				vecin_stg:
				incl i
				movl i, %eax
				movl $0, %edx
				mull n
				addl j, %eax
				mov (%edi, %eax, 4), %ebx
				cmp $1, %ebx
				jne comp_stg_minus1
				jmp stg_viu
				comp_stg_minus1:
				cmp $-1, %ebx
				jne vecin_dr
				stg_viu:
				incl nr_vecini_vii
				
				vecin_dr:
				addl $2, %eax
				mov (%edi, %eax, 4), %ebx
				cmp $1, %ebx
				jne comp_dr_minus1
				jmp dr_viu
				comp_dr_minus1:
				cmp $-1, %ebx
				jne vecin_stg_jos
				dr_viu:
				incl nr_vecini_vii
				
				vecin_stg_jos:	
				incl i
				movl i, %eax
				movl $0, %edx
				mull n
				addl j, %eax
				mov (%edi, %eax, 4), %ebx
				cmp $1, %ebx
				jne comp_stg_jos_minus1
				jmp stg_jos_viu
				comp_stg_jos_minus1:
				cmp $-1, %ebx
				jne vecin_jos
				stg_jos_viu:
				incl nr_vecini_vii
				
				vecin_jos:
				incl %eax
				mov (%edi, %eax, 4), %ebx
				cmp $1, %ebx
				jne comp_jos_minus1
				jmp jos_viu
				comp_jos_minus1:
				cmp $-1, %ebx
				jne vecin_dr_jos
				jos_viu:
				incl nr_vecini_vii
				
				vecin_dr_jos:
				incl %eax
				mov (%edi, %eax, 4), %ebx
				cmp $1, %ebx
				jne comp_dr_jos_minus1
				jmp dr_jos_viu
				comp_dr_jos_minus1:
				cmp $-1, %ebx
				
				jne creare_generatia_urmatoare
				dr_jos_viu:
				incl nr_vecini_vii
						
				creare_generatia_urmatoare:
				
					#j intra aici ca j-1 => e necesar un:	
					incl j
					#i intra aici ca i+1 => e necesar un:
					decl i
					
					movl i, %eax
					movl $0, %edx
					mull n
					addl j, %eax
					
					lea a, %edi
					movl (%edi, %eax, 4), %ebx
					
					movl nr_vecini_vii, %ecx
					
					cmp $1, %ebx
					jne Este0
					
					Este1:
						cmp $2, %ecx
						jl va_muri
						je continuare_for_columns
						
					
					o_fi_mai_mare_decat3: 
						cmp $3, %ecx
						jg va_muri
						jmp continuare_for_columns
						
					va_muri:
						lea a, %edi
						movl $-1, (%edi, %eax, 4)
						
						jmp continuare_for_columns
						
					Este0:							
						cmp $3, %ecx
						jne continuare_for_columns
					va_invia:
						lea a, %edi
						movl $2, (%edi, %eax, 4)
						
						jmp continuare_for_columns
					
			continuare_for_columns:
				incl j
				jmp for_columns
			
		continuare_for_liniute:
			incl i
			jmp for_liniute
			
		omorare_sau_inviere_efectiva:
		movl $1, i
		for_linie_in_matrice:
			movl i, %ecx
			cmp m2, %ecx
			je continuare_for_contor
			
			movl $1, j
			for_coloana_in_matrice:
				movl j, %ecx
				cmp n2, %ecx
				je continuare_for_linie_in_matrice
				
				movl i, %eax
				movl $0, %edx
				mull n
				addl j, %eax
				movl (%edi, %eax, 4), %ebx
				
				cmp $-1, %ebx
				je il_omor
				cmp $2, %ebx
				jne continuare_for_coloana_in_matrice
				il_aduc_la_viata:
					movl $1, (%edi, %eax, 4)
					jmp continuare_for_coloana_in_matrice
				il_omor:
					movl $0, (%edi, %eax, 4)
			continuare_for_coloana_in_matrice:
				incl j
				jmp for_coloana_in_matrice                               
				
		continuare_for_linie_in_matrice:
			incl i
			jmp for_linie_in_matrice
			
	continuare_for_contor:
		incl contor
		jmp for_contor

et_afisare:
	movl $1, i
	for_line:
		movl i, %ecx
		cmp %ecx, m2
		je et_exit
		
		movl $1, j
		for_col:
			movl j, %ecx
			cmp %ecx, n2
			je continuare_for_line
			
			movl i, %eax
			movl $0, %edx
			mull n   		
			addl j, %eax		
			
			
			movl (%edi, %eax, 4), %ebx
	
			pushl %ebx
			pushl $formatPrintf
			call printf
			popl %ebx
			popl %ebx
			
			pushl $0
			call fflush
			popl %ebx
	
			incl j
			jmp for_col
	continuare_for_line:
		movl $4, %eax
		movl $1, %ebx
		movl $linie_noua, %ecx
		movl $2, %edx
		int $0x80
		
		incl i
		jmp for_line

et_exit:

pushl $0
call fflush
addl $4, %esp
	mov $1, %eax
	mov $0, %ebx
	int $0x80

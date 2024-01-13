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
	de_afisat: .space 4
	contor: .space 4
	i_mes_fin_decript: .space 4
	lung_mesaj: .space 4
	litera: .space 1
	mesajul_pe_biti: .space 500
	mesajul_in_hexa: .space 500
	
	cript_sau_decript: .space 4
	mesaj: .space 30
	lungime_mesaj: .space 4
	
	nr_celula: .space 4
	
	nr_vecini_vii: .space 4
	formatScanf: .asciz "%d"
	
	afisare8b_hexa: .asciz "%0X"
	scanMesaj: .asciz "%s"
	printMesaj: .asciz "%s"
	formatPrintf: .asciz "%d "
	formatPrintfnospace: .asciz "%d"
	linie_noua: .asciz "\n"
	
	inceput_hexa: .asciz "0x"
	printLitera: .asciz "%c"
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
	
citeste_cript_sau_decript:
	pushl $cript_sau_decript
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
citeste_mesaj:

	push $mesaj
	push $scanMesaj
	call scanf
	pop %ebx
	pop %ebx
/*
afiseaza_mesaj:
	push $mesaj
	push $printMesaj
	call printf
	pop %ebx
	pop %ebx
	
	pushl $0
	call fflush
	popl %ebx
*/
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
	/*
	movl $1, i
	for_line:
		movl i, %ecx
		cmp %ecx, m2
		je et_distractie_mare
		
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
	*/
et_distractie_mare:
	lea mesaj, %esi
	movl $0, lung_mesaj
	mov $0, %ecx
	mov $0, %ebx
	lungimea_mesajului:
		mov (%esi, %ecx, 1), %bl
		cmp $0, %bl
		je se_stie_lung_mesaj
		incl %ecx
		jmp lungimea_mesajului
	
	se_stie_lung_mesaj:
		movl %ecx, lung_mesaj

cmpl $0, cript_sau_decript
jne decriptare
criptare:

	movl $0, %eax
	lea mesajul_pe_biti, %edi
	
	movl $0, i
	for_lung_mesaj:
		movl i, %ecx
		cmp %ecx, lung_mesaj
		je altceva
		movl $0, %ebx
		mov (%esi, %ecx, 1), %bl #in bl am acum litera curenta
		movl $7, j
		for_biti_in_litera:
		
			movl j, %ecx
			cmp $0, %ecx
			jl continuare_for_lung_mesaj
			
			mov %bl, %dl
			shr %ecx, %edx
			and $1, %edx
			
			cmp $1, %edx
			je pune_1_in_vector
			movl $0, (%edi, %eax, 4)
			jmp incr_eax
			pune_1_in_vector:
			   movl $1, (%edi, %eax, 4)
			incr_eax:
			   incl %eax
			decl j
		jmp for_biti_in_litera
	continuare_for_lung_mesaj:
		incl i
		jmp for_lung_mesaj
	
	altceva:
	
	movl %eax, lung_mesaj
	/*
	movl $0, i
	afisare_mesaj_pe_biti:
		movl i, %ecx
		cmp %ecx, lung_mesaj
		je mergem_mai_departe
		
		movl (%edi, %ecx, 4), %ebx
		
		pushl %ebx
		pushl $formatPrintfnospace
		call printf
		pop %ebx
		pop %ebx
		
		push $0
		call fflush
		pop %ebx
		
		incl i
		jmp afisare_mesaj_pe_biti
	*/
	mergem_mai_departe:
	
	lea a, %edi
	lea mesajul_pe_biti, %esi
	
	comparare_lungime_mesaj_pe_biti_cu_lungime_cheie:
	
	#matricea mea are dimensiunea m x n
	movl m, %eax
	movl $0, %edx
	mull n
	
	# in eax am lungimea cheii
	
	cmp lung_mesaj, %eax
	jg dimensiunile_sunt_ok
	
	#daca lungimea cheii<lungime mesaj pe biti => problemuta
	
	movl $0, i
	movl %eax, j
	
	for_alungire_cheie:
		movl j, %edx
		cmp %edx, lung_mesaj
		je dimensiunile_sunt_ok
		
		cmp i, %eax
		jne i_nu_devine_iar_0
		movl $0, i
		i_nu_devine_iar_0:
		movl i, %ecx
		movl (%edi, %ecx, 4), %ebx
		movl %ebx, (%edi, %edx, 4)
		
		incl i
		incl j
		jmp for_alungire_cheie
	
	dimensiunile_sunt_ok:
	
	movl $0, i
	for_xorare:
		movl i, %ecx
		cmp lung_mesaj, %ecx
		je print_mesaj_criptat
		
		movl (%edi, %ecx, 4), %ebx
		movl (%esi, %ecx, 4), %edx
		xorl %ebx, %edx
		movl %edx, (%esi, %ecx, 4)
		incl i
	jmp for_xorare
	
	
	print_mesaj_criptat:
		/*
		print_endl:
			push $linie_noua
			call printf
			pop %ebx
			push $0
			call fflush
			pop %ebx
		
		movl $0, i
		for_print_mesaj_criptat:
			movl i, %ecx
			cmp %ecx, lung_mesaj
			je gata_xorarea
			
			movl (%esi, %ecx, 4), %ebx
			push %ebx
			push $formatPrintfnospace
			call printf
			pop %ebx
			pop %ebx
			
			pushl $0
			call fflush
			pop %ebx
			
			incl i
			jmp for_print_mesaj_criptat
		*/
	gata_xorarea:
	
	trecem_la_hexa:
	lea mesajul_in_hexa, %edi
	
	afisez_inceput_de_hexa:
	push $inceput_hexa
	call printf
	pop %ebx
	
	pushl $0
	call fflush
	pop %ebx
	
	
	movl $0, i
	
	for_hexare:
		movl i, %eax	#eax=contor sir biti  	ebx=reg de afisare hexa cate 8b
		cmp lung_mesaj, %eax
		je finalul
		
		movl $0, %edx
		movl $8, %ecx
		divl %ecx
		cmp $0, %edx	#daca i(contor sir biti)e multiplu de 8 si diferit de 0, trebuie sa afisez ce aveam in ebx+resetez
		jne nu_e_multiplu_de_8
		cmp $0, %eax
		je nu_e_multiplu_de_8
		
		#ma asigur ca se afiseaza ce trebuie si daca primii 4b sunt de 0
		movl $15, %edx
		shl $4, %edx
		and %ebx, %edx
		shr $4, %edx
		cmp $0, %edx
		jne nu_ie_problema
		push %ebx
		push %edx
		push $afisare8b_hexa
		call printf
		pop %ebx
		pop %ebx
		
		
		pushl $0
		call fflush
		pop %ebx
		pop %ebx
		
		nu_ie_problema:
		push %ebx
		push $afisare8b_hexa
		call printf
		pop %ebx
		pop %ebx
		
		pushl $0
		call fflush
		pop %ebx
		
		movl $0, %ebx
		nu_e_multiplu_de_8:
		movl i, %eax
		movl (%esi, %eax, 4), %ecx
		shl $1, %ebx
		cmp $0, %ecx
		je pun_zero
		
		pun_unu:
		or $1, %ebx
		
		pun_zero:
		#nu trebuie sa fac nimic/am shiftat la staga si e suficient
		
		incl i
		jmp for_hexare
		
	finalul:
		#afisez ultimii 8b:
		
		#ma asigur ca se afiseaza ce trebuie si daca primii 4b sunt de 0
		movl $15, %edx
		shl $4, %edx
		and %ebx, %edx
		shr $4, %edx
		cmp $0, %edx
		jne nu_ieste_problema
		push %ebx
		push %edx
		push $afisare8b_hexa
		call printf
		pop %ebx
		pop %ebx
		
		
		pushl $0
		call fflush
		pop %ebx
		pop %ebx
		
		nu_ieste_problema:
		push %ebx
		push $afisare8b_hexa
		call printf
		pop %ebx
		pop %ebx
		
		pushl $0
		call fflush
		pop %ebx
		jmp et_exit
	
decriptare:
	#in esi e mesaj
	lea a, %edi
	movl $2, i 			#primele 2 car din mesaj sunt 0x
	movl m, %eax
	movl $0, %edx
	movl n, %ecx
	mull %ecx
	movl %eax, p 			 #in p e acum lungimea matricei
	
	movl $0, j
	movl $0, %ebx
	movl $0, contor		#imi numara cate 8b din vector(matrice)
	movl $0, i_mes_fin_decript
	for_xorare_si_afisare:
		movl i, %ecx		#i=contor litere din mesaj
		cmp lung_mesaj, %ecx
		je finale
		
		
		for_mutare_8b:
			movl j, %eax
			
			cmp p, %eax
			jne am_umplut_ebx_ma_intreb
			je j_trebuie_resetat_la0
			
			
			j_trebuie_resetat_la0:
			movl $0, j
			jmp am_umplut_ebx_ma_intreb
			
			am_umplut_ebx_ma_intreb:
			#am atins 8 biti in ebx si trebuie sa merg la xorare? (contorul e 8?)
			
			movl contor, %ecx
			cmp $8, %ecx
			je predau_ebx
			jne continui_sa_adaug_biti
			
			predau_ebx:
			movl $0, contor
			jmp continuare_xorare_afisare
			
			continui_sa_adaug_biti:
			shl $1, %ebx
			movl j, %ecx
			movl (%edi, %ecx, 4), %eax
			cmp $0, %eax
			je adaug_0
			or $1, %ebx
			adaug_0:
			
			incl j
			incl contor
			
		jmp for_mutare_8b
				
			continuare_xorare_afisare:
			movl i, %ecx
			movb (%esi, %ecx, 1), %al
			
			#cercetez daca e cifra (ascii intre 48 si 57)
			cmp $48, %eax
			jge lim_sup
			jl cercetare_litera
			
			lim_sup:
			cmp $57, %eax
			jle e_cifra
			jg cercetare_litera
			
			e_cifra:
			subl $48, %eax
			#in eax am acum cifra in binar
			movl %eax, %ecx #o transfer in ecx, ca cu eax mai am treaba pt urm 4b
			jmp urmatorii_4b
			
			cercetare_litera:
			#daca nu e cifra, altceva in afara de litera nu poate fi=> sigur e litera
			subl $65, %eax
			#acum in eax am a cata litera era eax (valori intre 0=A.....5=F)
			addl $10, %eax #=> ca sa ma duc in valori 10.....15
			movl %eax, %ecx #o transfer in ecx, ca cu eax mai am treaba pt urm 4b
			jmp urmatorii_4b
			
			urmatorii_4b:
			incl i
			movl i, %edx
			movb (%esi, %edx, 1), %al
			
			#cercetez daca e cifra (ascii intre 48 si 57)
			cmp $48, %eax
			jge lim_supe
			jl cercetare_literaa #desi fie vorba intre noi, mai putin de 48 n-are cum a fie, lasa asa
			
			lim_supe:
			cmp $57, %eax
			jle e_cifraa
			jg cercetare_literaa
			
			e_cifraa:
			subl $48, %eax
			#in eax am acum cifra in binar
			
			jmp wir_gehen_weiter
			
			cercetare_literaa:
			#daca nu e cifra, altceva in afara de litera nu poate fi=> sigur e litera
			subl $65, %eax
			#acum in eax am a cata litera era eax (valori intre 0=A.....5=F)
			addl $10, %eax #=> ca sa ma duc in valori 10.....15
			
			jmp wir_gehen_weiter
			
			wir_gehen_weiter:
			
			shl $4, %ecx
			or %eax, %ecx
			
			xor %ecx, %ebx
			movl i_mes_fin_decript, %edx
			movb %bl, (%esi, %edx, 1)
			
			movl $0, %ebx
		incl i
		incl i_mes_fin_decript
		jmp for_xorare_si_afisare
	finale:
	
	
		movl i_mes_fin_decript, %ecx
		movl $0, (%esi, %ecx, 1)
		
		push $mesaj
		push $printMesaj
		call printf
		pop %ebx
		pop %ebx
		
		pushl $0
		call fflush
		pop %ebx
			
		push $linie_noua
		call printf
		pop %ebx
			
		pushl $0
		call fflush
		pop %ebx								
		
	


et_exit:

pushl $0
call fflush
addl $4, %esp
	mov $1, %eax
	mov $0, %ebx
	int $0x80

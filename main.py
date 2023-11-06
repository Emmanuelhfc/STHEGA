from CascoTubo import*

cp_quente, cp_frio, T1, T2, t1, t2, wq, wf, num_casco, rho_q, rho_f, mi_f, mi_q, k_q, k_f, tipo_q, tipo_f, Rd_f, Rd_q = []
trocador = CascoTubo(cp_quente, cp_frio, T1, T2, t1, t2, wq, wf, num_casco, rho_q, rho_f, mi_f, mi_q, k_q, k_f, tipo_q, tipo_f, Rd_f, Rd_q)

n, Ds, de_pol, a_tubos, passo_pol = []
trocador.filtro_tubos(n, Ds, de_pol, a_tubos, passo_pol)

L=0
trocador.area_projeto(L)

trocador.coef_global_min()

espe =0
trocador.diametro_interno_tubo(espe)

trocador.conveccao_tubo(True)

trocador.diametro_casco(0)

trocador.caract_chicana(1)

ls, lc, classe = []
trocador.conveccao_casco(ls, lc, classe)

trocador.calculo_temp_parede()
# trocador.correcao_temp_parede()

trocador.coef_global_limpo()
trocador.excesso_area()

trocador.perda_carga_tubo()
trocador.perda_carga_casco()
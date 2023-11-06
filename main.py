from CascoTubo import*

dados_entrada_nomes = ["cp_quente", "cp_frio", "T1", "T2", "t1", "t2", "wq", "wf", "num_casco", "rho_q", "rho_f", "mi_q", "mi_f", "k_q", "k_f", "tipo_q", "tipo_f", "Rd_q", "Rd_f"]
dados_entrada = []
trocador =CascoTubo(*dados_entrada)

n = [1, 2, 4, 6, 8]

individuo_cromossomo = ["n", "Ds", "de_pol", "a_tubos", "passo_pol", "L", "espess_tubo", "espess_casco", "classe", "ls", r"%lc", "grupo_material"]
n = 2
Ds = 8.071 * 0.0254
de_pol = 0.75
a_tubos = "quadrado"
L = 1
passo_pol = 1

trocador.filtro_tubos(n, Ds, de_pol, a_tubos, passo_pol)
trocador.area_projeto(L)

trocador.coef_global_min()

espe = 0.065 * pol2m
trocador.diametro_interno_tubo(espe)
trocador.conveccao_tubo(False)

trocador.diametro_casco(2 * pol2m)

print(trocador.caract_chicana(1))

# ls, lc, classe = []
ls = 0.2 
lc = trocador.Ds*0.25
classe = 150
trocador.conveccao_casco(ls, lc, classe)

trocador.calculo_temp_parede()
# trocador.correcao_temp_parede()

trocador.coef_global_limpo()
trocador.excesso_area()

trocador.perda_carga_tubo()
trocador.perda_carga_casco()
from CascoTubo import*

trocador1 = CascoTubo()

trocador1.add_dados_iniciais(
                            propriedades = {
                                'temp_ent_fluido_quente': 90.5,
                                'temp_sai_fluido_quente': 40.8,
                                'temp_sai_fluido_frio': 50,
                                'temp_ent_fluido_frio': 20,
                                'vazao_fluido_frio': 10,
                                'tipo_fluido_quente': "water",
                                'tipo_fluido_frio': "oil",
                            })


print(trocador1.sai_Tf)
print(trocador1.sai_Tq)

trocador1.balaco_de_energia()
print(trocador1.q, type(trocador1.q))
print(trocador1.v_quente, type(trocador1.v_quente))
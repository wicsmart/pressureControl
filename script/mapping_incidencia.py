mapping = {
   "mappings": {
        "dynamic": "false",
        "properties": {
          "location":{
              "type": "geo_point"
          },
          "al": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_area_risco": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_ba_dt": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_clientes_afetados_atual": {
            "type": "long"
          },
          "calculo_clientes_afetados_maximo": {
            "type": "long"
          },
          "calculo_clientes_normalizados_menos_3minutos": {
            "type": "long"
          },
          "calculo_conh_atual": {
            "type": "float"
          },
          "calculo_conh_maximo": {
            "type": "float"
          },
          "calculo_conh_total": {
            "type": "float"
          },
          "calculo_data_criacao_sistema": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_data_hora_final_ultima_etapa": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_data_hora_inicio_ultima_etapa": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_data_inicio_alarme_mr": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_data_inicio_incidencia": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_data_recomposicao_parcial": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_data_recomposicao_total": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_dec": {
            "type": "float"
          },
          "calculo_dispositivo_monitor_ramal": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_dispositivo_reincidente72": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_equipes_disponiveis": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_erro_cadastro": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_eta_deslocamento_incidencia": {
            "type": "float"
          },
          "calculo_improdutivo": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_km_percorrido_deslocamento_incidencia": {
            "type": "float"
          },
          "calculo_km_previsto_deslocamento_incidencia": {
            "type": "float"
          },
          "calculo_kva_atual": {
            "type": "float"
          },
          "calculo_kva_maximo": {
            "type": "float"
          },
          "calculo_lat_equipe_fim_reparacao": {
            "type": "float"
          },
          "calculo_lat_equipe_inicio_deslocamento": {
            "type": "float"
          },
          "calculo_lon_equipe_fim_reparacao": {
            "type": "float"
          },
          "calculo_lon_equipe_inicio_deslocamento": {
            "type": "float"
          },
          "calculo_lt_se": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_max_elemento_fatura": {
            "type": "float"
          },
          "calculo_nivel_conh": {
            "type": "long"
          },
          "calculo_nivel_risco_compensacao": {
            "type": "long"
          },
          "calculo_nome_elemento_primeira_etapa": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_nome_elemento_segunda_etapa": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_nome_elemento_ultima_etapa": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_numero_avisos_clientes_diferentes": {
            "type": "long"
          },
          "calculo_numero_elementos_afetacao": {
            "type": "long"
          },
          "calculo_odometro_equipe_inicio_deslocamento": {
            "type": "float"
          },
          "calculo_operador": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_ordem2": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_osm": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_pmc": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_status_callback": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_status_execucao": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_status_monitor_ramal": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_tempo_atraso_fechamento_equipe": {
            "type": "float"
          },
          "calculo_tempo_espera": {
            "type": "float"
          },
          "calculo_tempo_intermediario": {
            "type": "float"
          },
          "calculo_tempo_primeira_manobra": {
            "type": "float"
          },
          "calculo_tictac": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_tipo_dispositivo_monitor_ramal": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_tipo_elemento_primeira_etapa": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_tipo_elemento_segunda_etapa": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_tipo_elemento_ultima_etapa": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_tipo_trabalho": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "calculo_tma": {
            "type": "float"
          },
          "calculo_tmat": {
            "type": "float"
          },
          "calculo_tmd": {
            "type": "float"
          },
          "calculo_tme": {
            "type": "float"
          },
          "calculo_tmp": {
            "type": "float"
          },
          "calculo_total_elemento_fatura": {
            "type": "float"
          },
          "calculo_tronco_ramal": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "causa": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "clientes_afetados_3min_max": {
            "type": "long"
          },
          "clientes_avisos": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "conh_afetacao_minima": {
            "type": "float"
          },
          "conjunto": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "data_criacao_sistema": {
            "type": "date"
          },
          "data_edicao_sistema": {
            "type": "date"
          },
          "data_fechamento": {
            "type": "date"
          },
          "data_fim": {
            "type": "date"
          },
          "data_inicio": {
            "type": "date"
          },
          "data_localizacao": {
            "type": "date"
          },
          "data_ultimo_recebimento_sistema": {
            "type": "date"
          },
          "departamento": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "dia_critico": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "distribuidora": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "equipe_deslocamento": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "equipe_sugerida": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "equipes_validas": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "estado": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "expurgo": {
            "type": "boolean"
          },
          "gerencia": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "latitude": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "lista_inconsistencias": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "lista_prioridade_Desc": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "longitude": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "maior_prioridade_avisos": {
            "type": "long"
          },
          "municipio": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "n_avisos_rural": {
            "type": "long"
          },
          "n_avisos_urbano": {
            "type": "long"
          },
          "nivel_tensao": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "nivel_tensao_calculada": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "nome_cd": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "nome_er": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "numero_avisos": {
            "type": "long"
          },
          "numero_incidencia": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "observacao": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "operador": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "polo": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "prioridadeDesc": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "regiao": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "reincidentes_180_dias": {
            "type": "long"
          },
          "reincidentes_30_dias": {
            "type": "long"
          },
          "reincidentes_360_dias": {
            "type": "long"
          },
          "reincidentes_7_dias": {
            "type": "long"
          },
          "se": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "sucursal": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "tipo": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "tipo_cd": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "tipo_er": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "valor_dic": {
            "type": "float"
          },
          "valor_dmic": {
            "type": "float"
          },
          "valor_fic": {
            "type": "float"
          }
        }
      }
    
  }
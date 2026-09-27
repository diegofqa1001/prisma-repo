"""Figura 3.4 de la tesis: diagrama de flujo PRISMA 2020 de la revisión que
sustenta la taxonomía (identificación, cribado, elegibilidad pendiente y
síntesis temática a nivel de resumen).

Los conteos se calculan desde PRISMA_master_final.csv y
08-sintesis/tabla_dimensiones_candidatas.csv; los que no están en esos
archivos (duplicados, DOI verificados, Kappa, adjudicaciones) se toman de
03-deduplicacion/, 04-resolucion-doi/, 07-cribado/validacion.md y
08-sintesis/metodologia.md. Paleta Okabe-Ito, fondo blanco, sin título
interno (el título va en la leyenda de la tesis).

Uso: python3 08-sintesis/fig_3_4_prisma_flujo.py
"""
import csv
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

H = Path(__file__).resolve().parent
ROOT = H.parent

# ---- conteos desde los archivos del repositorio ----
with open(ROOT / 'PRISMA_master_final.csv', encoding='utf-8-sig') as fh:
    rows = list(csv.DictReader(fh))
n_unicos = len(rows)
par = Counter((r['cribado_decision_ia'], r['cribado_decision_final']) for r in rows)
n_excl_criterio = par[('EXCLUDE', 'EXCLUDE')]
n_inciertos = par[('UNCERTAIN', 'EXCLUDE')]
n_incl_a_excl = par[('INCLUDE', 'EXCLUDE')]
n_incluidos = sum(1 for r in rows if r['cribado_decision_final'] == 'INCLUDE')
n_excluidos = n_unicos - n_incluidos
assert n_excl_criterio + n_inciertos + n_incl_a_excl == n_excluidos
n_origen = Counter(r['origin'] for r in rows)

with open(H / 'tabla_dimensiones_candidatas.csv', encoding='utf-8') as fh:
    dims = {r['codigo']: int(r['n_resumenes']) for r in csv.DictReader(fh)}

N_SCOPUS, N_WOS, N_DUP = 438, 289, 167          # 01-protocolo-busqueda, 03-deduplicacion
N_DOI = 502                                     # 04-resolucion-doi
KAPPA_VAL, N_DESACUERDOS = '0,799', 10          # 07-cribado/validacion.md
N_MUESTRA_VAL = 102                             # 07-cribado/validacion.md (20 % de los 512 decididos)
KAPPA_RANGO, N_ADJ = '0,76–0,96', 149           # 08-sintesis/metodologia.md
assert N_SCOPUS + N_WOS - N_DUP == n_unicos
# decisiones automáticas sin revisión humana: las 512 que la primera pasada
# decidió (INCLUDE/EXCLUDE) menos los 10 desacuerdos resueltos por el autor
N_PROVISIONALES = n_unicos - n_inciertos - N_DESACUERDOS
N_CONFIRMADAS = N_MUESTRA_VAL - N_DESACUERDOS

OI = {'azul': '#0072B2', 'naranja': '#E69F00', 'verde': '#009E73',
      'bermellon': '#D55E00', 'purpura': '#CC79A7', 'tinta': '#1a1a1a'}


def fmt(x):
    return f'{x:,}'.replace(',', '.')


def caja(ax, x, y, w, h, texto, color, fs=10.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.12',
                                facecolor='white', edgecolor=color, linewidth=2.2))
    ax.text(x + w / 2, y + h / 2, texto, ha='center', va='center', fontsize=fs,
            color=OI['tinta'], linespacing=1.35)


def banda(ax, y, h, texto, color):
    ax.add_patch(FancyBboxPatch((0.15, y), 0.55, h, boxstyle='round,pad=0.0,rounding_size=0.05',
                                facecolor=color, edgecolor=color))
    ax.text(0.425, y + h / 2, texto, rotation=90, ha='center', va='center', fontsize=11,
            color='white', fontweight='bold')


def flecha(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='-|>', color='#333333', lw=1.8, mutation_scale=16))


fig, ax = plt.subplots(figsize=(10.8, 11.4), dpi=300)
fig.patch.set_facecolor('white')
ax.set_xlim(0, 10.8)
ax.set_ylim(0, 11.4)
ax.axis('off')

XL, XR, W = 1.0, 5.75, 4.3

# Identificación
banda(ax, 9.45, 1.75, 'Identificación', OI['azul'])
caja(ax, XL, 9.65, W, 1.3, f'Registros identificados\nScopus: n = {N_SCOPUS}\n'
     f'Web of Science: n = {N_WOS}\nTotal: n = {N_SCOPUS + N_WOS}', OI['azul'])
caja(ax, XR, 9.65, W, 1.3, 'Duplicados eliminados\n(cruce Scopus × WoS, título\n'
     f'normalizado + similitud ≥ 0,90)\nn = {N_DUP}', OI['bermellon'])
flecha(ax, XL + W, 10.3, XR, 10.3)
flecha(ax, XL + W / 2, 9.65, XL + W / 2, 9.05)

# Cribado
banda(ax, 5.2, 3.95, 'Cribado', OI['naranja'])
caja(ax, XL, 7.85, W, 1.2, f'Registros únicos cribados\n(título y resumen)\nn = {n_unicos}\n'
     f'DOI verificado: {N_DOI} ({100 * N_DOI / n_unicos:.1f} %)'.replace('.', ','), OI['naranja'])
caja(ax, XR, 7.75, W, 1.4, f'Registros excluidos\nn = {n_excluidos}\n'
     f'({n_excl_criterio} por criterios E1–E7, {n_inciertos} inciertos\n'
     f'y {n_incl_a_excl} incluidos que pasaron a excluidos\ntras la validación)', OI['bermellon'], fs=10)
flecha(ax, XL + W, 8.45, XR, 8.45)
flecha(ax, XL + W / 2, 7.85, XL + W / 2, 7.2)
caja(ax, XL, 5.45, W, 1.75, f'Registros incluidos\n(provisional, nivel resumen)\nn = {n_incluidos}\n'
     f'Acuerdo entre pasadas (20 %): κ = {KAPPA_VAL}', OI['verde'])
caja(ax, XR, 5.3, W, 2.05, f'Cribado asistido por modelos de lenguaje:\n1.ª pasada sobre {n_unicos}; 2.ª pasada ciega\n'
     f'sobre {N_MUESTRA_VAL} (20 %). {n_inciertos + N_DESACUERDOS} casos dudosos ({n_inciertos} inciertos\n'
     f'y {N_DESACUERDOS} desacuerdos) resueltos por el autor;\n'
     f'{N_PROVISIONALES} decisiones automáticas ({N_CONFIRMADAS} confirmadas\npor la 2.ª pasada), provisionales hasta\nverificación humana por submuestra',
     OI['naranja'], fs=9.4)

# Elegibilidad
flecha(ax, XL + W / 2, 5.45, XL + W / 2, 4.85)
banda(ax, 3.55, 1.45, 'Elegibilidad', OI['bermellon'])
caja(ax, XL, 3.65, W, 1.2, f'Evaluación a texto completo\nn = {n_incluidos} (pendiente: requiere\n'
     'doble revisor humano y acceso\ninstitucional a los textos)', OI['bermellon'], fs=10)

# Síntesis
flecha(ax, XL + W / 2, 3.65, XL + W / 2, 3.1)
banda(ax, 0.25, 3.0, 'Síntesis', OI['purpura'])
caja(ax, XL, 0.4, W, 2.7, f'Síntesis temática (nivel resumen)\nn = {n_incluidos} codificados\n'
     'Libro de códigos a priori:\n14 dimensiones candidatas (D1–D14)\n'
     'Doble codificación automatizada\n'
     f'κ por dimensión: {KAPPA_RANGO}\n{N_ADJ} desacuerdos adjudicados\n(modelo de lenguaje)\n'
     '→ 7 dimensiones retenidas', OI['purpura'], fs=9.8)
nombres = [('D1', 'Tolerancia al riesgo'), ('D5', 'Aversión a la pérdida'),
           ('D12', 'Influencia social'), ('D7', 'Regulación emocional'),
           ('D8', 'Horizonte'), ('D4', 'Autoeficacia'), ('D10', 'Tolerancia a la ambigüedad')]
caja(ax, XR, 0.4, W, 2.7, 'Dimensiones retenidas (n resúmenes)\n' +
     '\n'.join(f'{c} {t}: {dims[c]}' for c, t in nombres), OI['verde'], fs=10)
flecha(ax, XL + W, 1.75, XR, 1.75)

out = H / 'fig_3_4_prisma_flujo.png'
plt.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
print(f'OK {out.name}: excluidos {n_excluidos} = {n_excl_criterio} + {n_inciertos} + {n_incl_a_excl}; '
      f'incluidos {n_incluidos}; provisionales {N_PROVISIONALES}')

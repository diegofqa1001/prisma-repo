"""Figura 3.4 - Diagrama de flujo PRISMA del Capítulo 3 (síntesis de perfiles).
Paleta azul marino + grises, fondo blanco, sin título interno (el título va en la leyenda APA).
Fuentes: ../PRISMA_master_final.csv, 07-cribado/validacion.md, 08-sintesis/.
Uso: python fig_3_4_prisma_flujo.py  -> fig_3_4_prisma_flujo.png (300 dpi)
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "DejaVu Sans"
from matplotlib.patches import FancyBboxPatch

# Paleta institucional sobria: azul marino + grises
OI = {"azul": "#1F3A5F", "naranja": "#4A6585", "verde": "#1F3A5F",
      "bermellon": "#8C8C8C", "rosa": "#6B7F99", "celeste": "#A9B8C9"}
TXT = "#111111"; FLECHA = "#333333"

fig, ax = plt.subplots(figsize=(10.8, 12.4), dpi=300)
fig.patch.set_facecolor("white"); ax.set_facecolor("white")
ax.set_xlim(0, 100); ax.set_ylim(0, 120); ax.axis("off")

def caja(x, y, w, h, color, texto, fs=10.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.9",
                                lw=2.6, ec=color, fc="white"))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs,
            color=TXT, linespacing=1.18)

def fase(y, h, color, texto):
    ax.add_patch(FancyBboxPatch((2.5, y), 5.5, h, boxstyle="round,pad=0,rounding_size=0.3",
                                lw=1, ec=color, fc=color, alpha=0.92))
    ax.text(5.25, y + h / 2, texto, rotation=90, ha="center", va="center",
            fontsize=11.5, fontweight="bold", color="white")

def flecha(x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>,head_width=0.45,head_length=0.9",
                                lw=2, color=FLECHA))

L, W, R = 11, 35.5, 53.5
fase(102, 16, OI["azul"], "Identificación")
fase(57, 41, OI["naranja"], "Cribado")
fase(37, 16, OI["bermellon"], "Elegibilidad")
fase(2, 31, OI["rosa"], "Síntesis")

caja(L, 105, W, 12, OI["azul"],
     "Registros identificados\nScopus: n = 438\nWeb of Science: n = 289\nTotal: n = 727", 10.5)
caja(R, 105, W, 12, OI["bermellon"],
     "Duplicados eliminados\n(cruce Scopus × WoS, título\nnormalizado + similitud ≥ 0,90)\nn = 167", 10.5)
flecha(L + W, 111, R - 0.3, 111)
flecha(L + W / 2, 105, L + W / 2, 98.6)

caja(L, 84.5, W, 13.5, OI["naranja"],
     "Registros únicos cribados\n(título y resumen)\nn = 560\nDOI verificado: 502 (89,6 %)", 10.5)
caja(R, 84.5, W, 13.5, OI["bermellon"],
     "Registros excluidos\nn = 217\n(161 por criterios E1–E7,\n48 inciertos y 8 incluidos que\npasaron a excluidos tras la validación)", 10)
flecha(L + W, 91.25, R - 0.3, 91.25)
flecha(L + W / 2, 84.5, L + W / 2, 78.6)

caja(L, 59, W, 19.5, OI["verde"],
     "Registros incluidos\n(nivel resumen)\nn = 343\nAcuerdo entre pasadas (20 %):\nκ = 0,799", 11)
caja(R, 59, W, 19.5, OI["naranja"],
     "Cribado asistido por IA\n(8 lotes × 70 registros)", 12)
flecha(L + W / 2, 59, L + W / 2, 52.6)

caja(L, 39, W, 13.5, OI["bermellon"],
     "Evaluación a texto completo\nn = 343", 11.5)
flecha(L + W / 2, 39, L + W / 2, 33.6)

caja(L, 3, W, 30.5, OI["rosa"],
     "Síntesis temática (nivel resumen)\nn = 343 codificados\nLibro de códigos a priori:\n14 dimensiones candidatas (D1–D14)\n"
     "Doble codificación automatizada\nκ por dimensión: 0,76–0,96\n149 desacuerdos adjudicados\n→ 7 dimensiones retenidas", 10.5)
caja(R, 3, W, 30.5, OI["verde"],
     "Dimensiones retenidas (n resúmenes)\nD1 Tolerancia al riesgo: 189\nD5 Aversión a la pérdida: 153\n"
     "D12 Influencia social: 96\nD7 Regulación emocional: 48\nD8 Horizonte: 12\nD4 Autoeficacia: 9\n"
     "D10 Tolerancia a la ambigüedad: 6", 10.5)
flecha(L + W, 18.25, R - 0.3, 18.25)

fig.savefig("fig_3_4_prisma_flujo.png", dpi=300, facecolor="white", bbox_inches="tight", pad_inches=0.15)
fig.savefig("fig_3_4_prisma_flujo.svg", facecolor="white", bbox_inches="tight", pad_inches=0.15)

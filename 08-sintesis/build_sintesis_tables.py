"""Regenera las tablas de 08-sintesis/ a partir de codificacion_final_343.csv."""
import pandas as pd, json
from pathlib import Path
H = Path(__file__).resolve().parent
df = pd.read_csv(H / 'codificacion_final_343.csv')
dims = [f'D{i}' for i in range(1, 15)]
t = pd.DataFrame({'codigo': dims, 'n_resumenes': [int(df[d].sum()) for d in dims], 'pct': [round(100 * df[d].mean(), 1) for d in dims]})
t.to_csv(H / 'tabla_frecuencias_regeneradas.csv', index=False)
for f in ['tipo', 'poblacion', 'activo', 'propone_tipologia']:
    df[f].value_counts().rename_axis(f).reset_index(name='n').to_csv(H / f'tabla_{f}.csv', index=False)
df.year.value_counts().sort_index().rename_axis('year').reset_index(name='n').to_csv(H / 'tabla_anio.csv', index=False)
df.region.value_counts().rename_axis('region').reset_index(name='n').to_csv(H / 'tabla_region.csv', index=False)
df[['D1', 'D10', 'D5', 'D7', 'D4', 'D8', 'D12']].corr().round(3).to_csv(H / 'phi_dimensiones_retenidas.csv')
json.dump({d: df.loc[df[d] == 1, ['rid', 'doi', 'year', 'title']].to_dict('records') for d in dims}, open(H / 'matriz_evidencia.json', 'w'), ensure_ascii=False, indent=1)
print(t.to_string(index=False))

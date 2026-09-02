# Libro de códigos — síntesis temática a nivel de resumen (PRISMA fase 3, extracción)

Unidad: cada registro incluido (título + resumen). Codifique SOLO lo que el resumen afirma o examina explícitamente; no infiera.

## A. Dimensiones conductuales candidatas (marque todas las que el estudio examine, mida, modele o discuta sustantivamente; no basta con que aparezca la palabra)
- D1  Tolerancia / actitud / percepción del riesgo del inversionista (risk tolerance, risk attitude, risk appetite, risk perception, risk propensity, risk-taking)
- D2  Alfabetización / conocimiento financiero (financial literacy, financial knowledge, financial education)
- D3  Exceso de confianza (overconfidence, self-attribution, illusion of control)
- D4  Autoeficacia financiera (financial self-efficacy, perceived competence, confidence in own financial decisions)
- D5  Aversión a la pérdida / teoría prospectiva / efecto disposición (loss aversion, prospect theory, disposition effect, regret aversion, myopic loss aversion)
- D6  Otros sesgos cognitivos genéricos (anchoring, representativeness, availability, mental accounting, framing, status quo, familiarity/home bias, gambler's fallacy, hindsight)
- D7  Emociones y regulación emocional (emotions, affect, mood, sentiment del inversionista individual, fear, anxiety, stress, emotional regulation, emotional intelligence, panic)
- D8  Horizonte de inversión / ciclo de vida / edad como determinante temporal (investment horizon, time preference, long-term vs short-term, life-cycle, retirement horizon)
- D9  Experiencia inversora (investment experience, trading experience, years investing, sophistication)
- D10 Tolerancia a la ambigüedad / incertidumbre knightiana (ambiguity aversion/tolerance, uncertainty attitude, unknown probabilities)
- D11 Valores culturales / identidad (culture, religion, national culture dimensions, values, gender identity effects treated as culture)
- D12 Influencia social percibida / manada (herding, social influence, peer effects, social norms, social interaction, word of mouth)
- D13 Efectos de pares y redes sociales específicos (social networks, social media platforms, online communities, influencers) — codifique además D12 si aplica
- D14 Susceptibilidad mediática / información (media coverage, news, attention, information overload, fintech nudges, robo-advice framing)

## B. Metadatos
- tipo: uno de {encuesta, experimento, datos_transaccionales, teorico_conceptual, revision, computacional_ML, mixto}
- poblacion: uno de {minoristas, estudiantes, profesionales_asesores, mixta_no_especificada, institucionales}
- region: país o región principal del dato (o "NA" si teórico/global)
- activo: uno de {acciones, cripto, fondos, mixto_general, otro}
- propone_tipologia: true si el estudio propone o valida una clasificación/segmentación/tipología/perfil de inversionistas; false en caso contrario
- notas: ≤ 15 palabras, opcional

## Salida
Lista JSON: [{"rid": "...", "dims": ["D1","D5"], "tipo": "...", "poblacion": "...", "region": "...", "activo": "...", "propone_tipologia": false, "notas": ""}, ...]

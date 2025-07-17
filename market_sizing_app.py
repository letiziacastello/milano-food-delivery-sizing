# market_sizing_app.py per Streamlit usarlo, fare run, e poi scrivere nel terminale: streamlit run market_sizing_app.py

import streamlit as st
import matplotlib.pyplot as plt

# --- Titolo ---
st.set_page_config(page_title="Market Sizing – Food Delivery", layout="centered")
st.title("Market Sizing – Food Delivery a Milano")
st.markdown("**Analisi interattiva top-down sul valore annuo della pizza e sushi a domicilio.**")

# --- Sidebar: parametri ---
st.sidebar.header("Parametri")
population_milan = 3_100_000

active_pct = st.sidebar.slider("Percentuale utenti attivi (%)", 10, 90, 60) / 100
orders_per_week = st.sidebar.slider("Ordini per settimana", 0, 7, 2)
pizza_pct = st.sidebar.slider("Quota Pizza (%)", 0, 100, 30) / 100
sushi_pct = st.sidebar.slider("Quota Sushi (%)", 0, 100, 20) / 100

avg_price_pizza = 9.00
avg_price_sushi = 10.88

# --- Calcoli ---
active_users = population_milan * active_pct
annual_orders_per_user = orders_per_week * 52

spesa_pizza = active_users * annual_orders_per_user * pizza_pct * avg_price_pizza
spesa_sushi = active_users * annual_orders_per_user * sushi_pct * avg_price_sushi
spesa_totale = spesa_pizza + spesa_sushi

# --- Output ---
st.subheader("Stima Annuale della Spesa")
st.write(f"Pizza: **€{spesa_pizza:,.0f}**")
st.write(f"Sushi: **€{spesa_sushi:,.0f}**")
st.write(f"Totale stimato: **€{spesa_totale:,.0f}**")

# --- Grafico Spesa Annuale per Categoria (restyling) ---
fig, ax = plt.subplots(figsize=(7, 5))

labels = ['Pizza', 'Sushi']
values = [spesa_pizza, spesa_sushi]
colors = ['#FF9F1C', '#2EC4B6']

bars = ax.bar(labels, values, color=colors, width=0.5)

# Etichette sopra le barre in formato milioni
for bar in bars:
    height = bar.get_height()
    label = f"€{height/1e6:,.0f}M"
    ax.text(bar.get_x() + bar.get_width()/2., height + (0.03 * height),
        label, ha='center', va='bottom', fontsize=11, weight='bold')

import matplotlib.ticker as ticker  
ax.set_ylabel("Spesa annuale (€ in milioni)", fontsize=11)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1e6)}M'))
ax.set_title("Spesa Annuale Stimata per Categoria", fontsize=13, weight='bold', pad= 20)
ax.spines[['top', 'right']].set_visible(False)
ax.tick_params(axis='y', labelsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.5)
st.pyplot(fig)

# --- Calcolo TAM, SAM, SOM ---
TAM = spesa_totale
SAM = TAM * 0.80  # esempio: 80% raggiungibile
SOM = SAM * 0.25  # esempio: 25% quota ottenibile

# --- Funnel TAM – SAM – SOM (restyling) ---
st.subheader("Funnel di Mercato: TAM – SAM – SOM")

funnel_labels = ["TAM\nTotale Mercato", "SAM\nMercato Raggiungibile", "SOM\nQuota Conquistabile"]
funnel_values = [TAM, SAM, SOM]
funnel_colors = ["#A3C4BC", "#7D98A1", "#4B4E6D"]

fig2, ax2 = plt.subplots(figsize=(8, 4.5))
bars = ax2.barh(funnel_labels, funnel_values, color=funnel_colors)

for bar in bars:
    width = bar.get_width()
    label = f"€{width/1e6:,.0f}M"
    ax2.text(width + 1e7, bar.get_y() + bar.get_height()/2,
             label, va='center', ha='left', fontsize=10, weight='bold')

ax2.set_title("Funnel TAM – SAM – SOM – Food Delivery Milano", fontsize=12, weight='bold')
ax2.set_xlabel("Valore stimato (€)", fontsize=10)
ax2.spines[['top', 'right']].set_visible(False)
ax2.grid(axis='x', linestyle='--', alpha=0.5)
ax2.tick_params(labelsize=10)
st.pyplot(fig2)

st.subheader("Cosa ci raccontano questi numeri?")
st.markdown("""
Anche considerando solo due categorie e una singola città, il food delivery può generare decine o centinaia di milioni di euro ogni anno.
Questa analisi serve a stimare il valore raggiungibile da un operatore, distinguendo tra **potenziale totale**, **mercato servibile**, e **quota realisticamente ottenibile**.

Ecco alcuni insight strategici che emergono da questa analisi:
""")

st.markdown("""
**Mercato urbano ad alto potenziale**  
Anche limitandoci a una sola città e due categorie, il mercato stimato supera i **900 milioni di euro annui**.  
Questo dimostra che anche scenari locali e verticali possono offrire opportunità di business significative.
""")

st.markdown("""
 **Frequenza vs Margine: due logiche complementari**  
La **pizza** viene ordinata più frequentemente, ma con un ticket medio inferiore.  
Il **sushi** invece ha una frequenza più bassa, ma un valore per ordine molto più alto.  
Questo suggerisce strategie diverse per ciascuna categoria: promozioni ricorrenti per la pizza, esperienze premium e upselling per il sushi.
""")

st.markdown("""
**Modello adattabile e scalabile**  
Questa simulazione si basa su assunzioni modificabili e dati realistici.  
Il modello può essere facilmente adattato ad **altre città**, **categorie**, o **scenari di crescita**, semplicemente aggiornando:  
- la popolazione urbana,  
- le percentuali attive,  
- i prezzi medi per categoria.

È un framework utile per **espansione territoriale**, **analisi competitiva** o **decisioni di investimento**.
""")

st.subheader("Raccomandazioni Strategiche")

st.markdown("""
**Punta sulle categorie premium**  
Categorie come il sushi generano uno scontrino medio molto più alto.  
Suggerisco di focalizzare le campagne marketing e la UX su utenti ad alta spesa nelle zone centrali o di fascia alta.
""")

st.markdown("""
            **Personalizza e scala con i dati**  
Questo modello può diventare uno strumento decisionale:  
- per valutare **nuove aree di espansione**,  
- per creare simulazioni *what-if* in base a zone, categorie o trend,  
- oppure per costruire **dashboard interne** (BI) a supporto di growth e finance.

Suggerisco di integrarlo in un sistema più ampio con KPI e aggiornamento continuo.
""")

st.markdown("---")
st.markdown("""
### Conclusione

Questo progetto nasce da una sfida reale: stimare il valore di mercato in un contesto urbano e competitivo come il food delivery a Milano.  
Unisce **analisi dati, pensiero strategico e design interattivo**.

 È un esempio concreto di come trasformo dati in **decisioni** e numeri in **visione di business**.  
Saper analizzare è utile. Saper **guidare con i dati** è ciò che mi differenzia.
""")
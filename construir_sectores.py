import os
from generar import pagina, escribir, RAIZ

SECTORES = {
    "asesorias": {
        "titulo": "Asesorías y gestorías",
        "resumen": "Correos, documentación y plazos que se acumulan cada trimestre.",
        "dolores": [
            ("Correos sin clasificar", "Cada mensaje hay que leerlo para saber si es una duda, una entrega de documentación o una urgencia."),
            ("Papeles que faltan", "Cada cliente pregunta lo mismo por una vía distinta, y el asesor pierde tiempo repitiendo la misma respuesta."),
            ("Plazos que se acumulan", "Trimestre tras trimestre, la misma carrera contra el calendario fiscal."),
        ],
        "automatizaciones": [
            ("Clasificación de correo entrante", "Nivel 2", "Cada correo se lee, se clasifica y se reparte al buzón correcto antes de que nadie lo abra."),
            ("Extracción de datos de facturas", "Nivel 2", "Los datos de la factura entran solos en el programa de contabilidad, sin teclear nada."),
            ("Asistente que responde con tu documentación", "Nivel 3-4", "El cliente pregunta por WhatsApp qué papeles le faltan, y el sistema responde mirando su expediente real — el mismo que ves en la demostración de la portada."),
        ],
        "proyecto_rel": ("crm-energia", "CRM para consultoría energética", "Una consultoría con varios clientes y una única plataforma que separa los datos de cada uno."),
        "dato": '<p style="color:var(--gris);font-size:14px;margin-top:var(--s-6)">El plazo general del modelo 303 del tercer trimestre termina el 20 de octubre; si domicilias el pago, el 15 de octubre. <a href="https://sede.agenciatributaria.gob.es/Sede/iva/presentar-declaracion-iva-modelo-303/plazo-presentacion-modelo-303.html" target="_blank" rel="noopener" style="color:var(--acento)">Fuente: Agencia Tributaria</a>.</p>',
    },
    "clinicas": {
        "titulo": "Clínicas y centros",
        "resumen": "Citas, recordatorios y llamadas que llegan fuera de horario.",
        "dolores": [
            ("Ausencias sin recordatorio", "Un hueco libre a última hora que nadie avisó a tiempo de ocupar."),
            ("Llamadas fuera de horario", "El paciente llama a las 21:00 y hasta el día siguiente no hay quien conteste."),
            ("Agenda repartida entre varios canales", "Teléfono, WhatsApp y la propia web, sin un único sitio que lo centralice."),
        ],
        "automatizaciones": [
            ("Recordatorio automático de cita", "Nivel 1", "Un mensaje el día antes, sin que nadie tenga que acordarse de enviarlo."),
            ("Reserva de cita por WhatsApp", "Nivel 2-3", "El paciente pide hora y el sistema mira la agenda real antes de confirmar."),
            ("Recepción con agente de voz", "Nivel 4", "Atiende la llamada fuera de horario y crea la cita, con el reparto de responsabilidades documentado como en Distail."),
        ],
        "proyecto_rel": ("distail", "Distail — recepción y captación con IA", "Qué resuelve un agente conversacional al atender una llamada y qué resuelve un flujo determinista al crear la cita."),
        "dato": "",
    },
    "restauracion": {
        "titulo": "Restauración",
        "resumen": "Reservas, carta y reseñas gestionadas sin depender de una sola persona.",
        "dolores": [
            ("Reservas por teléfono y mensaje a la vez", "Dos canales que no se hablan entre sí, y el riesgo de doblar una mesa."),
            ("Carta que nadie actualiza", "Cada cambio de precio o de plato depende de que alguien avise al que lleva la web."),
            ("Reseñas sin seguimiento", "Una mala reseña se queda sin respuesta simplemente porque nadie la vio a tiempo."),
        ],
        "automatizaciones": [
            ("Reserva de mesa en la propia web", "Nivel 1", "Día, hora y comensales, sin depender del teléfono."),
            ("Carta editable por el propio negocio", "Nivel 1", "Se cambia un precio y se publica al momento, sin intermediarios."),
            ("Aviso de reseña nueva", "Nivel 2", "Un aviso automático en cuanto llega una reseña, para responder el mismo día."),
        ],
        "proyecto_rel": ("rustik", "Rustik Gastro Bar — carta y reservas", "Web con carta y reservas, más un panel para que el propio negocio la actualice sin intermediarios."),
        "dato": "",
    },
    "clubes": {
        "titulo": "Clubes y asociaciones",
        "resumen": "Cuotas, inscripciones y comunicación con las familias.",
        "dolores": [
            ("Morosidad sin control", "Saber quién debe algo exige repasar hojas sueltas o preguntar a tesorería."),
            ("Documentación caducada", "Un papel vencido que nadie nota hasta que ya es tarde."),
            ("Comunicación repetida con las familias", "El mismo aviso, mandado uno a uno por varios canales."),
        ],
        "automatizaciones": [
            ("Aviso de cuota pendiente", "Nivel 1", "Un recordatorio automático antes de que la deuda se acumule."),
            ("Alerta de documento a punto de caducar", "Nivel 1", "Aviso antes de la fecha límite, no después."),
            ("Panel para directivas sin perfil técnico", "Nivel 1", "Todo en un único sitio, como en Cantera."),
        ],
        "proyecto_rel": ("cantera", "Cantera — clubes de fútbol base", "Cuotas, morosidad y documentación con caducidad, en un panel que usa gente sin perfil técnico."),
        "dato": "",
    },
}

for slug, s in SECTORES.items():
    dolores_html = "".join(
        f'<div class="dolor"><span class="num">{i+1:02d}</span><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i, (t, d) in enumerate(s["dolores"])
    )
    autos_html = "".join(
        f'<div class="peldano"><span class="n">{niv}</span><h3>{t}</h3><p>{d}</p></div>'
        for t, niv, d in s["automatizaciones"]
    )
    rel_slug, rel_titulo, rel_texto = s["proyecto_rel"]
    cuerpo = f'''
  <section class="hero" style="padding-top:var(--s-7)">
    <div class="contenedor">
      <p class="etiqueta">Sectores · {s['titulo']}</p>
      <h1 style="font-size:clamp(32px,5vw,52px);margin-top:var(--s-3)">Automatización para {s['titulo'].lower()}</h1>
      <p class="sub">{s['resumen']}</p>
      <div class="hero-cta"><a class="btn btn-primario" href="../../#contacto">Reservar llamada</a></div>
    </div>
  </section>
  <section class="seccion" style="padding-top:0">
    <div class="contenedor">
      <div class="seccion-cabecera"><p class="etiqueta">¿Te suena?</p><h2>Lo que más se repite en este sector</h2></div>
      <div class="dolores-lista">{dolores_html}</div>
    </div>
  </section>
  <section class="seccion">
    <div class="contenedor">
      <div class="seccion-cabecera"><p class="etiqueta">Qué se automatiza</p><h2>Tres ejemplos, de menos a más complejo</h2></div>
      <div class="escalera">{autos_html}</div>
      {s['dato']}
    </div>
  </section>
  <section class="seccion bloque-crema">
    <div class="contenedor">
      <div class="seccion-cabecera"><p class="etiqueta">Caso relacionado</p><h2 style="color:var(--crema-tinta)">{rel_titulo}</h2><p>{rel_texto}</p></div>
      <a class="btn btn-sobre-crema" href="../../proyectos/{rel_slug}/">Ver el proyecto →</a>
    </div>
  </section>
  <section class="seccion">
    <div class="contenedor centro">
      <h2>¿Hay un proceso así en tu negocio?</h2>
      <div class="hero-cta" style="justify-content:center;margin-top:var(--s-5)">
        <a class="btn btn-primario" href="../../#contacto">Reservar llamada — 20 min, gratis</a>
        <a class="btn btn-secundario" href="https://wa.me/34931525368" target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </div>
    </div>
  </section>
'''
    escribir(
        os.path.join(RAIZ, "sectores", slug, "index.html"),
        pagina(
            rel="../../",
            titulo=f"Automatización para {s['titulo']} — MPAI Technologies",
            descripcion=f"Automatización y agentes de IA para {s['titulo'].lower()}: {s['resumen']}",
            url_canon=f"https://mpaitechnologies.es/sectores/{slug}/",
            cuerpo=cuerpo,
            activo="sectores",
        ),
    )

print("Sectores listos.")

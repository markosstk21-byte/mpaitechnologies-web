import os
from generar import pagina, escribir, RAIZ

cuerpo = '''
  <section class="seccion" style="padding-top:var(--s-8);max-width:760px;margin:0 auto">
    <div class="contenedor">
      <p class="etiqueta">Información legal</p>
      <h1 style="font-size:clamp(28px,4vw,40px);margin-top:var(--s-3)">Aviso legal</h1>
      <div style="margin-top:var(--s-6);color:#d5d5da;font-size:16px;display:grid;gap:var(--s-5);line-height:1.7">
        <p>Datos identificativos del titular de este sitio web, conforme al artículo 10 de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE).</p>
        <p><strong style="color:var(--blanco)">Titular:</strong> Marco Pavón Cobo<br>
        <strong style="color:var(--blanco)">NIF:</strong> 46717689C<br>
        <strong style="color:var(--blanco)">Nombre comercial:</strong> MPAI Technologies<br>
        <strong style="color:var(--blanco)">Domicilio:</strong> C/ Mirador, 8 · 08105 Sant Fost de Campsentelles (Barcelona), España<br>
        <strong style="color:var(--blanco)">Correo de contacto:</strong> info@mpaitechnologies.es<br>
        <strong style="color:var(--blanco)">Actividad:</strong> consultoría de automatización y agentes de inteligencia artificial, prestada como profesional autónomo bajo el nombre comercial MPAI Technologies.</p>
        <p>Este sitio no recoge datos personales mediante formularios ni utiliza cookies de seguimiento. Se emplea una analítica sin cookies (agregada, sin datos identificativos) para saber cuántas visitas recibe la web. El contacto se realiza por correo electrónico o WhatsApp. Si escribes, tu mensaje y tus datos de contacto se tratan con la única finalidad de responder y valorar una posible colaboración, y se conservan mientras dure esa relación. Puedes solicitar su acceso, rectificación o supresión en la misma dirección, y reclamar ante la Agencia Española de Protección de Datos.</p>
        <p>Los textos, el logotipo y el diseño de este sitio son de su titular. Los rangos de precios y los plazos son orientativos y no constituyen una oferta contractual: cada proyecto se cierra por escrito con su propio alcance y precio. Esta relación se rige por la legislación española.</p>
      </div>
    </div>
  </section>
'''
escribir(
    os.path.join(RAIZ, "aviso-legal", "index.html"),
    pagina(
        rel="../",
        titulo="Aviso legal — MPAI Technologies",
        descripcion="Información legal de mpaitechnologies.es, titularidad de Marco Pavón Cobo.",
        url_canon="https://mpaitechnologies.es/aviso-legal/",
        cuerpo=cuerpo,
    ),
)
print("Legal listo.")

"""Genera las tres páginas legales: /aviso-legal/, /privacidad/ y /cookies/.

Fuentes de cada apartado:
- Aviso legal: art. 10 de la Ley 34/2002 (LSSI-CE), BOE-A-2002-13758.
- Privacidad: arts. 6, 12, 13 y 15-22 del Reglamento (UE) 2016/679 (RGPD).
- Cookies: art. 22.2 LSSI-CE.
Si cambia un proveedor, un plazo o un dato del titular, se cambia AQUÍ y se
regenera con `python3 construir_legal.py`. No se editan los HTML a mano.
"""
import os
from generar import pagina, escribir, RAIZ

ACTUALIZADO = "25 de septiembre de 2026"

TITULAR = "Marco Pavón Cobo"
NIF = "46717689C"
DOMICILIO = "C/ Mirador, 8 · 08105 Sant Fost de Campsentelles (Barcelona), España"
CORREO = "info@mpaitechnologies.es"
TELEFONO = "931 525 368"


def b(texto):
    return f'<strong style="color:var(--blanco)">{texto}</strong>'


def envolver(etiqueta, titulo, bloques):
    contenido = "\n".join(f"        {x}" for x in bloques)
    return f'''
  <section class="seccion" style="padding-top:var(--s-8);max-width:760px;margin:0 auto">
    <div class="contenedor">
      <p class="etiqueta">{etiqueta}</p>
      <h1 style="font-size:clamp(28px,4vw,40px);margin-top:var(--s-3)">{titulo}</h1>
      <div class="texto-legal" style="margin-top:var(--s-6);color:#d5d5da;font-size:16px;display:grid;gap:var(--s-5);line-height:1.7">
{contenido}
        <p style="color:var(--gris);font-size:14px">Última actualización: {ACTUALIZADO}.</p>
      </div>
    </div>
  </section>
'''


def h2(texto):
    return f'<h2 style="font-size:20px;margin-top:var(--s-4);color:var(--blanco)">{texto}</h2>'


# ---------------------------------------------------------------- Aviso legal
aviso = envolver("Información legal", "Aviso legal", [
    f"<p>Datos identificativos del titular de este sitio web, conforme al artículo 10 de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE).</p>",
    f"<p>{b('Titular:')} {TITULAR}<br>\n        {b('NIF:')} {NIF}<br>\n        {b('Nombre comercial:')} MPAI Technologies<br>\n        {b('Domicilio:')} {DOMICILIO}<br>\n        {b('Correo electrónico:')} <a href=\"mailto:{CORREO}\">{CORREO}</a><br>\n        {b('Teléfono y WhatsApp:')} {TELEFONO}<br>\n        {b('Actividad:')} consultoría de automatización y agentes de inteligencia artificial, prestada como profesional autónomo bajo el nombre comercial MPAI Technologies.</p>",
    "<p>El titular ejerce como persona física, por lo que no figura inscrito en el Registro Mercantil. La actividad no requiere autorización administrativa previa ni pertenencia a un colegio profesional, y el titular no está adherido a ningún código de conducta.</p>",
    h2("Precios"),
    "<p>Los precios que aparecen en esta web son rangos orientativos, <strong>sin IVA incluido</strong>, y no constituyen una oferta contractual. Cada proyecto se cierra por escrito con su alcance, su precio definitivo y los impuestos aplicables antes de empezar.</p>",
    h2("Demostraciones"),
    "<p>Las conversaciones y pantallas de demostración de esta web usan datos de ejemplo y van rotuladas como tales. El chat de ejemplo de la página principal es un guion fijo: no está conectado a ningún sistema de inteligencia artificial ni guarda lo que pulses.</p>",
    h2("Propiedad intelectual"),
    "<p>Los textos, el logotipo, las imágenes propias y el diseño de este sitio pertenecen a su titular. Los nombres y marcas de terceros que se citan (por ejemplo, herramientas o plataformas) pertenecen a sus respectivos dueños y se mencionan solo a efectos descriptivos. No se permite reproducir el contenido con fines comerciales sin autorización por escrito.</p>",
    h2("Enlaces a otros sitios"),
    "<p>Esta web enlaza a servicios externos, como WhatsApp o la agenda de Google para reservar una llamada. Esos sitios tienen sus propias condiciones y políticas de privacidad, y el titular no responde de su contenido ni de su funcionamiento.</p>",
    h2("Protección de datos y cookies"),
    "<p>Cómo se tratan los datos de quien contacta está explicado en la <a href=\"../privacidad/\">política de privacidad</a>. Esta web no usa cookies: el detalle está en la <a href=\"../cookies/\">política de cookies</a>.</p>",
    h2("Legislación aplicable"),
    "<p>Este sitio y las relaciones que nazcan de él se rigen por la legislación española. Cualquier controversia se someterá a los juzgados y tribunales que correspondan conforme a la ley.</p>",
])

# ---------------------------------------------------------- Privacidad (RGPD)
privacidad = envolver("Información legal", "Política de privacidad", [
    "<p>Esta política explica qué datos personales se tratan cuando visitas esta web o te pones en contacto, para qué, con qué base legal, durante cuánto tiempo y qué derechos tienes. Cumple el artículo 13 del Reglamento (UE) 2016/679 (RGPD) y la Ley Orgánica 3/2018 (LOPDGDD).</p>",
    h2("1. Responsable del tratamiento"),
    f"<p>{TITULAR} (MPAI Technologies), NIF {NIF}.<br>\n        Domicilio: {DOMICILIO}.<br>\n        Correo: <a href=\"mailto:{CORREO}\">{CORREO}</a> · Teléfono: {TELEFONO}.</p>",
    h2("2. Qué datos se tratan y para qué"),
    "<p>Esta web <strong>no tiene formularios, registro de usuarios ni cookies</strong>. Solo se tratan datos personales en estos casos:</p>",
    "<ul style=\"display:grid;gap:var(--s-3);padding-left:1.2em\">"
    "<li><strong>Si escribes por correo o por WhatsApp.</strong> Se tratan tu nombre, tu correo o teléfono, el nombre de tu empresa si lo indicas y lo que cuentes en el mensaje. Finalidad: responderte y, si lo pides, preparar un diagnóstico o un presupuesto. Base jurídica: aplicar medidas precontractuales a petición tuya (art. 6.1.b RGPD) y, para consultas generales, el interés legítimo en atender a quien escribe (art. 6.1.f RGPD).</li>"
    "<li><strong>Si reservas una llamada.</strong> La reserva se hace en la agenda de Google. Se tratan el nombre, el correo y los datos que añadas al reservar, además de la fecha y la hora. Finalidad: organizar y mantener la llamada. Base jurídica: medidas precontractuales a petición tuya (art. 6.1.b RGPD).</li>"
    "<li><strong>Si llegas a ser cliente.</strong> Se tratan los datos de contacto y de facturación necesarios para prestar el servicio y emitir las facturas. Base jurídica: la ejecución del contrato (art. 6.1.b RGPD) y el cumplimiento de obligaciones legales fiscales y contables (art. 6.1.c RGPD).</li>"
    "<li><strong>Si tu empresa recibe un primer contacto comercial.</strong> Para buscar clientes se usan datos de empresas obtenidos de fuentes públicas: el Boletín Oficial del Registro Mercantil (BORME), la Plataforma de Contratación del Sector Público, OpenStreetMap y la propia web de la empresa. Se tratan el nombre de la empresa, su actividad, su dirección y su teléfono o correo de contacto profesional y, cuando la empresa es un profesional autónomo, su nombre. Finalidad: ofrecer los servicios de MPAI Technologies. Base jurídica: el interés legítimo en la prospección comercial entre empresas (art. 6.1.f RGPD y art. 19 LOPDGDD), valorado previamente frente a tus derechos. Antes de llamar a un profesional autónomo o empresario individual se consultan los sistemas de exclusión publicitaria (Lista Robinson). Puedes oponerte en cualquier momento, y desde ese momento no se te vuelve a contactar.</li>"
    "<li><strong>Al visitar la web.</strong> La web está alojada en GitHub Pages. Según su documentación, GitHub registra y guarda la dirección IP de cada visitante por motivos de seguridad. Ese registro lo gestiona GitHub, y el titular de esta web no tiene acceso a él.</li>"
    "</ul>",
    "<p>No se toman decisiones automatizadas ni se elaboran perfiles con tus datos, y no se usan para enviarte publicidad si no lo pides expresamente.</p>",
    h2("3. Cuánto tiempo se conservan"),
    "<p>Las consultas y reservas que no terminen en contratación se conservan hasta 12 meses desde el último contacto y después se borran. Los datos de prospección de una empresa que no muestre interés se borran en el mismo plazo. Si te opones a recibir comunicaciones, solo se guarda el dato mínimo para no volver a contactarte. Los datos de clientes se conservan mientras dure la relación y, después, durante los plazos que exige la ley: seis años para la documentación contable (art. 30 del Código de Comercio) y el plazo de prescripción de las obligaciones tributarias (art. 66 de la Ley General Tributaria).</p>",
    h2("4. Quién más accede a los datos"),
    "<p>Los datos no se venden ni se ceden a terceros, salvo por obligación legal (por ejemplo, a la Agencia Tributaria). Para poder funcionar se usan estos proveedores, que tratan datos por cuenta del titular o como parte del servicio que prestan:</p>",
    "<ul style=\"display:grid;gap:var(--s-3);padding-left:1.2em\">"
    "<li><strong>Soluciones Corporativas IP, S.L. (DonDominio)</strong>, NIF B57333601, con sede en España: dominio y correo electrónico.</li>"
    "<li><strong>Google</strong>: agenda para reservar llamadas (Google Calendar). Google LLC, en Estados Unidos, está adherida al Marco de Privacidad de Datos UE-EE. UU.</li>"
    "<li><strong>WhatsApp Ireland Limited</strong>: mensajería, si eliges escribir por WhatsApp. Según su política de privacidad, puede transferir datos a otros países, entre ellos Estados Unidos.</li>"
    "<li><strong>GitHub</strong> (GitHub B.V. y GitHub, Inc.): alojamiento de la web. GitHub, Inc. está adherida al Marco de Privacidad de Datos UE-EE. UU. y usa además cláusulas contractuales tipo de la Comisión Europea.</li>"
    "</ul>",
    h2("5. Transferencias fuera del Espacio Económico Europeo"),
    "<p>Algunos de los proveedores anteriores pueden tratar datos en Estados Unidos. Esas transferencias se amparan en la decisión de adecuación de la Comisión Europea sobre el Marco de Privacidad de Datos UE-EE. UU., para las empresas adheridas, o en las cláusulas contractuales tipo aprobadas por la Comisión (art. 45 y 46 RGPD).</p>",
    h2("6. Tus derechos"),
    f"<p>Puedes pedir el acceso a tus datos, su rectificación o supresión, la limitación del tratamiento, la portabilidad y oponerte al tratamiento basado en interés legítimo, incluida la prospección comercial. Escribe a <a href=\"mailto:{CORREO}\">{CORREO}</a> indicando qué derecho quieres ejercer. Si hay dudas razonables sobre tu identidad, se te pedirá que la acredites. Recibirás respuesta en el plazo de un mes, que puede ampliarse en los casos previstos en el artículo 12.3 del RGPD.</p>",
    "<p>Si crees que no se han respetado tus derechos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (<a href=\"https://www.aepd.es\" target=\"_blank\" rel=\"noopener\">www.aepd.es</a>).</p>",
    h2("7. Seguridad"),
    "<p>Se aplican medidas técnicas y organizativas adecuadas al riesgo (art. 32 RGPD): los datos se guardan en servicios con acceso protegido y solo accede a ellos el titular.</p>",
])

# -------------------------------------------------------------------- Cookies
cookies = envolver("Información legal", "Política de cookies", [
    "<p>Esta web <strong>no usa cookies</strong>, ni propias ni de terceros. Tampoco usa otras tecnologías que guarden o lean información en tu dispositivo, como el almacenamiento local del navegador, píxeles de seguimiento o analítica de visitas.</p>",
    "<p>Por eso no aparece ningún aviso ni banner de consentimiento. El artículo 22.2 de la LSSI-CE exige el consentimiento para guardar o leer información en tu dispositivo, y esta web no hace ninguna de las dos cosas.</p>",
    h2("Enlaces a servicios externos"),
    "<p>Si pulsas en los enlaces de WhatsApp o de la agenda de Google, sales de esta web. Esos servicios pueden usar sus propias cookies, según sus políticas, que no dependen del titular de esta web.</p>",
    h2("Si esto cambia"),
    "<p>Si en el futuro se añade alguna herramienta que use cookies no necesarias, esta política se actualizará antes y se pedirá tu consentimiento previo, con la opción de rechazarlas con la misma facilidad que aceptarlas.</p>",
    "<p>Más información en la <a href=\"../privacidad/\">política de privacidad</a> y en el <a href=\"../aviso-legal/\">aviso legal</a>.</p>",
])

PAGINAS = [
    ("aviso-legal", "Aviso legal — MPAI Technologies",
     "Información legal de mpaitechnologies.es, titularidad de Marco Pavón Cobo.", aviso),
    ("privacidad", "Política de privacidad — MPAI Technologies",
     "Qué datos personales se tratan en mpaitechnologies.es, para qué, durante cuánto tiempo y cómo ejercer tus derechos.", privacidad),
    ("cookies", "Política de cookies — MPAI Technologies",
     "mpaitechnologies.es no usa cookies ni tecnologías de seguimiento.", cookies),
]

for carpeta, titulo, descripcion, cuerpo in PAGINAS:
    escribir(
        os.path.join(RAIZ, carpeta, "index.html"),
        pagina(
            rel="../",
            titulo=titulo,
            descripcion=descripcion,
            url_canon=f"https://mpaitechnologies.es/{carpeta}/",
            cuerpo=cuerpo,
        ),
    )
print("Legal listo.")

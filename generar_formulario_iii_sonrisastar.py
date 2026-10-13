#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador automático del FORMULARIO III oficial + ANEXO LEGAL (Bono Crecimiento Pyme - Orden 116/2026)
para CLÍNICA DENTAL SONRISA STAR (Albacete) con presupuesto de 3.000 € (80% subvencionado = 2.400 €).
"""

import os
import docx
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def generar_formulario_iii_dental():
    base_dir = r"g:\Mi unidad\Altera Dental"
    template_path = r"g:\Mi unidad\AYUDAS IA\Normativa ayudas\1023976_35310.DOCX"
    output_path = os.path.join(base_dir, "Formulario_III_Sonrisastar.docx")
    
    if not os.path.exists(template_path):
        print(f"Error: No se encontró la plantilla en {template_path}")
        return False

    doc = docx.Document(template_path)

    # Insertar logos en la cabecera del documento
    logo_altera = r"g:\Mi unidad\AYUDAS IA\app\logo-altera-header.png"
    logo_cliente = os.path.join(base_dir, "logo-sonrisa.png")

    if doc.paragraphs:
        first_p = doc.paragraphs[0]
        p_logos = first_p.insert_paragraph_before()
        p_logos.alignment = WD_ALIGN_PARAGRAPH.RIGHT

        if os.path.exists(logo_altera):
            r_alt = p_logos.add_run()
            r_alt.add_picture(logo_altera, width=Inches(1.6))
            p_logos.add_run("   ")

        if os.path.exists(logo_cliente):
            r_cli = p_logos.add_run()
            r_cli.add_picture(logo_cliente, width=Inches(1.6))

        r_info = p_logos.add_run("\nAltera — Inteligencia REAL aplicada a tu negocio\ncontacto@altera-es.com · Tel.: +34 624 93 90 23 · www.altera-es.com\n")
        r_info.font.size = Pt(8.5)
        r_info.font.color.rgb = RGBColor(0x64, 0x74, 0x8b)

    servicios = [
        (
            "Modalidad 4",
            "Agente Omnicanal (WhatsApp/Instagram) y Recepcionista Telefónico de Voz con IA 24/7",
            "Implantación y entrenamiento de un agente de IA generativa (LLM) omnicanal integrado en la línea oficial de WhatsApp Business y redes sociales (Instagram Direct mediante plataforma Zernio) junto con un asistente telefónico de voz con IA conversacional (ElevenLabs) conectado al teléfono fijo de la clínica (967 116 136). El sistema opera 24/7 realizando triaje de consultas y urgencias dentales con dolor, resolviendo dudas sobre tratamientos (ortodoncia invisible, implantes, estética) y agendando citas en tiempo real con confirmación interactiva por mensajería.",
            1500.00
        ),
        (
            "Modalidad 4",
            "Rediseño Web UX de Alta Conversión, CRM Clínico y Automatización de Procesos Anti-No-Show",
            "Renovación completa de la presencia digital de sonrisastar.com mediante arquitectura moderna y responsive orientada a la conversión y velocidad de carga, integrada con un panel CRM clínico con pipeline Kanban omnicanal. Incluye la programación y despliegue de flujos automáticos de confirmación y recordatorio anti-no-show 24 horas antes por WhatsApp, protocolos de seguimiento post-intervención quirúrgica y motor de reactivación periódica para revisiones bucodentales y limpiezas semestrales.",
            1500.00
        )
    ]

    total = sum(s[3] for s in servicios)
    subvencion_80 = total * 0.80
    aportacion_20 = total - subvencion_80

    p_text_map = {
        "A) Breve presentación de la empresa solicitante": (
            "La entidad solicitante CLÍNICA DENTAL SONRISA STAR, con centro sanitario en Albacete capital, "
            "desarrolla su actividad profesional en el ámbito de las actividades odontológicas (CNAE 8623). "
            "La clínica cuenta con amplia trayectoria en odontología integral, implantología, ortodoncia, prótesis y estética dental. "
            "Para consolidar su crecimiento, optimizar la ocupación de sus gabinetes dentales y profesionalizar la atención al paciente, "
            "la empresa precisa acometer un proceso integral de modernización digital que incorpore inteligencia artificial en la recepción, "
            "canales de mensajería instantánea y una plataforma web adaptada a los estándares actuales de captación."
        ),
        "B) Localización del centro de trabajo": (
            "El proyecto se ejecuta íntegramente en las instalaciones clínicas de CLÍNICA DENTAL SONRISA STAR "
            "ubicadas en Calle Dionisio Guardiola, 2, 02002 Albacete (Castilla-La Mancha)."
        ),
        "C) Sector al que pertenece la empresa": (
            "Sector Sanitario / Actividades Odontológicas (CNAE Q8623). Actividad plenamente subvencionable "
            "dentro de la Modalidad 4 (Transformación Digital) conforme a la Orden 116/2026 de la JCCM."
        ),
        "D) Productos o servicios que ofrece la empresa actualmente": (
            "Sonrisastar ofrece servicios odontológicos integrales: diagnóstico y radiología digital, implantes dentales, "
            "ortodoncia convencional e invisible, estética dental (blanqueamientos y carillas), endodoncia, periodoncia, "
            "limpiezas bucodentales preventivas y prótesis fijas y removibles."
        ),
        "A) Definición de los objetivos de crecimiento": (
            "1) Implantar un servicio de recepción de llamadas e interacción digital 24/7 con Inteligencia Artificial (voz y mensajería) "
            "para erradicar la pérdida de citas fuera de horario comercial y durante horas punta de atención en gabinete.\n"
            "2) Reducir la tasa de ausencias a citas (no-shows) por debajo del 4% mediante flujos automáticos de confirmación interactiva por WhatsApp.\n"
            "3) Incrementar en un 40% la captación de nuevos pacientes en tratamientos de ticket medio/alto (implantes y ortodoncia) "
            "mediante una web corporativa rápida, accesible y conectada a canales sociales.\n"
            "4) Automatizar la reactivación periódica de la cartera histórica de pacientes para revisiones preventivas anuales y limpiezas."
        ),
        "-B) Justificación, en su caso, del carácter innovador": (
            "El carácter innovador reside en la integración pionera en el sector odontológico de Albacete de modelos de Inteligencia Artificial "
            "conversacional de voz ultrarrealista (ElevenLabs) y procesamiento de lenguaje natural en WhatsApp Business e Instagram Direct, "
            "conectados en tiempo real a una base de datos clínica relacional segura (PostgreSQL/Supabase) en servidor europeo propio. "
            "Esto permite cualificar necesidades, realizar triaje básico de urgencias y agendar citas automáticamente sin saturar al personal de recepción física."
        ),
        "C) Alineación de la actuación con la estrategia regional de especialización inteligente s3": (
            "El proyecto se alinea de forma directa con la prioridad transversal 'Digitalización, modernización y adopción de tecnologías "
            "disruptivas e inteligencia artificial en el tejido de pymes y micropymes' de la Estrategia de Especialización Inteligente S3 de Castilla-La Mancha 2021-2027."
        ),
        "A) Nº total de actuaciones propuestas conforme al art.8": (
            f"Se proponen 2 actuaciones técnicas integradas en la Modalidad 4 (Transformación Digital), "
            f"por un importe total presupuestado de {total:,.2f} € sin IVA.\n"
            f"• Subvención solicitada a la JCCM (80% a fondo perdido): {subvencion_80:,.2f} €.\n"
            f"• Aportación neta asumida por la clínica (20%): {aportacion_20:,.2f} €.\n\n"
            "Conforme al artículo 9.4 de la Orden 116/2026 y al artículo 118 de la Ley 9/2017 de Contratos del Sector Público, "
            "al ser el importe total del contrato inferior al umbral legal de contrato menor de servicios (15.000 €), "
            "no resulta exigible la presentación de tres ofertas de diferentes proveedores, bastando el presupuesto pro-forma aportado por Altera."
        ),
        "C) Justificación de la necesidad de las actuaciones propuestas": (
            "La actual infraestructura digital de la clínica presenta cuellos de botella severos: dependencia exclusiva de un teléfono fijo "
            "(sin WhatsApp oficial ni canal activo en Instagram), imposibilidad de atender llamadas en horario de mediodía, noches o fines de semana, "
            "y una página web desarrollada en 2015 no optimizada para dispositivos móviles. La modernización planteada resulta inaplazable para "
            "garantizar la competitividad, inmediatez y sostenibilidad del negocio frente a grandes franquicias dentales corporativas."
        ),
        "A) Duración de las actuaciones propuestas. Cronograma": (
            "Plazo de ejecución previsto: 3 meses desde la fecha del resguardo telemático de solicitud de la ayuda en la JCCM "
            "(muy inferior al plazo reglamentario máximo de 6 meses establecido en el art. 10.1 de la Orden 116/2026).\n"
            "• Mes 1 (Semanas 1–3): Arquitectura e Infraestructura. Despliegue de servidor dedicado en la UE, configuración de Supabase/Coolify, "
            "definición de protocolos de agendamiento clínico y diseño UX/UI de la nueva web corporativa.\n"
            "• Mes 2 (Semanas 4–8): Desarrollo e Integración IA. Entrenamiento del agente de voz de ElevenLabs para desvío telefónico, configuración "
            "del bot de WhatsApp/Instagram con Zernio, flujos anti-no-show y programación de la web sobre Tailwind CSS.\n"
            "• Mes 3 (Semanas 9–12): Pruebas, Puesta en Producción y Formación. Fase de pruebas de llamada y mensajería real, capacitación del "
            "personal de recepción de la clínica, acta de puesta en marcha operativa y preparación de la justificación técnica final (Formulario V)."
        ),
        "B) Resultados esperados en la empresa y temporalización": (
            "Resultados cuantificables a los 6 meses de la implantación:\n"
            "- 100% de llamadas y consultas entrantes atendidas de forma instantánea 24/7.\n"
            "- Reducción de citas fallidas (no-shows) a menos del 4%, recuperando más de 15 horas mensuales de sillón odontológico.\n"
            "- Captación estimada de entre 12 y 20 nuevos pacientes mensuales a través de la web renovada, WhatsApp y redes sociales.\n"
            "- Cumplimiento del compromiso formal de mantenimiento de las soluciones tecnológicas activas durante al menos 3 años."
        )
    }

    # Recorrer párrafos e insertar los textos
    for p in list(doc.paragraphs):
        for key, text_content in p_text_map.items():
            if key in p.text:
                p_after = p._p.getnext()
                if p_after is not None:
                    target_p = doc.add_paragraph(text_content)
                    p._p.addnext(target_p._p)
                    target_p.style = doc.styles['Normal']
                    for r in target_p.runs:
                        r.font.size = Pt(10)
                        r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Rellenar la tabla de actuaciones
    if doc.tables:
        tbl = doc.tables[0]
        # Fila 1 y Fila 2
        for idx, (mod, act_tipo, act_desc, imp) in enumerate(servicios, start=1):
            if idx < len(tbl.rows) - 1:
                row = tbl.rows[idx]
                row.cells[0].text = mod
                row.cells[1].text = act_tipo
                row.cells[2].text = act_desc
                row.cells[3].text = "Altera Soluciones Tecnológicas\n(www.altera-es.com)"
                row.cells[4].text = "Presupuesto Pro-Forma ALT-2026-DENT01"
                row.cells[5].text = f"{imp:,.2f} €"
                row.cells[6].text = "No aplica (Contrato menor < 15.000 € s/ Art. 9.4 Orden 116/2026)"

        # Fila TOTAL (última fila)
        last_row = tbl.rows[-1]
        if len(last_row.cells) >= 6:
            last_row.cells[5].text = f"{total:,.2f} €"

    # Salto de página y Anexo de Tramitación
    doc.add_page_break()
    p_anexo = doc.add_paragraph()
    r_anexo = p_anexo.add_run("ANEXO INFORMATIVO: GUÍA DE TRAMITACIÓN, DOCUMENTACIÓN Y MARCO LEGAL")
    r_anexo.bold = True
    r_anexo.font.size = Pt(13)
    r_anexo.font.color.rgb = RGBColor(0x02, 0x84, 0xC7)

    p_tram = doc.add_paragraph()
    p_tram.add_run("A) Procedimiento de Tramitación Integral (Llave en mano por Altera):\n").bold = True
    p_tram.add_run(
        "1. Presentación telemática oficial (Coste 0 €): Altera redacta íntegramente la Memoria Oficial (Formulario III) "
        "y acompaña a la clínica en la presentación en la sede de la JCCM con certificado digital. Queda fijado el número de registro "
        "y asegurada la reserva de fondos de los 9.000.000 €.\n"
        "2. Inicio inmediato del proyecto: Conforme al art. 10.2 de la Orden 116/2026, con el resguardo telemático de entrada ya se "
        "puede comenzar a ejecutar el proyecto legalmente (no hay que esperar 6 meses a la resolución).\n"
        f"3. Facturación e implantación: Altera despliega todas las soluciones y emite factura por 3.000,00 € + IVA. "
        "La clínica abona la factura por transferencia bancaria (el IVA es deducible al 100% en la declaración trimestral).\n"
        f"4. Reembolso directo de la Junta: Altera elabora la memoria final de justificación técnica (Formulario V). "
        f"La Junta transfiere directamente a la cuenta corriente de la clínica el 80% ({subvencion_80:,.2f} €). "
        f"El coste neto definitivo asumido por Sonrisastar es de únicamente {aportacion_20:,.2f} €.\n"
    )

    p_docs = doc.add_paragraph()
    p_docs.add_run("B) Documentación Necesaria de la Clínica Solicitante:\n").bold = True
    p_docs.add_run(
        "• NIF/DNI del titular o representante legal de Clínica Dental Sonrisastar.\n"
        "• Certificado digital para firma telemática en sede electrónica de la JCCM.\n"
        "• Certificados tributarios de estar al corriente con AEAT, Seguridad Social y Tributos de CLM (o autorización de consulta telemática).\n"
        "• Certificado bancario acreditativo de la titularidad de la cuenta corriente (IBAN) para el abono de la subvención.\n"
    )

    p_ley = doc.add_paragraph()
    p_ley.add_run("C) Marco Normativo y Referencias Oficiales de la Convocatoria:\n").bold = True
    p_ley.add_run(
        "• Bases Reguladoras: Orden 116/2026, de 29 de julio (DOCM nº 149 de 03/08/2026).\n"
        "• Código SIACI oficial del trámite en la Junta de CLM: 1023976.\n"
        "• Procedimiento: Concesión directa y simplificada (NO competitiva) por riguroso orden de registro de entrada.\n"
        "• Enlace oficial de descarga del DOCM: https://docm.castillalamancha.es/portaldocm/descargarArchivo.do?ruta=2026/08/03/pdf/2026_5787.pdf&tipo=rutaDocm\n"
        "• Enlace oficial al trámite en Sede Electrónica JCCM: https://www.jccm.es/tramites/1023976\n"
    )

    doc.save(output_path)
    print(f"Documento oficial Formulario III generado con éxito en:\n{output_path}")
    return True

if __name__ == "__main__":
    generar_formulario_iii_dental()

# Brief de Proyecto: Altera_Dental — Transformación Digital & IA Integral
## Clínica Dental Sonrisastar (Albacete)

**Para:** Claude Code / Antigravity (Sesión de diseño y desarrollo de propuesta)  
**De:** José Miguel Olmeda Pascual (Altera)  
**Fecha:** Octubre 2026  
**Cliente Objetivo:** Clínica Dental Sonrisastar (Dionisio Guardiola, 2, 02002 Albacete)  
**Web actual:** [https://sonrisastar.com/](https://sonrisastar.com/)  
**Marco de Financiación:** Subvención Bono Crecimiento Pyme — JCCM (Orden 116/2026, 80% a fondo perdido)

---

## 1. Resumen Ejecutivo & Contexto del Negocio

**Clínica Dental Sonrisastar** es una clínica odontológica consolidada en el centro de Albacete (c/ Dionisio Guardiola, 2), que ofrece tratamientos integrales: odontología general, ortodoncia (tradicional e invisible), implantes dentales, blanqueamiento, prótesis y estética dental.

A diferencia del modelo de consultorio puramente online (como FitFusion o Adela Fisio), Sonrisastar es un **negocio sanitario local y presencial de alto valor**. Su rentabilidad depende de:
1. La ocupación de sus sillones odontológicos durante la jornada.
2. La captación continua de nuevos pacientes para tratamientos de ticket medio/alto (implantes, ortodoncia, estética).
3. La retención y reactivación sistemática de su base histórica de pacientes (limpiezas semestrales, revisiones anuales).
4. La tasa de asistencia (reducir a cero el "no-show" o citas fallidas).

### Los 5 Cuellos de Botella Críticos Detectados en Sonrisastar:

1. **Llamadas y citas perdidas fuera de horario:**  
   El horario físico es de lunes a viernes (10:00 a 14:00 y 17:00 a 21:00). Todos los pacientes con urgencias dentales o que buscan dentista a mediodía, noches o fines de semana encuentran la clínica cerrada y llaman a la competencia.
2. **Recepción física sobrecargada:**  
   El personal de recepción compagina la atención presencial, cobros, presupuestos y desinfección con el teléfono. En horas punta, las llamadas comunican o no se atienden a tiempo.
3. **El freno de disponer únicamente de un teléfono fijo (`967 116 136`):**  
   No disponen de línea móvil ni WhatsApp oficial. Para el paciente actual (especialmente menores de 50 años), no poder escribir por WhatsApp, no poder enviar fotos de una pieza rota o una urgencia, ni recibir recordatorios interactivos es una barrera de entrada crítica que resta decenas de citas mensuales.
4. **Web desactualizada (WordPress 2015 con Visual Composer):**  
   Su web actual (`sonrisastar.com`) tiene más de 10 años de desfase tecnológico: carga lenta en móviles, maquetación pesada, sin botón directo ni flujo de agendamiento por WhatsApp, y sin formularios interactivos que guíen al paciente a reservar su primera cita con revisión y diagnóstico gratis.
5. **Inexistencia de presencia en Instagram (Oportunidad Desaprovechada):**  
   Tras auditar su huella digital, se constata que Sonrisastar **no tiene perfil de Instagram activo** (o está completamente inerte y no indexado). En un sector donde la estética dental (blanqueamientos, ortodoncia invisible, carillas) se vende por impacto visual, no estar en Instagram regala el 100% de la demanda local a clínicas competidoras.
6. **No-Shows y falta de reactivación activa:**  
   Las ausencias a citas dentales programadas dejan huecos muertos de 45-60 minutos de sillón y doctor. No disponen de un sistema automático por WhatsApp que confirme la cita 24h antes ni que recuerde revisiones a los 6 meses del último tratamiento.

---

## 2. Alcance del Proyecto Altera_Dental

Altera no ofrece un simple software, sino una **Solución Integral Llave en Mano** compuesta por 6 pilares sinérgicos:

### Pilar 1: Recepcionista Telefónica con Voz IA 24/7 (ElevenLabs Conversational AI)
- **Atención telefónica al teléfono fijo de la clínica (`967 116 136`):** Desvío inteligente en horarios fuera de consulta o por saturación de línea.
- **Voz ultra-realista española:** Trato cercano, profesional y sanitario con timbre humano.
- **Triaje de urgencias dentales:** Diferencia entre urgencia con dolor agudo (prioridad inmediata en agenda) y citas ordinarias (limpieza, revisión, información de presupuestos).
- **Agendamiento y confirmación instantánea:** Consulta disponibilidad en la agenda del CRM, agenda la cita y envía un WhatsApp automático al paciente con fecha, hora y ubicación en Google Maps.

### Pilar 2: Agente Omnicanal WhatsApp + Instagram (Integración con Zernio)
- **WhatsApp Oficial 24/7:** Atención en caliente para agendar citas, responder dudas sobre tratamientos (cuánto dura una ortodoncia, cómo funciona el blanqueamiento, facilidades de financiación).
- **Integración con Instagram Direct vía Zernio:** Cualquier persona que pregunte por un post o envíe un mensaje directo a `@sonrisastar` es atendida al instante por el mismo bot inteligente, guiándola al cierre de cita en clínica.
- **Presentación de servicios de alto ticket:** Envío de explicaciones interactivas y casos de éxito de implantes y ortodoncia invisible.

### Pilar 3: Automatización de Flujos & Fidelización Anti-No-Show
- **Recordatorio 24h Anti-No-Show con botón interactivo:** WhatsApp automático un día antes de la cita. Con un solo clic ("✅ Confirmo" o "🔄 Reagendar"), optimiza la agenda. Si cancela con antelación, el hueco se ofrece a la lista de espera.
- **Seguimiento post-intervención automático:** Envío de mensaje personalizado 24h después de una cirugía, empaste o endodoncia: *"Hola Carmen, ¿cómo va esa molestia tras la intervención de ayer? Recuerda seguir las pautas que te dio el doctor..."*.
- **Motor de reactivación periódica (Re-calling):** A los 6 o 10 meses de la última visita, el sistema contacta de forma natural para agendar la limpieza o revisión anual preventiva.

### Pilar 4: Rediseño Web Corporativa + UX de Alta Conversión (Skill Frontend)
- **Renovación total sobre stack moderno:** Eliminación del WordPress monolítico antiguo por una landing ultra-rápida, responsive y mobile-first con Tailwind CSS / HTML5 limpio y micro-interacciones.
- **Enfoque de captación:** Oferta gancho clara ("Primera Consulta, Diagnóstico y Radiografía Digital GRATIS"), selectores visuales de tratamientos, testimonios verificados, casos de éxito antes/después y CTAs flotantes directos a WhatsApp y llamada.
- **Carga instantánea (< 1 segundo en móvil):** Máxima puntuación en Google Core Web Vitals.

### Pilar 5: Posicionamiento SEO Local & AEO (Artificial Intelligence Engine Optimization)
- **SEO Local Albacete:** Optimización técnica y de contenido para términos clave: *"dentista albacete"*, *"implantes dentales albacete"*, *"ortodoncia invisible albacete"*, *"urgencias dentales albacete"*.
- **Optimización Google Business Profile (Ficha Google Maps):** Flujo automatizado por WhatsApp que invita a pacientes satisfechos tras su visita a dejar una reseña de 5 estrellas en Google con un enlace directo.
- **Optimización AEO:** Estructura semántica de datos (Schema.org Dentists/MedicalBusiness) para que motores de IA (ChatGPT Search, Perplexity, Google Gemini) recomienden Sonrisastar como clínica dental de referencia en Albacete.

### Pilar 6: Panel de Gestión CRM Dental a Medida
- **Pipeline Kanban visual omnicanal:** Columnas de estado (`Lead Nuevo`, `En Conversación WhatsApp/IG`, `Cita Agendada`, `Asistido / Presupuesto`, `Tratamiento Activo`, `Reactivación`).
- **Insignias de origen:** Identificación inmediata del canal (Teléfono ElevenLabs, WhatsApp, Instagram Zernio, Web).
- **Ficha clínica básica del paciente:** Datos de contacto, historial de citas, notas privadas del doctor/higienista (protegidas por candado y RLS) y estado del presupuesto.
- **Cuadro de Mandos (Dashboard de KPIs):** Tasa de ocupación, citas concertadas por canal, pacientes reactivados y valor estimado de tratamientos presupuestados.

---

## 3. Infraestructura Técnica & Aislamiento (100% Independiente)

Siguiendo el estándar de seguridad y privacidad de Altera:

- **VPS dedicado en Contabo (Alemania / UE):** Infraestructura completamente aislada para la clínica dental. No comparte servidor, recursos ni datos con ningún otro cliente ni proyecto de Altera.
- **Coolify como orquestador self-hosted:** Gestión de contenedores Docker de forma autónoma y segura en el servidor del cliente.
- **Supabase Autoalojado (Self-Hosted Postgres + Auth + RLS + Storage):**
  - Cero costes de suscripciones mensuales recurrentes a Supabase Cloud.
  - Base de datos relacional PostgreSQL con políticas RLS (Row Level Security).
  - Almacenamiento seguro para fichas o documentación clínica.
- **Zernio:** Orquestador y pasarela API para WhatsApp Business e Instagram Messaging.
- **ElevenLabs Conversational AI + OpenRouter:** Cerebro de procesamiento de voz y razonamiento de lenguaje natural sanitario.
- **Monitorización externa (HetrixTools):** Vigila uptime (24/7), uso de memoria, CPU y estado del VPS desde la cuenta técnica de Altera, garantizando alta disponibilidad sin trabajo para el cliente.

---

## 4. Privacidad y RGPD Sanitario (Art. 9 RGPD & Ley 41/2002)

El tratamiento de datos odontológicos exige el máximo rigor normativo desde el primer momento:

1. **Datos de Categoría Especial (Art. 9 RGPD):**  
   Cualquier diagnóstico bucodental, historial de salud médica, alergias o radiografías requiere **consentimiento explícito, informado y separado** previo a su almacenamiento.
2. **Plazo de Conservación de Documentación Clínica (Ley 41/2002):**  
   La historia clínica dental debe conservarse un **mínimo legal de 5 años** desde la fecha del alta del último proceso asistencial. El sistema diferencia nítidamente entre:
   - *Lead comercial no convertido* (sometido a plazos estándar de supresión/anonimización).
   - *Paciente con historia clínica* (bloqueado legalmente para cumplir el periodo de 5 años obligatorio).
3. **Control de Acceso Estricto (RLS):**  
   Solo el personal clínico autorizado accede a los datos de salud de los expedientes. Las notas clínicas privadas nunca son expuestas públicamente.
4. **Soberanía y Ubicación de Datos en la UE:**  
   Servidor ubicado en territorio de la Unión Europea (Alemania) con cifrado en tránsito (TLS/HTTPS) y en reposo.
5. **Registro de Actividades de Tratamiento (RAT) & Contratos de Encargo (DPA):**  
   Altera figura como encargado de tratamiento de la infraestructura técnica y aporta la documentación de cumplimiento lista para firmar.

---

## 5. El Gran Argumento Comercial: Subvención Junta de Castilla-La Mancha (Bono Crecimiento Pyme)

Este es el **factor decisivo de cierre de venta**: el cliente no asume el coste a pulmón.

### Ficha Técnica de la Subvención:
- **Programa:** Bono Crecimiento Pyme — Modalidad Transformación Digital.
- **Organismo:** Junta de Comunidades de Castilla-La Mancha (Consejería de Economía, Empresas y Empleo).
- **Normativa:** Orden 116/2026 (DOCM 03/08/2026).
- **Código Trámite Sede Electrónica:** **1023976**.
- **Tipo de Procedimiento:** **Concesión DIRECTA / SIMPLIFICADA (NO COMPETITIVA)**. Se aprueban y adjudican por estricto orden de entrada en el registro telemático hasta agotar los 9.000.000 € de dotación presupuestaria.
- **Intensidad de la ayuda:** **80% a fondo perdido** (hasta un máximo de 12.000 € de ayuda neta).

### Ventajas Competitivas para Altera & el Cliente:
1. **El cliente solo abona 600 € netos de inversión real:**  
   - **Inversión total del proyecto:** **3.000 €** (+ IVA deducible).  
   - **Subvención neta concedida JCCM (80% a fondo perdido):** **2.400 €**.  
   - **Coste real final asumido por la clínica:** **600 €** (un retorno de inversión inmediato con apenas 1 o 2 tratamientos de ortodoncia o implantes).
2. **Encaje 100% oficial en los conceptos subvencionables:**
   - Asistente de IA y chatbot de WhatsApp (expresamente contemplado en Modalidad 4 de la Orden).
   - Automatización de procesos de citas y recordatorios.
   - CRM e integración de canales comerciales.
   - Rediseño web UX y arquitectura digital.
3. **Sin burocracia de tres presupuestos:** Al tratarse de un contrato de prestación de servicios de 3.000 € (muy inferior al umbral de contrato menor de 15.000 €), no se requiere presentar 3 ofertas comparativas de competidores.
4. **Altera como Proveedor Tecnológico Directo:** Cero exigencias de años de antigüedad o intermediarios.
5. **Llave en Mano Oficial (Formulario III):** Altera entrega la **Memoria Técnica Oficial (Formulario III)** redactada al detalle, justificando la necesidad, objetivos, impacto digital y cronograma de ejecución a 3 meses, junto al presupuesto pro-forma.

---

## 6. Fases de Ejecución del Proyecto

```
┌────────────────────────────────────────────────────────┐
│ FASE 1: PRESENTACIÓN AL CLIENTE & TRÁMITE JCCM (Sem 1) │
│ • Dossier de propuesta interactivo y mockups           │
│ • Entrega de Formulario III cumplimentado + Presupuesto│
│ • Registro telemático de la solicitud en la JCCM       │
└───────────────────────────┬────────────────────────────┘
                            │ (Efecto incentivador cubierto)
                            ▼
┌────────────────────────────────────────────────────────┐
│ FASE 2: INFRAESTRUCTURA & CANALES 24/7 (Semanas 2-4)   │
│ • Aprovisionamiento de VPS Contabo + Coolify + Supabase│
│ • Configuración de Recepcionista de Voz (ElevenLabs)   │
│ • Conexión de Zernio (WhatsApp Oficial + Instagram)    │
│ • Automatización de recordatorios Anti-No-Show         │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ FASE 3: REDISEÑO WEB, CRM & SEO LOCAL (Semanas 5-8)    │
│ • Nueva web corporativa ultrarrápida (Tailwind/HTML5)  │
│ • Puesta en marcha del CRM Dental con pipeline Kanban  │
│ • Optimización SEO Local Albacete + Google Business    │
│ • Campaña de reactivación de pacientes inactivos       │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ FASE 4: JUSTIFICACIÓN DE LA AYUDA & SOPORTE (Mes 3-6)  │
│ • Emisión de facturas y memoria económica final        │
│ • Justificación ante la JCCM para cobro del 80%        │
│ • Mantenimiento preventivo, backups y monitorización   │
└────────────────────────────────────────────────────────┘
```

---

## 7. Claves de la Visita Comercial & Puntos a Validar

1. **El argumento de oro (Inversión 3.000 € · Coste Real 600 €):**  
   Presentar la propuesta como una oportunidad única financiada al 80% por el **Bono Crecimiento Pyme de la Junta de Comunidades de Castilla-La Mancha** (Orden 116/2026). Altera entrega el Formulario III listo para registrar. Por solo **600 € netos**, modernizan toda su infraestructura de captación y atención.
2. **El cuello de botella del teléfono fijo:**  
   Demostrar al cliente cómo depender exclusivamente del `967 116 136` está ahogando la entrada de nuevos pacientes jóvenes y cómo habilitar una línea móvil oficial de WhatsApp conectada con Zernio multiplicará sus primeras citas.
3. **El canal de Instagram (Creación & Automatización):**  
   Aprovechar que Sonrisastar no tiene presencia activa en Instagram para proponerles la activación de su canal oficial con galería visual de tratamientos y respuesta automática por DM con Zernio.
4. **Software dental y sincronización de agenda:**  
   Se preguntará en la visita comercial qué programa utilizan en clínica (Gesden, DentalSoft, Google Calendar, etc.) para conectar los agentes vía webhook o implantar directamente el CRM de Altera.
5. **Oferta gancho confirmada:**  
   Se mantendrá en toda la comunicación la oferta estrella de *"Primera Consulta, Diagnóstico y Radiografía Digital GRATIS"*, maximizando la conversión de visitantes a pacientes en sillón.

---

**Conclusión:**  
Este brief adapta el ecosistema tecnológico probado de Altera al sector dental presencial, combinando recepcionista por voz de vanguardia, automatización multicanal y una palanca comercial insuperable: el **Bono Crecimiento Pyme de Castilla-La Mancha (80% subvencionado)** con la Memoria Técnica Formulario III lista para registrar por un importe total de 3.000 € (coste real para la clínica: 600 €).

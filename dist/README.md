# Herramienta de Tiering de Soluciones Analíticas
## Versión Ejecutable v2.1

### 📋 Descripción
Esta es la versión ejecutable de la Herramienta de Tiering de Soluciones Analíticas de Bancolombia. Permite evaluar soluciones analíticas según la metodología v2.1 de la Gerencia de Riesgo de Modelos.

### 🚀 Instrucciones de Uso

#### Ejecución Simple
1. **Ubicar el ejecutable**: Localice el archivo `TieringApp-Bancolombia.exe`
2. **Ejecutar**: Haga doble clic en el archivo o ejecute desde terminal:
   ```
   .\TieringApp-Bancolombia.exe
   ```
3. **Acceso automático**: La aplicación se abrirá automáticamente en su navegador predeterminado
4. **URL manual**: Si no se abre automáticamente, vaya a: `http://localhost:5000`

#### Cierre de la Aplicación
- **Método 1**: Cierre la ventana de consola que aparece al ejecutar el .exe
- **Método 2**: Presione `Ctrl+C` en la ventana de consola
- **Método 3**: Cierre desde el Administrador de Tareas si es necesario

### 🔧 Características Implementadas

#### ✅ Mejoras de Rendimiento
- **Debouncing**: Optimización de cálculos con retraso de 300ms
- **Validación avanzada**: Sanitización de inputs y validación en tiempo real
- **Auto-guardado**: Guardado automático de borradores cada 2 segundos
- **Manejo de errores**: Control de excepciones y notificaciones usuario-amigables

#### ✅ Funcionalidades Principales
- **Evaluación de Tiering**: Sistema completo de evaluación en 6 criterios
- **Taxonomía Automática**: Asignación automática de complejidad según nivel
- **Gestión de Evaluaciones**: Guardar, cargar, editar y eliminar evaluaciones
- **Exportación**: Generación de PDF y exportación a CSV
- **Base de Datos**: Importar/exportar base completa de evaluaciones

#### ✅ Accesibilidad y UX
- **Tooltips informativos**: Ayuda contextual en todos los criterios
- **Navegación intuitiva**: Interfaz responsive y fácil de usar
- **Notificaciones**: Sistema de toasts para feedback inmediato
- **Indicadores visuales**: Estados claros de guardado y validación

### 🛡️ Seguridad
- **Código protegido**: El HTML y JavaScript están encapsulados en el ejecutable
- **Validación robusta**: Prevención de inyección de scripts maliciosos
- **Sanitización**: Limpieza automática de inputs del usuario
- **Almacenamiento local**: Datos guardados localmente en localStorage del navegador

### 📊 Metodología v2.1
- **Dimensión 1 (40%)**: Complejidad e Incertidumbre
  - Complejidad Algorítmica (Automático)
  - Opacidad y Explicabilidad (Automático)
  - Grado de Autonomía (Manual)

- **Dimensión 2 (60%)**: Impacto y Criticidad
  - Impacto Económico (Manual)
  - Impacto Operacional (Manual)
  - Impacto Reputacional y Ético (Manual)

### 🎯 Clasificación de Tiers
- **Tier 1**: Puntuación > 2.75 (Alto Riesgo)
- **Tier 2**: Puntuación 1.76 - 2.75 (Riesgo Moderado)
- **Tier 3**: Puntuación ≤ 1.75 (Bajo Riesgo)

### 📝 Notas Técnicas
- **Tecnología**: Flask + PyInstaller
- **Compatibilidad**: Windows 10/11 (64-bit)
- **Dependencias**: Todas incluidas en el ejecutable
- **Tamaño**: ~25 MB aproximadamente
- **Puerto**: Se asigna automáticamente (por defecto 5000)

### 🔍 Solución de Problemas

#### El ejecutable no inicia
- Verifique que no haya otro proceso usando el puerto 5000
- Ejecute como administrador si es necesario
- Verifique que Windows Defender no esté bloqueando el archivo

#### No se abre el navegador automáticamente
- Abra manualmente: `http://localhost:5000`
- Verifique la ventana de consola para el puerto correcto
- Pruebe con diferentes navegadores

#### Problemas de rendimiento
- Cierre otros programas que consuman mucha memoria
- Verifique que haya al menos 1GB de RAM disponible
- Reinicie el ejecutable si se vuelve lento

### 📞 Soporte
Para soporte técnico o reportar problemas, contacte a la Gerencia de Riesgo de Modelos de Bancolombia.

---
**Gerencia de Riesgo de Modelos - Grupo Bancolombia**  
*Herramienta Interactiva de Tiering v2.1*
*riesgodemodelos@bancolombia.com.co*
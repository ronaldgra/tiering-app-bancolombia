# 🏦 Herramienta de Tiering de Soluciones Analíticas

## 📋 Descripción

Aplicación web profesional para evaluar y clasificar soluciones analíticas según su nivel de riesgo, implementando la metodología v2.1 de la Gerencia de Riesgo de Modelos de Grupo Bancolombia.

## ✨ Características Principales

- **Sistema de Tiering Completo**: Evaluación basada en 6 criterios estructurados
- **Taxonomía Inteligente**: Asignación automática de complejidad algorítmica (L0-L5)
- **Gestión de Evaluaciones**: CRUD completo con persistencia local
- **Exportación Avanzada**: Generación de reportes PDF profesionales y CSV
- **Interfaz Moderna**: UI responsive con Tailwind CSS
- **Auto-guardado**: Sistema automático de respaldo cada 2 segundos
- **Aplicación Portable**: Ejecutable independiente sin instalación (8.24 MB)

## 🚀 Instalación y Uso

### Opción 1: Ejecutable (Recomendado para usuarios finales)

1. Descargar `TieringApp-Bancolombia.exe` desde [Releases](../../releases)
2. Ejecutar el archivo .exe
3. Se abrirá automáticamente en el navegador en `http://localhost:5000`

### Opción 2: Desarrollo Local

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/tiering-app-bancolombia.git
cd tiering-app-bancolombia

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

### Opción 3: Generar Ejecutable

```bash
# Ejecutar script de construcción
.\build.bat  # Windows
```

## 📊 Metodología de Tiering

### Dimensiones de Evaluación

**Dimensión 1: Complejidad e Incertidumbre (40%)**
- **Complejidad Algorítmica** (automático por taxonomía)
- **Opacidad y Explicabilidad** (automático por taxonomía)  
- **Grado de Autonomía** (evaluación manual)

**Dimensión 2: Impacto y Criticidad (60%)**
- **Impacto Económico** (evaluación manual)
- **Impacto Operacional** (evaluación manual)
- **Impacto Reputacional y Ético** (evaluación manual)

### Taxonomía de Soluciones

| Nivel | Tipo | Descripción | Complejidad | Explicabilidad |
|-------|------|-------------|-------------|----------------|
| L0 | Cómputo | Cálculos directos sin lógica decisional | 1 | 1 |
| L1 | Experto | Reglas y árboles de decisión definidos | 1 | 1 |
| L2 | Tradicional | Modelos estadísticos/econométricos | 2 | 2 |
| L3 | ML | Algoritmos de aprendizaje automático | 3 | 3 |
| L4 | GenAI | Modelos generativos a gran escala | 4 | 4 |
| L5 | Híbrida | Sistemas que combinan múltiples niveles | 4 | 4 |

### Clasificación de Resultados

- **Tier 1**: Puntuación > 2.75 - **Alto riesgo** 🔴
- **Tier 2**: Puntuación 1.75-2.75 - **Riesgo moderado** 🟡  
- **Tier 3**: Puntuación < 1.75 - **Bajo riesgo** 🟢

## 🏗️ Arquitectura Técnica

```
tiering_app/
├── app.py                      # Servidor Flask
├── requirements.txt            # Dependencias Python
├── build.bat                  # Script de construcción PyInstaller
├── TieringApp-Bancolombia.spec # Configuración PyInstaller
├── templates/
│   └── index.html             # Aplicación web completa (940 líneas)
├── static/                    # Recursos estáticos
├── dist/                      # Ejecutables generados
│   ├── TieringApp-Bancolombia.exe
│   └── README.md
├── build/                     # Archivos temporales PyInstaller
└── venv/                      # Entorno virtual Python
```

## 🔧 Tecnologías Utilizadas

### Backend
- **Python 3.9+**
- **Flask 2.3.3** - Framework web
- **PyInstaller 6.2.0** - Empaquetado ejecutable

### Frontend
- **HTML5, CSS3, JavaScript ES6**
- **Tailwind CSS** - Framework UI
- **Chart.js** - Gráficos radar interactivos
- **jsPDF + html2canvas** - Generación PDF

### Librerías CDN
- Tailwind CSS
- Chart.js
- html2canvas
- jsPDF

## 📦 Dependencias

```txt
Flask==2.3.3
Werkzeug==2.3.7
pyinstaller==6.2.0
Jinja2==3.1.2
MarkupSafe==2.1.3
itsdangerous==2.1.2
click==8.1.7
blinker==1.6.3
```

## 🔒 Características de Seguridad

- ✅ **Sanitización de inputs** contra ataques XSS
- ✅ **Validación robusta** de formularios en tiempo real
- ✅ **Servidor local** sin exposición externa
- ✅ **Código fuente protegido** en ejecutable
- ✅ **Manejo seguro** de localStorage del navegador
- ✅ **Detección automática** de puertos disponibles

## 🎯 Funcionalidades Implementadas

### ✅ Core Features
- Sistema completo de evaluación de tiering
- Taxonomía automática L0-L5
- Gestión completa de evaluaciones (CRUD)
- Persistencia local con localStorage
- Auto-guardado inteligente cada 2 segundos

### ✅ Exportación y Reportes
- Generación de PDF profesional con logo Bancolombia
- Exportación a CSV estructurado
- Gráfico radar de perfil de riesgo
- Exportar/importar base de datos completa

### ✅ UX/UI Avanzada
- Interfaz moderna responsive
- Tooltips informativos en todos los criterios
- Sistema de notificaciones toast
- Indicadores visuales de estado
- Navegación intuitiva con debouncing (300ms)

### ✅ Optimizaciones de Rendimiento
- Debouncing en cálculos automáticos
- Validación asíncrona de campos
- Carga optimizada de dependencias
- Manejo eficiente de memoria

## 📈 Roadmap

### v2.2 (Próxima versión)
- [ ] Sistema de autenticación básico
- [ ] Base de datos SQLite local
- [ ] Historial de cambios en evaluaciones
- [ ] Exportación a Excel nativo

### v3.0 (Futuro)
- [ ] Interfaz multi-idioma (ES/EN)
- [ ] Flujo de aprobación colaborativo
- [ ] API REST para integraciones
- [ ] Dashboard de analytics avanzado
- [ ] Integración con Active Directory

## 🛠️ Modificaciones y Desarrollo

### Archivo Principal
**`templates/index.html`** contiene toda la aplicación:
- HTML estructura completa
- CSS estilos (líneas 12-46)
- JavaScript lógica (líneas 141-940)

### Workflow de Desarrollo
1. Modificar `templates/index.html`
2. Probar con `python app.py`
3. Regenerar ejecutable con `.\build.bat`
4. Distribuir nueva versión

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

**Uso interno - Grupo Bancolombia**  
Todos los derechos reservados.

## 👨‍💻 Desarrollado por

**Gerencia de Riesgo de Modelos**  
Grupo Bancolombia  

**Versión**: v2.1.0  
**Fecha**: Julio 2025  
**Metodología**: Tiering v2.1  

---

*Para soporte técnico o consultas, contactar al equipo de Gerencia de Riesgo de Modelos.*

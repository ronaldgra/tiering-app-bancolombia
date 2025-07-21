#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta de Tiering de Soluciones Analíticas
Aplicación Desktop - Grupo Bancolombia
Versión: 2.1
"""

import os
import sys
import webbrowser
import threading
import time
import socket
from flask import Flask, render_template, send_from_directory, jsonify
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(level=logging.ERROR)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class TieringApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'tiering_app_bancolombia_2024'
        self.setup_routes()
        self.port = self.find_free_port()
        
    def find_free_port(self):
        """Encuentra un puerto libre para la aplicación"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            s.listen(1)
            port = s.getsockname()[1]
        return port
    
    def setup_routes(self):
        """Configura las rutas de la aplicación"""
        
        @self.app.route('/')
        def index():
            """Página principal de la aplicación"""
            return render_template('index.html')
        
        @self.app.route('/favicon.ico')
        def favicon():
            """Icono de la aplicación"""
            return send_from_directory(
                os.path.join(self.app.root_path, 'static'),
                'favicon.ico',
                mimetype='image/vnd.microsoft.icon'
            )
        
        @self.app.route('/health')
        def health():
            """Endpoint de salud para verificar que la app funciona"""
            return jsonify({
                'status': 'ok',
                'timestamp': datetime.now().isoformat(),
                'version': '2.1'
            })
        
        @self.app.errorhandler(404)
        def not_found(error):
            """Manejo de errores 404"""
            return render_template('index.html'), 200
    
    def open_browser(self):
        """Abre el navegador automáticamente"""
        url = f'http://localhost:{self.port}'
        print(f"🚀 Iniciando Herramienta de Tiering...")
        print(f"📊 Acceda a la aplicación en: {url}")
        print(f"🔒 Aplicación ejecutándose de forma segura")
        print(f"❌ Para cerrar, presione Ctrl+C en esta ventana")
        
        # Esperar un momento para que el servidor inicie
        time.sleep(1.5)
        
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"⚠️  No se pudo abrir el navegador automáticamente: {e}")
            print(f"   Abra manualmente: {url}")
    
    def run(self):
        """Ejecuta la aplicación"""
        # Abrir navegador en un hilo separado
        threading.Thread(target=self.open_browser, daemon=True).start()
        
        try:
            # Ejecutar la aplicación Flask
            self.app.run(
                host='127.0.0.1',
                port=self.port,
                debug=False,
                use_reloader=False,
                threaded=True
            )
        except KeyboardInterrupt:
            print("\n🛑 Aplicación cerrada por el usuario")
        except Exception as e:
            print(f"❌ Error al ejecutar la aplicación: {e}")
            input("Presione Enter para cerrar...")

def main():
    """Función principal"""
    try:
        app = TieringApp()
        app.run()
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        input("Presione Enter para cerrar...")

if __name__ == '__main__':
    main()

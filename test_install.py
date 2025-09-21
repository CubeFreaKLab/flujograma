#!/usr/bin/env python
"""Test de instalación del paquete flujograma"""

try:
    from flujograma.diagrams_api import Diagram, ELB, EC2, RDS
    print("✅ Importación exitosa")
    
    with Diagram("Test Install", filename="test_install.png"):
        ELB("load-balancer") >> EC2("web-server") >> RDS("database")
    
    print("✅ Generación de diagrama exitosa")
    print("📄 Archivo generado: test_install.png")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
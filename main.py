from service.api import obtener_aves
from front.template import genera_template_html, exportar_html

def main():
    """
    Función principal que ejecuta el programa
    
    """
    url = 'https://aves.ninjas.cl/api/birds'
    datos = obtener_aves(url)

    if datos:
        html_content = genera_template_html(datos)
        exportar_html(html_content)

if __name__ == "__main__":
    main()
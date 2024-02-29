from string import Template

#Crear el Template a utilizar   
def genera_template_html(datos):
    """
    Genera una plantilla HTML con tarjetas Bootstrap

    :param datos: diccionario con la informacion
    :type datos: (dict)
    :return: str - una cadena con el contenido HTML
    """

    template_html = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aves Chilenas</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <style>
            body {
                background-color: #add8e6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="text-center">Aves de Chile</h1>
            <hr>

            <div class="row">
                $contenido_aves
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
    </html>
""")
    template_lista = Template("""   
        <div class="col-md-3">
            <div class="card mb-4">
                <img class="card-img-top" src="$img_url" alt="$nombre_esp" style="height:228px">
                <div class="card-body">
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">$nombre_esp</li>
                        <li class="list-group-item">$nombre_eng</li>
                    </ul>
                </div>
            </div>
        </div>
""")
    
    contenido_aves = '\n'.join([template_lista.substitute(
        nombre_esp=ave['name']['spanish'],
        nombre_eng=ave['name']['english'],
        img_url=ave['images']['main']
    ) for ave in datos])

    html = template_html.substitute(contenido_aves=contenido_aves)
    return html

def exportar_html(html_content, filename='aves_chilenas.html'):
    """
    Exporta el contenido HTML a un archivo

    :param html_content: El contenido HTML a exportar
    :type html_content: (str)
    :param filename:El nombre del archivo HTML "aves_chilenas.html"
    :type filename: (str)
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Sitio exportado como: '{filename}'")
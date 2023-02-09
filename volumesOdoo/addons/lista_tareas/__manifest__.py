# -*- coding: utf-8 -*-
{
    'name':'Lista de tareas',
    'summary': """Sencilla Lista de tareas""",
    'description':"""Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevomodelo de datos""",
    'author':"Omar Pastor",
    'website':"https://github.com/niffelheim87",

    # Indicamos que es una aplicación
    'application':True,

    # En la siguiente URL se indica qué categorías puedenusarse
    # https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # Vamos a utilizar la categoría Productivity
    'category':'Productivity',
    'version':'0.1',

    # Indicamos lista de módulos necesarios para queeste funcione correctamente 
    # En este ejemplo solo depende del módulo "base"
    'depends': ['base'],

    # Esto siempre se carga
    'data': [
    # Este primero indica la politica de acceso delmódulo
    'security/ir.model.access.csv',
    # Cargamos las vistas y las plantillas
    'views/views.xml',
    ]

    
}
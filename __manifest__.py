# -*- coding: utf-8 -*-
{
    'name': 'SXE2BernalMendez_Cristian',
    'version': '1.0',
    'category': 'Education',

    'summary': 'Gestión de notas de alumnos',


    'description': """
        Gestión de notas de alumnos
    """,

    'author': "Cristian Bernal",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'name': 'SXE2Tapellido_nombre',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestión de notas de alumnos',
    'depends': ['base'],
    'data': [
        'views/curso.xml',
        'views/ciclo.xml',
        'views/modulo.xml',
        'views/nota.xml',
        'views/menu.xml',
        'data/fp.modulo.csv',
        'data/fp.nota.csv',
    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

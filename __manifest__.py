# -*- coding: utf-8 -*-
{
    'name': "Open Academy",
    'summary': """
        Administración de estudiantes y cursos""",
    'description': """
        Módulo encargado de la administración de los estudiantes y los cursos.
        Se administra:
            - La lista de cursos que un estudiante puede tomar.
            - El cronograma de los cursos.
    """,
    'author': "Giancarlo Javier Paredes Urquieta",
    'website': "http://www.realmadrid.com",
    'license': "LGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Pruebas',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install': False,
    'application': True,
    'css': [

    ],
    'images': [

    ],
    'installable': False,
    'manteiner': 'Cristiano Ronaldo'
}
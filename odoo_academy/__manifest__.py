# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'depends': ['base'],
    'description': """
                    Academy Module to manage Trainning:
                    -Courses
                    -Sessions
                    -Attendees
    """,
    'category': 'Trainning',
    'data': [
        'views/course_views.xml',
        

    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    'application': True,

}


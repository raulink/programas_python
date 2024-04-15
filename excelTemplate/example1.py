# -*- coding: utf-8 -*-

import os
from datetime import datetime
from xlsxtpl.writerx import BookWriter


def write_test():
    pth = os.path.dirname(__file__)
    fname = os.path.join(pth, 'example.xlsx')
    writer = BookWriter(fname)
    writer.jinja_env.globals.update(dir=dir, getattr=getattr)

    now = datetime.now()

    person_info = {'address': u'Zona Mercedario B52B', 'name': u'Raul Mamani Cusi', 'fm': 1986, 'date': now}
    person_info2 = {'address': u'Cosmos 77. #35', 'name': u'Patricia Yujra Sanca', 'fm': 1985, 'date': now}
    rows = [['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
             ['1', '1', '1', '1', '1', '1', '1', '1', ],
            ]
    person_info['rows'] = rows
    person_info2['rows'] = rows
    payload0 = {'tpl_name': 'cn', 'sheet_name': u'Hoja 1',  'ctx': person_info}
    payload1 = {'tpl_name': 'en', 'sheet_name': u'Formulario2', 'ctx': person_info2}
    payload2 = {'tpl_idx': 2, 'ctx': person_info2}
    payloads = [payload0, payload1, payload2]
    writer.render_book2(payloads=payloads)
    fname = os.path.join(pth, 'result12.xlsx')
    writer.save(fname)
    payloads = [payload2, payload1, payload0]
    writer.render_book2(payloads=payloads)
    writer.render_sheet(person_info2, 'form2', 1)
    fname = os.path.join(pth, 'result13.xlsx')
    writer.save(fname)


if __name__ == "__main__":
    write_test()

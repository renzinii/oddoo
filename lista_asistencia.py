#-*- coding: utf-8 -*-
from openerp import models, fields, api
class ListaAsistencia(models.Model):
    _name = 'lista.asistencia'
    _inherit = ['lista.asistencia','mail.thread']
    user_id = fields.Many2one('res.users', 'Responsable: ')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="Introduce tu nombre y el primer apellido")
    @api.one
    def do_marcar(self):
        if self.user_id != self.env.user:
            raise Exception('Solo el responsable puede marcar como pagado')
        else:
            return super(ListaAsistencia, self).do_marcar()

    @api.multi
    def do_limpiar(self):
        domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True
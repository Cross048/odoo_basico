from odoo import api, models

class Report(models.AbstractModel):
    _name = 'report.sxetap.report'
    _description = 'Informe de Notas de Alumnos'

    @api.model
    def _get_report_values(self, docids, data=None):
        notas = self.env['sxetap.nota'].browse(docids)
        return {
            'docs': notas,
        }

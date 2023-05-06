import odoo
from odoo import fields, models


class AppointmentLetter(models.Model):
    _name = 'my_custom_module.appointment_letter'
    _description = 'Appointment Letter'

    employee_name = fields.Char(string='Employee Name')
    employee_id = fields.Char(string='Employee ID')
    date_of_joining = fields.Date(string='Date of Joining')
    department = fields.Many2one('my_custom_module.department', string='Department')
    designation = fields.Char(string='Designation')
    salary = fields.Float(string='Salary')

    content = fields.Text(string='Letter Content')

    #def print_letter(self):
        #  logic to generate/print the appointment letter here
        #pass

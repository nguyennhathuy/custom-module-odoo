from odoo import http
from odoo.http import request

class PowerBIController(http.Controller):
    @http.route('/powerbi_report', type='http', auth='user', website=True) # website=True nếu là trang web
    def show_powerbi_report(self, **kw):
        powerbi_url = request.env['ir.config_parameter'].sudo().get_param('powerbi_integration.report_url')
        if not powerbi_url:
            # Xử lý trường hợp URL chưa được cấu hình
            powerbi_url = "https://app.powerbi.com/view?r=yourDefaultLinkIfNoneSet" # Liên kết mặc định hoặc thông báo lỗi
        return request.render('powerbi_integration.PowerBiReportQWebPage', {'powerbi_url': powerbi_url})
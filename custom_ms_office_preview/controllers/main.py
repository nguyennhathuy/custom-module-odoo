import logging
from werkzeug.exceptions import NotFound
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class AttachmentPreviewController(http.Controller):

    @http.route("/preview-url/<int:attachment_id>", type="http", auth="public", cors="*")
    def public_guest_attachment(self, attachment_id, download=False, **kwargs):
        try:    
            # Todo: Implement a better way to handle guest_token

            attachment_sudo = request.env["ir.attachment"].sudo().browse(attachment_id)
            _logger.debug(f"✅ Guest env applied {attachment_sudo}")

            if not attachment_sudo.exists():
                raise NotFound()

            stream = request.env["ir.binary"]._get_stream_from(attachment_sudo)

            # stream = request.env['ir.binary']._get_stream_from(record, field, filename, filename_field, mimetype)

            stream.public = True  # Allow Microsoft Online Viewer to access the file

            return stream.get_response(as_attachment=bool(download))

        except Exception as e:
            _logger.exception(f"❌ Error serving attachment preview: {e}")
            raise NotFound()

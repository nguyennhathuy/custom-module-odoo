/** @odoo-module **/

import { Attachment } from "@mail/core/common/attachment_model";
import { patch } from "@web/core/utils/patch";
import { url } from "@web/core/utils/urls";


patch(Attachment.prototype, {
    get isMsOfficeDocument() {
        console.log("isMsOfficeDocument");
        const officeMimeTypes = [
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document", // .docx
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", // .xlsx
            "application/vnd.openxmlformats-officedocument.presentationml.presentation", // .pptx
            "application/msword", // .doc
            "application/vnd.ms-excel", // .xls
            "application/vnd.ms-powerpoint", // .ppt
        ];
        return officeMimeTypes.includes(this.mimetype);
    },

    get isViewable() {
        return super.isViewable || this.isMsOfficeDocument;
    },


    get urlRoute() {
        if (this.isMsOfficeDocument) {
            return `/preview-url/${this.id}`;
        }
        return super.urlRoute;
    },

    get defaultSource() {
        if (this.isMsOfficeDocument) {
            const route = url(this.urlRoute, this.urlQueryParams);
            const encodedRoute = encodeURIComponent(route);
            return `https://view.officeapps.live.com/op/embed.aspx?src=${encodedRoute}&wdStartOn=1&wdPrint=1&wdEmbedCode=0`;
        }
        return super.defaultSource;
    },
});

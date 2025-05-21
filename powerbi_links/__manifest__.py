# -*- coding: utf-8 -*-
{
    'name': "Power BI Links",  # Tên module, hiển thị cho người dùng [5, 6]
    'version': '18.0.1.0.0',   # Phiên bản module, nên theo semantic versioning [5, 6]
    'summary': "Manage and display public Power BI report links", # Mô tả ngắn gọn [6]
    'description': """
        This module allows users to store, manage, and easily access public Power BI report links
        directly within Odoo. It provides a centralized list of reports and an option
        to view them embedded in the Odoo interface.
    """,  # Mô tả chi tiết, có thể dùng reStructuredText [5, 6]
    'author': "Your Name/Company Name",  # Tên tác giả hoặc công ty [5, 6]
    'website': "https://www.yourwebsite.com",  # URL website của tác giả hoặc tài liệu module [6]
    'license': 'LGPL-3',  # Loại giấy phép, ví dụ: AGPL-3, LGPL-3, OEEL-1 [5, 6]
    'category': 'Productivity',  # Phân loại module, ví dụ: Sales, Inventory, Reporting [5, 6]
    'depends': ['base', 'web'],  # Danh sách các module phụ thuộc. 'base' gần như luôn cần thiết. 'web' cần nếu có tương tác giao diện web phức tạp hoặc assets. [5, 6]
    'data': [
        'security/powerbi_security.xml',
        'security/ir.model.access.csv',
        'views/powerbi_link_views.xml',
        'views/powerbi_link_menus.xml',
    ], # Danh sách các file XML, CSV được load. Thứ tự rất quan trọng. [5, 6, 7]
    'installable': True,  # True nếu module có thể cài đặt từ UI [5, 6]
    'application': True,  # True nếu module này là một ứng dụng chính, xuất hiện trong danh sách Apps [6]
    'auto_install': False, # True nếu muốn module tự động cài đặt khi tất cả dependencies được đáp ứng [5, 6]
}
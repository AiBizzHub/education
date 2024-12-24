# Copyright (c) 2020, AiBizzHub, LLC and Contributors
# License: GNU General Public License v3. See license.txt

from frappe import _


def get_data():
	return {
		"fieldname": "course_schedule",
		"transactions": [{"label": _("Attendance"), "items": ["Student Attendance"]}],
	}

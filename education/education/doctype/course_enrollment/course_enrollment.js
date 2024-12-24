// Copyright (c) 2018, AiBizzHub, LLC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Course Enrollment', {
	onload: function(frm) {
		frm.set_query('course', function() {
			return {
				query: 'education.education.doctype.program_enrollment.program_enrollment.get_program_courses',
				filters: {
					'program': frm.doc.program
				}
			};
		});
	}
});

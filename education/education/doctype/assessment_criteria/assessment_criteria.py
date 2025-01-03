# Copyright (c) 2015, AiBizzHub, LLC and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document

STD_CRITERIA = [
	"total",
	"total score",
	"total grade",
	"maximum score",
	"score",
	"grade",
]


class AssessmentCriteria(Document):
	def validate(self):
		if self.assessment_criteria.lower() in STD_CRITERIA:
			frappe.throw(_("Can't create standard criteria. Please rename the criteria"))

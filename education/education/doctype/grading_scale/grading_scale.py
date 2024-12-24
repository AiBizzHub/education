# Copyright (c) 2015, AiBizzHub, LLC and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cint


class GradingScale(Document):
	def validate(self):
		thresholds = []
		for d in self.intervals:
			if d.threshold in thresholds:
				frappe.throw(_("Treshold {0}% appears more than once").format(d.threshold))
			else:
				thresholds.append(cint(d.threshold))
		if 0 not in thresholds:
			frappe.throw(_("Please define grade for Threshold 0%"))
# -*- coding: utf-8 -*-
# Copyright (c) 2015, taher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import string 
import random
from frappe.model.document import Document

class Voucher(Document):
	def validate(self):
		size= 6
		chars= string.ascii_uppercase + string.digits
		self.code = ''.join(random.choice(chars) for _ in range(size))
		vc = frappe.new_doc("Voucher balance table")
		vc.code = self.code
		vc.remaining_amount = self.amount
		vc.insert(ignore_permissions=True)
		vc.save()

def on_voucher_apply(doc,method):
	voucher_list =frappe.db.sql("select code from `tabVoucher balance table`",as_list=1)
	vl= [x[0] for x in voucher_list]
	frappe.errprint([voucher_list,vl])

	if doc.voucher != "0":
		frappe.errprint("not zero")
		if doc.voucher in vl:
			vou= frappe.get_doc("Voucher balance table", doc.voucher)
			balance= vou.remaining_amount
			if balance != 0:
				frappe.errprint("balance there")
				if doc.total >= vou.remaining_amount:
					doc.total =int(doc.total) - int(vou.remaining_amount)
					vou.remaining_amount = 0
					vou.save()
				else:
					frappe.errprint("voucher has more")
					doc.discount_amount = doc.total
					doc.total = 0
					doc.grand_total =0

					vou.remaining_amount = int(vou.remaining_amount) - int(doc.total)
					vou.insert()
					vou.save()
			else:
				frappe.msgprint("no Balance in voucher")
		else:
			frappe.msgprint("invalid voucher")




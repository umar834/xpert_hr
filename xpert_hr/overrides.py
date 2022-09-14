import frappe
from erpnext.stock.doctype.item.item import Item


class CustomItem(Item):
	def custom_fun(self):
		frappe.throw('not possible')

# Returns technical attributes that belong to the technical attribute group that is provided
@frappe.whitelist()
def get_tech_attrs_based_on_group(group_name=None):
    if group_name:
        query = """select *
				from `tabTechnical Attribute Group Items`
				where parent=%s"""
        tech_attrs = frappe.db.sql(query,(group_name),as_dict=1)
        attrs_list = list()
        if tech_attrs:
            for tech_attr in tech_attrs:
                if tech_attr.technical_attribute:
                    query = """select *
                        from `tabTechnical Attribute Value`
                        where parent=%s"""
                    techinical_attr = frappe.db.sql(query,(tech_attr.technical_attribute),as_dict=1)
                    new_record = {'attribute_name': tech_attr.technical_attribute, 'attribute_values': techinical_attr}
                    attrs_list.append(new_record)
        return attrs_list
    else:
        return 0
	    
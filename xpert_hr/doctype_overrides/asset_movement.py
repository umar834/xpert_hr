import frappe
from erpnext.assets.doctype.asset_movement.asset_movement import AssetMovement

class CustomAssetMovement(AssetMovement):
    def validate(self):
        self.validate_asset()
        self.validate_location()
        self.validate_employee()
        if self.purpose == "Issue":
            for d in self.assets:
                if d.to_employee:
                    frappe.db.set_value("Asset", d.asset, "assignment_status", "Assigned")

    def on_cancel(self):
        self.set_latest_location_in_asset()
        if self.purpose == "Issue":
            for d in self.assets:
                if d.to_employee:
                    frappe.db.set_value("Asset", d.asset, "assignment_status", "Available")

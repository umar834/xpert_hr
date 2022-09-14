import frappe
from erpnext.assets.doctype.asset.asset import Asset

class CustomAsset(Asset):
    def on_submit(self):
        self.validate_in_use_date()
        self.set_status()
        self.make_asset_movement()
        if not self.booked_fixed_asset and self.validate_make_gl_entry():
            self.make_gl_entries()
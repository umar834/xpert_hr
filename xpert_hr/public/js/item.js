frappe.ui.form.on("Item", {
    refresh: function(frm){
        /* If technical attribute group is selected for exisiting item then when it is loaded we need to change 
           default DATA field of technical specification table to SELECT field for the attributes that have pre-defined values.
        */
        if(frm.doc.technical_attribute_group)
        {
            var group_name = frm.doc.technical_attribute_group;
            //Call the method to get all attributes of selected group
            frappe.call({
                method: "xpert_hr.overrides.get_tech_attrs_based_on_group",
                args: {
                    "group_name": group_name
                }, 
                callback: function(r) {
                    if(r.message != '0' && r.message[0])
                    { 
                        //unhide the technical attribute table
                        frm.set_df_property("item_technical_specifications", "hidden", 0);
                        var index = 1;
                        //loop through each attribute 
                        for (const element of r.message) 
                        {
                            //if the attribute has pre-defined values(select)
                            if(element.attribute_values.length > 0)
                            {
                                //get all the options returned by ajax and add them to array. then change DATA type to SELECT
                                //and put option array into that select
                                var options = [];
                                for(const opt of element.attribute_values)
                                {
                                    options.push(opt.attribute_value);
                                }
                                var current_row = frm.fields_dict["item_technical_specifications"].grid.grid_rows[index-1];
                                current_row.columns.attribute_value.df.fieldtype = "Select";
                                current_row.columns.attribute_value.df.options = options;
                            }
                            index++;
                        }
                        frm.refresh_fields();
                        
                        //hide and disable all buttons & functions that we don't need
                        $('[data-fieldname="item_technical_specifications"]').find('.grid-remove-rows').hide();
                        $('[data-fieldname="item_technical_specifications"]').find('.grid-add-row').hide();
                        $('[data-fieldname="item_technical_specifications"]').find('.grid-row-open').hide();
                        $('[data-fieldname="item_technical_specifications"]').find('.btn-open-row').hide();
                        $("[data-fieldname=item_technical_specifications] .row-index").unbind("click");
                        $('[data-fieldname="item_technical_specifications"] .grid-heading-row .data-row .col').last().attr('style', 'display: none!important');
    
                    }
                }
            });
        }
    },

    // same code as of refresh. comments can be found in refresh function code
    onload: function(frm){
        if(frm.doc.technical_attribute_group)
        {
            var group_name = frm.doc.technical_attribute_group;
            frappe.call({
                method: "xpert_hr.overrides.get_tech_attrs_based_on_group",
                args: {
                    "group_name": group_name
                }, 
                callback: function(r) {
                    if(r.message != '0' && r.message[0])
                    { 
                        frm.set_df_property("item_technical_specifications", "hidden", 0);
                        var index = 1;
                        for (const element of r.message) 
                        {
                            if(element.attribute_values.length > 0)
                            {
                                var options = [];
                                for(const opt of element.attribute_values)
                                {
                                    options.push(opt.attribute_value);
                                }
                                var current_row = frm.fields_dict["item_technical_specifications"].grid.grid_rows[index-1];
                                current_row.columns.attribute_value.df.fieldtype = "Select";
                                current_row.columns.attribute_value.df.options = options;
                            }
                            index++;
                        }
                        frm.refresh_fields();
                        
                        $('[data-fieldname="item_technical_specifications"]').find('.grid-remove-rows').hide();
                        $('[data-fieldname="item_technical_specifications"]').find('.grid-add-row').hide();
                        $('[data-fieldname="item_technical_specifications"]').find('.grid-row-open').hide();
                        $('[data-fieldname="item_technical_specifications"]').find('.btn-open-row').hide();
                        $("[data-fieldname=item_technical_specifications] .row-index").unbind("click");
                        $('[data-fieldname="item_technical_specifications"] .grid-heading-row .data-row .col').last().attr('style', 'display: none!important');
    
                    }
                }
            });
        }
    },

    //When technical attribute group is selected
    technical_attribute_group: function(frm) {
        var group_name = frm.doc.technical_attribute_group;
        //ajax to get all attributes of selected group
        frappe.call({
            method: "xpert_hr.overrides.get_tech_attrs_based_on_group",
            args: {
                "group_name": group_name
            }, 
            callback: function(r) {
                if(r.message != '0' && r.message[0])
                { 
                    //clear table 
                    frm.clear_table("item_technical_specifications");
                    frm.set_df_property("item_technical_specifications", "hidden", 0);

                    // for each attribute returned add a new child in the table
                    for (const element of r.message) 
                    {
                        var childTable = frm.add_child("item_technical_specifications");
                        //add attribute name
                        childTable.attribute_name = element.attribute_name; 
                        
                    }
                    
                    frm.refresh_fields();
                
                    var index = 1;

                    for (const element of r.message) 
                    {
                        //if the attribute has pre-defined values(select)
                        if(element.attribute_values.length > 0)
                        {
                            // get all options and put them into an array
                            var options = [];
                            for(const opt of element.attribute_values)
                            {
                                options.push(opt.attribute_value);
                            }
                            // get current row from the table and then change its attribute value type from DATA to SELECT and put 
                            //in the array as options
                            var custom_cdt="Item Technical Specifications";
                            var custom_cdn="new-item-technical-specification-" + index;
                            var current_row = frm.fields_dict["item_technical_specifications"].grid.grid_rows_by_docname[custom_cdn];
                            current_row.columns.attribute_value.df.fieldtype = "Select";
                            current_row.columns.attribute_value.df.options = options;
                        }
                        index++;
                    }
                    frm.refresh_fields();
                    //hide and disable all buttons & functions that we don't need
                    $('[data-fieldname="item_technical_specifications"]').find('.grid-remove-rows').hide();
                    $('[data-fieldname="item_technical_specifications"]').find('.grid-add-row').hide();
                    $('[data-fieldname="item_technical_specifications"]').find('.grid-row-open').hide();
                    $('[data-fieldname="item_technical_specifications"]').find('.btn-open-row').hide();
                    $("[data-fieldname=item_technical_specifications] .row-index").unbind("click");
                    $('[data-fieldname="item_technical_specifications"] .grid-heading-row .data-row .col').last().attr('style', 'display: none!important');

                }
            }
        });
    }
})

// frappe.ui.form.on("Item Technical Specification", {
//     attribute_value: function(frm, cdt, cdn)
//     {
//         alert(cdt); alert(cdn);
//         const row = locals[cdt][cdn];
//         console.log('######',row);
//     }
// })

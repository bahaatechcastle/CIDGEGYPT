odoo.define('pos_id.models', function (require) {
    "use strict";

    var models = require('point_of_sale.models');

    models.load_fields('res.partner', 'email_parent');
    models.load_fields('res.partner', 'phone_whatsapp');
    models.load_fields('res.partner', 'phone_2');
    models.load_fields('res.partner', 'profession');
    models.load_fields('res.partner', 'note');
    models.load_fields('res.partner', 'parent_name');
    models.load_fields('res.partner', 'source');
    models.load_fields('res.partner', 'id');
    models.load_fields('res.partner', 'id');
    models.load_fields('res.partner', 'create_date');




   models.load_models({
            model: '',
            fields: ['email_parent','phone_whatsapp','phone_2','profession','note','parent_name','source','id','create_date'],
            loaded: function (self, responsability_type) {
            self.responsability_type=responsability_type;

            },
        },);



});

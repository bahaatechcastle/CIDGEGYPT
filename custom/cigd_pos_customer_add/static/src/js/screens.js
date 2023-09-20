odoo.define('cigd_pos_customer_add.screens', function (require) {
    'use strict';

    const PartnerListScreen = require('point_of_sale.PartnerListScreen');
    const Registries = require('point_of_sale.Registries');
    var {Gui} = require('point_of_sale.Gui');
    var models = require('point_of_sale.models');

    const POSSaveClientOverride2 = PartnerListScreen =>
        class extends PartnerListScreen {
            /**
             * @override
             */
            async saveChanges(event) {
                    var email_parent = $('.email_parent').val();
                    var phone_whatsapp = $('.phone_whatsapp').val();
                    var parent_name_id = $('.parent_name').val();
                    var parent_name_id = $('.phone_2').val();
                    var parent_name_id = $('.profession').val();
                    var parent_name_id = $('.note').val();
                    var parent_name_id = $('.source').val();
                    let partnerId = await this.rpc({
                        model: 'res.partner',
                        method: 'create_from_ui',
                        args: [event.detail.processedChanges],
                    });
                    await this.env.pos.load_new_partners();
                    this.state.selectedPartner = this.env.pos.db.get_partner_by_id(partnerId);
                    this.confirm();
                }

            }
        };

    Registries.Component.extend(PartnerListScreen, POSSaveClientOverride2);

    return PartnerListScreen;
});

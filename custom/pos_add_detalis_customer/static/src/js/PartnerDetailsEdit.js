odoo.define('pos_add_one_field_custmer.PartnerDetailsEdit', function (require) {
    "use strict";

    const { _t } = require("web.core");
    var PartnerDetailsEdit = require('point_of_sale.PartnerDetailsEdit');
    var Registries = require('point_of_sale.Registries');
    var { useState, onMounted, onWillUnmount } = require('web.core');

    const TestPartnerDetailsEdit = (PartnerDetailsEdit) => class TestPartnerDetailsEdit extends PartnerDetailsEdit {
        setup() {
            super.setup();
            const partner = this.props.partner;
            this.changes.text_test = partner.text_test || "";
            this.changes.parent_name = partner.parent_name || "";
            this.changes.birthday_kid = partner.birthday_kid || "";
            this.changes.email_parent = partner.email_parent || "";
            this.changes.phone_whatsapp = partner.phone_whatsapp || "";
            this.changes.phone_2 = partner.phone_2 || "";
            this.changes.profession = partner.profession || "";
            this.changes.note = partner.note || "";
            this.changes.source = partner.source || "";
            this.changes.age = partner.age || "";
        }

        captureChange(event) {}
        saveChanges() {
            const processedChanges = {};
            for (const [key, value] of Object.entries(this.changes)) {
                if (this.intFields.includes(key)) {
                    processedChanges[key] = parseInt(value) || false;
                } else {
                    processedChanges[key] = value;
                }
            }
            if (
                processedChanges.state_id &&
                this.env.pos.states.find((state) => state.id === processedChanges.state_id)
                    .country_id[0] !== processedChanges.country_id
            ) {
                processedChanges.state_id = false;
            }

            if (
                (!this.props.partner.name && !processedChanges.name) ||
                processedChanges.name === ""
            ) {
                return this.showPopup("ErrorPopup", {
                    title: _t("A Customer Name Is Required"),
                });
            }
            if (
                (!this.props.partner.parent_name && !processedChanges.parent_name) ||
                processedChanges.name === ""
            ) {
                return this.showPopup("ErrorPopup", {
                    title: _t("A Customer parent_name Is Required"),
                });
            }
            if (
                (!this.props.partner.street && !processedChanges.street) ||
                processedChanges.street === ""
            ) {
                return this.showPopup("ErrorPopup", {
                    title: _t("A Customer street Is Required"),
                });
            }
            if (
                (!this.props.partner.city && !processedChanges.city) ||
                processedChanges.city === ""
            ) {
                return this.showPopup("ErrorPopup", {
                    title: _t("A Customer city Is Required"),
                });
            }
            if (
                (!this.props.partner.country_id && !processedChanges.country_id) ||
                processedChanges.country_id === ""
            ) {
                return this.showPopup("ErrorPopup", {
                    title: _t("A Customer country Is Required"),
                });
            }
            if (
                (!this.props.partner.birthday_kid && !processedChanges.birthday_kid) ||
                processedChanges.birthday_kid === ""
            ) {
                return this.showPopup("ErrorPopup", {
                    title: _t("A Customer birthday_kid Is Required"),
                });
            }
            if (
                (!this.props.partner.email && !processedChanges.email) ||
                processedChanges.email === ""
            ) {
                return this.showPopup("ErrorPopup", {
                    title: _t("A Customer email Is Required"),
                });
            }
            if (
                (!this.props.partner.phone && !processedChanges.phone) ||
                processedChanges.phone === ""
            ) {
                return this.showPopup("ErrorPopup", {
                    title: _t("A Customer phone Is Required"),
                });
            }
            if (
                (!this.props.partner.email_parent && !processedChanges.email_parent) ||
                processedChanges.phone === ""
            ) {
                return this.showPopup("ErrorPopup", {
                    title: _t("A Customer email_parent Is Required"),
                });
            }


            processedChanges.id = this.props.partner.id || false;
            this.trigger("save-changes", { processedChanges });
        }

    }

    Registries.Component.extend(PartnerDetailsEdit, TestPartnerDetailsEdit);
});


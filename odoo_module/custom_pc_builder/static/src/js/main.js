odoo.define('custom_pc_builder.main', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var ajax = require('web.ajax');

    var QWeb = core.qweb;
    var _t = core._t;

    var CustomPCBuilder = Widget.extend({
        template: 'custom_pc_builder',
        events: {
            'click .component-selection': 'onComponentSelection',
            'click .save-configuration': 'onSaveConfiguration',
            'click .load-configuration': 'onLoadConfiguration',
            'click .place-order': 'onPlaceOrder',
        },

        start: function () {
            this.loadComponents();
            return this._super.apply(this, arguments);
        },

        loadComponents: function () {
            var self = this;
            ajax.jsonRpc('/custom_pc_builder/load_components', 'call', {})
                .then(function (data) {
                    self.renderComponents(data);
                });
        },

        renderComponents: function (data) {
            this.$('.component-list').html(QWeb.render('ComponentList', {components: data}));
        },

        onComponentSelection: function (event) {
            var componentId = $(event.currentTarget).data('id');
            this.selectComponent(componentId);
        },

        selectComponent: function (componentId) {
            var self = this;
            ajax.jsonRpc('/custom_pc_builder/select_component', 'call', {component_id: componentId})
                .then(function (data) {
                    self.updateConfiguration(data);
                });
        },

        updateConfiguration: function (data) {
            this.$('.configuration').html(QWeb.render('Configuration', {configuration: data}));
        },

        onSaveConfiguration: function () {
            var self = this;
            ajax.jsonRpc('/custom_pc_builder/save_configuration', 'call', {})
                .then(function (data) {
                    self.showNotification(data.message);
                });
        },

        onLoadConfiguration: function () {
            var self = this;
            ajax.jsonRpc('/custom_pc_builder/load_configuration', 'call', {})
                .then(function (data) {
                    self.updateConfiguration(data);
                });
        },

        onPlaceOrder: function () {
            var self = this;
            ajax.jsonRpc('/custom_pc_builder/place_order', 'call', {})
                .then(function (data) {
                    self.showNotification(data.message);
                });
        },

        showNotification: function (message) {
            this.do_notify(_t('Custom PC Builder'), _t(message));
        },
    });

    core.action_registry.add('custom_pc_builder', CustomPCBuilder);

    return CustomPCBuilder;
});
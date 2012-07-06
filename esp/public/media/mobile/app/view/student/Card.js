Ext.define('LU.view.student.Card', {

    extend: 'Ext.NavigationView',
    xtype: 'studentContainer',

    config: {
        navigationBar: {
            ui: 'dark',
            docked: 'top',
            items: [
                {
                    xtype: 'button',
                    align: 'right',
                    text: 'Logout'
                }
            ]
        },
        title: 'Search',
        iconCls: 'search',

        autoDestroy: false,

        items: [
            {
                xtype: 'studentList'
            }
        ]
    }
});

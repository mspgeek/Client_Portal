var DatatablesBasicScrollable = function() {

    var initTable1 = function() {
        var table = $('#m_table_1');

        // begin first table
        table.DataTable({
            scrollY: '50vh',
            scrollX: true,
            scrollCollapse: true,
            paging: false,
            createdRow: function(row, data, index) {
                var status = {
                    1: {'title': 'Pending', 'class': 'm-badge--brand'},
                    2: {'title': 'Delivered', 'class': ' m-badge--metal'},
                    3: {'title': 'Canceled', 'class': ' m-badge--primary'},
                    4: {'title': 'Success', 'class': ' m-badge--success'},
                    5: {'title': 'Info', 'class': ' m-badge--info'},
                    6: {'title': 'Danger', 'class': ' m-badge--danger'},
                    7: {'title': 'Warning', 'class': ' m-badge--warning'},
                };
                var badge = '<span class="m-badge ' + status[data[7]].class + ' m-badge--wide">' + status[data[7]].title + '</span>';
                row.getElementsByTagName('td')[7].innerHTML = badge;

                status = {
                    1: {'title': 'Online', 'state': 'danger'},
                    2: {'title': 'Retail', 'state': 'primary'},
                    3: {'title': 'Direct', 'state': 'accent'},
                };
                badge = '<span class="m-badge m-badge--' + status[data[8]].state + ' m-badge--dot"></span>&nbsp;' +
                    '<span class="m--font-bold m--font-' + status[data[8]].state + '">' + status[data[8]].title + '</span>';
                row.getElementsByTagName('td')[8].innerHTML = badge;
            },
            columnDefs: [
                {
                    targets: -1,
                    data: 'name',
                    title: 'Actions',
                    orderable: false,
                    render: function(data, type, full, meta) {
                        return `
                        <span class="dropdown">
                            <a href="#" class="btn m-btn m-btn--hover-brand m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="dropdown" aria-expanded="true">
                              <i class="la la-ellipsis-h"></i>
                            </a>
                            <div class="dropdown-menu dropdown-menu-right">
                                <a class="dropdown-item" href="#"><i class="la la-edit"></i> Edit Details</a>
                                <a class="dropdown-item" href="#"><i class="la la-leaf"></i> Update Status</a>
                                <a class="dropdown-item" href="#"><i class="la la-print"></i> Generate Report</a>
                            </div>
                        </span>
                        <a href="#" class="m-portlet__nav-link btn m-btn m-btn--hover-brand m-btn--icon m-btn--icon-only m-btn--pill" title="View">
                          <i class="la la-edit"></i>
                        </a>`;
                    },
                }],
        });
    };

    var initTable2 = function() {
        var table = $('#m_table_2');

        // begin second table
        table.DataTable({
            scrollY: '50vh',
            scrollX: true,
            scrollCollapse: true,
            paging: false,
            createdRow: function(row, data, index) {
                var status = {
                    1: {'title': 'Pending', 'class': 'm-badge--brand'},
                    2: {'title': 'Delivered', 'class': ' m-badge--metal'},
                    3: {'title': 'Canceled', 'class': ' m-badge--primary'},
                    4: {'title': 'Success', 'class': ' m-badge--success'},
                    5: {'title': 'Info', 'class': ' m-badge--info'},
                    6: {'title': 'Danger', 'class': ' m-badge--danger'},
                    7: {'title': 'Warning', 'class': ' m-badge--warning'},
                };
                var badge = '<span class="m-badge ' + status[data[19]].class + ' m-badge--wide">' + status[data[19]].title + '</span>';
                row.getElementsByTagName('td')[19].innerHTML = badge;

                status = {
                    1: {'title': 'Online', 'state': 'danger'},
                    2: {'title': 'Retail', 'state': 'primary'},
                    3: {'title': 'Direct', 'state': 'accent'},
                };
                badge = '<span class="m-badge m-badge--' + status[data[20]].state + ' m-badge--dot"></span>&nbsp;' +
                    '<span class="m--font-bold m--font-' + status[data[20]].state + '">' + status[data[20]].title + '</span>';
                row.getElementsByTagName('td')[20].innerHTML = badge;
            },
            columnDefs: [
                {
                    targets: 9,
                    width: '200px',
                },
                {
                    targets: -1,
                    data: 'name',
                    title: 'Actions',
                    orderable: false,
                    render: function(data, type, full, meta) {
                        return `
                        <span class="dropdown">
                            <a href="#" class="btn m-btn m-btn--hover-brand m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="dropdown" aria-expanded="true">
                              <i class="la la-ellipsis-h"></i>
                            </a>
                            <div class="dropdown-menu dropdown-menu-right">
                                <a class="dropdown-item" href="#"><i class="la la-edit"></i> Edit Details</a>
                                <a class="dropdown-item" href="#"><i class="la la-leaf"></i> Update Status</a>
                                <a class="dropdown-item" href="#"><i class="la la-print"></i> Generate Report</a>
                            </div>
                        </span>
                        <a href="#" class="m-portlet__nav-link btn m-btn m-btn--hover-brand m-btn--icon m-btn--icon-only m-btn--pill" title="View">
                          <i class="la la-edit"></i>
                        </a>`;
                    },
                }],
        });
    };

    return {

        //main function to initiate the module
        init: function() {
            initTable1();
            initTable2();
        },

    };

}();

jQuery(document).ready(function() {
    DatatablesBasicScrollable.init();
});
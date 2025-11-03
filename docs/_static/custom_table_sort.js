// Custom sorting for different table types
$(document).ready(function() {
    // Wait a bit for DataTables to initialize
    setTimeout(function() {
        $('table.sphinx-datatable').each(function() {
            if ($.fn.DataTable.isDataTable(this)) {
                var table = $(this).DataTable();
                var headers = [];

                // Get column headers
                $(this).find('thead th').each(function() {
                    headers.push($(this).text().trim());
                });

                // Main results table: sort by FINAL score (descending)
                if (headers.includes('FINAL')) {
                    var finalIdx = headers.indexOf('FINAL');
                    table.order([finalIdx, 'desc']).draw();
                }
                // DEC Modes comparison table: sort by Changeable (descending)
                else if (headers.includes('Changeable') && headers.includes('Supported Modes')) {
                    var changeableIdx = headers.indexOf('Changeable');
                    table.order([changeableIdx, 'desc']).draw();
                }
                // Language Support table: sort by pct_success (ascending)
                else if (headers.includes('lang') && headers.includes('pct_success')) {
                    var pctIdx = headers.indexOf('pct_success');
                    table.order([pctIdx, 'asc']).draw();
                }
            }
        });
    }, 200);
});

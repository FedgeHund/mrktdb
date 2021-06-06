import React from 'react';

function Pagination({ rowsPerPage, totalRows, paginate, currentPage }) {
    const pageNumbers = [];

    for (let i = 1; i <= Math.ceil(totalRows / rowsPerPage); i++) {
        pageNumbers.push(i);
    }

    function getPageList(totalPages, page, maxLength) {
        if (maxLength < 5) throw "maxLength must be at least 5";

        function range(start, end) {
            return Array.from(Array(end - start + 1), (_, i) => i + start);
        }

        var sideWidth = maxLength < 9 ? 1 : 2;
        var leftWidth = (maxLength - sideWidth * 2 - 3) >> 1;
        var rightWidth = (maxLength - sideWidth * 2 - 2) >> 1;
        if (totalPages <= maxLength) {
            // no breaks in list
            return range(1, totalPages);
        }
        if (page <= maxLength - sideWidth - 1 - rightWidth) {
            // no break on left of page
            return range(1, maxLength - sideWidth - 1)
                .concat(0, range(totalPages - sideWidth + 1, totalPages));
        }
        if (page >= totalPages - sideWidth - 1 - rightWidth) {
            // no break on right of page
            return range(1, sideWidth)
                .concat(0, range(totalPages - sideWidth - 1 - rightWidth - leftWidth, totalPages));
        }
        // Breaks on both sides
        return range(1, sideWidth)
            .concat(0, range(page - leftWidth, page + rightWidth),
                0, range(totalPages - sideWidth + 1, totalPages));
    }

    return (
        <nav>
            <ul className="pagination justify-content-end">
                <li class="page-item">
                    <a class="page-link table_previous_btn" href="javascript:void(0);" aria-label="Previous" onClick={() => paginate(currentPage - 1)}>
                        <span aria-hidden="true">&laquo;</span>
                        <span class="sr-only">Previous</span>
                    </a>
                </li>
                {pageNumbers.map(function (number) {
                    if (number === pageNumbers[0]) {
                        return (
                            <li key={number} className="page-item">
                                < a onClick={() => paginate(number)} href="javascript:void(0);" className="page-link table_nav_btn">
                                    {currentPage}
                                </a>
                            </li>
                        )
                    }
                    else if (number === pageNumbers[pageNumbers.length - 1]) {
                        return (
                            <li key={number} className="page-item">
                                < a onClick={() => paginate(number)} href="javascript:void(0);" className="page-link table_nav_btn">
                                    {number}
                                </a>
                            </li>
                        )
                    }
                    else if (number === pageNumbers[1]) {
                        return (
                            <li key={number} className="page-item">
                                < a onClick={() => paginate(number)} href="javascript:void(0);" className="page-link table_nav_btn">
                                    ...
                                </a>
                            </li>
                        )
                    }
                    else
                        return
                })}
                <li class="page-item">
                    <a class="page-link table_next_btn" href="javascript:void(0);" aria-label="Next" onClick={() => paginate(currentPage + 1)} >
                        <span aria-hidden="true">&raquo;</span>
                        <span class="sr-only">Next</span>
                    </a>
                </li>
            </ul >
        </nav >
    )
}

export default Pagination;
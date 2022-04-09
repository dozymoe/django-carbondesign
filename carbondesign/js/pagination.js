import Pagination from 'carbon-components/src/components/pagination/pagination';

export default function()
{
    Pagination.init()

    for (let el of document.querySelectorAll('[data-pagination]'))
    {
        el.addEventListener('itemsPerPage', onPagination);
        el.addEventListener('pageNumber', onPagination);
        el.addEventListener('pageChange', onPagination);
    }
}

function onPagination(event)
{
    let qs = new URLSearchParams(location.search);
    let qname;
    if (event.type === 'itemsPerPage')
    {
        qname = event.target.getAttribute('data-pagesize-name');
    }
    else
    {
        qname = event.target.getAttribute('data-page-name');
    }
    if (event.type === 'pageChange' && !event.detail.value)
    {
        event.detail.value = parseInt(qs.get(qname)) || 1;
        if (event.detail.direction === 'forward')
        {
            event.detail.value += 1;
        }
        else if (event.detail.value > 1)
        {
            event.detail.value -= 1;
        }
    }
    qs.set(qname, event.detail.value);
    location.search = qs.toString();
}

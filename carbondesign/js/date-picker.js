import DatePicker from 'carbon-components/src/components/date-picker/date-picker';

export default function()
{
    Array.prototype.forEach.call(
            document.querySelectorAll(DatePicker.options.selectorInit),
            (el) =>
            {
                const format = el.getAttribute('data-date-picker-format');
                DatePicker.create(el, format ? {dateFormat: format} : {});
            });
}

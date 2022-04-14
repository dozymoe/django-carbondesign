import Modal from 'carbon-components/src/components/modal/modal';

export default function()
{
    for (let el of document.querySelectorAll('[data-modal-target]'))
    {
        Modal.init(el);
    }
}

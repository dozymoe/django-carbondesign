import ContentSwitcher from 'carbon-components/src/components/content-switcher/content-switcher';

export default function()
{
    ContentSwitcher.init()
    for (let el of document.querySelectorAll('.bx--content-switcher--selected'))
    {
        el.click();
    }
}

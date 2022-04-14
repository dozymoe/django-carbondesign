import HeaderNav from 'carbon-components/src/components/ui-shell/header-nav';
import HeaderSubmenu from 'carbon-components/src/components/ui-shell/header-submenu';
import NavigationMenu from 'carbon-components/src/components/ui-shell/navigation-menu';
import ProductSwitcher from 'carbon-components/src/components/ui-shell/product-switcher';
import SideNav from 'carbon-components/src/components/ui-shell/side-nav';

export default function()
{
    let el;
    el = document.querySelector('button.bx--header__menu-trigger');
    if (el) NavigationMenu.init(el);

    HeaderNav.init();
    HeaderSubmenu.init();

    for (el of document.querySelectorAll('button[data-panel-switcher-target]'))
    {
        ProductSwitcher.init(el, {
            attribInitTarget: 'data-panel-switcher-target',
        });
    }

    SideNav.init();
}
